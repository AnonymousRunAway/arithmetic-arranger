# Arithmetic Arranger
This Python script provides a function to arrange (and solve) arithmetic problems in a neat, readable format.

# Function:

```python
arithmetic_arranger(problems, show_answers=False):
```
Takes a list of strings representing arithmetic problems as input.
Optionally displays the answers to the problems.
Returns a formatted string containing the arranged problems.

# Example Usage
```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems, True)
print(result)
```
