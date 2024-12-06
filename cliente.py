# Classe abstrata cliente, branch principal

from abc import ABC, abstractmethod 

class Cliente(ABC):
    def __init__(self, nome, nascimento, idade, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes):
        self.__nome = nome
        self.__nascimento = nascimento
        self.__idade = idade
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
    def get_idade(self):
        return self.__idade
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

    def set_nome(self, nome):
        self.__nome = nome
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
    def set_idade(self, idade):
        self.__idade = idade
    def set_genero(self, genero):
        self.__genero = genero
    def set_rg(self, rg):
        self.__rg = rg
    def set_cpf(self, cpf):
        self.__cpf = cpf
    def set_telefone(self, telefone):
        self.__telefone = telefone
    def set_email(self, email):
        self.__email = email
    def set_historico(self, historico):
        self.__historico = historico
    def set_nome(self, nome):
        self.__nome = nome
    def set_condicoes(self, condicoes):
        self.__condicoes = condicoes
    
# Método

    def mostrar(self):
        return (
        f"Dados do(a) cliente: \n"
        f"Nome: {self.get_nome()}\n"
        f"Data de nascimento: {self.get_nascimento()}\n" 
        f"Idade:{self.get_idade()}\n" 
        f"Gênero: {self.get_genero()}\n" 
        f"RG: {self.get_rg()}\n"
        f"CPF: {self.get_cpf()}\n" 
        f"Telefone/Celular: {self.get_telefone()}\n" 
        f"Email: {self.get_email()}\n" 
        f"Histórico médico: {self.get_historico()}\n"
        f"Uso de medicamentos: {self.get_medicamentos()}\n" 
        f"Condições odontológicas: {self.get_condicoes()}. \n "
        )



# Classe concreta que se refere aos clientes acima de 18 anos de idade, segunda branch

class clientemaior(Cliente):
    def __init__(self, nome, idade, nascimento, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes):
        super().__init__(nome,idade, nascimento, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes)


# Classe concreta que se refere aos clientes abaixo de 18 anos de idade, terceira branch

class clientemenor(Cliente):
    def __init__(self, nome, nascimento, idade, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes, \
        nomeresponsavel, parentesco, rgresponsavel, cpfresponsavel, telefoneresponsavel, emailresponsavel):
        super().__init__(nome, nascimento,idade, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes)

        self.__nomeresponsavel = nomeresponsavel
        self.__parentesco = parentesco
        self.__rgresponsavel = rgresponsavel
        self.__cpfresponsavel = cpfresponsavel
        self.__telefoneresponsavel = telefoneresponsavel
        self.__emailresponsavel = emailresponsavel

    def get_nomeresponsavel(self):
        return self.__nomeresponsavel
    def get_parentesco(self):
        return self.__parentesco
    def get_rgresponsavel(self):
        return self.__rgresponsavel
    def get_cpfresponsavel(self):
        return self.__cpfresponsavel
    def get_telefoneresponsavel(self):
        return self.__telefoneresponsavel
    def get_emailresponsavel(self):
        return self.__emailresponsavel
    
    def set_nomeresponsavel(self, nomeresponsavel):
        self.__nomeresponsavel = nomeresponsavel
    def set_parentesco(self, parentesco):
        self.__parentesco = parentesco
    def set_rgresponsavel(self, rgresponsavel):
        self.__rgresponsavel = rgresponsavel
    def set_cpfresponsavel(self, cpfresponsavel):
        self.__cpfresponsavel = cpfresponsavel
    def set_telefoneresponsavel(self, telefoneresponsavel):
        self.__telefoneresponsavel = telefoneresponsavel
    def set_emailresponsavel(self, emailresponsavel):
        self.__emailresponsavel = emailresponsavel

    def mostrarresponsavel(self):
        return (
        f"Dados do responsável do(a) cliente {self.get_nome()}:\n" 
        f"Nome: {self.get_nomeresponsavel()}\n" 
        f"Parentesco: {self.get_parentesco()}\n " 
        f"RG: {self.get_rgresponsavel()}\n" 
        f"CPF: {self.get_cpfresponsavel()}\n" 
        f"Telefone/Celular: {self.get_telefoneresponsavel()}\n" 
        f"Email: {self.get_emailresponsavel()}. \n"
        )


# Quarta branch, criação da janela de cadastro
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


# Função de criação de objetos
lista = []
def cadastra_cliente():
    nome = entry_nome.get()
    nascimento = entry_nascimento.get()
    idade = entry_idade.get()
    genero = entry_genero.get()
    rg = entry_rg.get()
    cpf = entry_cpf.get()
    telefone = entry_telefone.get()
    email = entry_email.get()
    historico = entry_historico.get()
    medicamentos = entry_medicamentos.get()
    condicoes = entry_condicoes.get()

    if not nome or not nascimento or not idade or not genero or not rg or not cpf or not telefone or not email or not historico or not medicamentos or not condicoes:
        messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios!")
        return

    if var_menordeidade.get() == "Sim":
        nomeresponsavel = entry_responsavel_nome.get()
        parentesco = entry_responsavel_parentesco.get()
        rgresponsavel = entry_responsavel_rg.get()
        cpfresponsavel = entry_responsavel_cpf.get()
        telefoneresponsavel = entry_responsavel_telefone.get()
        emailresponsavel = entry_responsavel_email.get()

        cliente = clientemenor(nome, nascimento, idade, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes, nomeresponsavel, parentesco, rgresponsavel, cpfresponsavel, telefoneresponsavel, emailresponsavel)
    else:
        cliente = clientemaior(nome, nascimento, idade, genero, rg, cpf, telefone, email, historico, medicamentos, condicoes)

    lista.append(cliente)
    messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    atualiza_listbox()  # Atualiza a lista de clientes na interface

janela = tk.Tk()
janela.title("Cadastro de clientes")
janela.geometry("700x700")

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

interior = ttk.Notebook(janela)
interior.grid(row= 0, column=0, sticky="nsew")

tab_cadastro = ttk.Frame(interior)
for i in range (18):
    tab_cadastro.grid_rowconfigure(i, weight=1)
    tab_cadastro.grid_columnconfigure(0, weight=1)
    tab_cadastro.grid_columnconfigure(1, weight=1)

tab_lista = tk.Frame(interior)
tab_lista.grid_rowconfigure(0, weight=1)
tab_lista.grid_columnconfigure(0, weight=1)

interior.add(tab_cadastro, text="Cadastro de clientes")
interior.add(tab_lista, text="Lista")

label1 = tk.Label(tab_cadastro, text="Por favor, preencha com seus dados:", font=("Helvetica", 15, "bold"))
label1.grid(row=0, column=0, sticky="w", padx=10, pady=8)

label2 = tk.Label(tab_cadastro, text="Nome:", font=("Helvetica", 15))
label2.grid(row=1, column=0, sticky="w", padx=10, pady=8)

entry_nome=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_nome.grid(row=1, column=1, sticky="nsew", padx=10, pady=8)

label3 = tk.Label(tab_cadastro, text="Data de nascimento:", font=("Helvetica", 15))
label3.grid(row=2, column=0, sticky="w", padx=10, pady=8)

entry_nascimento=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_nascimento.grid(row=2, column=1, sticky="nsew", padx=10, pady=8)

label4 = tk.Label(tab_cadastro, text="Idade:", font=("Helvetica", 15))
label4.grid(row=3, column=0, sticky="w", padx=10, pady=8)

entry_idade=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_idade.grid(row=3, column=1, sticky="nsew", padx=10, pady=8)

label5 = tk.Label(tab_cadastro, text="Gênero:", font=("Helvetica", 15))
label5.grid(row=4, column=0, sticky="w", padx=10, pady=8)

entry_genero=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_genero.grid(row=4, column=1, sticky="nsew", padx=10, pady=8)

label6 = tk.Label(tab_cadastro, text="RG:", font=("Helvetica", 15))
label6.grid(row=5, column=0, sticky="w", padx=10, pady=8)

entry_rg=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_rg.grid(row=5, column=1, sticky="nsew", padx=10, pady=8)

label7 = tk.Label(tab_cadastro, text="CPF:", font=("Helvetica", 15))
label7.grid(row=6, column=0, sticky="w", padx=10, pady=8)

entry_cpf=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_cpf.grid(row=6, column=1, sticky="nsew", padx=10, pady=8)

label8 = tk.Label(tab_cadastro, text="Telefone/Celular:", font=("Helvetica", 15))
label8.grid(row=7, column=0, sticky="w", padx=10, pady=8)

entry_telefone=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_telefone.grid(row=7, column=1, sticky="nsew", padx=10, pady=8)

label9 = tk.Label(tab_cadastro, text="Email:", font=("Helvetica", 15))
label9.grid(row=8, column=0, sticky="w", padx=10, pady=8)

entry_email=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_email.grid(row=8, column=1, sticky="nsew", padx=10, pady=8)

label10 = tk.Label(tab_cadastro, text="Histórico médico (alergias/doenças):", font=("Helvetica", 15))
label10.grid(row=9, column=0, sticky="w", padx=10, pady=8)

entry_historico=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_historico.grid(row=9, column=1, sticky="nsew", padx=10, pady=8)

label11 = tk.Label(tab_cadastro, text="Uso de medicamentos (nome e finalidade):", font=("Helvetica", 15))
label11.grid(row=10, column=0, sticky="w", padx=10, pady=8)

entry_medicamentos=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_medicamentos.grid(row=10, column=1, sticky="nsew", padx=10, pady=8)

label12 = tk.Label(tab_cadastro, text="Condições odontológicas:", font=("Helvetica", 15))
label12.grid(row=11, column=0, sticky="w", padx=10, pady=8)

entry_condicoes=tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_condicoes.grid(row=11, column=1, sticky="nsew", padx=10, pady=8)

label13 = tk.Label(tab_cadastro, text="Menor de idade?", font=("Helvetica", 15))
label13.grid(row=12, column=0, sticky="w", padx=10, pady=10)

campos_responsavel = []

label_responsavel_nome = tk.Label(tab_cadastro, text="Nome do responsável:", font=("Helvetica", 15))
label_responsavel_nome.grid(row=14, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_nome = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_nome.grid(row=14, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_nome, entry_responsavel_nome])

label_responsavel_parentesco = tk.Label(tab_cadastro, text="Parentesco:", font=("Helvetica", 15))
label_responsavel_parentesco.grid(row=15, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_parentesco = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_parentesco.grid(row=15, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_parentesco, entry_responsavel_parentesco])

label_responsavel_rg = tk.Label(tab_cadastro, text="RG do responsável:", font=("Helvetica", 15))
label_responsavel_rg.grid(row=16, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_rg = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_rg.grid(row=16, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_rg, entry_responsavel_rg])

label_responsavel_cpf = tk.Label(tab_cadastro, text="CPF do responsável:", font=("Helvetica", 15))
label_responsavel_cpf.grid(row=17, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_cpf = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_cpf.grid(row=17, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_cpf, entry_responsavel_cpf])

label_responsavel_telefone = tk.Label(tab_cadastro, text="Telefone do responsável:", font=("Helvetica", 15))
label_responsavel_telefone.grid(row=18, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_telefone = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_telefone.grid(row=18, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_telefone, entry_responsavel_telefone])

label_responsavel_email = tk.Label(tab_cadastro, text="Email do responsável:", font=("Helvetica", 15))
label_responsavel_email.grid(row=19, column=0, sticky="w", padx=10, pady=8)
entry_responsavel_email = tk.Entry(tab_cadastro, font=("Helvetica", 15))
entry_responsavel_email.grid(row=19, column=1, sticky="nsew", padx=10, pady=8)
campos_responsavel.extend([label_responsavel_email, entry_responsavel_email])

for widget in campos_responsavel:
            widget.grid_remove()

botao_cadastrar = tk.Button(tab_cadastro, text="Cadastrar", font=("Helvetica", 15), command=cadastra_cliente)
botao_cadastrar.grid(row=13, column=0, columnspan=2, padx=10, pady=8)

def mostrar_campos_responsavel():
    if var_menordeidade.get() == "Sim":
        for widget in campos_responsavel:
            widget.grid()
    else:
        for widget in campos_responsavel:
            widget.grid_remove()

def botao_cadastrar_posicao():
    if var_menordeidade.get() == "Sim":
        botao_cadastrar.grid(row=20, column=0, sticky="e", padx=10, pady=8)
    else:
        botao_cadastrar.grid(row=13, column=0, sticky="e", padx=10, pady=8)

var_menordeidade = tk.StringVar(value = "Não")
tk.Radiobutton(tab_cadastro, text="Sim", font=("Helvetica", 15,), variable= var_menordeidade, value="Sim", indicatoron=0, bg="green", fg="white", command=mostrar_campos_responsavel).grid(row=12, column=1, sticky="w", padx=10, pady=8)
tk.Radiobutton(tab_cadastro, text="Não", font=("Helvetica", 15,), variable= var_menordeidade, value="Não", indicatoron=0, bg="red", fg="white", command=mostrar_campos_responsavel).grid(row=12, column=1, sticky="e", padx=10, pady=8)
    
if var_menordeidade.get() == "Sim":
        nomeresponsavel = entry_responsavel_nome.get()
        parentesco = entry_responsavel_parentesco.get()
        rgresponsavel = entry_responsavel_rg.get()
        cpfresponsavel = entry_responsavel_cpf.get()
        telefoneresponsavel = entry_responsavel_telefone.get()
        emailresponsavel = entry_responsavel_email.get()

        if not nomeresponsavel or not parentesco or not rgresponsavel or not cpfresponsavel or not telefoneresponsavel or not emailresponsavel:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios do responsável!")
        cadastra_cliente()

listbox = tk.Listbox(tab_lista)
listbox.config(font=("Helvetica", 15,))
listbox.grid(row=0, column=0, sticky="nsew", padx=10, pady=8)
tk.Button(tab_lista, text="Atualizar", font=("Helvetica", 15,)).grid(row=13, columnspan=2, padx=10, pady=8)

def salvar(cliente):
    if var_menordeidade.get() == "Sim":
        lista.append(cliente), campos_responsavel.append(cliente)
    else:
        lista.append(cliente)

def atualiza_listbox():
    listbox.delete(0, tk.END)
    if var_menordeidade.get() =="Sim":
    
        for cliente in lista:
            listbox.insert(tk.END, cliente.mostrar())
        for cliente in campos_responsavel:
            listbox.insert(tk.END, cliente.mostrarresponsavel())
    
    else:
        for cliente in lista:
            listbox.insert(tk.END, cliente.mostrar())
        


janela.mainloop()