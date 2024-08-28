# bibpy

Merge bib files.

Expected tree structure. Put your files in `data/input/` separated by folder.
The parsed files will be placed at `data/output/`.

```bash
# example
 data
├──  input
│  ├──  acm
│  │  └──  acm.bib
│  ├──  ieee
│  │  └──  'IEEE Xplore Citation BibTeX Download 2024.7.2.10.24.25.bib'
│  ├──  scienceDirect
│  │  ├──  ScienceDirect_citations_1719926677787.bib
│  │  ├──  ScienceDirect_citations_1719926692726.bib
│  │  └──  ScienceDirect_citations_1719926704464.bib
│  └──  scopus
│     └──  scopus.bib
└──  output
   ├──  acm.bib
   ├──  ieee.bib
   ├──  scienceDirect.bib
   └──  scopus.bib
```

## Quickstart

Tested on Ubuntu 22.04.1 LTS with Python 3.12.3.

```bash
git clone https://github.com/arthurazs/bibpy
cd bibpy
make install-py
make merge
```
