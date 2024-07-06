import logging
import sys
from pathlib import Path
from time import perf_counter_ns

from rich.logging import RichHandler

from bibpy import parser

log_handler = RichHandler(rich_tracebacks=True, omit_repeated_times=False)
logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[log_handler])
logger = logging.getLogger(__name__)
INPUT_PATH = Path("data/input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("data/output")
OUTPUT_PATH.mkdir(exist_ok=True)

NS2US = 1_000
US2MS = NS2US
NS2MS = NS2US * US2MS
TRUNC_AT = 21


argv = sys.argv[1]
if argv == "-p":
    logger.info("Starting...\n")
    counter_parse = 0
    start_parse = perf_counter_ns()
    for folder in INPUT_PATH.iterdir():
        counter_folder = 0
        start_folder = perf_counter_ns()
        logger.info('Parsing files from "%s/"...', folder)
        for file in folder.iterdir():
            with file.open(encoding="utf8") as bib:
                counter_file = 0
                start_file = perf_counter_ns()
                while True:
                    entry = parser.next_entry(bib)
                    if parser.is_empty(entry):
                        break
                    parsed_entry = parser.parse_entry(entry)
                    counter_file += 1
                msg = '"%s" took' % (("..." + file.name[-TRUNC_AT:]) if len(file.name) > TRUNC_AT else file.name)
                logger.info(
                    "%-32s %8.3f ms to parse %4d entries...",
                    msg, (perf_counter_ns() - start_file) / NS2MS, counter_file,
                )
                counter_folder += counter_file
        msg = f"{folder} took"
        logger.info(
            "%-32s %8.3f ms to parse %4d entries.\n",
            msg, (perf_counter_ns() - start_folder) / NS2MS, counter_folder,
        )
        counter_parse += counter_folder
    msg = "Took"
    logger.info("%-32s %8.3f ms to parse %4d entries!", msg, (perf_counter_ns() - start_parse) / NS2MS, counter_parse)
elif argv == "-d":
    logger.info("Calculating...")
    counter = 0
    start = perf_counter_ns()
    for folder in INPUT_PATH.iterdir():
        for file in folder.iterdir():
            with file.open(encoding="utf8") as bib:
                while True:
                    entry = parser.next_entry(bib)
                    if parser.is_empty(entry):
                        break
                    parsed_entry = parser.parse_entry(entry)
                    counter += 1
    elapsed = perf_counter_ns() - start
    logger.info("Took     %.3f ms to parse %d entries", elapsed / NS2MS, counter)
    logger.info("Averaged %.3f us per entry", (elapsed / NS2US) / counter)
else:
    logger.error("Expected -m for merge, or -a for analyse")

