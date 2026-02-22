import argparse

import yt_concate.logging_config

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


def main():
    parser = argparse.ArgumentParser(description="Concatenate clips with the same keyword")

    parser.add_argument("-c", "--channel", type=str, help="Channel ID", required=True)
    parser.add_argument("-s", "--search", type=str, help="Search keyword", required=True)
    parser.add_argument("-d", "--download", type=int, help="Download limit", default=80)
    parser.add_argument("--concat", type=int, help="Concat limit", default=40)
    parser.add_argument(
        "--console-level",
        type=str.upper,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level for console handler"
    )

    parser.add_argument(
        "--file-level",
        type=str.upper,
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level for file handler"
    )

    args = parser.parse_args()

    inputs = {
        'channel_id': args.channel,
        'search_word': args.search,
        'download_videos_limit': args.download,
        'concat_videos_limit': args.concat,
        'console_level': args.console_level,
        'file_level': args.file_level,
    }

    yt_concate.logging_config.setup_logging(inputs)

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
