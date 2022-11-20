# Evaluating the strength of Python's Type System

This covers type hints and other typing features introduced in
[PEP-484](https://peps.python.org/pep-0484/).

## Comparing Type Checkers
Note that since there are multiple implementation of the Python type checker, 
this project also includes some tests that run them all.

### Test Results
- [MyPy](https://jackgene.github.io/strongly-typed/python-type-checking/mypy.html)
- [Pyre](https://jackgene.github.io/strongly-typed/python-type-checking/pyre.html)
- [Pyright](https://jackgene.github.io/strongly-typed/python-type-checking/pyright.html)

tl;dr
- **Pyright** has always been the strongest and so far that remains the case.
  This is particularly true when it comes to exhaustiveness checking of Python 3.10 `match`es.
- **MyPy** is largely on parity with Pyright, but exhaustiveness checking is slightly lacking.
- **Pyre** is currently the weakest of the 3.
  However, it does do one thing the others don't, which is prevent public uses of the `Any` type.

### Running The Tests
To run the tests locally, first set up your environment (you should only have to do this once):
1. Install Python 3.10 if not already installed
   (we are evaluating `match`, amongst other things, which is a Python 3.10 feature).
2. (Optional, but recommended) Create a virtual environment, and activate it `python -m venv venv`, `. venv/bin/activate`.
3. Install dependencies `pip install -r requirements.txt`.

Once your environment is set up, you should be able to run: 
```shell
behave
```

Or to output a HTML report:
```shell
behave -t mypy -f behave_html_formatter:HTMLFormatter > ../docs/python-type-checking/mypy.html
behave -t pyre -f behave_html_formatter:HTMLFormatter > ../docs/python-type-checking/pyre.html
behave -t pyright -f behave_html_formatter:HTMLFormatter > ../docs/python-type-checking/pyright.html
```
