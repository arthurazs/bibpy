from bibpy.merger import merge
from bibpy.analyser import pub_date

import sys

from pathlib import Path
import logging
from rich.logging import RichHandler
log_handler = RichHandler(rich_tracebacks=True, omit_repeated_times=False)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[log_handler])
logger = logging.getLogger(__name__)
INPUT_PATH = Path("input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

argv = sys.argv[1]
if argv == "-m":
    merge(INPUT_PATH, OUTPUT_PATH)
elif argv == "-a":
    pub_date(OUTPUT_PATH)
else:
    logger.error("Expected -m for merge, or -a for analyse")
