# pytest-vs-unitest
Project to compare pytest and unitest Test Frameworks

##Comparison Table

| Feature                    | Pytest                          | Unitest                        | Winner  |
|----------------------------|---------------------------------|--------------------------------|---------|
| Instalation                | Third Party                     | Built in                       | Unitest |
| Basic Infra                | Can be only a function          | Inheritance                    | Pytest  |
| Basic Assertion            | assert bultin                   | TestCase instance methods      | Pytest  |
| Flat is better than nested | Function (1 level)              | Method (2 level)               | Pytest  |
| Can run each other test    | Can run unitest test            | Can't can pytest               | Pytest  |
| Test Result on console     | Sintax Highlight, Code snippet  | Only line error                | Pytest  |
| Multi param test           | Yes, parametrize, keep flat     | Yes, subtest, increase nesting | Pytest  |
