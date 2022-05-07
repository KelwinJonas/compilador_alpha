from tkinter.messagebox import RETRY
from wsgiref.validate import validator


class Variavel:
    INTEGER = 1
    BOLEANO = 2

    def __init__(self, nome, valor, tipo, lexval):
        self.nome = nome
        self.valor = valor
        self.tipo = tipo
        self.lexval = lexval

    def print(self):
        print("Variavel: " + str(self.nome) + ", Valor: " + str(self.valor) + ", Tipo: " + str(self.tipo) + ", Lexval: " + str(self.lexval))

class VariavelHash:
    def __init__(self):
        self.variaveis = []
    
    def add(self, varivel):
        self.variaveis.append(varivel)

    def print(self):
        print("========================= SEMANTICA ===========================")
        for i in self.variaveis:
            self.variaveis[i].print()
        print("========================= X SEMANTICA X ===========================")

    def exists(self, nome):
        for i in range(len(self.variaveis)):
            if nome == self.variaveis[i].nome:
                return True

        return False

    def size(self):
        return len(self.variaveis)   

    def last(self):
        ultima = None
        for var in self.variaveis:
            ultima = self.variaveis[var]
        return ultima

    def lista_de_variaveis(self, nome):
        lista = []
        for i in range(len(self.variaveis)):
            if nome == self.variaveis[i].nome:
                lista.append(self.variaveis[i])

        return lista