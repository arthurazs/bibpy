from io import StringIO
import pytest

from case_tests import ACM_STR, IEEE_STR, SCI_DIR_STR, SCOPUS_STR
from bibpy.model import Entry
from bibpy.parser import next_entry, parse_entry, get_category, get_key, get_next_element, get_element_key, get_element_value


TEST_DATA_HEADER = (
    # name, case, expected_tell
    ("acm", ACM_STR, 10),
    ("ieee", IEEE_STR, 10),
    ("scienceDirect", SCI_DIR_STR, 10),
    ("scopus", SCOPUS_STR, 44),
)

TEST_DATA_BODY = (
    # name, case, key, value, expected_key_tell, expected_value_tell
    ("acm", ACM_STR, "author", r"Ahmad, Waqar and Hasan, Osman and Tahar, Sofi\`{e}ne", 21, 76),
    ("ieee", IEEE_STR, "author", "Wang, Wenlong and Liu, Minghui and Zhao, Xicai and Yang, Gui", 22, 84),
    (
        "scienceDirect", SCI_DIR_STR, "title",
        "Research and implementation of virtual circuit test tool for smart substations", 20, 101,
    ),
    (
        "scopus", SCOPUS_STR, "author",
        "Chamana, Manohar and Bhatta, Rabindra and Schmitt, Konrad and Shrestha, Rajendra and Bayne, Stephen", 56, 158,
    ),
)

TEST_DATA_BODY_2ND_RUN = (
    # name, case, key, value, expected_tell
    (
        "acm", ACM_STR, "title",
        "Formal reliability and failure analysis of ethernet based communication networks in a smart grid substation",
        195,
    ),
    ("ieee", IEEE_STR, "journal", "Journal of Modern Power Systems and Clean Energy", 146),
    ("scienceDirect", SCI_DIR_STR, "journal", "Procedia Computer Science", 140),
    ("scopus", SCOPUS_STR, "title", "An Integrated Testbed for Power System Cyber-Physical Operations Training", 244),
)


@pytest.mark.parametrize("_name, case, expected_tell", TEST_DATA_HEADER)
def test_get_category(_name, case, expected_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    category = get_category(entry)
    assert category == "article"
    assert entry.tell() == expected_tell


@pytest.mark.parametrize("_name, case, expected_tell", TEST_DATA_HEADER)
def test_get_key(_name, case, expected_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    key = get_key(entry)
    assert key == "1"
    assert entry.tell() == expected_tell + 2


@pytest.mark.parametrize("_name, case, expected_key, _ev, expected_key_tell, _evt", TEST_DATA_BODY)
def test_get_next_element_key(_name, case, expected_key, _ev, expected_key_tell, _evt) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    key = get_element_key(entry)
    assert key == expected_key
    assert entry.tell() == expected_key_tell


@pytest.mark.parametrize("_name, case, _ek, expected_value, _ekt, expected_value_tell", TEST_DATA_BODY)
def test_get_next_element_value(_name, case, _ek, expected_value, _ekt, expected_value_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    get_element_key(entry)
    value = get_element_value(entry)
    assert value == expected_value
    assert entry.tell() == expected_value_tell


@pytest.mark.parametrize("_name, case, expected_key, expected_value, _ekt, expected_value_tell", TEST_DATA_BODY)
def test_get_next_element(_name, case, expected_key, expected_value, _ekt, expected_value_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    key, value = get_next_element(entry)
    assert key == expected_key
    assert value == expected_value
    assert entry.tell() == expected_value_tell


@pytest.mark.parametrize("_name, case, expected_key, expected_value, expected_tell", TEST_DATA_BODY_2ND_RUN)
def test_get_next_element_twice(_name, case, expected_key, expected_value, expected_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    get_category(entry)
    get_key(entry)
    get_next_element(entry)
    key, value = get_next_element(entry)
    assert key == expected_key
    assert value == expected_value
    assert entry.tell() == expected_tell


@pytest.mark.parametrize("_name, case, expected_tell", TEST_DATA_HEADER)
def test_parse_entry(_name, case, expected_tell) -> None:
    file = StringIO(case)
    entry = next_entry(file)
    parsed_entry = parse_entry(entry)
    assert parsed_entry == Entry("article", "1")
    assert entry.tell() == expected_tell + 2
