from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from playwright.sync_api import sync_playwright
from give_me_sub import extract_sub







# Set DEVELOPER_KEY to the API key value from the APIs & Services > Credentials
# tab of your project in the Google Developers Console.
DEVELOPER_KEY = 'enter your api key here'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_video_ids(channel_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Retrieve the ID of the playlist that represents the uploads from the channel.
    content_data = youtube.channels().list(
        id=channel_id,
        part='contentDetails'
    ).execute()

    playlist_id = content_data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Retrieve the list of videos in the playlist.
    videos = []
    next_page_token = None
    while True:
        playlist_items = youtube.playlistItems().list(
            playlistId=playlist_id,
            part='snippet',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        videos += playlist_items['items']
        next_page_token = playlist_items.get('nextPageToken')

        if not next_page_token:
            break

    # Extract the video IDs from the list of videos.
    video_ids = [video['snippet']['resourceId']['videoId'] for video in videos]

    return video_ids


for id in get_video_ids("UCQ4FNww3XoNgqIlkBqEAVCg"):
    extract_sub(id)

