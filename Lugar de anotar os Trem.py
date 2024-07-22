import tkinter as tk  # Importa o módulo tkinter para criar interfaces gráficas de usuário (GUIs)
from tkinter import ttk, font,messagebox, filedialog  # Importa messagebox e filedialog do módulo tkinter
from tkinter import PhotoImage  # Importa PhotoImage do módulo tkinter para lidar com imagens

# Configuração da Janela principal
janela = tk.Tk()  # Cria a janela principal
janela.title("App de Tarefas - To do List")  # Define o título da janela
janela.configure (bg="#d3d3d3")  # Define a cor de fundo da janela
janela.geometry("800x1000")  # Define o tamanho da janela
 
frame_em_edicao = None  # Inicializa uma variável global para armazenar o frame que está sendo editado

# Função para adicionar tarefa
def adicionar_tarefa():
    global frame_em_edicao  # Declara que vamos usar a variável global frame_em_edicao
    
    tarefa = entrada_tarefa.get().strip()  # Obtém o texto da entrada de tarefa e remove espaços em branco no início e no fim
    if tarefa and tarefa != "Escreva sua tarefa aqui":  # Verifica se a tarefa não está vazia e não é igual a "Escreva sua tarefa aqui"
        if frame_em_edicao is not None:  # Se há um frame sendo editado
            atualizar_tarefa(tarefa)  # Atualiza a tarefa
            frame_em_edicao = None  # Reseta a variável frame_em_edicao
        else: 
            adicionar_item_tarefa(tarefa)  # Adiciona a tarefa como um novo item
            entrada_tarefa.delete( 0, tk.END )  # Limpa a entrada de tarefa
    else:
        messagebox.showwarning("Entrada Inválida","Por favor,Insira uma tarefa")  # Mostra uma mensagem de aviso se a entrada é inválida

def adicionar_item_tarefa(tarefa):
    frame_tarefa =tk.Frame(canvas_interior,bg="white", bd = 1, relief= tk.SOLID)  # Cria um novo frame para a tarefa
    label_tarefa = tk.Label(frame_tarefa,text= tarefa, font= ("roboto", 16), bg= "white", width = 25, height= 2, anchor= "w")  # Cria um rótulo com o texto da tarefa
    label_tarefa.pack(side=tk.LEFT, fill= tk.X, padx= 10, pady= 5)  # Adiciona o rótulo ao frame da tarefa

    botao_editar = tk.Button(frame_tarefa, image = icon_editar,command= lambda f= frame_tarefa, l= label_tarefa: preparar_edicao(f, l), bg= "white", relief= tk.FLAT)  # Cria um botão para editar a tarefa
    botao_editar.pack(side=tk.RIGHT, padx= 5)  # Adiciona o botão de editar ao frame da tarefa

    botao_deletar = tk.Button(frame_tarefa, image = icon_deletar,command= lambda f= frame_tarefa:deletar_tarefa(f), bg="white", relief= tk.FLAT)  # Cria um botão para deletar a tarefa
    botao_deletar.pack(side=tk.RIGHT, padx= 5)  # Adiciona o botão de deletar ao frame da tarefa

    frame_tarefa.pack(fill= tk.X, padx= 5, pady= 5)  # Adiciona o frame da tarefa ao frame interior do canvas
 
    checkbutton = tk.Checkbutton(frame_tarefa,command= lambda label= label_tarefa: alterar_sublinhado(label))  # Cria um botão de seleção para alternar o sublinhado do rótulo da tarefa

    checkbutton.pack(side= tk.RIGHT, padx= 5)  # Adiciona o botão de seleção ao frame da tarefa
    canvas_interior.update_idletasks()  # Atualiza as tarefas ociosas do frame interior do canvas
    canvas.config(scrollregion= canvas.bbox("all"))  # Configura a região de rolagem do canvas para incluir todos os itens

def preparar_edicao(frame_tarefa,label_tarefa):
    global frame_em_edicao  # Declara que vamos usar a variável global frame_em_edicao
    frame_em_edicao = frame_tarefa  # Define o frame que está sendo editado
    entrada_tarefa.delete(0,tk.END)  # Limpa a entrada de tarefa
    entrada_tarefa.insert(0,label_tarefa.cget("text"))  # Insere o texto da tarefa que está sendo editada na entrada de tarefa

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao  # Declara que vamos usar a variável global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():  # Para cada widget no frame que está sendo editado
        if isinstance(widget, tk.Label):  # Se o widget é um rótulo
            widget.config(text= nova_tarefa)  # Atualiza o texto do rótulo

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()  # Deleta o frame da tarefa
    canvas_interior.update_idletasks()  # Atualiza as tarefas ociosas do frame interior do canvas
    canvas.config( scrollregion= canvas.bbox("all"))  # Configura a região de rolagem do canvas para incluir todos os itens

def alterar_sublinhado(label):
    font_atual = label.cget("font")  # Obtém a fonte atual do rótulo
    if "underline" in font_atual:  # Se a fonte atual tem sublinhado
        nova_fonte = font_atual.replace("underline","")  # Remove o sublinhado da fonte
    else:
        nova_fonte = font_atual + " underline"  # Adiciona sublinhado à fonte
    label.config(font = nova_fonte)  # Configura a fonte do rótulo para a nova fonte

icon_editar = PhotoImage(file="c:/Users/C9951742/OneDrive - Eaton/Documents/Portifólio/editar.png").subsample(2,2)  # Carrega a imagem do ícone de editar
icon_deletar = PhotoImage(file= "c:/Users/C9951742/OneDrive - Eaton/Documents/Portifólio/lixeira.png").subsample(2,2)  # Carrega a imagem do ícone de deletar

fonte_cabecalho = font.Font(family= "Garamond", size= 26,weight="bold")  # Define a fonte do cabeçalho
rotulo_cabecalho = tk.Label(janela, text= "Lugar de anotar os Trem", font= fonte_cabecalho, bg= "#F0F0F0", fg= "#333").pack(pady=20)  # Cria um rótulo para o cabeçalho e adiciona ao frame da janela

frame = tk.Frame (janela,bg="#3a3c40")  # Cria um frame para a entrada de tarefa e o botão de adicionar
frame.pack(pady=10)  # Adiciona o frame ao frame da janela

entrada_tarefa = tk.Entry(frame, font=("Arial",14),relief=tk.FLAT,bg= "#4CAF50", fg="#333", width=30 )  # Cria uma entrada para a tarefa
entrada_tarefa.pack(side=tk.LEFT,padx=10 )  # Adiciona a entrada de tarefa ao frame

botao_adicionar = tk.Button(frame, command= adicionar_tarefa, text="Escreva sua tarefa aqui", bg= "#4CAF50",fg= "#333", height=3, width=35, font=("Roboto", 11), relief=tk.FLAT)  # Cria um botão para adicionar tarefa
botao_adicionar.pack(side= tk.LEFT,padx= 20)  # Adiciona o botão de adicionar ao frame

# Criar um frame para lista de tarefas com rolagem   
frame_lista_Tarefas = tk.Frame(janela, bg="white")  # Cria um frame para a lista de tarefas
frame_lista_Tarefas.pack(fill=tk.BOTH,expand= True, padx= 10, pady= 10)  # Adiciona o frame da lista de tarefas ao frame da janela

canvas = tk.Canvas(frame_lista_Tarefas,bg= "white")  # Cria um canvas para a lista de tarefas
canvas.pack(side= tk.LEFT,fill= tk.BOTH, expand= True)  # Adiciona o canvas ao frame da lista de tarefas

scrollbar = tk.Scrollbar(frame_lista_Tarefas, orient= "vertical", command= canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand= scrollbar.set)  # Configura o canvas para atualizar a posição da barra de rolagem quando o usuário rola o canvas
canvas_interior = tk.Frame(canvas, bg="White")  # Cria um frame dentro do canvas. Este frame vai conter todos os itens da lista de tarefas
canvas.create_window((0, 0),window=canvas_interior,anchor="nw")  # Cria uma janela dentro do canvas no ponto (0,0) que vai conter o frame interior. O parâmetro 'anchor="nw"' faz com que o frame interior seja ancorado no canto superior esquerdo (noroeste) da janela
canvas_interior.bind("<Configure>",lambda e: canvas.configure(scrollregion= canvas.bbox("all")))  # Vincula o evento <Configure> do frame interior a uma função que atualiza a região de rolagem do canvas para incluir todos os itens. O evento <Configure> é disparado sempre que o frame interior é redimensionado

janela.mainloop()  # Inicia o loop principal do tkinter. Isso faz com que a janela fique aberta e responda aos eventos do usuário

 
