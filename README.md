# pytest-vs-unitest
Project to compare pytest and unitest Test Frameworks

##Comparison Table

| Feature                    | Pytest                             | Unitest                          | Winner   |
|----------------------------|------------------------------------|----------------------------------|----------|
| Installation               | Third Party                        | Built in                         | Unittest |
| Basic Infra                | Can be only a function             | Inheritance                      | Pytest   |
| Basic Assertion            | assert bultin                      | TestCase instance methods        | Pytest   |
| Flat is better than nested | Function (1 level)                 | Method (2 level)                 | Pytest   |
| Can run each other test    | Can run unittest test              | Can't can pytest                 | Pytest   |
| Test Result on console     | Syntax Highlight, Code snippet     | Only line error                  | Pytest   |
| Multi param test           | Yes, parametrize, keep flat        | Yes, sub-test, increase nesting  | Pytest   |
| Test setup                 | fixture: module, session, function | Template Method: setup, tearDown | Pytest   |
| Name Refactoring           | poor, because of name conventions  | rich, regular object orientation | Unittest |
| Running Failed Tests       | built in (--lf, --ff)              | your own =,(                     | Pytest   |
| Marks                      | built in                           | your own =,(                     | Pytest   |

pytest cli

pytest -s test/test_pytest/ | grep '###'
pytest -s --ff test/test_pytest/
pytest -s --ff test/test_pytest/

ToDo:
