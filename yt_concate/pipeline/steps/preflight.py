import logging

from .step import Step

logger = logging.getLogger(__name__)


class Preflight(Step):
    def process(self, data, inputs, utils):
        logger.info('in preflight')
        utils.create_dirs()
