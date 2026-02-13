from moviepy import VideoFileClip
from moviepy import concatenate_videoclips

from .step import Step

class EditVideo(Step):
    def process(self, data, inputs, utils):
        clips = []
        for found in data:
            start, end = self.parse_caption_time(found.time)

            clip = (
                VideoFileClip(found.yt.video_filepath)
                .subclipped(start, end)
            )
            clips.append(clip)

            if len(clips) >= inputs['concat_videos_limit']:
                break

        output_filepath = utils.get_output_filepath(inputs['channel_id'], inputs['search_word'])

        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile(output_filepath)

    def parse_caption_time(self, caption_time):
        start, end = caption_time.split(' --> ')
        return self.parse_time_str(start), self.parse_time_str(end)

    @staticmethod
    def parse_time_str(time_str):
        h, m, s = time_str.split(':')
        s, ms = s.split(',')
        return int(h), int(m), (int(s) + int(ms) / 1000)
