import tkinter as tk
from tkinter import ttk, messagebox


def criar_secao_titulo(parent_window):
    titulo_label = ttk.Label(parent_window, text="🍕 Jampa Pizzaria 🍕", font=("Helvetica", 20, "bold"), foreground="#4CAF50")
    titulo_label.pack(pady=20)
    return titulo_label

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


    criar_secao_titulo(root)

    root.mainloop()


if __name__ == "__main__":
    main()

