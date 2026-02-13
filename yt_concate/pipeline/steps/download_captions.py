import time

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from .step import Step
from .step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('downloading captions for ' + yt.id)
            if utils.caption_file_exists(yt):
                print('found existing caption file')
                continue
            # 取得英文字幕（自動或人工都會抓）
            url = yt.url
            opts = {
                "outtmpl": yt.caption_filepath.split(".en.srt")[0],
                "skip_download": True,
                "writesubtitles": True,
                "writeautomaticsub": True,
                "subtitleslangs": ["en"],
                "subtitlesformat": "srt",

                "sleep_interval": 4,
                "max_sleep_interval": 8,
                "retries": 5,
            }

            try:
                with YoutubeDL(opts) as ydl:
                    ydl.download([url])

            except DownloadError as e:
                msg = str(e).lower()

                if "subtitle" in msg or "caption" in msg:
                    print('captions : not found, skip video' + yt.id)
                    continue

                elif "429" in msg or "too many requests" in msg:
                    print("rate limited, sleeping")
                    raise

                elif "not available" in msg:
                    print('video not available, skip video' + yt.id)
                    continue

                elif "private" in msg:
                    print('private video, skip video' + yt.id)
                    continue

                else:
                    raise

        end = time.time()
        print(f"took {end - start} seconds")

        return data
