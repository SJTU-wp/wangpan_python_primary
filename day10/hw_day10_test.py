str_test = '12321'
str_test_reverse = str_test[::-1]
print(str_test_reverse)
print(id(str_test))
print(id(str_test_reverse))
str_test_complete = str_test[:]
print(id(str_test_complete))

print('-' * 50)
a = 2
b = 2
print(id(a))
print(id(b))
c = a + 3 - 3
print(id(c))
