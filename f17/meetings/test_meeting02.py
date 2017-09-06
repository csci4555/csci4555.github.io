# Meeting 02: P0, Abstract Syntax

# P0
#   print statements
#   simple assignment statements: x = ...
#   integer arithmetic: binary +, unary -
#   input integer

## 3 * 4
## print 3
## x = 3 + input()

# ASTs

import compiler
from compiler.ast import *

# Recursion over 

def p0ast_height(ast):
    if isinstance(ast, Module):
      return 1 + p0ast_height(ast.node)
    elif isinstance(ast, Stmt):
      return 1 + max([p0ast_height(c) for c in ast.nodes])
    elif isinstance(ast, Printnl):
      return 1 + p0ast_height(ast.nodes[0])
    elif isinstance(ast, Add):
      return 1 + max(p0ast_height(ast.left), p0ast_height(ast.right))
    elif isinstance(ast, Const):
      return 1
    else:
      raise Exception('Error: unrecognized AST node {}'.format(ast.__class__))

def test_p0ast_height():
    ast = compiler.parse('print 3\n3 + 4 + 5 + 6')
    print ast
    assert p0ast_height(ast) == 7
