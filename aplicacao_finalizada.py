import tkinter as tk
from tkinter import ttk, messagebox

def criar_secao_titulo(parent_window):
    titulo_label = ttk.Label(parent_window, text="🍕 Jampa Pizzaria 🍕", font=("Helvetica", 20, "bold"), foreground="#4CAF50")
    titulo_label.pack(pady=20)
    return titulo_label

import tkinter as tk
from tkinter import ttk, messagebox

sabor_valor = None
bebida_valor = None
total_pedido = 0.0
endereco_var = None
pagamento_var = None

sabores_precos = {
    "Mussarela": 35.00,
    "Calabresa": 38.00,
    "Frango com Catupiry": 42.00,
    "Quatro Queijos": 45.00
}

bebidas_precos = {
    "Refrigerante Lata": 6.00,
    "Suco Natural": 8.00,
    "Água Mineral": 2.00,
    "Cerveja Long Neck": 10.00
}

def criar_secao_sabores(parent_window):
    global sabor_valor
    sabor_valor = tk.StringVar(value="Mussarela") 

    sabor_frame = ttk.LabelFrame(parent_window, text="Escolha o Sabor da Pizza", padding=(15, 10))

    for texto, preco in sabores_precos.items():
        ttk.Radiobutton(
            sabor_frame,
            text=f"{texto} (R$ {preco:.2f})", 
            variable=sabor_valor,
            value=texto,
            command=atualizar_total 
        ).pack(anchor="w", pady=3)

    sabor_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return sabor_frame

def criar_secao_bebidas(parent_window):
    global bebida_valor

    bebida_valor = tk.StringVar(value=list(bebidas_precos.keys())[0]) 

    bebidas_frame = ttk.LabelFrame(parent_window, text="Escolha a Bebida", padding=(15, 10))

    for nome, preco in bebidas_precos.items():
        ttk.Radiobutton(
            bebidas_frame,
            text=f"{nome} (R$ {preco:.2f})",
            variable=bebida_valor,
            value=nome,
            command=atualizar_total 
        ).pack(anchor="w", pady=3)

    bebidas_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return bebidas_frame

def criar_secao_pagamento(parent_window):
    
    global pagamento_var
    pagamento_var = tk.StringVar(value="Dinheiro") 

    pagamento_frame = ttk.LabelFrame(parent_window, text="Forma de Pagamento", padding=(15, 10))

    formas_pagamento = ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Pix"]

    for forma in formas_pagamento:
        ttk.Radiobutton(
            pagamento_frame,
            text=forma,
            variable=pagamento_var,
            value=forma
        ).pack(anchor="w", pady=3)

    pagamento_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return pagamento_frame

def criar_secao_endereco(parent_window):
    
    global endereco_var
    endereco_var = tk.StringVar() 

    endereco_frame = ttk.LabelFrame(parent_window, text="Endereço de Entrega:", padding=(15, 10))

    ttk.Label(endereco_frame, text="Informe o seu endereço:").pack(anchor="w", pady=5)
    endereco_entry = ttk.Entry(endereco_frame, textvariable=endereco_var, width=60)
    endereco_entry.pack(anchor="w", pady=5)

    endereco_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return endereco_frame

def criar_label_total(parent_window):
    global total_pedido_label
    total_pedido_label = ttk.Label(parent_window, text="Total: R$ 0.00", font=("Helvetica", 14, "bold"), foreground="#E67E22")
    total_pedido_label.pack(pady=10)
    return total_pedido_label

def atualizar_total():
    global total_pedido, total_pedido_label, sabor_valor, bebida_valor, sabores_precos, bebidas_precos
    
    total_pedido = 0.0

    sabor_selecionado = sabor_valor.get()
    total_pedido += sabores_precos.get(sabor_selecionado, 0.0) 

    bebida_selecionada = bebida_valor.get()
    total_pedido += bebidas_precos.get(bebida_selecionada, 0.0) 

    total_pedido_label.config(text=f"Total: R$ {total_pedido:.2f}")

def finalizar_pedido():
    
    sabor_selecionado = sabor_valor.get()
    bebida_selecionada = bebida_valor.get()
    pagamento_selecionado = pagamento_var.get()
    endereco_digitado = endereco_var.get()

    if not sabor_selecionado:
        messagebox.showwarning("Atenção", "Por favor, escolha um sabor de pizza.")
        return
    if not pagamento_selecionado:
        messagebox.showwarning("Atenção", "Por favor, escolha uma forma de pagamento.")
        return

    janela_resumo = tk.Toplevel()
    janela_resumo.title("✅ Pedido Confirmado!")
    janela_resumo.geometry("450x450")
    janela_resumo.resizable(False, False)

    janela_resumo.update_idletasks()
    x = janela_resumo.winfo_x() + (janela_resumo.winfo_width() / 2)
    y = janela_resumo.winfo_y() + (janela_resumo.winfo_height() / 2)
    janela_resumo.geometry(f"+{int(janela_resumo.winfo_screenwidth()/2 - janela_resumo.winfo_width()/2)}+{int(janela_resumo.winfo_screenheight()/2 - janela_resumo.winfo_height()/2)}")
    
    janela_resumo.configure(bg="#F0F8FF") 
    
    titulo_resumo = ttk.Label(janela_resumo, text="🍕 Seu Pedido na Jampa Pizzaria! 🍕",
                              font=("Helvetica", 16, "bold"), foreground="#4CAF50", background="#F0F8FF")
    titulo_resumo.pack(pady=15)

    info_frame = tk.Frame(janela_resumo, bg="#F0F8FF", padx=20, pady=10)
    info_frame.pack(fill="x", padx=20)

    ttk.Label(info_frame, text="Sabor:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=0, column=0, sticky="w", pady=5)
    ttk.Label(info_frame, text=sabor_selecionado, font=("Helvetica", 12), background="#F0F8FF").grid(row=0, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(info_frame, text="Bebida:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=1, column=0, sticky="w", pady=5) 
    ttk.Label(info_frame, text=bebida_selecionada, font=("Helvetica", 12), background="#F0F8FF").grid(row=1, column=1, sticky="w", padx=10, pady=5) 

    ttk.Label(info_frame, text="Pagamento:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=2, column=0, sticky="w", pady=5)
    ttk.Label(info_frame, text=pagamento_selecionado, font=("Helvetica", 12), background="#F0F8FF").grid(row=2, column=1, sticky="w", padx=10, pady=5)

    ttk.Label(info_frame, text="Endereço:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=3, column=0, sticky="w", pady=5) 
    ttk.Label(info_frame, text=endereco_digitado, font=("Helvetica", 12), background="#F0F8FF", wraplength=300).grid(row=3, column=1, sticky="w", padx=10, pady=5) 

    ttk.Label(info_frame, text="Preço Total:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=4, column=0, sticky="w", pady=5)
    ttk.Label(info_frame, text=f"R$ {total_pedido:.2f}", font=("Helvetica", 12, "bold"), foreground="#E67E22", background="#F0F8FF").grid(row=4, column=1, sticky="w", padx=10, pady=5)

    agradecimento_label = ttk.Label(janela_resumo, text="🌟 Obrigado por escolher a Jampa Pizzaria! 🌟",font=("Helvetica", 13, "italic"), foreground="#3498DB", background="#F0F8FF")
    agradecimento_label.pack(pady=20, side="bottom")

    btn_fechar = ttk.Button(janela_resumo, text="OK", command=janela_resumo.destroy, style="Accent.TButton")
    btn_fechar.pack(pady=10, ipadx=10, ipady=5)

def criar_botao_finalizar(parent_window):
    
    finalizar_button = ttk.Button(parent_window, text="Finalizar Pedido", command=finalizar_pedido, style="Accent.TButton")
    finalizar_button.pack(pady=30, ipadx=15, ipady=8)
    return finalizar_button

def main():
    global sabor_valor, bebida_valor, endereco_var, pagamento_var, total_pedido_label

    root = tk.Tk()
    root.title(" Jampa Pizzaria")
    root.geometry("500x900")
    root.resizable(False, False)

    sabor_valor = tk.StringVar(value="Mussarela")
    bebida_valor = tk.StringVar(value=list(bebidas_precos.keys())[0]) 
    endereco_var = tk.StringVar()
    pagamento_var = tk.StringVar(value="Dinheiro")

   #tema tkinter
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TRadiobutton", font=("Helvetica", 11))
    style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), background="#2ECC71", foreground="white")


    criar_secao_titulo(root)
    criar_secao_sabores(root)
    criar_secao_bebidas(root)
    criar_secao_pagamento(root)
    criar_secao_endereco(root)
    criar_label_total(root)

    atualizar_total()

    criar_botao_finalizar(root)

    root.mainloop()


if __name__ == "__main__":
    main()