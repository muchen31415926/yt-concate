from yt_dlp import YoutubeDL

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('need to download video:', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            print('downloading' + url)
            opts = {
                "format": "mp4",
                "outtmpl": yt.video_filepath
            }

            with YoutubeDL(opts) as ydl:
                ydl.download([url])

        return data
