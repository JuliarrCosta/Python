class Contato:
    ##instanciando o objeto contato
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero
    
    def imprimir_contato(self):
        print(f"Nome: {self.nome}\nNúmero: {self.numero}")

