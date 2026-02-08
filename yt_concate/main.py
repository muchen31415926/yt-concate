from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import PipeLine
from yt_concate.utils import Utils

CHANNEL_ID = 'UCtI0Hodo5o5dUb67FeUjDeA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'launch',
    }

    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]

    utils = Utils()

    p = PipeLine(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
