import tkinter as tk
from tkinter import messagebox

class SaborRapidoApp:
    # Cria a classe que contém o modelo do objeto (neste caso, nosso app)
    def __init__(self, root):
        # Construtor da classe, define a janela principal
        self.root = root
        self.root.title("Sabor Rápido - Protótipo")
        self.root.geometry("400x500")

        # Dicionário com os itens disponíveis no menu
        self.itens_menu = {"hamburger": 10.90, "batata": 15.60, "refrigerante": 7.50}
        self.pedido = []  # Lista de pedidos vazia

        # Interface de seleção de itens
        tk.Label(root, text="Selecionar os itens do pedido:", font=("Arial", 12)).pack(pady=10)
        self.listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, font=("Arial", 10))
        self.atualizar_lista_menu()
        self.listbox.pack()

        # Botões de ação
        tk.Button(root, text="Adicionar ao Pedido", command=self.adicionar_pedido).pack(pady=5)
        tk.Button(root, text="Visualizar Pedido", command=self.visualizar_pedidos).pack(pady=5)
        tk.Button(root, text="Finalizar Pedido", command=self.finalizar_pedido).pack(pady=5)

        # Interface para adicionar novos itens ao menu
        tk.Label(root, text="Adicionar novo item ao Menu:", font=("Arial", 12)).pack(pady=10)
        self.entry_item = tk.Entry(root, font=("Arial", 10))
        self.entry_item.pack()
        self.entry_preco = tk.Entry(root, font=("Arial", 10))
        self.entry_preco.pack()
        tk.Button(root, text="Adicionar item", command=self.adicionar_item_menu).pack(pady=5)

    def atualizar_lista_menu(self):
        # Atualiza o listbox com os itens do menu
        self.listbox.delete(0, tk.END)
        for item in self.itens_menu.keys():
            self.listbox.insert(tk.END, item)

    def adicionar_pedido(self):
        # Adiciona os itens selecionados ao pedido
        selecionados = self.listbox.curselection()
        for index in selecionados:
            item = self.listbox.get(index)
            self.pedido.append(item)
        messagebox.showinfo("Pedido", "Itens adicionados com sucesso!")

    def visualizar_pedidos(self):
        # Exibe os itens do pedido atual
        if not self.pedido:
            messagebox.showinfo("Pedido", "Nenhum item no pedido")
            return
        pedido_texto = "\n".join(self.pedido)
        messagebox.showinfo("Pedido Atual", f"Itens no pedido:\n{pedido_texto}")

    def finalizar_pedido(self):
        # Calcula o total e finaliza o pedido
        if not self.pedido:
            messagebox.showinfo("Pedido", "Adicione itens antes de finalizar o pedido")
            return
        total = sum(self.itens_menu[item] for item in self.pedido)
        messagebox.showinfo("Total", f"Total do Pedido: R$ {total:.2f}\nPedido finalizado!")
        self.pedido.clear()

    def adicionar_item_menu(self):
        # Adiciona um novo item ao menu
        item = self.entry_item.get().strip()
        preco = self.entry_preco.get().strip()
        if item and preco:
            try:
                self.itens_menu[item] = float(preco)
                self.atualizar_lista_menu()
                self.entry_item.delete(0, tk.END)
                self.entry_preco.delete(0, tk.END)
                messagebox.showinfo("Sucesso", "Item adicionado ao menu com sucesso!")
            except ValueError:
                messagebox.showerror("Erro", "Preço inválido. Digite um valor numérico.")
        else:
            messagebox.showerror("Erro", "Preencha ambos os campos corretamente.")

# Execução do app
if __name__ == "__main__":
    root = tk.Tk()
    app = SaborRapidoApp(root)
    root.mainloop()







