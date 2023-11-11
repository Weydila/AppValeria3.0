from tkinter import ttk, Tk
from tkcalendar import Calendar, DateEntry
import TM, tkinter

# Definição da janela principal
janela = Tk()
janela.title('GERENCIADOR DE TAREFAS')
janela.geometry('450x700')
janela.config(bg='white')
janela.resizable(0,0)
fundo = tkinter.PhotoImage(file="praia2.png")
plano = tkinter.Label(janela, image=fundo)
plano.place(x=0, y=0)

# Variável que armazena a entrada do input da tarefa
tarefaInput = tkinter.StringVar(janela)
# Rotulo tarefa
textoInput = tkinter.Label(janela, text="TAREFA", bg='White')
# Input para coleta do dado da tarefa
tarefa = tkinter.Entry(janela, textvariable=tarefaInput, font=30)
# Rotulo da prioridade
label = ttk.Label(janela, text="PRIORIDADE ", background='white')
# Variavel que armazena a entrada do campo do combobox de prioridades
qualprio = tkinter.StringVar()
# Input da lista do combobox
prios = ttk.Combobox(janela, textvariable=qualprio)
# Classe que cria o calendario
cal = Calendar(janela)
# Definindo os valores da entrada do combobox
prios["values"] = ["Alta", "Média", "Baixa"]
# Criando um bloco de notebook
bloco_status = ttk.Notebook(janela)
# Criando novas tabs para o bloco de notebook
tab1 = ttk.Frame(bloco_status, width=200, height=400)
tab2 = ttk.Frame(bloco_status, width=200, height=400)
tab3 = ttk.Frame(bloco_status, width=200, height=400)
# Armazena classe Treeview("tabela")
tabelaTab1 = ttk.Treeview(tab1, selectmode='browse')
tabelaTab2 = ttk.Treeview(tab2, selectmode='browse')
tabelaTab3 = ttk.Treeview(tab3, selectmode='browse')
# Criação da tabela do tab1
tabelaTab1.grid(row=1, column=1, padx=5, pady=5)
tabelaTab1["columns"] = ("1", "2", "3", "4")
tabelaTab1["show"] = 'headings'
tabelaTab1.column("1", width=100, anchor='c')
tabelaTab1.column("2", width=145, anchor='c')
tabelaTab1.column("3", width=95, anchor='c')
tabelaTab1.column("4", width=95, anchor='c')

tabelaTab1.heading("1", text="STATUS")
tabelaTab1.heading("2", text="TAREFA")
tabelaTab1.heading("3", text="DATA")
tabelaTab1.heading("4", text="PRIORIDADE")

# Criação da tabela do tab2
tabelaTab2.grid(row=1, column=1, padx=5, pady=5)
tabelaTab2["columns"] = ("1", "2", "3", "4")
tabelaTab2["show"] = 'headings'
tabelaTab2.column("1", width=100, anchor='c')
tabelaTab2.column("2", width=145, anchor='c')
tabelaTab2.column("3", width=95, anchor='c')
tabelaTab2.column("4", width=95, anchor='c')

tabelaTab2.heading("1", text="STATUS")
tabelaTab2.heading("2", text="TAREFA")
tabelaTab2.heading("3", text="DATA")
tabelaTab2.heading("4", text="PRIORIDADE")

# Criação da tabela do tab3
tabelaTab3.grid(row=1, column=1, padx=5, pady=5)
tabelaTab3["columns"] = ("1", "2", "3", "4")
tabelaTab3["show"] = 'headings'
tabelaTab3.column("1", width=100, anchor='c')
tabelaTab3.column("2", width=145, anchor='c')
tabelaTab3.column("3", width=95, anchor='c')
tabelaTab3.column("4", width=95, anchor='c')

tabelaTab3.heading("1", text="STATUS")
tabelaTab3.heading("2", text="TAREFA")
tabelaTab3.heading("3", text="DATA")
tabelaTab3.heading("4", text="PRIORIDADE")

## Instancia a classe TaskManager
t = TM.TaskManager()


## Pequena entrada
def entrada():
    status = "novo"
    if tarefa.get() != '' and prios.get() != '':
        t.add_task(prios.get().upper(), tarefa.get().upper(), cal.get_date(), status.upper())
        novoItem = t.list_last()
        tabelaTab1.insert("", 'end', values=(
        novoItem["status"].upper(), novoItem["tarefa"].upper(), novoItem["data"], novoItem["prioridade"].upper()))


# Funções que alternam os status
def nextTab1(event):
    i = tabelaTab1.selection()
    lista = tabelaTab1.item(i, "values")
    novoItem = t.change_status(lista)
    tabelaTab1.delete(i)
    tabelaTab2.insert("",
                      'end',
                      values=(novoItem[0]["status"].upper(),
                              novoItem[0]["tarefa"].upper(),
                              novoItem[0]["data"],
                              novoItem[0]["prioridade"].upper()))


def nextTab2(event):
    i = tabelaTab2.selection()
    lista = tabelaTab2.item(i, "values")
    novoItem = t.change_status(lista)
    tabelaTab2.delete(i)
    tabelaTab3.insert("",
                      'end',
                      values=(novoItem[0]["status"].upper(),
                              novoItem[0]["tarefa"].upper(),
                              novoItem[0]["data"],
                              novoItem[0]["prioridade"].upper()))


def nextTab3(event):
    i = tabelaTab3.selection()
    lista = tabelaTab3.item(i, "values")
    t.change_status(lista)
    tabelaTab3.delete(i)


# Copiar e alterar a variavel da tabelaTab
def deletClick1(event):
    if tabelaTab1.selection():
        i = tabelaTab1.selection()
        lista = tabelaTab1.item(i, "values")
        t.deleteTarefa(lista)
        tabelaTab1.delete(i)


def deletClick2(event):
    if tabelaTab2.selection():
        i = tabelaTab2.selection()
        lista = tabelaTab2.item(i, "values")
        t.deleteTarefa(lista)
        tabelaTab2.delete(i)


def deletClick3(event):
    if tabelaTab3.selection():
        i = tabelaTab3.selection()
        lista = tabelaTab3.item(i, "values")
        t.deleteTarefa(lista)
        tabelaTab3.delete(i)


# Criando um botão de envio
btn = tkinter.Button(janela, text="Inserir", command=entrada)

# Ações da tabelaTab1
tabelaTab1.bind('<Double-1>', nextTab1)
tabelaTab1.bind('<Button-3> ', deletClick1)
# Ações da tabelaTab2
tabelaTab2.bind('<Double-1>', nextTab2)
tabelaTab2.bind('<Button-3> ', deletClick2)
# Ações da tabelaTab3
tabelaTab3.bind('<Double-1>', nextTab3)
tabelaTab3.bind('<Button-3> ', deletClick3)

# Labels de informação
info1 = ttk.Label(janela,
                  text=" # Clicar sobre o item para selecionar uma tarefa.\n "
                    "# Clicar 2 vezes sobre o item para atualizar uma tarefa.\n "
                    "# Selecionar e clicar com o botão esquerdo para remover a tarefa. ",
                  background='white')

# Adicionando os elementos dentro da janela principal
textoInput.pack(pady=5)
tarefa.pack()
label.pack()
prios.pack()
cal.pack()
btn.pack()
bloco_status.pack(pady=10, expand=True)
info1.pack(ipady=1, pady=25)
tab1.pack(fill='both', expand=True)
bloco_status.add(tab1, text="       NOVAS TAREFAS       ")
tab2.pack(fill='both', expand=True)
bloco_status.add(tab2, text="           TAREFAS EM PROCESSO         ")
tab3.pack(fill='both', expand=True)
bloco_status.add(tab3, text="       TAREFAS FINALIZADAS         ")

janela.mainloop()
