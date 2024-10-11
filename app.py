import os 
import shutil

from pixivpy3 import *
image_folder = input("Enter the path for images: ")
image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

franchise_dict = {
    ### Example Tags
    # "Arknights":["Arknights", "明日方舟", "アークナイツ"], 
    # "Azur Lane":["AzurLane", "アズールレーン"],
    # "Blue Archive":["BlueArchive", "ブルーアーカイブ", "ブルアカ"],
    # "Fate": ["Fate/GrandOrder", "FGO", "Fate", "Fate/SamuraiRemnant"],
    # "Genshin Impact":["GenshinImpact", "原神"],
    # "Girls' Frontline":["ドールズフロントライン","少女前線","girlsfrontline"],
    # "Honkai":["崩坏星穹铁道", "崩壊:スターレイル", "崩坏3rd", "崩壊3rd","崩壊スターレイル","スターレイル"],
    # "Hololive":["hololive", "ホロライブ"],
    # "imas":["学園アイドルマスター","アイドルマスターシンデレラガールズ","アイドルマスター","IDOLM@STER","アイドルマスターシャイニーカラーズ"],
    # "Misc":["オリジナル","original","Original"],
    # "Nikke":["勝利の女神:NIKKE","NIKKE","メガニケ"],
    # "Touhou":["東方Project","東方","Touhou"],
    # "Uma Musume":["ウマ娘プリティーダービー"],
    # "Vocaloid":["初音ミク","VOCALOID","鏡音リン","鏡音レン","重音テト"],
    # "Vtuber":["バーチャルYouTuber", "VTuber","にじさんじ","vtuber"],
    # "Wuthering Waves":["鸣潮","鳴潮","WutheringWaves"],
    # "ZZZ":["ゼンレスゾーンゼロ","ゼンゼロ","绝区零"]
}

api = AppPixivAPI()
api.auth(refresh_token=REFRESH_TOKEN)

def get_pixiv_tags(image_id):
    json_result = api.illust_detail(image_id)
    tags = json_result['illust']['tags']
    tag_names = [tag['name'] for tag in tags]
    return tag_names

#identify the franchise by searching for the required tags. 
def identify_franchises(tag_names):
    matching_franchises = set()
    for franchise, tag in franchise_dict.items():
        for keyword in tag:
            if keyword in tag_names:
                matching_franchises.add(franchise)
    return list(matching_franchises)  

def organise_images(image_files):
    for image_file in image_files:
        image_id = image_file.split('_')[1]
        
        tags = get_pixiv_tags(image_id)
        if not tags:
            print(f"Tags not found for {image_file}")
            continue
        
        
        matching_franchises = identify_franchises(tags)
        
        #further edge cases can be added here
        if "Vtuber" in matching_franchises and "Hololive" in matching_franchises:
            franchise = "Hololive"
        elif "Vtuber" in matching_franchises and "Misc" in matching_franchises:
            franchise = "Vtuber"
        elif len(matching_franchises)!=1:
            print(f"Skipping {image_file} (matches multiple or no franchises)")
            continue
        
        # Move the image to the single matching franchise folder
        franchise = matching_franchises[0]
        franchise_folder = os.path.join(image_folder, franchise)
        if not os.path.exists(franchise_folder):
            os.makedirs(franchise_folder)
            
        src_path = os.path.join(image_folder, image_file)
        dest_path = os.path.join(franchise_folder, image_file)
        shutil.move(src_path, dest_path)
        print(f"Moved {image_file} to {franchise}")
    
organise_images(image_files)