import os

from yt_concate.settings import DOWNLOADS_DIR
from yt_concate.settings import CAPTIONS_DIR
from yt_concate.settings import VIDEOS_DIR


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exists(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def caption_file_exists(yt):
        path = yt.get_caption_filepath()
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def video_file_exists(yt):
        path = yt.get_video_filepath()
        return os.path.exists(path) and os.path.getsize(path) > 0
