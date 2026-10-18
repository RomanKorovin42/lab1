from python_basics import count_vowels, mse, has_unique_characters, count_one_bits, multiplicative_persistence, prime_factorization, pyramid, is_balanced_number
import numpy as np

# Задача 1
class data1:
    value = 'ddoelkuarwt'

class data2:
    value='water'

class data3:
    value = value='kdncnvkjdsn'

print(count_vowels(data1) == 4)
print(count_vowels(data2) == 2)
print(count_vowels(data3) == 1)

print('--------------------------------')

# Задача 2
print(has_unique_characters(data1))
print(has_unique_characters(data2))
print(has_unique_characters(data3))

print('--------------------------------')

# Задача 3

class data4:
    value = 42

class data5:
    value = 5

class data6:
    value = 0

print(count_one_bits(data4) == 3)
print(count_one_bits(data5) == 2)
print(count_one_bits(data6) == 0)

print('--------------------------------')

# Задача 4

class data7:
    value = 39

class data8:
    value = 4

class data9:
    value = 999

print(multiplicative_persistence(data7) == 3)
print(multiplicative_persistence(data8) == 0)
print(multiplicative_persistence(data9) == 4)

print('--------------------------------')

# Задача 5

class data10:
    predicted = [1, 2]
    expected = [3, 4]

class data11:
    predicted = [1, 2]
    expected = [1, 2]

class data12:
    predicted = [3, 5, 4]
    expected = [5, 4, 1]

print(mse(data10) == 4.0)
print(mse(data11) == 0)
print(mse(data12) == 4.666666666666667)

print('--------------------------------')

# Задача 6

class data13:
    value = 86240

class data14:
    value = 6780

class data15:
    value = 0

print(prime_factorization(data13) == '(2**5)(5)(7**2)(11)')
print(prime_factorization(data14) == '(2**2)(3)(5)(113)')
print(prime_factorization(data15) == '0')

print('--------------------------------')

# Задача 7

class data16:
    value = 5

class data17:
    value = 17

class data18:
    value = 0

print(pyramid(data16) == 2)
print(pyramid(data17) == 'It is impossible')
print(pyramid(data18) == 'It is impossible')

print('--------------------------------')

# Задача 8

class data19:
    value = 1234006

class data20:
    value = 123456

class data21:
    value = 5558456

print(is_balanced_number(data19))
print(is_balanced_number(data20))
print(is_balanced_number(data21))

print('--------------------------------')