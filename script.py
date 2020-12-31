###--- IMPORTS ---###
import settings
import requests
from youtube_transcript_api import YouTubeTranscriptApi
# https://pypi.org/project/youtube-transcript-api/

###--- GLOBAL VARIABLES ---###
# https://www.youtube.com/watch?v=F2KcZGwntgg
youtube_video_id = 'F2KcZGwntgg'

###--- FUNCTIONS ---###


def get_transcripts():
    global youtube_video_id
    print(YouTubeTranscriptApi.get_transcript(youtube_video_id))


###--- DRIVER CODE ---###
if __name__ == "__main__":
    get_transcripts()
