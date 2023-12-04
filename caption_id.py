from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set DEVELOPER_KEY to the API key value from the APIs & Services > Credentials
# tab of your project in the Google Developers Console.
DEVELOPER_KEY = 'enter your api key here'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def get_caption_tracks(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Retrieve the list of caption tracks.
    caption_tracks = youtube.captions().list(
        part='id',
        videoId=video_id
    ).execute()

    return caption_tracks["items"][0]["id"]

# Call the function to get the list of caption tracks for a video.
caption_tracks = get_caption_tracks('KCCMwCTLEkQ')
print(caption_tracks)
