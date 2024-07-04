from io import StringIO

from case_tests import ACM_STR, IEEE_STR, SCI_DIR_STR, SCOPUS_STR
from bibpy.model2 import Entry


ACM_FILE = StringIO(ACM_STR)
IEEE_FILE = StringIO(IEEE_STR)
SCI_DIR_FILE = StringIO(SCI_DIR_STR)
SCOPUS_FILE = StringIO(SCOPUS_STR)

IEEE_ENTRY1 = Entry(
    author=("Wang, Wenlong", "Liu, Minghui", "Zhao, Xicai", "Yang, Gui"),
    journal="Journal of Modern Power Systems and Clean Energy",
    title="Shared-network scheme of SMV and GOOSE in smart substation", 
    year=2014,
    volume=2,
    number=4,
    pages="438-443",
    doi="10.1007/s40565-014-0073-z",
    issn="2196-5420",
    month="December",
)

IEEE_ENTRY2 = Entry(
    author=("Ali, Ikbal", "Hussain, S. M. Suhail", "Tak, Ashok",  "Ustun, Taha Selim"),
    journal="IEEE Transactions on Industry Applications",
    title="Communication Modeling for Differential Protection in IEC-61850-Based Substations",
    year=2018,
    volume=54,
    number=1,
    pages="135-142",
    doi="10.1109/TIA.2017.2740301",
    issn="1939-9367",
    month="Jan",
)


def test_parse_entry() -> None:
    assert False

# def test_load() -> None:
#     entries = bibpy.load(IEEE_EXAMPLE)
#     assert len(entries) == 2
#     assert entries == (IEEE_ENTRY1, IEEE_ENTRY2)

