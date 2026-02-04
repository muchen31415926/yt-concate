from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import PipeLine
from yt_concate.utils import Utils

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        Postflight(),
    ]

    utils = Utils()

    p = PipeLine(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
