from lascosas import *
from inspect import currentframe

cf = currentframe()

# List Comprehensions
printColor('\nBienvenido a Generator Expressions', 'title', '\n\n')

printColor('\nBuscar definición y demás', 'subtitle', '\n\n', cf.f_lineno)