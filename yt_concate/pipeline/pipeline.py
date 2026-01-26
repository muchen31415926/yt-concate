from .steps.step import StepException


class PipeLine:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('exception happened to:', e)
                break
