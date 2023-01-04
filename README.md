# COMP0035 Content to support the testing activity in the lecture
This is a simple example designed to introduce the core concepts.

Further examples are in the problem based learning class.

## Setup
1. Clone the repository and open it in your preferred IDE
2. Create a virtual environment (venv)
3. Activate a virtual environment (venv)
4. Install the testing packages e.g. `pip install -r requirements.txt` or `pip install pytest pytest-cov`
5. Install the calculator package in editable mode e.g. `pip install -e .` ([Refer to pytest Good Integration Practices](https://docs.pytest.org/en/6.2.x/goodpractices.html))
6. Change the test runner preferences/settings for your IDE to pytest ([VS Code](https://code.visualstudio.com/docs/python/testing#_configure-tests) or [PyCharm](https://www.jetbrains.com/help/pycharm/pytest.html))

## Activities
1. Create a test directory: `tests` ([pytest directory naming convention](https://docs.pytest.org/en/6.2.x/goodpractices.html#tests-outside-application-code))
2. Create a python test file to test `calculator_class.py` and `calculator_functions.py`: see `tests/test_calculator_class.py` and `tests/test_calculator_functions.py` ([pytest test file naming convention](https://docs.pytest.org/en/6.2.x/goodpractices.html#tests-outside-application-code))
3. Create a fixture: see `conftest.py`
4. Create a test: see `tests/test_calculator_class.py` and `tests/test_calculator_functions.py`
5. Run the test from terminal in the IDE: `pytest --verbose`
6. Run tests and report on coverage from terminal in the IDE: `pytest tests --cov calculator --cov-report term-missing`
7. Add two more tests to the class and the functions versions of the tests (square and square_root) yourself
8. Re-run the tests with coverage

## References

[Pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html)

[pytest Good Integration Practices](https://docs.pytest.org/en/6.2.x/goodpractices.html)

[pytest-cov documentation](https://pytest-cov.readthedocs.io/en/latest/)

[Configure VS Code for pytest](https://code.visualstudio.com/docs/python/testing#_configure-tests)

[Configure PyCharm for pytest](https://www.jetbrains.com/help/pycharm/pytest.html)