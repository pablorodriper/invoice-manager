import sys

import regex as re
from loguru import logger


def set_logger():
    level = "DEBUG"

    logger.remove()
    logger_format = "<level>{time:YYYY-MM-DD HH:mm:ss.SSS}</level> | " \
                    "<level>{level: <8}</level> | " \
                    "<level>{message}</level>"
                    # "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan>"
    
    # STDOUT logger
    logger.add(sys.stderr, colorize=True, format=logger_format, level=level)


def search_regex(text, regex):
    
    if found_text := re.search(regex, text):
        # print(found_text.group(0))
        return found_text.group(0)

    return None