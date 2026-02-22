import logging

from .step import Step

logger = logging.getLogger(__name__)


class Postflight(Step):
    def process(self, data, inputs, utils):
        logger.info('in postflight')
