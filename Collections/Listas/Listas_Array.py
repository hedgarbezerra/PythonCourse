from array import array

a = input('Insira algo: \n')
#' - '.join([str(i) for i in self.__elementos])
x = [i for i in a.strip()]
y = ''.join([i for i in x])
print(x)
print(y)

