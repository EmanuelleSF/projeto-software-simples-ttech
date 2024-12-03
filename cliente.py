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


# Classe concreta que se refere aos clientes acima de 18 anos de idade, segunda branch

class clientemaior(Cliente):
    def __init__(self, nome, nascimento, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes, maioridade):
        super().__init__(nome, nascimento, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes)

        self.__maioridade = maioridade
        maioridade == True

    def mostrar(self):
        return f"Dados do cliente: Nome: {self.get_nome}, Data de nascimento: {self.get_nascimento}, Gênero: {self.get_genero}, RG: {self.get_rg},\
           CPF: {self.get_cpf}, Telefone/Celular: {self.get_telefone}, Email: {self.get_email}, Histórico médico: {self.get_historico},\
             Uso de medicamentos: {self.get_medicamentos}, Condições odontológicas: {self.get_condicoes}. "
