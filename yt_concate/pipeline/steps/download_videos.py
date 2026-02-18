from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

from yt_dlp import YoutubeDL

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_list = self.filter_duplicate_videos(data)
        print('need to download video:', len(yt_list))

        self.download_until_limit(yt_list, inputs, utils)

        return data

    def download_until_limit(self, yt_list, inputs, utils):
        yt_iter = iter(yt_list)
        success_count = 0
        max_workers = 3
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            limit = inputs['download_video_limit']
            futures = self.submit_initial_tasks(executor, yt_iter, utils, max_workers)
            while futures:
                future = next(as_completed(futures))
                futures.remove(future)

                try:
                    if future.result():
                        success_count += 1
                except Exception as e:
                    print(e)

                if success_count >= limit:
                    break
                self.submit_next_tasks(executor, yt_iter, utils, futures)

    def submit_initial_tasks(self, executor, yt_iter, utils, max_workers):
        futures = []
        for _ in range(max_workers):
            yt = next(yt_iter, None)
            if yt is None:
                break
            futures.append(executor.submit(self.download_video, yt, utils))
        return futures

    def submit_next_tasks(self, executor, yt_iter, utils, futures):
        yt = next(yt_iter, None)
        if yt is None:
            return
        futures.append(executor.submit(self.download_video, yt, utils))

    def download_video(self, yt, utils):
        if utils.video_file_exists(yt):
            print(f'found existing video file for {yt.url}, skipping')
            return True

        self.do_download(yt)
        return True

    @staticmethod
    def filter_duplicate_videos(data):
        return list(dict.fromkeys(found.yt for found in data))

    @staticmethod
    def do_download(yt):
        url = yt.url
        print('downloading' + url)

        opts = {
            "format": "mp4",
            "outtmpl": yt.video_filepath,
        }

        with YoutubeDL(opts) as ydl:
            ydl.download([url])
