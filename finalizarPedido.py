import tkinter as tk
from tkinter import ttk, messagebox

sabores_precos = {
    "Mussarela": 35.00,
    "Calabresa": 38.00,
    "Frango com Catupiry": 42.00,
    "Quatro Queijos": 45.00
}

def criar_secao_sabores(parent_window):
    
    global sabor_var
    sabor_var = tk.StringVar(value="Mussarela") 

    sabor_frame = ttk.LabelFrame(parent_window, text="Escolha o Sabor da Pizza", padding=(15, 10))

    for texto, preco in sabores_precos.items():
        ttk.Radiobutton(
            sabor_frame,
            text=f"{texto} (R$ {preco:.2f})", 
            variable=sabor_var,
            value=texto 
        ).pack(anchor="w", pady=3)

    sabor_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return sabor_frame

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

def finalizar_pedido():
    
    sabor_selecionado = sabor_var.get()
    pagamento_selecionado = pagamento_var.get()

    if not sabor_selecionado:
        messagebox.showwarning("Atenção", "Por favor, escolha um sabor de pizza.")
        return
    if not pagamento_selecionado:
        messagebox.showwarning("Atenção", "Por favor, escolha uma forma de pagamento.")
        return

    janela_resumo = tk.Toplevel()
    janela_resumo.title("✅ Pedido Confirmado!")
    janela_resumo.geometry("450x300")
    janela_resumo.resizable(False, False)

    janela_resumo.update_idletasks()
    x = janela_resumo.winfo_x() + (janela_resumo.winfo_width() / 2)
    y = janela_resumo.winfo_y() + (janela_resumo.winfo_height() / 2)
    janela_resumo.geometry(f"+{int(janela_resumo.winfo_screenwidth()/2 - janela_resumo.winfo_width()/2)}+{int(janela_resumo.winfo_screenheight()/2 - janela_resumo.winfo_height()/2)}")
    
    janela_resumo.configure(bg="#F0F8FF") 
    
    titulo_resumo = ttk.Label(janela_resumo, text="🍕 Seu Pedido na Pizzaria Python! 🍕",
                              font=("Helvetica", 16, "bold"), foreground="#4CAF50", background="#F0F8FF")
    titulo_resumo.pack(pady=15)

    info_frame = tk.Frame(janela_resumo, bg="#F0F8FF", padx=20, pady=10)
    info_frame.pack(fill="x", padx=20)

    ttk.Label(info_frame, text="Pagamento:", font=("Helvetica", 12, "bold"), background="#F0F8FF").grid(row=2, column=0, sticky="w", pady=5)
    ttk.Label(info_frame, text=pagamento_selecionado, font=("Helvetica", 12), background="#F0F8FF").grid(row=2, column=1, sticky="w", padx=10, pady=5)

    agradecimento_label = ttk.Label(janela_resumo, text="🌟 Obrigado por escolher a Pizzaria Python! 🌟",font=("Helvetica", 13, "italic"), foreground="#3498DB", background="#F0F8FF")
    agradecimento_label.pack(pady=20, side="bottom")

    btn_fechar = ttk.Button(janela_resumo, text="OK", command=janela_resumo.destroy, style="Accent.TButton")
    btn_fechar.pack(pady=10, ipadx=10, ipady=5)

def criar_botao_finalizar(parent_window):
    
    finalizar_button = ttk.Button(parent_window, text="Finalizar Pedido", command=finalizar_pedido, style="Accent.TButton")
    finalizar_button.pack(pady=30, ipadx=15, ipady=8)
    return finalizar_button

def main():
    
    root = tk.Tk()
    root.title("Pizzaria Python")
    root.geometry("700x700")
    root.resizable(False, False)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TLabel", font=("Helvetica", 12))
    style.configure("TRadiobutton", font=("Helvetica", 11))
    style.configure("Accent.TButton", font=("Helvetica", 12, "bold"), background="#000000", foreground="white")

    criar_secao_sabores(root)
    criar_secao_pagamento(root)
    criar_botao_finalizar(root)
    
    
    root.mainloop()

if __name__ == "__main__":
    main()