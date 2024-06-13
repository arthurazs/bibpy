import logging
import sys
from pathlib import Path

from bibpy.analyser import analyse
from bibpy.merger import merge

INPUT_PATH = Path("input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

SCIENCE_DIRECT = "scienceDirect"


logging.basicConfig(
    level=logging.INFO, format=("[%(levelname)-7s] %(asctime)s | %(name)-15s:%(lineno)4d > %(message)s"),
)


if sys.argv[1] == "-m":
    merge(INPUT_PATH / SCIENCE_DIRECT, (OUTPUT_PATH / SCIENCE_DIRECT).with_suffix(".bib") )
else:
    analyse((OUTPUT_PATH / SCIENCE_DIRECT).with_suffix(".bib"))
