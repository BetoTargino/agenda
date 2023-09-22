from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# storage in memory
agenda = []
index = 0

def adicionarContato() -> None:
    # Pega o valor digitado em txt_nome
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    categoria = cb_categoria.get()
    contato = {
        'nome': nome,
        'telefone': telefone,
        'categoria': categoria
    }
    agenda.append(contato)
    limparCampos()
    atualizarTabela()
    messagebox.showinfo('Sucesso!', 'Contato adicionado com sucesso!')
    txt_nome.focus_set()

def editarContato() -> None:
    agenda[index] = {
        'nome': txt_nome.get(),
        'telefone': txt_telefone.get(),
        'categoria': cb_categoria.get()
    }
    messagebox.showinfo('Editado!', 'Dados alterados com sucesso!')
    atualizarTabela()
    limparCampos()

def deletarContato() -> None:
    agenda.remove(agenda[index])
    messagebox.showinfo('Deletado!', 'Contato apagado com sucesso!')
    limparCampos()
    atualizarTabela()

def limparCampos() -> None:
    # Limpar os campos
    txt_nome.delete(0, END)
    txt_telefone.delete(0, END)
    cb_categoria.set('')

def atualizarTabela() -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)
        
    for contato in agenda:
        tabela.insert('', END, values=(contato['nome'], contato['telefone'], contato['categoria']))

def tabelaClique(event) -> None:
    # Obter a linha selecionada
    linha_selecionada = tabela.selection()
    global index
    index = tabela.index(linha_selecionada[0])
    contato = agenda[index]
    limparCampos()
    txt_nome.insert(0, contato['nome'])
    txt_telefone.insert(0, contato['telefone'])
    cb_categoria.set(contato['categoria'])

#Janela
janela = Tk()
janela.title('Agenda Telefonica')
janela.geometry('600x400')

#Label
label_nome = Label(janela, text='Nome: ', font='Arial 14 bold', fg='black')
label_nome.grid(row=0, column=0)
label_telefone = Label(janela, text='Telefone: ', font='Arial 14 bold', fg='black')
label_telefone.grid(row=1, column=0)

#Entry
txt_nome = Entry(janela, font='Arial 14', bg='white', fg='navy', width=27)
txt_nome.grid(row=0, column=1)
txt_telefone = Entry(janela, font='Arial 14', bg='white', fg='navy', width=27)
txt_telefone.grid(row=1, column=1)

# Combobox
label_categoria = Label(janela, text='Categoria: ', font='Arial 14 bold', fg='black')
label_categoria.grid(row=2, column=0)

categorias = ['Amigos', 'Família', 'Trabalho']
cb_categoria = ttk.Combobox(janela, values=categorias, width=25, font='Arial 14')
cb_categoria.grid(row=2, column=1)

#Button
# Adicionar
btn_adicionar = Button(janela, text='Adicionar', font='Arial 10 bold',
                       bg='navy', fg='white', width=8, command=adicionarContato)
btn_adicionar.grid(row=3, column=0)
# Editar
btn_editar = Button(janela, text='Editar', font='Arial 10 bold',
                       bg='navy', fg='white', width=8, command=editarContato)
btn_editar.grid(row=3, column=1)
# Deletar
btn_deletar = Button(janela, text='Deletar', font='Arial 10 bold',
                       bg='navy', fg='white', width=8, command=deletarContato)
btn_deletar.grid(row=3, column=2)
# Limpar
btn_limpar = Button(janela, text='Limpar Campos', font='Arial 10 bold', command=limparCampos)
btn_limpar.grid(row=1, column=2)


colunas = ['Nome', 'Telefone', 'Categoria']
#criando uma tabela/TreeView
tabela = ttk.Treeview(janela, columns=colunas, show='headings')
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
tabela.grid(row=4, columnspan=3)
# Criando uma bind
tabela.bind('<ButtonRelease-1>', tabelaClique)

# Executa a janela
janela.mainloop()