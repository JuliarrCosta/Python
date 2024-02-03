##importando os elementos da classe contato
from Contato import *
class AgendaTelefonica:
    def __init__(self):
        self.agendaTelefonica = []
    ##Retorna se o contatato é true ou false na lista
    def verificarContato(self, nome):
        for contato in self.agendaTelefonica:
            if contato.nome == nome:
                return True
        else:
            return False
    ##Cria um novo objeto contato e adiciona na lista agendaTelefonica
    def adicionarContato(self, nome, numero):
        if self.verificarContato(nome):
            print(f'Contato existente')
        else:
            novo_contato= Contato(nome, numero)
            self.agendaTelefonica.append(novo_contato)
    ##remove o contato
    def removerContato(self, nome):
        if self.verificarContato(nome):
             for contato in self.agendaTelefonica:
                if contato.nome == nome:
                    self.agendaTelefonica.remove(contato)
                
        else:
            print(f'Contato não encotrado!')
    ##caso o contato tenha o nome especificado acima o novo numero será adicionado no antigo
    def editarContato(self, nome, novoNumero):
        if self.verificarContato(nome):
            for contato in self.agendaTelefonica:
                contato.numero = novoNumero
        else:
            print(f'Contato não encontrado')
    ##percorre a lista e aciona o método imprimir_contato do objeto
    def imprimirContatos(self):
        for contato in self.agendaTelefonica:
            contato.imprimir_contato()
    ##pesquisa contato por nome
    def buscarContato(self, nome):
        for contato in self.agendaTelefonica:
            if contato.nome == nome:
                print(f'Nome: {contato.nome} \n Número: {contato.numero}')
            else:
                print(f'Contato não encontrado')
    ##cria um arquivo csv se não existir e escreve dentro dele a agenda de contatos
    def exportarContatos(self):
        try: 
            with open('Agenda.csv', 'w') as arquivo:
                for contato in self.agendaTelefonica:
                    arquivo.write(contato.nome + ',')
                    arquivo.write(contato.numero + '\n')
        except Exception as error:
            print('Erro ao exportar contatos, tente novamente!')
    ##lê um arquivo e adiciona dentro do objto
    def importarContatos(self, nome):
        try:
            with open(nome, 'r') as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    ## o strip retira todos espaços da linha enquanto o split divide uma string de acordo com o caracter delimitador especificado
                    dado = linha.strip().split(',')
                    nomeImportado = dado[0]
                    numeroImportado = dado[1]
                    self.adicionarContato(nomeImportado, numeroImportado)
        except FileNotFoundError as error:
            print('Arquivo não encontrado')



##TESTANDO O CÓDIGO
agenda = AgendaTelefonica()
agenda.adicionarContato('Julia', '12232312')
agenda.editarContato('Julia', '1234444')
agenda.adicionarContato('Jose', '1232312')
agenda.imprimirContatos()
print('--------------')
agenda.removerContato('Julia')
agenda.imprimirContatos()
print('--------------')
agenda.adicionarContato('Julia', '12232312')
agenda.imprimirContatos()
print('--------------')
agenda.exportarContatos()
agenda.importarContatos('Agenda.txt')
agenda.imprimirContatos()