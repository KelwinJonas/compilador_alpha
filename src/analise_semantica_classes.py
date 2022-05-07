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
        self.variaveis = {}
    
    def add(self, varivel):
        self.variaveis[varivel.nome] = varivel

    def print(self):
        print("========================= SEMANTICA ===========================")
        for i in self.variaveis:
            self.variaveis[i].print()
        print("========================= X SEMANTICA X ===========================")

    def exists(self, nome):
        return nome in self.variaveis

    def size(self):
        return len(self.variaveis)

class Funcao:
    INTEGER = 1
    BOLEANO = 2
    VAZIO = 3

    def __init__(self, nome, tipo, parametros, lexval):
        self.nome = nome
        self.tipo = tipo
        self.parametros = parametros
        self.lexval = lexval

    def print(self):
        print("Variavel: " + str(self.nome) + ", Tipo: " + str(self.tipo) + ", Parametros: " + str(self.parametros) + ", Lexval: " + str(self.lexval))


class FuncaoHash:

    def __init__(self):
        self.funcoes = {}
    
    def add(self, funcao):
        self.funcoes[funcao.nome] = funcao

    def print(self):
        print("========================= SEMANTICA ===========================")
        for i in self.funcoes:
            self.funcoes[i].print()
        print("========================= X SEMANTICA X ===========================")

    def exists(self, nome):
        return nome in self.funcoes

    def size(self):
        return len(self.funcoes)    