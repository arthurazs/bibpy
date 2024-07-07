from bibpy.model import Entry

ACM_STR = r"""
@article{1,
author = {Ahmad, Waqar and Hasan, Osman and Tahar, Sofi\`{e}ne},
title = {Formal reliability and failure analysis of ethernet based communication networks in a smart grid substation},
year = {2020},
issue_date = {Feb 2020},
publisher = {Springer-Verlag},
address = {Berlin, Heidelberg},
volume = {32},
number = {1},
issn = {0934-5043},
url = {https://doi.org/10.1007/s00165-019-00503-1},
doi = {10.1007/s00165-019-00503-1},
journal = {Form. Asp. Comput.},
month = {feb},
pages = {71–111},
numpages = {41},
keywords = {Theorem proving, Higher-order logic, Fault tree, Reliability block diagrams, Smart grid}
}

@article{2,
author = {Formby, David and Walid, Anwar and Beyah, Raheem},
title = {A Case Study in Power Substation Network Dynamics},
year = {2017},
issue_date = {June 2017},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
volume = {1},
number = {1},
url = {https://doi.org/10.1145/3084456},
doi = {10.1145/3084456},
journal = {Proc. ACM Meas. Anal. Comput. Syst.},
month = {jun},
articleno = {19},
numpages = {24},
keywords = {scada, power grid, network characterization}
}
"""

ACM_ENTRY = Entry(
    category="article", key="1", author=("Ahmad, Waqar", "Hasan, Osman", r"Tahar, Sofi\`{e}ne"),
    title="Formal reliability and failure analysis "
          "of ethernet based communication networks in a smart grid substation",
    year=2020, issue_date="Feb 2020", publisher="Springer-Verlag", address="Berlin, Heidelberg", volume=32, number=1,
    issn="0934-5043", url="https://doi.org/10.1007/s00165-019-00503-1", doi="10.1007/s00165-019-00503-1",
    journal="Form. Asp. Comput.", month="feb", pages="71–111", numpages=41,
    keywords=("Theorem proving", "Higher-order logic", "Fault tree", "Reliability block diagrams", "Smart grid"),
)

ACM_PARSED = r"""@article{1,
address = {Berlin, Heidelberg},
author = {Ahmad, Waqar and Hasan, Osman and Tahar, Sofi\`{e}ne},
doi = {10.1007/s00165-019-00503-1},
issn = {0934-5043},
issue_date = {Feb 2020},
journal = {Form. Asp. Comput.},
keywords = {Theorem proving; Higher-order logic; Fault tree; Reliability block diagrams; Smart grid},
month = {feb},
number = {1},
numpages = {41},
pages = {71–111},
publisher = {Springer-Verlag},
title = {Formal reliability and failure analysis of ethernet based communication networks in a smart grid substation},
url = {https://doi.org/10.1007/s00165-019-00503-1},
volume = {32},
year = {2020}
}"""

IEEE_STR = """
@ARTICLE{1,
  author={Wang, Wenlong and Liu, Minghui and Zhao, Xicai and Yang, Gui},
  journal={Journal of Modern Power Systems and Clean Energy}, 
  title={Shared-network scheme of SMV and GOOSE in smart substation}, 
  year={2014},
  volume={2},
  number={4},
  pages={438-443},
  doi={10.1007/s40565-014-0073-z},
  ISSN={2196-5420},
  month={December},}@ARTICLE{2,
  author={Ali, Ikbal and Hussain, S. M. Suhail and Tak, Ashok and Ustun, Taha Selim},
  journal={IEEE Transactions on Industry Applications}, 
  title={Communication Modeling for Differential Protection in IEC-61850-Based Substations}, 
  year={2018},
  volume={54},
  number={1},
  pages={135-142},
  doi={10.1109/TIA.2017.2740301},
  ISSN={1939-9367},
  month={Jan},}
"""

IEEE_ENTRY = Entry(
    category="article", key="1", author=("Wang, Wenlong", "Liu, Minghui", "Zhao, Xicai", "Yang, Gui"),
    title="Shared-network scheme of SMV and GOOSE in smart substation",
    journal="Journal of Modern Power Systems and Clean Energy", year=2014, volume=2, number=4, pages="438-443",
    doi="10.1007/s40565-014-0073-z", issn="2196-5420", month="December",
)

IEEE_PARSED = """@article{1,
author = {Wang, Wenlong and Liu, Minghui and Zhao, Xicai and Yang, Gui},
doi = {10.1007/s40565-014-0073-z},
issn = {2196-5420},
journal = {Journal of Modern Power Systems and Clean Energy},
month = {December},
number = {4},
pages = {438-443},
title = {Shared-network scheme of SMV and GOOSE in smart substation},
volume = {2},
year = {2014}
}"""

SCI_DIR_STR = """
@article{1,
title = {Research and implementation of virtual circuit test tool for smart substations},
journal = {Procedia Computer Science},
volume = {183},
pages = {197-204},
year = {2021},
note = {Proceedings of the 10th International Conference of Information and Communication Technology},
issn = {1877-0509},
doi = {https://doi.org/10.1016/j.procs.2021.02.050},
url = {https://www.sciencedirect.com/science/article/pii/S1877050921005159},
author = {Jin Wang and Zengkai Wang},
keywords = {Smart substation, IEC61850, virtual circuit},
}
@article{2,
title = {Comparative analysis of the DAQ cards-based and the IEC 61850-based real time simulations in the matlab/simulink environment for power system protections},
journal = {Electric Power Systems Research},
volume = {192},
pages = {107000},
year = {2021},
issn = {0378-7796},
doi = {https://doi.org/10.1016/j.epsr.2020.107000},
url = {https://www.sciencedirect.com/science/article/pii/S0378779620307987},
author = {M. Krakowski and K. Kurek and Ł. Nogal},
keywords = {Hardware-in-the-loop, Real time simulations, DAQ Cards, IEC 61850, Real time Linux},
}
"""

SCI_DIR_PARSED = """@article{1,
author = {Jin Wang and Zengkai Wang},
doi = {https://doi.org/10.1016/j.procs.2021.02.050},
issn = {1877-0509},
journal = {Procedia Computer Science},
keywords = {Smart substation; IEC61850; virtual circuit},
note = {Proceedings of the 10th International Conference of Information and Communication Technology},
pages = {197-204},
title = {Research and implementation of virtual circuit test tool for smart substations},
url = {https://www.sciencedirect.com/science/article/pii/S1877050921005159},
volume = {183},
year = {2021}
}"""

SCI_DIR_ENTRY = Entry(
    category="article", key="1", author=("Jin Wang", "Zengkai Wang"),
    title="Research and implementation of virtual circuit test tool for smart substations",
    journal="Procedia Computer Science", year=2021, keywords=("Smart substation", "IEC61850", "virtual circuit"),
    volume=183, pages="197-204", doi="https://doi.org/10.1016/j.procs.2021.02.050", issn="1877-0509",
    url="https://www.sciencedirect.com/science/article/pii/S1877050921005159",
    note="Proceedings of the 10th International Conference of Information and Communication Technology",
)

SCOPUS_STR = """
Scopus
EXPORT DATE: 02 July 2024

@ARTICLE{1,
	author = {Chamana, Manohar and Bhatta, Rabindra and Schmitt, Konrad and Shrestha, Rajendra and Bayne, Stephen},
	title = {An Integrated Testbed for Power System Cyber-Physical Operations Training},
	year = {2023},
	journal = {Applied Sciences (Switzerland)},
	volume = {13},
	number = {16},
	doi = {10.3390/app13169451},
	url = {https://www.scopus.com/inward/record.uri?eid=2-s2.0-85169099191&doi=10.3390%2fapp13169451&partnerID=40&md5=17b896c1c440787efcbc5d384003d31c},
	affiliations = {National Wind Institute, Texas Tech University, Lubbock, 79401, TX, United States; Electrical and Computer Engineering Department, Texas Tech University, Lubbock, 79401, TX, United States},
	author_keywords = {cyberattacks; cyber–physical systems; education; power systems; real-time testbed; smart grids},
	correspondence_address = {R. Bhatta; National Wind Institute, Texas Tech University, Lubbock, 79401, United States; email: rabindra.bhatta(at)ttu.edu},
	publisher = {Multidisciplinary Digital Publishing Institute (MDPI)},
	issn = {20763417},
	language = {English},
	abbrev_source_title = {Appl. Sci.},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 3; All Open Access, Gold Open Access}
}

@ARTICLE{2,
	author = {Tabish, Nimra and Chaur-Luh, Tsai},
	title = {Maritime Autonomous Surface Ships: A Review of Cybersecurity Challenges, Countermeasures, and Future Perspectives},
	year = {2024},
	journal = {IEEE Access},
	volume = {12},
	pages = {17114 – 17136},
	doi = {10.1109/ACCESS.2024.3357082},
	url = {https://www.scopus.com/inward/record.uri?eid=2-s2.0-85184014406&doi=10.1109%2fACCESS.2024.3357082&partnerID=40&md5=45e865ea0976a8c03ec29d3410837818},
	affiliations = {National Kaohsiung University of Science and Technology (NKUST), Department of Maritime Science and Technology, Kaohsiung City, 81157, Taiwan},
	author_keywords = {Cyber security; cyberattack detection; intrusion detection systems; marine autonomous surface ships; prevention and countermeasures},
	keywords = {Computer crime; Cryptography; Cybersecurity; Interactive computer systems; Intrusion detection; Ships; Autonomous Vehicles; Cyber security; Cyber-attacks; Cyberattack detection; Guideline; Intrusion Detection Systems; Intrusion-Detection; Marine autonomous surface ship; Marine vehicles; Prevention and countermeasure; Real - Time system; Surface ship; Real time systems},
	correspondence_address = {T. Chaur-Luh; National Kaohsiung University of Science and Technology (NKUST), Department of Maritime Science and Technology, Kaohsiung City, 81157, Taiwan; email: chaurluh(at)nkust.edu.tw},
	publisher = {Institute of Electrical and Electronics Engineers Inc.},
	issn = {21693536},
	language = {English},
	abbrev_source_title = {IEEE Access},
	type = {Article},
	publication_stage = {Final},
	source = {Scopus},
	note = {Cited by: 0; All Open Access, Gold Open Access}
}
"""

SCOPUS_PARSED = """@article{1,
abbrev_source_title = {Appl. Sci.},
affiliations = {National Wind Institute, Texas Tech University, Lubbock, 79401, TX, United States; Electrical and Computer Engineering Department, Texas Tech University, Lubbock, 79401, TX, United States},
author = {Chamana, Manohar and Bhatta, Rabindra and Schmitt, Konrad and Shrestha, Rajendra and Bayne, Stephen},
author_keywords = {cyberattacks; cyber–physical systems; education; power systems; real-time testbed; smart grids},
correspondence_address = {R. Bhatta; National Wind Institute, Texas Tech University, Lubbock, 79401, United States; email: rabindra.bhatta(at)ttu.edu},
doi = {10.3390/app13169451},
issn = {20763417},
journal = {Applied Sciences (Switzerland)},
language = {English},
note = {Cited by: 3; All Open Access, Gold Open Access},
number = {16},
publication_stage = {Final},
publisher = {Multidisciplinary Digital Publishing Institute (MDPI)},
source = {Scopus},
title = {An Integrated Testbed for Power System Cyber-Physical Operations Training},
url = {https://www.scopus.com/inward/record.uri?eid=2-s2.0-85169099191&doi=10.3390%2fapp13169451&partnerID=40&md5=17b896c1c440787efcbc5d384003d31c},
volume = {13},
year = {2023}
}"""

SCOPUS_ENTRY = Entry(
    category="article", key="1",
    author=("Chamana, Manohar", "Bhatta, Rabindra", "Schmitt, Konrad", "Shrestha, Rajendra", "Bayne, Stephen"),
    title="An Integrated Testbed for Power System Cyber-Physical Operations Training",
    journal="Applied Sciences (Switzerland)", year=2023, volume=13, number=16, doi="10.3390/app13169451",
    issn="20763417", publisher="Multidisciplinary Digital Publishing Institute (MDPI)",
    url="https://www.scopus.com/inward/record.uri?eid=2-s2.0-85169099191&doi="
        "10.3390%2fapp13169451&partnerID=40&md5=17b896c1c440787efcbc5d384003d31c",
    note="Cited by: 3; All Open Access, Gold Open Access", 
    affiliations=(
        "National Wind Institute, Texas Tech University, Lubbock, 79401, TX, United States",
        "Electrical and Computer Engineering Department, Texas Tech University, Lubbock, 79401, TX, United States",
    ),
    author_keywords=(
        "cyberattacks", "cyber–physical systems", "education", "power systems", "real-time testbed", "smart grids",
    ),
    correspondence_address=(
        "R. Bhatta",
        "National Wind Institute, Texas Tech University, Lubbock, 79401, United States",
        "email: rabindra.bhatta(at)ttu.edu",
    ),
    language="English", abbrev_source_title="Appl. Sci.", publication_stage="Final", source="Scopus",
)
