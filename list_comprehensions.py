from lascosas import *
from inspect import currentframe

cf = currentframe()

# List Comprehensions
printColor('\nBienvenido a List Comprehensions', 'title', '\n\n')

printColor('\nList Comprehensions', 'subtitle', '\n\n', cf.f_lineno)
printColor('\nCambiar a mayúsculas los valores de una lista:', 'text', '\n\n')

items = ["Jairo", "Max", "Peter"]
upper_item = []

for item in items:
    upper_item.append(item.upper())

printColor(f"\t• Lo podemos obtener de la manera ''normal''", 'text', '\n')
printColor("\t\tfor item in items:\n\t\t\tupper_item.append(item.upper())", 'code', '\n')
printColor(f"\t\t{upper_item}", 'result', '\n\n\n')

upper_item = []
upper_item = [item.upper() for item in items]

printColor(f"\t• Pero hay una manera mas guay de obtener esta lista (list comprehensions)", 'text', '\n')
printColor("\t\t[item.upper() for item in items]", 'code', '\n')
printColor(f"\t\t{upper_item}", 'result', '\n\n\n')




printColor('\n* Sabiendo esto podemos hacer las siguientes cositas:', 'text', '\n\n')
result = []
result = [num + num for num in range(5)]
printColor("\t[num + num for num in range(5)]", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n\n')


items = ["Jairo", "Max", "Peter"]
result = []
result = [("length", item, len(item))for item in items]
printColor("\t[(\"length\", item, len(item))for item in items]", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n\n')

items = "12, 85, 156, 885, 666, 1000, 1"
result = []
result = max([int(num) for num in items.split(", ")])
printColor("\tmax([int(num) for num in items.split(\", \")])", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n\n')

items = ["Jairo", "Max", "Peter"]
result = {}
result = {i:x for i, x in enumerate(items, 1)}
printColor(f"Tambien lo podemos aplicar a dict", 'text', '\n')
printColor("\t{i:x for i, x in enumerate(items, 1)}", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n\n')


items = ["Jairo", "Max", "Peter"]
result = ",  ".join([f"Names is {name}" for name in items])
printColor(f"Y con joins...", 'text', '\n')
printColor("\t\",  \".join([f\"My names is {name}\" for name in items])", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n\n')



printColor('\nCondicionales', 'subtitle', '\n\n', cf.f_lineno)

printColor(f"Podemos meter condiciones a las list comprehensions para los 'calculos' que realizamos", 'text', '\n\n')
printColor(f"Por ejemplo, sabiendo que el modulo de 2 devuelve 0 (num % 2) para los numeros pares, podemos sacar una lista con la suma de todos los números pares", 'text', '\n')
result = []
result = [num + num for num in range(6) if num % 2 == 0]
printColor("\t[num + num for num in range(6) if num % 2 == 0]", 'code', '\n')
printColor(f"\t{result}", 'result', '\n\n')
