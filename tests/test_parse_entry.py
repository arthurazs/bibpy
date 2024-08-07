import os
from io import StringIO
from typing import TYPE_CHECKING

import pytest
from bibpy.parser import (
    EMPTY_CHARS,
    end_of_file,
    get_category,
    get_element_key,
    get_element_value,
    get_key,
    get_next_element,
    is_empty,
    next_entry,
    parse_entry,
)

from tests.case_tests import (
    ACM_ENTRY,
    ACM_PARSED,
    ACM_STR,
    IEEE_ENTRY,
    IEEE_PARSED,
    IEEE_STR,
    SCI_DIR_ENTRY,
    SCI_DIR_PARSED,
    SCI_DIR_STR,
    SCOPUS_ENTRY,
    SCOPUS_PARSED,
    SCOPUS_STR,
)

if TYPE_CHECKING:
    from bibpy.model import Entry


TEST_DATA_HEADER = (
    # case, expected_tell
    (ACM_STR, 10),
    (IEEE_STR, 10),
    (SCI_DIR_STR, 10),
    (SCOPUS_STR, 44),
)

TEST_DATA_ENTRY = (
    # case, expected_tell, expected_entry
    (ACM_STR, 621, ACM_ENTRY),
    (IEEE_STR, 357, IEEE_ENTRY),
    (SCI_DIR_STR, 542, SCI_DIR_ENTRY),
    (SCOPUS_STR, 1273, SCOPUS_ENTRY),
)

TEST_DATA_BODY = (
    # case, key, value, expected_key_tell, expected_value_tell
    (ACM_STR, "author", r"Ahmad, Waqar and Hasan, Osman and Tahar, Sofi\`{e}ne", 21, 76),
    (IEEE_STR, "author", "Wang, Wenlong and Liu, Minghui and Zhao, Xicai and Yang, Gui", 22, 84),
    (SCI_DIR_STR, "title", "Research and implementation of virtual circuit test tool for smart substations", 20, 101),
    (
        SCOPUS_STR, "author",
        "Chamana, Manohar and Bhatta, Rabindra and Schmitt, Konrad and Shrestha, Rajendra and Bayne, Stephen",
        56, 158,
    ),
)

TEST_DATA_BODY_2ND_RUN = (
    # case, key, value, expected_tell
    (
        ACM_STR, "title",
        "Formal reliability and failure analysis of ethernet based communication networks in a smart grid substation",
        195,
    ),
    (IEEE_STR, "journal", "Journal of Modern Power Systems and Clean Energy", 146),
    (SCI_DIR_STR, "journal", "Procedia Computer Science", 140),
    (SCOPUS_STR, "title", "An Integrated Testbed for Power System Cyber-Physical Operations Training", 244),
)

TEST_DATA_PARSED = (
    # case, parsed_str
    (ACM_STR, ACM_PARSED),
    (IEEE_STR, IEEE_PARSED),
    (SCI_DIR_STR, SCI_DIR_PARSED),
    (SCOPUS_STR, SCOPUS_PARSED),
)


@pytest.mark.parametrize(("case", "expected_tell"), TEST_DATA_HEADER)
def test_get_category(case: str, expected_tell: int) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    category = get_category(entry)
    assert category == "article"
    assert entry.tell() == expected_tell


@pytest.mark.parametrize(("case", "expected_tell"), TEST_DATA_HEADER)
def test_get_key(case: str, expected_tell: int) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    key = get_key(entry)
    assert key == "1"
    assert entry.tell() == expected_tell + 2


@pytest.mark.usefixtures("expected_value", "expected_value_tell")
@pytest.mark.parametrize(
    ("case", "expected_key", "expected_value", "expected_key_tell", "expected_value_tell"), TEST_DATA_BODY,
)
def test_get_next_element_key(case: str, expected_key: str, expected_key_tell: int) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    key = get_element_key(entry)
    assert key == expected_key
    assert entry.tell() == expected_key_tell


@pytest.mark.usefixtures("expected_key", "expected_key_tell")
@pytest.mark.parametrize(
    ("case", "expected_key", "expected_value", "expected_key_tell", "expected_value_tell"), TEST_DATA_BODY,
)
def test_get_next_element_value(
    case: str,
    expected_value: str,
    expected_value_tell: int,
) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    get_element_key(entry)
    value = get_element_value(entry)
    assert value == expected_value
    assert entry.tell() == expected_value_tell


@pytest.mark.usefixtures("expected_key_tell")
@pytest.mark.parametrize(
    ("case", "expected_key", "expected_value", "expected_key_tell", "expected_value_tell"), TEST_DATA_BODY,
)
def test_get_next_element(case: str, expected_key: str, expected_value: str, expected_value_tell: int) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    key, value = get_next_element(entry)
    assert key == expected_key
    assert value == expected_value
    assert entry.tell() == expected_value_tell


@pytest.mark.parametrize(("case", "expected_key", "expected_value", "expected_tell"), TEST_DATA_BODY_2ND_RUN)
def test_get_next_element_twice(
    case: str,
    expected_key: str,
    expected_value: str,
    expected_tell: int,
) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    get_next_element(entry)
    key, value = get_next_element(entry)
    assert key == expected_key
    assert value == expected_value
    assert entry.tell() == expected_tell


@pytest.mark.parametrize(("case", "expected_tell", "expected_entry"), TEST_DATA_ENTRY)
def test_parse_entry(case: str, expected_tell: int, expected_entry: "Entry") -> None:
    file = StringIO(case)
    entry = next_entry(file)
    parsed_entry = parse_entry(entry)
    assert parsed_entry == expected_entry
    assert entry.tell() == expected_tell

@pytest.mark.parametrize(("case", "expected_str"), TEST_DATA_PARSED)
def test_to_string(case: str, expected_str: str) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    parsed_entry = parse_entry(entry)
    assert str(parsed_entry) == expected_str

def test_end_of_file() -> None:
    entry = next_entry(StringIO(EMPTY_CHARS))
    entry.seek(0, os.SEEK_END)
    assert end_of_file(entry)

def test_empty_entry() -> None:
    entry = next_entry(StringIO(EMPTY_CHARS))
    assert is_empty(entry)

