from tkinter import * # Importa todas as classes e funções do módulo tkinter
from tkinter import ttk # Importa o módulo ttk para usar widgets temáticos

# Define cores para serem usadas na interface do usuário
cor1 = "#3b3b3b" #preta
cor2 = "#feffff" #branco
cor3 = "#38576b" #azul carregado
cor4 = "#ECEFF1" #cinzenta
cor5 = "#FFAB40" #laranja

janela = Tk()  # Cria a janela principal
janela.title("Calculadora") # Define o título da janela
janela.geometry("235x310") # Define o tamanho da janela
janela.config( bg = cor1) # Define a cor de fundo da janela


frame_tela = Frame(janela, width= 235, height= 50,bg= cor3)# Cria um frame para a tela
frame_tela.grid(row= 0, column= 0)  # Posiciona o frame na janela

frame_corpo = Frame(janela, width= 235, height= 268 ) # Cria um frame para o corpo
frame_corpo.grid(row= 1, column= 0)# Posiciona o frame na janela

# Variável para armazenar todos os valores inseridos pelo usuário
todos_valores= ''

valor_texto = StringVar() # Cria uma variável de texto para exibir na tela


# Função para adicionar valores à variável todos_valores
def entrar_valores(event):

    global todos_valores # Declara todos_valores como global

    todos_valores = todos_valores + str(event) # Adiciona o valor do evento à variável todos_valores
    
    #passando valor para tela
    valor_texto.set(todos_valores) # Atualiza o valor exibido na tela

# Função para calcular a expressão armazenada em todos_valores
def calcular():
    global todos_valores # Declara todos_valores como global
    resultado = eval(todos_valores) # Calcula o resultado da expressão
    valor_texto.set(str(resultado)) # Atualiza o valor exibido na tela com o resultado

#função limpar tela
def limpar_tela():
    global todos_valores  # Declara todos_valores como global
    todos_valores = "" # Limpa a variável todos_valores
    valor_texto.set("") # Limpa o valor exibido na tela



# Cria um label para exibir o valor na tela
# O comando pode ser uma função definida anteriormente ou uma expressão lambda que chama a função entrar_valores com um valor específico
# Os botões são posicionados no frame do corpo usando o método place
app_label = Label(frame_tela, textvariable= valor_texto, width= 16, height= 2,padx= 7, relief= FLAT, anchor= "e",justify= RIGHT, font=('Ivy 18'),bg= cor3, fg= cor2)
app_label.place(x= 0, y=0)  # Posiciona o label no frame da tela

# Cria os botões da calculadora
b_1 = Button(frame_corpo, command= limpar_tela, text= "C", width= 11, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_1.place(x= 0, y= 0) # Cada botão tem um comando associado que é executado quando o botão é pressionado

b_2 = Button(frame_corpo, command= lambda: entrar_valores( '%' ),  text= "%", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_2.place(x= 118, y= 0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores( '/' ),text= "/", width= 5, height= 2,bg= cor5,fg= cor2, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_3.place(x= 177, y= 0)

b_4 = Button(frame_corpo, command= lambda: entrar_valores( '7' ),text= "7", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_4.place(x= 0, y= 52)
b_5 = Button(frame_corpo, command= lambda: entrar_valores( '8' ),text= "8", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_5.place(x= 59, y= 52)
b_6 = Button(frame_corpo, command= lambda: entrar_valores( '9' ),text= "9", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_6.place(x= 118, y= 52)
b_7 = Button(frame_corpo, command= lambda: entrar_valores( '*' ),text= "*", width= 5, height= 2,bg= cor5,fg= cor2, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_7.place(x= 177, y= 52)

b_8 = Button(frame_corpo, command= lambda: entrar_valores( '4' ),text= "4", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_8.place(x= 0, y= 104)
b_9 = Button(frame_corpo, command= lambda: entrar_valores( '5' ),text= "5", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_9.place(x= 59, y= 104)
b_10 = Button(frame_corpo, command= lambda: entrar_valores( '6' ),text= "6", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_10.place(x= 118, y= 104)
b_11= Button(frame_corpo, command= lambda: entrar_valores( '-' ),text= "-", width= 5, height= 2,bg= cor5,fg= cor2, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_11.place(x= 177, y= 104)

b_12= Button(frame_corpo, command= lambda: entrar_valores( '1' ),text= "1", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_12.place(x= 0, y= 156)
b_13= Button(frame_corpo, command= lambda: entrar_valores( '2' ),text= "2", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_13.place(x= 59, y= 156)
b_14= Button(frame_corpo, command= lambda: entrar_valores( '3' ),text= "3", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_14.place(x= 118, y= 156)
b_15= Button(frame_corpo, command= lambda: entrar_valores( '+' ),text= "+", width= 5, height= 2,bg= cor5,fg= cor2, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_15.place(x= 177, y= 156)

b_12 = Button(frame_corpo, command= lambda: entrar_valores( '0' ),text= "0", width= 11, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_12.place(x= 0, y= 208)

b_13 = Button(frame_corpo, command= lambda: entrar_valores( '.' ),text= ".", width= 5, height= 2,bg= cor4, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_13.place(x= 118, y= 208)

b_14= Button(frame_corpo, command= calcular,text= "=", width= 5, height= 2,bg= cor5,fg= cor2, font= ('Ivy 13 bold'),relief= RAISED, overrelief=RIDGE)
b_14.place(x= 177, y= 208)

# Botões para inserir operadores e números
# O restante do código segue o mesmo padrão para criar e posicionar os botões



janela.mainloop()
# Finalmente, o loop principal da janela é iniciado
 