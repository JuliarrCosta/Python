from Contato import Contato

class AgendaTelefonica:
    def __init__(self):
        self.agendaTelefonica = []

    def verificarContato(self, nome):
        for contato in self.agendaTelefonica:
            if contato.nome == nome:
                return True
        else:
            return False

    def adicionarContato(self, nome, numero):
        if self.verificarContato(nome):
            print(f'Contato existente')
        else:
            novo_contato = Contato(nome, numero)
            self.agendaTelefonica.append(novo_contato)
    
    def removerContato(self, nome):
        if self.verificarContato(nome):
            for contato in self.agendaTelefonica.copy():
                self.agendaTelefonica.remove(contato)
        else:
            print(f'Contato não encontrado!')

    def editarContato(self, nome, novoNumero):
        if self.verificarContato(nome):
            for contato in self.agendaTelefonica:
                contato.numero = novoNumero
        else:
            print(f'Contato não encontrado')

    def imprimirContatos(self):
        for contato in self.agendaTelefonica:
            contato.imprimir_contato()

    def buscarContato(self, nome):
        for contato in self.agendaTelefonica:
            if contato.nome == nome:
                print(f'Nome: {contato.nome} Número: {contato.numero}')
from Contato import Contato
class AgendaTelefonica:
    def __init__(self):
        self.agendaTelefonica = []

    def verificarContato(self, nome):
        for contato in self.AgendaTelefonica:
            if contato.nome == nome:
                return True;
        else:
            return False;

    def adicionarContato(self, nome, numero):
        if self.verificarContato(nome):
            print(f'Contato existente')
        else:
            novo_contato= Contato(nome, numero)
            self.agendaTelefonica.append(novo_contato)
    
    def removerContato(self, nome):
        if self.verificarContato(nome):
            for contato in self.AgendaTelefonica.copy():
                self.agendaTelefonica.remove(contato)
        else:
            print(f'Contato não encotrado!')

    def editarContato(self, nome, novoNumero):
        if self.verificarContato(nome):
            for contato in self.AgendaTelefonica:
                contato.numero = novoNumero
        else:
            print(f'Contato não encontrado')

    def imprimirContatos(self):
        for contato in self.agendaTelefonica:
            contato.imprimir_contato

    def buscarContato(self, nome):
        for contato in self.AgendaTelefonica:
            if self.nome == nome:
                print(f'Nome: {contato.nome} Número: {contato.numero}')
            else:
                print(f'Contato não encontrado')
     

            