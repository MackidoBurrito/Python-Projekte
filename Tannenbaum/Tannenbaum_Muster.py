h = int(input("Height: "))
print('\n'.join([' '*(h-i)+'x '*i for i in range(0,h)]),' '*(h-1)+'x',sep='\n')
