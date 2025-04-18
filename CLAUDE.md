# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build/Lint/Test Commands
- Install development version: `uv pip install -e .`
- Run all tests: `pytest`
- Run specific test: `pytest tests/test_file.py::TestClass::test_method`
- Run tests with coverage: `pytest --cov=src`
- Lint code: `ruff check .`
- Format code: `ruff format .`

## Code Style Guidelines
- Use Python 3.12+ features
- Require type hints for all function parameters and return values
- Follow PEP 8 naming conventions (snake_case for variables/functions, PascalCase for classes)
- Use Pydantic for data models and configuration
- Organize imports: standard library, third-party, local (alphabetized within groups)
- Use proper exception handling with specific exception types
- Document classes and public methods with docstrings
- Use XDG specifications for file locations
- Keep code simple and focused on configuration management tasks
- Follow the src/ layout structure for package organization