import logging
import sys
from pathlib import Path
from time import perf_counter_ns
from typing import TYPE_CHECKING

from rich.logging import RichHandler

from bibpy import parser

if TYPE_CHECKING:
    from bibpy.model import Entry

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
if argv == "-m":
    logger.info("Opening folders...")
    counter = 0
    start = perf_counter_ns()
    for folder in INPUT_PATH.iterdir():
        logger.info("Opening %s...", folder)
        entries: dict[str, "Entry"] = {}
        for file in folder.iterdir():
            logger.info("Parsing %s...", file)
            with file.open(encoding="utf8") as bib_input:
                while True:
                    entry = parser.next_entry(bib_input)
                    if parser.is_empty(entry):
                        break
                    parsed_entry = parser.parse_entry(entry)
                    if parsed_entry.code in entries:
                        logger.warning("Duplicated entry, skipping %s", parsed_entry.code)
                        logger.debug(entries[parsed_entry.code])
                        logger.debug(parsed_entry)
                    else:
                        entries[parsed_entry.code] = parsed_entry
                    counter += 1
        with (OUTPUT_PATH / folder.name).with_suffix(".bib").open("w") as bib_output:
            bib_output.writelines(str(entry) + "\n" for entry in entries.values())
        logger.info("")
    elapsed = perf_counter_ns() - start
    logger.info("Took     %7.3f ms to parse %d entries", elapsed / NS2MS, counter)
    logger.info("Averaged %7.3f ms per entry", (elapsed / NS2MS) / counter)
else:
    logger.error("Expected -m for merge")

