# PixivTag

This app automatically organises images from Pixiv by identifying the franchise tags associated with each illustration. Based on the tags retrieved via [Pixivpy](https://github.com/upbit/pixivpy), the program sorts images into appropriate folders by franchise (e.g., Hololive, Genshin Impact, etc.).

> Due to #158 reason, password login no longer exist. Please use api.auth(refresh_token=REFRESH_TOKEN) instead
>
> To get refresh\*token, see [@ZipFile Pixiv OAuth Flow](https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362) or [OAuth with Selenium/ChromeDriver](https://gist.github.com/upbit/6edda27cb1644e94183291109b8a5fde)

\*taken from pixivpy homepage\*

## Current Features:

- Retrieves image tags using the Pixivpy.
- Sorts images into franchise-specific folders based on the tags.
- Handles multiple franchises and prioritizes based on predefined franchise categories.

## Future Improvements:

- <p>Artist Sorting: <br>In future updates, I plan to implement functionality to organize images by the artist as well, creating dedicated folders for each artist in addition to sorting by franchise.</p>
