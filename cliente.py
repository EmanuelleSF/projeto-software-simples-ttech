# Classe abstrata cliente, branch principal

from abc import ABC, abstractmethod 

class Cliente(ABC):
    def __init__(self, nome, nascimento, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__genero = genero
        self.__rg = rg
        self.__cpf = cpf
        self.__telefone = telefone
        self.__email = email
        self.__historico = historico
        self.__medicamentos = medicamentos
        self.__condicoes = condicoes

#Getters e Setters

    def get_nome(self):
        return self.__nome
    def get_nascimento(self):
        return self.__nascimento
    def get_genero(self):
        return self.__genero
    def get_rg(self):
        return self.__rg
    def get_cpf(self):
        return self.__cpf
    def get_telefone(self):
        return self.__telefone
    def get_email(self):
        return self.__email
    def get_historico(self):
        return self.__historico
    def get_medicamentos(self):
        return self.__medicamentos
    def get_condicoes(self):
        return self.__condicoes
    
# Métodos
    @abstractmethod
    def mostrar(self):
        pass

