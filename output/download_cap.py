from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import io
import os

# Set DEVELOPER_KEY to the API key value from the APIs & Services > Credentials
# tab of your project in the Google Developers Console.
DEVELOPER_KEY = 'AIzaSyAqCiw7KUThYOgxrvLAO0nmZ3P7R-YtV7w'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def download_caption(video_id, caption_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Retrieve the caption track.
    caption = youtube.captions().download(
        id=caption_id,
        tfmt='srt'
    ).execute()

    # Write the caption track to a file.
    with io.open(os.path.join(os.getcwd(), f'{video_id}.srt'), 'w', encoding='utf-8') as f:
        f.write(caption)

# Call the function to download the caption track.
download_caption('KCCMwCTLEkQ', 'AUieDabBSUJ_YexhoR_37AiEBqilqWS-dCNFA3Os9UCZDfrii2w')

