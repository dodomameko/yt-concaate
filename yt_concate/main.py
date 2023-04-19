from yt_concate.pipeline.Step.Get_Video_List import GetVideoList
from yt_concate.pipeline.Step.step import StepException
from yt_concate.pipeline.Pipeline import Pipeline

CHANNEL_ID = 'UC32mYgIHS-e3C3Eyd2tRw6g'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()


