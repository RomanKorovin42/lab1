"""Заготовки задач на базовый Python."""

from grader_contracts.python_basics import PositiveIntegerInput, TextInput, VectorPairInput


def count_vowels(data: TextInput) -> int:
    text = data.value
    count = 0
    letters = ['a', 'e', 'i', 'o', 'u']

    for i in text:
        if i.lower() in letters:
            count += 1

    return count


def has_unique_characters(data: TextInput) -> bool:
    text = data.value
    uniqueCharacters = []

    for i in text:
        if i in uniqueCharacters:
            return False
        else:
            uniqueCharacters.append(i)
            
    return True

    


def count_one_bits(data: PositiveIntegerInput) -> int:

    def getBit(number):
        quotient = number
        bitNum = []

        while quotient >= 1:
            bitNum.append(round(quotient % 2))
            quotient = quotient // 2 

        return bitNum

    number = data.value
    bitNumbers = getBit(number)
    count = 0

    for i in bitNumbers:
        if i:
            count += 1

    return count


def multiplicative_persistence(data: PositiveIntegerInput) -> int:
    number = data.value
    count = 0

    while number // 10 != 0:
        currentNumSymbols = map(lambda x: int(x), str(number))
        newNum = 1

        for i in currentNumSymbols:
            newNum *= i
            
        number = newNum
        count += 1

    return count


def mse(data: VectorPairInput) -> float:
    predicted, expected = data.predicted, data.expected
    pLength =  len(predicted)
    sum = 0
    
    for i in range(pLength):
        diff = predicted[i] - expected[i]
        sum += diff**2

    print(sum/pLength)

    return sum/pLength


def prime_factorization(data: PositiveIntegerInput) -> str:
    number = data.value
    numDictionary = {}
    result = ''
    x = 2

    if number == 0:
        return '0'
    
    while number != 1:
        while number % x == 0:
            if x not in numDictionary:
                numDictionary[x] = 1
            else:
                numDictionary[x] += 1
            number = number / x
            x = 2
        x += 1

    for i in numDictionary:
        result += f"({i}" + (f"**{numDictionary[i]})" if numDictionary[i] > 1 else ")")

    return result


def pyramid(data: PositiveIntegerInput) -> int | str:
    cube_count = data.value
    k = 1
    sum = 0

    while True:
        sum += k**2

        if sum == cube_count:
            return k

        if sum > cube_count:
            return 'It is impossible'

        k += 1


def is_balanced_number(data: PositiveIntegerInput) -> bool:
    number = data.value
    numbersList = list(map(lambda x: int(x), str(data)))
    numbersL = []
    numbersR = []

    if len(numbersList) % 2 != 0:
        numbersL = numbersList[0:len(numbersList) // 2]
        numbersR = numbersList[(len(numbersList) // 2) + 1:len(numbersList)]
    else:
        numbersL = numbersList[0:len(numbersList) // 2 - 1]
        numbersR = numbersList[(len(numbersList) // 2) + 1:len(numbersList)]

    if sum(numbersL) == sum (numbersR):
        return True
    else:
        return False
