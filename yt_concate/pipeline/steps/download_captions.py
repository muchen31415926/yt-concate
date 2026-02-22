import time
import concurrent.futures
import logging

from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError

from .step import Step
from .step import StepException

logger = logging.getLogger(__name__)


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        max_workers = 5
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = [
                executor.submit(self.download_caption, yt, utils)
                for yt in data
            ]

            for future in concurrent.futures.as_completed(futures):
                future.result()

        end = time.time()
        logger.info(f"took {end - start} seconds")

        return data

    def download_caption(self, yt, utils):
        if self.caption_exists(yt, utils):
            logger.debug('found existing caption file')
            return

        self.do_download(yt)

    @staticmethod
    def do_download(yt):
        logger.debug('downloading captions for ' + yt.id)
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
                logger.warning('captions : not found, skip captions' + yt.id)
                return

            elif "429" in msg or "too many requests" in msg:
                logger.warning("rate limited, sleeping")
                raise

            elif "not available" in msg:
                logger.warning('video not available, skip subtitle' + yt.id)
                return

            elif "private" in msg:
                logger.warning('private video, skip subtitle' + yt.id)
                return

            else:
                raise

    @staticmethod
    def caption_exists(yt, utils):
        return utils.caption_file_exists(yt)
