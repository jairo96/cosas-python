
# list = [num * num for num in range(11)] # List ordenado
# print(list)

# set = {num * num for num in range(11)} # set desordenado
# print(set)

# dict = {num: num * num for num in range(11)} # Dict desordenado
# print(dict)



# items_dups = ["silla", "mesa", "pc", "mesa", "silla", "silla"]
# (len(name) for name in items_dups)
# print(set(len(name) for name in items_dups))
# print(max(len(name) for name in items_dups))
# print(min(len(name) for name in items_dups))


# mi_rango = (num + num for num in range(100))
# print([int(num / 2) for num in mi_rango])

# Genrator expressions son intesresates para el rendimiento
a = "12"


print (f"line "+a if  a else "hola")