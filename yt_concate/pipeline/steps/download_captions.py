import time

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import SRTFormatter
from youtube_transcript_api._errors import TranscriptsDisabled
from youtube_transcript_api._errors import NoTranscriptFound


from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for url in data:
            print('downloading captions for ' + url)
            video_id = url.split("v=")[-1].split("&")[0]

            if utils.caption_file_exists(video_id):
                print('found existing caption file')
                continue
            # 取得英文字幕（自動或人工都會抓）
            try:
                transcript = YouTubeTranscriptApi().fetch(video_id, languages=['en'])

            except TranscriptsDisabled:
                print('captions : disabled, skip video' + video_id)
                continue

            except NoTranscriptFound:
                print('captions : not found, skip video' + video_id)
                continue

            # 轉成 SRT 格式和存檔
            formatter = SRTFormatter()
            srt_text = formatter.format_transcript(transcript)
            print(srt_text)

            with open(utils.get_caption_filepath(video_id), "w", encoding="utf-8") as f:
                f.write(srt_text)

        end = time.time()
        print(f"took {end - start} seconds")
