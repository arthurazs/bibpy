import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass(slots=True, kw_only=True)
class Entry:
    category: str
    key: str
    author: tuple[str, ...] | None = None
    abstract: str | None = None
    title: str | None = None
    journal: str | None = None
    year: int | None = None
    keywords: tuple[str, ...] | None = None
    volume: int | None = None
    number: int | None = None
    pages: str | None = None
    doi: str | None = None
    issn: str | None = None
    month: str | None = None
    issue_date: str | None = None
    publisher: str | None = None
    address: str | None = None
    url: str | None = None
    numpages: int | None = None
    articleno: int | None = None
    note: str | None = None
    affiliations: tuple[str, ...] | None = None
    author_keywords: tuple[str, ...] | None = None
    correspondence_address: tuple[str, ...] | None = None
    language: str | None = None
    abbrev_source_title: str | None = None
    publication_stage: str | None = None
    source: str | None = None
    coden: str | None = None
    pmid: int | None = None

    def add_element(self: "Entry", key: str, value: str) -> None:
        try:
            if key == "type":
                if self.category != value.lower():
                    logger.warning('Entry category "%s" differs from element type "%s"', self.category, value.lower())
            else:
                setattr(self, key, value)
        except AttributeError:
            logger.warning('Entry doesn\'t have an attribute "%s", skipping value "%s"', key, value)
            raise

