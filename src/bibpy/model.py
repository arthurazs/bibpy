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
    volume: int | str | None = None
    number: int | str | None = None
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

    @property
    def code(self: "Entry") -> str:
        return self.key + "-" + (self.issn if self.issn else "None") + "-" + (self.doi if self.doi else "None")

    @staticmethod
    def _parse_value(key: str, value: str) -> str | tuple[str, ...] | None | int:
        if value == "":
            return None
        if key == "author":
            return tuple(map(str.strip, value.split("and")))
        if key in ("keywords", "author_keywords"):
            comma = value.count(",")
            sep = ",;"[comma < value.count(";")]
            return tuple(map(str.strip, value.split(sep)))
        if key in ("affiliations", "correspondence_address"):
            return tuple(map(str.strip, value.split(";")))
        if key in ("year", "volume", "number", "numpages"):
            try:
                return int(value)
            except ValueError:
                logger.warning('Could not parse "%s" = "%s" to int, falling back to str', key, value)
                return value
        return value

    def add_element(self: "Entry", key: str, value: str) -> None:
        try:
            if key == "type":
                if self.category != value.lower():
                    logger.warning('Entry category "%s" differs from element type "%s"', self.category, value.lower())
            else:
                try:
                    parsed_value = self._parse_value(key, value)
                except ValueError:
                    logger.error(self.title)
                    raise
                setattr(self, key, parsed_value)
        except AttributeError:
            logger.warning('Entry doesn\'t have an attribute "%s", skipping value "%s"', key, value)
            raise

    def __str__(self: "Entry") -> str:
        entry = "@%s{%s,\n" % (self.category, self.key)  # noqa: UP031
        for attr in dir(self):
            if attr[0] == "_":
                continue
            if attr in ("add_element", "category", "key", "type", "code"):
                continue
            value = getattr(self, attr)
            if value is None:
                continue
            if attr == "author":
                parsed_value = " and ".join(value)
            elif attr in ("keywords", "affiliations", "author_keywords", "correspondence_address"):
                parsed_value = "; ".join(value)
            elif attr in ("year", "volume", "number", "numpages"):
                parsed_value = str(value)
            else:
                parsed_value = value
            entry += attr + " = {" + parsed_value + "},\n"
        return entry.removesuffix(",\n") + "\n}"

