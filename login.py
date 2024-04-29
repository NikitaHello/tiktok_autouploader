from tiktok_uploader import tiktok
from tiktok_uploader.ytscrapper.video_scrapper import yt_urls_to_json
import logging

logger = logging.getLogger('user login.py')

if __name__ == "__main__":
    name = input("Enter user name (recommended tik-tok channel name): ")
    youtube = input("Enter url link to youtube channel with '.../videos': ")
    # Name of file to save the session id.
    tiktok.login(name)
    # automaticaly starting parser
    yt_urls_to_json(youtube, name)
