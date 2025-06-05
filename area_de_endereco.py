import tkinter as tk
from tkinter import ttk, messagebox

def criar_secao_endereco(parent_window):
    
    global endereco_var
    endereco_var = tk.StringVar() 

    endereco_frame = ttk.LabelFrame(parent_window, text="Endereço de Entrega", padding=(15, 10))

    ttk.Label(endereco_frame, text="Informe o seu endereço:").pack(anchor="w", pady=5)
    endereco_entry = ttk.Entry(endereco_frame, textvariable=endereco_var, width=60)
    endereco_entry.pack(anchor="w", pady=5)

    endereco_frame.pack(padx=25, pady=10, fill="x", expand=True)
    return endereco_frame

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

    
    
    criar_secao_endereco(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()