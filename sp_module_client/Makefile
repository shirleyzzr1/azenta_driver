.DEFAULT_GOAL := all
isort = isort sp_module_client
black = black --target-version py39 sp_module_client

.PHONY: format
format:
	$(isort)
	$(black)

.PHONY: lint
lint:
	$(black) --check --diff
	flake8 sp_module_client/
	pydocstyle sp_module_client/ --count



.PHONY: mypy
mypy:
	mypy --config-file setup.cfg --package sp_module_client/
	mypy --config-file setup.cfg sp_module_client/

.PHONY: all
all: format lint
