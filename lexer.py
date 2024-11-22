import ply.lex as lex

# Lista de tokens
tokens = [
    'PRINT',
    'LPAREN',
    'RPAREN',
    'STRING'
]

# Regras de expressões regulares para os tokens
t_PRINT = r'print'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'"[^"]*"'  # Reconhece qualquer string entre aspas duplas

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Contagem de linhas para mensagens de erro
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Mensagem de erro léxico
def t_error(t):
    print(f"Erro léxico: '{t.value[0]}' na linha {t.lexer.lineno}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()
