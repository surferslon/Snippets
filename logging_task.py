import logging
import glob
import os


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        files = ["\033[1;%dm" % 32 + file + "\033[0m" if file.endswith('.py') else file for file in record.msg]
        record.msg = '\n'.join(files)
        return logging.Formatter.format(self, record)


handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(ColoredFormatter('%(message)s'))

logger = logging.getLogger('log_colored')
logger.setLevel(logging.INFO)
logger.addHandler(handler)


if __name__ == '__main__':
    files = glob.glob('*.*')
    logger.info(files)
