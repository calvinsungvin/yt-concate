from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.step import StepException

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():

    inputs = {
        'channel_id': CHANNEL_ID
    }

    steps = [
        GetVideoList()
    ]

    p = Pipeline(steps)
    p.run(inputs)

if __name__ == '__main__':
    main()


# for step in steps:
#     try:
#         step.process()
#     except StepException as e:
#         print(e)
#         break


# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(video_list)

