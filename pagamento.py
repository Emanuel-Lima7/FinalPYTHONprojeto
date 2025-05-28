import tkinter as tk
from tkinter import ttk, messagebox

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

    
    
    criar_secao_pagamento(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()