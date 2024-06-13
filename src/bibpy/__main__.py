import logging
from pathlib import Path

from bibpy.merger import merge

INPUT_PATH = Path("input")
INPUT_PATH.mkdir(exist_ok=True)

OUTPUT_PATH = Path("output")
OUTPUT_PATH.mkdir(exist_ok=True)

SCIENCE_DIRECT = "scienceDirect"


logging.basicConfig(
    level=logging.INFO, format=("[%(levelname)-7s] %(asctime)s | %(name)-15s:%(lineno)4d > %(message)s"),
)


merge(INPUT_PATH / SCIENCE_DIRECT, (OUTPUT_PATH / SCIENCE_DIRECT).with_suffix(".bib") )

