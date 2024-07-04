install-py:
	uv venv
	uv pip install -e .[dev]

install-r:
	Rscript -e 'install.packages(c("ggplot2", "tidyr"))'

merge:
	.venv/bin/python -m bibpy -m

analyse:
	.venv/bin/python -m bibpy -a

plot:
	Rscript scripts/pub_date.r
