import logging
from typing import TYPE_CHECKING

from bibpy.parser import load_entries

if TYPE_CHECKING:
    from pathlib import Path

logger = logging.getLogger(__name__)
MIN_NUMBER_OF_PAPERS = 100


def analyse(file_path: "Path") -> None:
    entries, _ = load_entries(file_path.open())
    journals = set()
    years: dict[int, int] = {}
    for entry in entries.values():
        journals.add(entry.journal)
        if entry.year is None:
            msg = f"Missing year: {entry}"
            raise ValueError(msg)
        try:
            years[entry.year] += 1
        except KeyError:
            years[entry.year] = 1
    logger.info("Total entries: %d", len(entries))
    logger.info("Unique journals: %d", len(journals))
    logger.info("Year count:")
    for year, count in sorted(years.items(), key=lambda item: item[1], reverse=True):
        if count < MIN_NUMBER_OF_PAPERS:
            continue
        logger.info("- %d: %d", year, count)
