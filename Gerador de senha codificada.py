import tkinter as tk  # Importa o módulo tkinter para criar interfaces gráficas de usuário (GUIs)
from tkinter import messagebox, filedialog  # Importa messagebox e filedialog do módulo tkinter
import random  # Importa o módulo random para gerar números aleatórios
import string  # Importa o módulo string para trabalhar com strings
import hashlib  # Importa o módulo hashlib para criptografar senhas

# Função para gerar uma senha aleatória
def generate_password():
    length = 12  # Define o tamanho da senha
    characters = string.ascii_letters + string.digits + string.punctuation  # Define os caracteres que podem ser usados na senha
    password = ''.join(random.choice(characters) for i in range(length))  # Gera a senha
    return password  # Retorna a senha gerada

# Função para criptografar a senha
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  # Criptografa a senha usando SHA256

# Função para salvar a senha em um arquivo
def save_password():
    password = generate_password()  # Gera uma senha
    encrypted_password = encrypt_password(password)  # Criptografa a senha
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])  # Abre uma caixa de diálogo para o usuário escolher onde salvar a senha
    if file_path:  # Verifica se um caminho de arquivo foi selecionado
        with open(file_path, "w") as file:  # Abre o arquivo selecionado em modo de escrita
            file.write(encrypted_password)  # Escreve a senha criptografada no arquivo
        messagebox.showinfo("Sucesso", f"Senha salva em {file_path}")  # Exibe uma mensagem de sucesso
    else:  # Se nenhum arquivo foi selecionado
        messagebox.showwarning("Aviso", "Nenhum arquivo selecionado. Senha não foi salva.")  # Exibe uma mensagem de aviso

# Função para copiar a senha para a área de transferência
def copy_to_clipboard():
    password = generate_password()  # Gera uma senha
    encrypted_password = encrypt_password(password)  # Criptografa a senha
    root.clipboard_clear()  # Limpa a área de transferência
    root.clipboard_append(encrypted_password)  # Adiciona a senha criptografada à área de transferência
    root.update()  # Atualiza a área de transferência
    messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")  # Exibe uma mensagem de sucesso

# Criar a janela principal
if __name__ == "__main__":
    root = tk.Tk()  # Cria a janela principal
    root.title("Gerador de Senhas")  # Define o título da janela

    # Botão para gerar e salvar a senha
    generate_button = tk.Button(root, text="Nova senha Bloco de nota", command=save_password)  # Cria um botão para gerar e salvar a senha
    generate_button.pack(pady=20)  # Adiciona o botão à janela

    # Botão para copiar a senha para a área de transferência
    copy_button = tk.Button(root, text="Gerar e Copiar Senha", command=copy_to_clipboard)  # Cria um botão para copiar a senha para a área de transferência
    copy_button.pack(pady=10)  # Adiciona o botão à janela

    # Executar a aplicação
    root.mainloop()  # Inicia o loop principal da janela
