import re
from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)"
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL")


def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    text = " ".join([item["text"] for item in transcript])

    return text
