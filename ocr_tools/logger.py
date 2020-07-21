import logging


class Log:
    __logger = None

    @staticmethod
    def _get_level(level) -> int:
        switcher = {0: logging.NOTSET, 1: logging.DEBUG, 2: logging.INFO}
        if level > 3:
            level = 3

        return switcher.get(level)

    @staticmethod
    def initialize(level):
        if Log.__logger is None:
            logger = logging.getLogger(__name__)
            logger.setLevel(level)
            Log.__logger = logger
        return Log.__logger

    @staticmethod
    def get_logger() -> logging.Logger:
        return Log.__logger
