from googleapiclient.discovery import build
import json
def title(video_id):
    # Set DEVELOPER_KEY to the API key value from the Google Developers Console.
    DEVELOPER_KEY = 'enter your api key here'
    YOUTUBE_API_SERVICE_NAME = 'youtube'
    YOUTUBE_API_VERSION = 'v3'

    # Create a YouTube API client
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    # Call the videos().list() method to retrieve the video details
    video_id = f'{video_id}'
    response = youtube.videos().list(part='snippet', id=video_id).execute()

    # Extract the video title from the response
    title = response['items'][0]['snippet']['title']

    return title

