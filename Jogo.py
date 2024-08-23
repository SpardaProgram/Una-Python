from decimal import Decimal
import sys
class Jogo:
    def __init__(self, titulo=str, classe=str, preco=float):
        self.titulo = titulo
        self.classe = classe
        self.preco = preco

    def getPreco(self):
        return self.preco

    def getTitulo(self):
        return self.titulo

    def getClasse(self):
        return self.classe

    def setPreco(self, preco):
        try:
            self.preco = float(preco)

        except:
            print("Formato inválido!")

    def setTitulo(self, titulo):
        self.titulo = str(titulo)

    def setClasse(self, classe):
        self.classe = str(classe)

    def aplicarDesconto(self, desconto):
        self.preco = self.preco * (1 - float(desconto)/100)

    def aumentarPreco(self, aumento):
        self.preco = self.preco * (1 + float(aumento)/100)

    def toString(self):
        return f"Título: {self.titulo}\nClassificação Etária: {self.classe}\nPreço: R${Decimal(self.preco).quantize(Decimal(10)**-2)}"

opcao = int(input("\nDeseja criar um jogo? (1 - Sim, 2 - Não)"))

if opcao == 1:
    titulo = input("Digite o nome do jogo: ")

    classificacao = input("Digite a classificação etária do jogo (L, +10, +12, +16, +18): ")

    preco = float(input("Digite o preço do jogo: "))

    jogo = Jogo(titulo, classificacao, preco)

    while (True):
        print("\nEscolha uma das opções:\n1 - Aumentar preço\n2 - Descontar preço\n3 - Atualizar classificação etária\n4 - Mostrar detalhes\n5 - Adicionar novo jogo\n6 - Sair")

        escolha = input()
        porcentagem = 0.0
        texto = ""

        if escolha == "1":
                porcentagem = input("\nEscolha uma porcentagem (0.0 - 100.0):")
                jogo.aumentarPreco(porcentagem)

        elif escolha == "2":
                porcentagem = input("\nEscolha uma porcentagem (0.0 - 100.0):")
                jogo.aplicarDesconto(porcentagem)

        elif escolha == "3":
                texto = input("\nEscolha uma nova classificação etária:")
                jogo.setClasse(texto)

        elif escolha == "4":
                print(jogo.toString())

        elif escolha == "5":
            titulo = input("Digite o nome do jogo: ")

            classificacao = input("Digite a classificação etária do jogo (L, +10, +12, +16, +18): ")

            preco = float(input("Digite o preço do jogo: "))

            jogo = Jogo(titulo, classificacao, preco)

        else:
            sys.exit(0)