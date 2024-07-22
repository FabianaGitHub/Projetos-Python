import tkinter as tk #Importa o módulo tkinter e o renomeia como tk. O tkinter é um módulo para criar interfaces gráficas de usuário (GUIs) em Python.
from tkinter import messagebox, filedialog #é usado para exibir caixas de mensagem e filedialog é usado para abrir caixas de diálogo de arquivos.
import random # Importa o módulo random que contém funções para gerar números aleatórios.
import string # Importa o módulo random que contém funções para gerar números aleatórios.

# Função para gerar uma senha aleatória
def generate_password(): #Define uma função chamada generate_password.
    length = 12  # Tamanho da senha
    characters = string.ascii_letters + string.digits + string.punctuation #Define os caracteres que podem ser usados na senha. Inclui letras maiúsculas e minúsculas, dígitos e pontuação.
    password = ''.join(random.choice(characters) for i in range(length)) #Gera uma senha aleatória de comprimento length escolhendo aleatoriamente de characters.
    return password # Retorna a senha gerada.

# Função para salvar a senha em um arquivo
def save_password(): #Define uma função chamada save_password.
    password = generate_password() #Gera uma senha usando a função generate_password.
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")]) #Abre uma caixa de diálogo para o usuário escolher onde salvar a senha. O arquivo será salvo com a extensão .txt.
    if file_path: #Verifica se um caminho de arquivo foi selecionado.
        with open(file_path, "w") as file: #Abre o arquivo selecionado em modo de escrita.
            file.write(password) #Escreve a senha no arquivo.
        messagebox.showinfo("Sucesso", f"Senha salva em {file_path}") #Exibe uma caixa de mensagem informando que a senha foi salva com sucesso.
    else: #Se nenhum arquivo foi selecionado…
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado. Senha não foi salva.") #Exibe uma caixa de mensagem de aviso informando que nenhuma senha foi salva.

# Função para copiar a senha para a área de transferência
def copy_to_clipboard(): #Define uma função chamada copy_to_clipboard.
    password = generate_password() #Gera uma senha usando a função generate_password.
    root.clipboard_clear()  # Limpar a área de transferência
    root.clipboard_append(password)  # Adicionar a senha à área de transferência
    root.update()  # Atualizar a área de transferência
    messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!") #Exibe uma caixa de mensagem informando que a senha foi copiada para a área de transferência.

# Criar a janela principal
if __name__ == "__main__": #Verifica se o script está sendo executado diretamente (não sendo importado).
    root = tk.Tk() #Cria a janela principal.
    root.title("Gerador de Senhas")#Define o título da janela como “Gerador de Senhas”.

    # Botão para gerar e salvar a senha
    generate_button = tk.Button(root, text="Nova senha Bloco de nota", command=save_password)
    generate_button.pack(pady=20)#Cria um botão que, quando clicado, chama a função

    # Botão para copiar a senha para a área de transferência
    copy_button = tk.Button(root, text="Gerar e Copiar Senha", command=copy_to_clipboard)#Cria um botão que, quando clicado, chama a função
    copy_button.pack(pady=10) #Adiciona o botão à janela com um preenchimento vertical de 10 pixels.

    # Executar a aplicação
    root.mainloop() #Inicia o loop principal da janela, o que faz com que a janela apareça na tela.
