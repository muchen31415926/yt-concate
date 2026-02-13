from yt_dlp import YoutubeDL

from .step import Step


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_list = list(dict.fromkeys(found.yt for found in data))
        print('need to download video:', len(yt_list))

        processed_count = 0
        for yt in yt_list:
            url = yt.url

            if processed_count >= inputs['download_video_limit']:
                break

            if utils.video_file_exists(yt):
                print(f'found existing video file for {url}, skipping')
                processed_count += 1
                continue

            print('downloading' + url)
            opts = {
                "format": "mp4",
                "outtmpl": yt.video_filepath,
            }

            with YoutubeDL(opts) as ydl:
                ydl.download([url])
                processed_count += 1

        return data
