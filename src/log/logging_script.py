import logging
import inspect
import os

class EndOfNameFilter(logging.Filter):
    def filter(self, record):
        record.trunc_name = record.name[-35:]
        return True


def get_logger(name=None, logging_format=None):
    if not logging_format:
        json_logging_format = """{"class_name": "%(name)s", "time": "%(asctime)s", "level": "%(levelname)s", "message": "%(message)s"}"""
        logging_format = (
            "%(trunc_name)35.35s - %(asctime)-15s - %(levelname)5.5s: %(message)s"
        )
    if not name:
        name = os.path.basename(inspect.stack()[1].filename)
    logger = logging.getLogger(name)
    if not logger.handlers:
        sh = logging.StreamHandler()
        sh.setFormatter(logging.Formatter(logging_format))
        logger.addHandler(sh)
        sh.addFilter(EndOfNameFilter())
        #lf = logging.FileHandler(filename="log//logging.log", mode="w")
        #lf.setFormatter(logging.Formatter(json_logging_format))
        #logger.addHandler(lf)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger