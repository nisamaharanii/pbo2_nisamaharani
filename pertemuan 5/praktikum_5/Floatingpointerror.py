from decimal import Decimal
from fractions import Fraction

Fraction.from_float(0.1)
Fraction(3602879701896397, 36028797018963968)

(0.1).as_integer_ratio()
(3602879701896397, 36028797018963968)

Decimal.from_float(0.1)
Decimal('0.1000000000000000055511151231257827021181583404541015625')

format(Decimal.from_float(0.1), '.17')
'0.10000000000000001'