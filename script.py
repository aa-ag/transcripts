###--- IMPORTS ---###
import settings
from youtube_transcript_api import YouTubeTranscriptApi
# https://pypi.org/project/youtube-transcript-api/


###--- GLOBAL VARIABLES ---###
# https://www.youtube.com/watch?v=F2KcZGwntgg
youtube_video_id = 'F2KcZGwntgg'


###--- FUNCTIONS ---###

def get_transcripts():
    '''
    Gets transcript object: list of dictionaries. Example:
    "{'text': "you may not realize it but we're", 'start': 1.25, 'duration': 4.96}, ..."
    Then loops thru list to create one, human-readable string.
    '''
    global youtube_video_id

    entire_transcript = YouTubeTranscriptApi.get_transcript(youtube_video_id)

    clean_transcript = ''

    for transcript in entire_transcript:
        clean_transcript += transcript['text'] + '\n'

    with open('Transcript.txt', 'w') as readable_transcript:
        readable_transcript.write(clean_transcript)
        readable_transcript.close()


###--- DRIVER CODE ---###
if __name__ == "__main__":
    get_transcripts()
