# Sorted containers
Contrary to its name, this package cannot really help you to efficiently sort your data, - you may use built-in tools of Python, numpy or pandas for that purpose.

This tool, however, allows you to _declare_ that certain container is already sorted and, based on that information, perform certain operations more efficiently.

## Usage Examples

```python
from itertools import count, islice
from platonic_sorted import Sorted

print(list(Sorted([0, 2, 4]) + Sorted([1, 3, 5])))
# [0, 1, 2, 3, 4, 5]

natural_numbers = Sorted(count())
even_numbers = Sorted(filter(lambda i: i % 2 == 0, count()))
odd_numbers = natural_numbers - even_numbers
print(list(islice(odd_numbers, 5)))
# [1, 3, 5, 7, 9] 
```

To perform these operations, `platonic-sorted` uses lazy iterative algorithms with linear complexity by time and constant complexity by RAM.
