import logging
import glob
import os


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        record.msg = "\033[1;%dm" % 32 + record.msg + "\033[0m"
        return logging.Formatter.format(self, record)


handler_color = logging.StreamHandler()
handler_color.setLevel(logging.INFO)
handler_color.setFormatter(ColoredFormatter('%(message)s'))

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(message)s'))

logger_color = logging.getLogger('log_colored')
logger_color.setLevel(logging.INFO)
logger_color.addHandler(handler_color)

logger_plain = logging.getLogger('log_plain')
logger_plain.setLevel(logging.INFO)
logger_plain.addHandler(handler)


def log_files():
    files = glob.glob('*.*')
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        if file_ext == '.py':
            logger_color.info(file)
        else:
            logger_plain.info(file)


if __name__ == '__main__':
    log_files()
