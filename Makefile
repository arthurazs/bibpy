bin := .venv/bin

# prod
install-py:
	uv venv
	uv pip install -e .[dev]

install-r:
	Rscript -e 'install.packages(c("ggplot2", "tidyr"))'

merge:
	$(bin)/python -m bibpy -m

plot:
	Rscript scripts/pub_date.r


# dev
mypy:
	$(bin)/mypy .

ruff:
	$(bin)/ruff check .

pytest:
	$(bin)/pytest

ruff-fix:
	$(bin)/ruff check --fix .

