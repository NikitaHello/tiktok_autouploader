import youtube_dl
import json
import logging

from ..Config import Config

logger = logging.getLogger('video_scrapper')


def get_json_data():
    filename = Config.get().json_filepath
    try:
        with open(filename, 'r') as file:
            json_data = json.load(file)
    except json.decoder.JSONDecodeError:
        json_data = []  # return empty list if file is empty'
    return json_data


def get_video_urls(channel_url: str, user_name: str) -> dict:
    ydl_opts = {
        'extract_flat': True,
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
    if not result:
        logger.error('Channel is empty')
        raise ValueError('Channel is empty')
    info_dict = {
                'channel name': result['title'],
                'user': user_name,
                'channel_url': channel_url,
                'vid_information': []
    }
    for video in result['entries']:
        if video['duration'] < 600.0:
            vid_information = {
                'url': 'https://www.youtube.com/watch?v=' + video['url'],
                'title': video['title'],
                'duration': video['duration'],
                "uploaded": False
            }
            info_dict['vid_information'].append(vid_information)
    logger.info(f"Video links from channel '{info_dict['channel name']}' OK")
    return info_dict


def save_to_json(video_links: dict):
    filename = Config.get().json_filepath
    json_data = get_json_data()
    data = []
    data_dict = {
        "channel_name": video_links['channel name'],
        "user": video_links['user'],
        "channel_url": video_links['channel_url'],
        "vid_information": video_links['vid_information']
    }
    data.append(data_dict)
    if json_data:
        json_data.extend(data)
    else:
        json_data = data
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file, indent=4)
    logger.info(f"JSON data for '{data_dict['channel_name']}' created")


def json_parser(user_name: str) -> dict:
    data = get_json_data()

#    unpacked_data = []
    for entry in data:
        if entry.get("user") == user_name:
            channel_name = entry.get("channel_name")
            channel_url = entry.get("channel_url")
            vid_information = entry.get("vid_information", [])

            videos = []
            for vid_info in vid_information:
                url = vid_info.get("url")
                title = vid_info.get("title")
                duration = vid_info.get("duration")
                uploaded = vid_info.get("uploaded")
                video = {
                    "url": url,
                    "title": title,
                    "duration": duration,
                    "uploaded": uploaded
                }
                videos.append(video)
            return {
                    "channel_name": channel_name,
                    "user": user_name,
                    "channel_url": channel_url,
                    "vid_information": videos
            }
        logger.error(f'User {user_name} does not exist in JSON file')

#            unpacked_data.append({
#                "channel_name": channel_name,
#                "user": user_name,
#                "videos": videos
#            })

#    return unpacked_data


def json_vid_status_uploaded(user_name: str, link: str):
    filename = Config.get().json_filepath
    json_data = get_json_data()
    for entry in json_data:
        if entry.get("user") == user_name:
            vid_information = entry.get("vid_information", [])
            for vid_info in vid_information:
                if vid_info.get("url") == link:
                    vid_info["uploaded"] = True
                    with open(filename, "w") as json_file:
                        json.dump(json_data, json_file, indent=4)
                    logger.info(f"Video '{vid_info['title']}' "
                                "now has status uploaded")
                    return True
    logger.error(f"For user {user_name} no video {link} have been found")


def json_vid_delete(json_data, yt_data):
    yt_vid_list = []
    vid_information = yt_data['vid_information']
    for vid_info in vid_information:
        yt_vid_list.append(vid_info['url'])

    for entry in json_data:
        vid_information = entry.get("vid_information", [])
        for vid_info in vid_information:
            if vid_info['url'] not in yt_vid_list:
                try:
                    vid_information.remove(vid_info)
                except ValueError:
                    logger.info('Error in video deletion')
    return json_data


def json_vid_add(json_data, yt_data):
    json_vid_list = []
    for entry in json_data:
        json_vid_information = entry.get("vid_information", [])
        for vid_info in json_vid_information:
            json_vid_list.append(vid_info['url'])

        yt_vid_information = yt_data['vid_information']
        for vid_info in yt_vid_information:
            if vid_info['url'] not in json_vid_list:
                try:
                    json_vid_information.append(vid_info)
                except ValueError:
                    logger.info('Error in video deletion')
    return json_data


def json_videos_update(user_name: str):
    filename = Config.get().json_filepath
    video_data = json_parser(user_name)
    json_data = get_json_data()
    yt_data = get_video_urls(video_data['channel_url'], user_name)
    if json_data and yt_data:
        json_vid_delete(json_data, yt_data)
        json_vid_add(json_data, yt_data)
        with open(filename, "w") as json_file:
            json.dump(json_data, json_file, indent=4)
        logger.info("Video information successfuly updated")
    else:
        logger.info("Data is empty while updating")


def yt_urls_to_json(channel_url: str, user_name: str):
    video_links = get_video_urls(channel_url, user_name)
    save_to_json(video_links)


"""
for testing

if __name__ == "__main__":
    yt_link = input("Insert channel url with /videos: ")
    user = input("Insert user name: ")
    yt_urls_to_json(yt_link, user)
    unpaked = json_parser(user)
    print(unpaked)
"""
