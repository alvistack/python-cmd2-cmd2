# Simple Makefile for use with a uv-based development environment
.PHONY: install
install: ## Install the virtual environment
	@echo "🚀 Creating virtual environment"
	@uv sync

.PHONY: check
check: ## Run code quality tools.
	@echo "🚀 Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "🚀 Linting code: Running pre-commit"
	@uv run pre-commit run -a
	@echo "🚀 Static type checking: Running mypy"
	@uv run mypy

.PHONY: test
test: ## Test the code with pytest.
	@echo "🚀 Testing code: Running pytest"
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml tests_isolated

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

.PHONY: docs
docs: ## Build and serve the documentation
	@uv run mkdocs serve

.PHONY: build
build: clean-build ## Build wheel file
	@echo "🚀 Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "🚀 Removing build artifacts"
	@uv run python -c "import shutil; import os; shutil.rmtree('dist') if os.path.exists('dist') else None"

.PHONY: tag
tag: ## Add a Git tag and push it to origin with syntax: make tag TAG=tag_name
	@echo "🚀 Creating git tag: ${TAG}"
	@git tag -a ${TAG}
	@echo "🚀 Pushing tag to origin: ${TAG}"
	@git push origin ${TAG}

.PHONY: validate-tag
validate-tag: ## Check to make sure that a tag exists for the current HEAD and it looks like a valid version number
	@echo "🚀 Validating version tag"
	@uv run inv validatetag

.PHONY: publish-test
publish-test: validatetag build ## Test publishing a release to PyPI.
	@echo "🚀 Publishing: Dry run."
	@uvx twine upload --repository testpypi dist/*

.PHONY: publish
publish: validatetag build ## Publish a release to PyPI.
	@echo "🚀 Publishing."
	@uvx twine upload --repository-url https://upload.pypi.org/legacy/ dist/*

.PHONY: help
help:
	@uv run python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
