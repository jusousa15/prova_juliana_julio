import tkinter as tk
from openai import OpenAI

# Configuração do cliente OpenAI
client = OpenAI(api_key="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")

def send_command():
    command = entry.get()
    if command:
        response_label.config(text="Processando...")
        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": command}]
            )
            response = completion.choices[0].message.content
        except Exception as e:
            response = f"Erro: {str(e)}"
        response_label.config(text=response)

# Criando a interface Tkinter
root = tk.Tk()
root.title("Painel de Comandos")
root.geometry("400x300")

# Campo de entrada
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Botão de envio
send_button = tk.Button(root, text="Enviar Comando", command=send_command)
send_button.pack(pady=5)

# Rótulo para exibir a resposta
response_label = tk.Label(root, text="", wraplength=380, justify="left")
response_label.pack(pady=10)

root.mainloop()