case = (int)(input("No of case"))
string = []
odd = ''
even = ''
for i in range(case):
    string.append(input("your value"))
    for i in range(len(string[i])):
        if i%2 == 1:
            odd += string[i]
        else:
            even += string[i]
    print("{} {}".format(even, odd))
