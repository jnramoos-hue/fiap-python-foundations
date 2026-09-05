from ManageUsers import*


def perguntar():
    return input("Oque deseja realizar ?\n" +
              "<I> - Para inserir um usuário.\n" +
              "<P> - Para pesquisar um usuário.\n" +
              "<E> - Para excluir um usuário.\n" +
              "<L> - Para Listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite seu nome: ").upper(),
                                                   input("Digite a ultima data de acesso: "),
                                                   input("Qual a última estação acessada: ").upper()]