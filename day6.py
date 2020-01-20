def stringEvenOrOdd(number_of_strings,strings):
    for number in range(number_of_strings):
        for index,char in strings[number]:
            if index % 2 == 0:
                