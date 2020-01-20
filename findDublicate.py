# Exercise : Check for duplicate
some_list = ['a,','b','c','b','d','m','n','n']
duplicate_values = []
for i,char in enumerate(some_list):
    if char in some_list[i:]:
        duplicate_values.append(char)
print(duplicate_values)
