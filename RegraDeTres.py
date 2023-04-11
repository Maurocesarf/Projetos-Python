# este projeto tem uma interface grafica, por tanto utilizei o tkinter que é uma biblioteca instalada nativamente no python que ajuda com isso

import tkinter as tk

janela = tk.Tk()
nome = ""

janela.title("Regra de Três Simples")
janela.geometry("340x150")


#verificando o tipo de regra de 3 que o usuario quer utilizar

texto = tk.Label(janela, text="""Qual regra de três você quer usar? 
Digite: 'I' para inversa ou 'N' normal """)

resposta = tk.Entry(janela)

def enviar_resposta():
    global nome
    nome = resposta.get().upper()
    if nome == 'I' or nome == 'N':
        janela.destroy()
    else:
        texto_erro = tk.Label(janela, text='Digite apenas "N" ou "I"')
        texto_erro.grid(row=4, column=0, padx=0, pady=5)

botao = tk.Button(janela, text="Ok", command=enviar_resposta)

texto.grid(row=1, column=0, padx=70, pady=5)
resposta.grid(row=2, column=0, padx=0, pady=5)
botao.grid(row=3, column=0, padx=0, pady=5)

janela.mainloop()


# Calculando a regra de 3

def calcularnormal():
    valor1 = float(entry1.get())
    valor2 = float(entry2.get())
    valor3 = float(entry3.get())

    resultado ='{:.0f}'.format((valor3 * valor2) / valor1)

    resultado_label.config(text="O valor de X é: " + str(resultado))

def calcularinversa():
    valor1 = float(entry1.get())
    valor2 = float(entry2.get())
    valor3 = float(entry3.get())

    resultado ='{:.0f}'.format((valor1 * valor2) / valor3)

    resultado_label.config(text="O valor de X é: " + str(resultado))

    
# Editando a interface grafica
    
janela = tk.Tk()
janela.geometry("340x120")

label1 = tk.Label(janela, text="")
label2 = tk.Label(janela, text="para")
label3 = tk.Label(janela, text="")
entry1 = tk.Entry(janela)
entry2 = tk.Entry(janela)
entry3 = tk.Entry(janela)

if nome == 'N':
    calcular_btn = tk.Button(janela, text="Calcular", command=calcularnormal)
    janela.title("Regra de Três Normal")
elif nome == 'I':
    calcular_btn = tk.Button(janela, text="Calcular", command=calcularinversa)
    janela.title("Regra de Três Inversa")
resultado_label = tk.Label(janela, text="")

label1.grid(row=1, column=0, padx=5, pady=5)
entry1.grid(row=1, column=1, padx=5, pady=5)
label2.grid(row=1, column=2, padx=5, pady=5)
entry2.grid(row=1, column=3, padx=5, pady=5)
label3.grid(row=2, column=1, padx=5, pady=5)
entry3.grid(row=2, column=1, padx=5, pady=5)
calcular_btn.grid(row=3, column=1,columnspa=3, padx=10, pady=15)
resultado_label.grid(row=2, column=3,columnspa=1, padx=5, pady=5)

janela.mainloop()
