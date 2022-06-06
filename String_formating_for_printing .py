# String Formatting for Printing

# print('This is a string {}'.format('INSERTED'))
# print('This {} {} {} string'. format('is', 'a', 'multipal'))
# print('5 {} {} {} {}'.format('4', '3', '2', '1'))

# print('5 {3} {2} {1} {0}'.format('4', '3', '2', '1'))

# # we can also assign variable name

# print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick')) 


# Float formatting
result = 100/777
# print(result)
print("The result is {r}" .format(r=result))
# Float Formatting with presision
print('The result was {r:10.7f}'.format(r=result))


# f string method
x = 'Akash'
print(f'My name is {x}')