# prod
install-py:
	uv venv
	uv pip install -e .[dev]

install-r:
	Rscript -e 'install.packages(c("ggplot2", "tidyr"))'

merge:
	.venv/bin/python -m bibpy -m

plot:
	Rscript scripts/pub_date.r


# dev
mypy:
	.venv/bin/mypy .

ruff:
	.venv/bin/ruff check .

pytest:
	.venv/bin/pytest

ruff-fix:
	.venv/bin/ruff check --fix .

