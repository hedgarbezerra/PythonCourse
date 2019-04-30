lista = [i+1 for i in range(5)]
print(lista)
iterator = iter(lista)
while True:
    try:
        elemento = next(iterator)
    except StopIteration:
        break
