from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import PipeLine
from yt_concate.utils import Utils

CHANNEL_ID = 'UCRa323qW1-btI2PCU_U7upQ'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'Prime',
        'download_video_limit': 80,
        'concat_videos_limit': 40,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]

    utils = Utils()

    p = PipeLine(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
