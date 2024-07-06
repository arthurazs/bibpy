import logging
import sys
from pathlib import Path

from rich.logging import RichHandler

from bibpy import parser

log_handler = RichHandler(rich_tracebacks=True, omit_repeated_times=False)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[log_handler])
logger = logging.getLogger(__name__)
INPUT_PATH = Path("input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

argv = sys.argv[1]
if argv == "-d":
    counter = 0
    for folder in INPUT_PATH.iterdir():
        for file in folder.iterdir():
            logger.info(file)
            with file.open(encoding="utf8") as bib:
                entry = parser.next_entry(bib)
                logger.critical(parser.parse_entry(entry))
                counter += 1
            logger.info("")
    logger.error(counter)
else:
    logger.error("Expected -m for merge, or -a for analyse")

