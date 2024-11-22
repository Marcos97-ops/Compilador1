from parser import parser, ast_root  # Importa o parser e a variável global ast_root

# Função para processar o código e gerar a AST
def parse_code(code):
    global ast_root  # Garante que estamos manipulando a variável global ast_root
    ast_root = None  # Reseta a AST antes de processar novo código
    result = parser.parse(code)
    if ast_root:
        print("\nEstrutura da Árvore Sintática (AST):")
        ast_root.display()
    else:
        print("\nAST vazia ou falha na análise sintática.")

# Ponto de entrada do programa
if __name__ == "__main__":
    while True:
        filename = input("\nDigite o caminho do arquivo .py (ou 'sair' para encerrar): ").strip()
        if filename.lower() == 'sair':
            print("Encerrando o programa.")
            break
        try:
            # Lê o conteúdo do arquivo
            with open(filename, 'r') as file:
                code = file.read()
                print(f"\nConteúdo do arquivo:\n{code}\n")
                parse_code(code)  # Processa o código
        except FileNotFoundError:
            print(f"Erro: Arquivo '{filename}' não encontrado.")
        except Exception as e:
            print(f"Erro: {e}")
