import tkinter as tk
from tkinter import ttk, messagebox

sabor_valor = None
bebida_valor = None
total_pedido = 0.0

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

def main():
    root = tk.Tk()
    root.title(" Jampa Pizzaria")
    root.geometry("500x700")
    root.resizable(False, False)

   #tema tkinter
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TRadiobutton", font=("Helvetica", 11))
    style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), background="#2ECC71", foreground="white")

    criar_secao_sabores(root)
    criar_secao_bebidas(root) 
    criar_label_total(root)
 

    root.mainloop()


if __name__ == "__main__":
    main()

