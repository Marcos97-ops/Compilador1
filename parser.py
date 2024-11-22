import ply.yacc as yacc
from lexer import tokens

# Classe para nós da árvore
class NaryTreeNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.node_type}: {self.value}")
        for child in self.children:
            child.display(level + 1)

# Variável global para armazenar a raiz da AST
ast_root = None

# Regras de gramática
def p_program(p):
    'program : statement'
    global ast_root
    ast_root = NaryTreeNode("program")
    ast_root.add_child(p[1])

def p_statement_print(p):
    'statement : PRINT LPAREN STRING RPAREN'
    print_node = NaryTreeNode("print_statement")
    print_node.add_child(NaryTreeNode("string", p[3]))
    p[0] = print_node

def p_error(p):
    print("Erro de sintaxe!")
    if p:
        print(f"Erro na posição: {p}")
    else:
        print("Erro no final da entrada.")

# Construção do parser
parser = yacc.yacc()
