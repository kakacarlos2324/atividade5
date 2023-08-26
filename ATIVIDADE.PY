def listar_compras(lista):
    print("Lista de Compras:")
    for index, item in enumerate(lista, start=1):
        print(f"{index}. {item}")

def main():
    lista_de_compras = []

    while True:
        print("\nMenu:")
        print("1. Adicionar item")
        print("2. Editar item")
        print("3. Apagar item")
        print("4. Listar itens")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            item = input("Digite o item a ser adicionado: ")
            lista_de_compras.append(item)
            print(f"{item} foi adicionado à lista!")

        elif escolha == '2':
            listar_compras(lista_de_compras)
            index = int(input("Digite o número do item a ser editado: ")) - 1
            novo_item = input("Digite o novo valor: ")
            lista_de_compras[index] = novo_item
            print("Item editado com sucesso!")

        elif escolha == '3':
            listar_compras(lista_de_compras)
            index = int(input("Digite o número do item a ser apagado: ")) - 1
            item_removido = lista_de_compras.pop(index)
            print(f"{item_removido} foi removido da lista!")

        elif escolha == '4':
            listar_compras(lista_de_compras)

        elif escolha == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    main()