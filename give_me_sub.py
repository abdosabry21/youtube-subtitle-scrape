from youtube_transcript_api import YouTubeTranscriptApi
import srt
from givemeTitle import title
def extract_sub(video_id):
    # Get the transcript of the YouTube video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    print(transcript)
    # Convert the transcript to an SRT file


    subtitles = []
    for item in transcript:
        start = srt.timedelta(seconds=item["start"])
        end = srt.timedelta(seconds=item["start"] + item["duration"])
        text = item["text"]
        subtitle = srt.Subtitle(index=None, start=start, end=end, content=text)
        subtitles.append(subtitle)

    # Write the subtitles to an SRT file
    srt_content = srt.compose(subtitles)

    tt=title(video_id)[:30]
    with open(f"{tt}.srt", "w") as f:
        f.write(srt_content)


extract_sub("8k8S5ruFAUs")