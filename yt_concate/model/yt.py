import os

from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class YT:
    def __init__(self, url):
        self.url = url
        self.id = self.get_video_id_from_url()
        self.caption_filepath = self.get_caption_filepath()
        self.video_filepath = self.get_video_filepath()
        self.captions = None

    def get_video_id_from_url(self):
        return self.url.split("v=")[-1].split("&")[0]

    def get_caption_filepath(self):
        return os.path.join(CAPTIONS_DIR, self.id + '.en.srt')

    def get_video_filepath(self):
        return os.path.join(VIDEOS_DIR, self.id + '.mp4')

    def __str__(self):
        return f'<YT({self.id})>'

    def __repr__(self):
        content = ' : '.join([
            f'id={str(self.id)}',
            f'caption_filepath={str(self.caption_filepath)}',
            f'video_filepath={str(self.video_filepath)}',
        ])
        return f'<YT({content})>'

