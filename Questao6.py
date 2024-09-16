
#Exercício 6: Crie um programa que gerencie o banco de dados de uma biblioteca. O programa deve permitir adicionar um novo livro (como uma lista contendo título, autor e ano), listar todos os livros, e permitir a busca de livros pelo título.


biblioteca = []

def adicionar_livro(titulo, autor, ano):
    livro = {'Título': titulo, 'Autor': autor, 'Ano': ano}
    biblioteca.append(livro)
    print(f'Livro "{titulo}" adicionado com sucesso!')

def listar_livros():
    if len(biblioteca) == 0:
        print("Nenhum livro cadastrado.")
    else:
        for i, livro in enumerate(biblioteca, 1):
            print(f"{i}. Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")

def buscar_livro(titulo):
    resultados = []
    for livro in biblioteca:
        if titulo.lower() in livro['Título'].lower():
            resultados.append(livro)
    if resultados:
        for livro in resultados:
            print(f"Encontrado: Título: {livro['Título']}, Autor: {livro['Autor']}, Ano: {livro['Ano']}")
    else:
        print(f"Nenhum livro encontrado com o título '{titulo}'.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Buscar livro por título")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Título: ")
            autor = input("Autor: ")
            ano = input("Ano: ")
            adicionar_livro(titulo, autor, ano)
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            titulo = input("Digite o título que deseja buscar: ")
            buscar_livro(titulo)
        elif escolha == '4':
            print("Saindo...")
            print("Programa finalizado.")
            break
        else:
            print("Opção inválida, tente novamente.")
menu()