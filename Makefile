test: ## run tests quickly with the default Python
	pytest --cov=tests --cov=src --cov-fail-under=99

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build

clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache build .coverage htmlcov
