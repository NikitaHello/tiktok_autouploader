import logging
import os

from tiktok_uploader import tiktok, Video
from tiktok_uploader.ytscrapper.video_scrapper import (
    json_parser, json_vid_status_uploaded, json_videos_update
)
from tiktok_uploader.Config import Config


logging.basicConfig(
    filename=Config.get().log_dir,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
logger = logging.getLogger(__name__)


def video_upload(
        youtube: str,
        title: str,
        user: str,
        ) -> bool:
    video_obj = Video(youtube, title)
    video_obj.is_valid_file_format()
    video = video_obj.source_ref
    result = tiktok.upload_video(user, video,  title)
    if result is True:
        json_vid_status_uploaded(user, youtube)

    # Add video status updater to uploaded == true
    return result


if __name__ == "__main__":

    logger.info("starting videos transition from youtube to tik-tok")
    user_names = []
    reupload_list = []
    tries = 0
    cookie_dir = os.path.join(os.getcwd(), Config.get().cookies_dir)
    for name in os.listdir(cookie_dir):
        if name.startswith("tiktok_session-"):
            user_names.append((name.split("tiktok_session-")[1]).split(".")[0])
    for user in user_names:
        json_videos_update(user)
        video_data = json_parser(user)
        if video_data:
            logger.info("Successfuly extracted data from JSON for new video")
        videos = video_data['vid_information']
        channel_name = video_data['channel_name']
        for video in videos:
            if not video['uploaded']:
                link = video['url']
                title = video['title']
                break
        try:
            logger.info(f"Starting upload {title}")
            result = video_upload(link, title, user)
        except TypeError:
            logger.error("JS error while uploading")
        if result:
            logger.info(f"Video '{title}' has been successfuly uploaded")
        else:
            logger.error(f"Error while uploading '{title}'")
            reupload_list.append({'link': link, 'title': title, 'user': user})
        
    while reupload_list != [] or tries < 5:
        tries += 1
        for video in reupload_list:
            try:
                result = video_upload(video['link'], 
                                      video['title'], 
                                      video['user'])
            except TypeError:
                logger.error("JS error while uploading")
            if result:
                logger.info(f"Video '{video['title']}' has been "
                            "successfuly uploaded")
                reupload_list.remove(video)
            else:
                logger.error(f"Error while uploading '{video['title']}'")
