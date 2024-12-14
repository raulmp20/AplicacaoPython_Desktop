import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import webbrowser

class DesktopApp:
    def __init__(self, root):
        # Inicializa a aplicação com a janela principal
        self.root = root
        self.root.title("Aplicação Desktop")
        self.root.geometry("800x600")

        # Notebook para múltiplas telas (abas)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Criação daas diferentes telas/abas
        self.create_notepad_tab() # Bloco de Notas
        self.create_counter_tab() # Contador
        self.create_movie_tab() # Lista de Filmes

    # Definindo as configurações do fundo da tela usando uma imagem
    def set_background(self, frame, image_path):
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(frame, image=bg_photo)
        bg_label.image = bg_photo  # Manter referência para evitar coleta de lixo
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Centralizando as funcionalidades de cada tela
    def create_centered_frame(self, parent, width, height):
        frame = tk.Frame(parent, bg="white", width=width, height=height)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        frame.pack_propagate(False)  # Desabilitar redimensionamento automático
        return frame

    # Bloco de Notas
    def create_notepad_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Bloco de Notas")

        self.set_background(frame, "images/background1.jpg")

        content_frame = self.create_centered_frame(frame, 600, 400)

        # Área de texto
        self.text_area = tk.Text(content_frame, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Botões
        button_frame = tk.Frame(content_frame, bg="white")
        button_frame.grid(row=1, column=0, pady=5)

        open_btn = ttk.Button(button_frame, text="Abrir", command=self.open_file)
        open_btn.grid(row=0, column=0, padx=5)

        save_btn = ttk.Button(button_frame, text="Salvar", command=self.save_file)
        save_btn.grid(row=0, column=1, padx=5)

        # Tornar a área de texto expansível para preencher o espaço
        content_frame.grid_rowconfigure(0, weight=1)
        content_frame.grid_columnconfigure(0, weight=1)

    # Abrindo os arquivos de texto
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:  # Usar UTF-8 para preservar a codificação
                    content = file.read()
                    self.text_area.delete(1.0, tk.END)  # Limpar o conteúdo atual
                    self.text_area.insert(tk.END, content)  # Inserir o conteúdo lido no Text
            except Exception as e:
                print(f"Erro ao abrir o arquivo: {e}")

    # Salvando os arquivos de texto
    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)

    # Contador
    def create_counter_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Contador Numérico")

        self.set_background(frame, "images/background2.jpg")

        content_frame = self.create_centered_frame(frame, 300, 200)

        self.counter = tk.IntVar(value=0)

        # Exibição do contador
        label = tk.Label(content_frame, textvariable=self.counter, font=("Arial", 36), bg="lightblue", width=10)
        label.pack(pady=20)

        # Botões
        button_frame = tk.Frame(content_frame, bg="white")
        button_frame.pack()

        increment_btn = ttk.Button(button_frame, text="+", command=self.increment_counter)
        increment_btn.pack(side="left", padx=5)

        decrement_btn = ttk.Button(button_frame, text="-", command=self.decrement_counter)
        decrement_btn.pack(side="left", padx=5)

        reset_btn = ttk.Button(button_frame, text="Zerar", command=self.reset_counter)
        reset_btn.pack(side="left", padx=5)

    # Incrementa o contador em 1
    def increment_counter(self):
        self.counter.set(self.counter.get() + 1)

    # Decrementa o contador em 1
    def decrement_counter(self):
        self.counter.set(self.counter.get() - 1)

    # Reseta o contador para 0
    def reset_counter(self):
        self.counter.set(0)

    # Lista de Filmes
    def create_movie_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Filmes")

        self.set_background(frame, "images/background3.jpg")

        content_frame = self.create_centered_frame(frame, 700, 500)

        movies = [
            {
                "title": "O Senhor dos Anéis: A Sociedade do Anel",
                "actors": ["Elijah Wood", "Ian McKellen", "Viggo Mortensen"],
                "synopsis": "Em uma terra fantástica e única, um hobbit recebe de presente de seu tio um anel mágico e maligno que precisa ser destruído antes "
                            "que caia nas mãos do mal. Para isso, o hobbit Frodo tem um caminho árduo pela frente, onde encontra perigo, medo e seres bizarros. "
                            "Ao seu lado para o cumprimento desta jornada, ele aos poucos pode contar com outros hobbits, um elfo, um anão, dois humanos e um mago, "
                            "totalizando nove seres que formam a Sociedade do Anel.",
                "poster": "images/poster1.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=V75dMMIW2B4"
            },
            {
                "title": "Matrix",
                "actors": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
                "synopsis": "O jovem programador Thomas Anderson é atormentado por estranhos pesadelos em que está sempre conectado por cabos a um imenso sistema de "
                            "computadores do futuro. À medida que o sonho se repete, ele começa a desconfiar da realidade. Thomas conhece os misteriosos Morpheus e "
                            "Trinity e descobre que é vítima de um sistema inteligente e artificial chamado Matrix, que manipula a mente das pessoas e cria a ilusão de "
                            "um mundo real enquanto usa os cérebros e corpos dos indivíduos para produzir energia.",
                "poster": "images/poster2.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=m8e-FF8MsqU"
            },
            {
                "title": "Interestelar",
                "actors": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
                "synopsis": "As reservas naturais da Terra estão chegando ao fim e um grupo de astronautas recebe a missão de verificar possíveis planetas para receberem a "
                            "população mundial, possibilitando a continuação da espécie. Cooper é chamado para liderar o grupo e aceita a missão sabendo que pode nunca mais "
                            "ver os filhos. Ao lado de Brand, Jenkins e Doyle, ele seguirá em busca de um novo lar.",
                "poster": "images/poster3.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=zSWdZVtXT7E"
            },
            {
                "title": "Inception",
                "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"],
                "synopsis": "Dom Cobb é um ladrão com a rara habilidade de roubar segredos do inconsciente, obtidos durante o estado de sono. Impedido de retornar para sua "
                            "família, ele recebe a oportunidade de se redimir ao realizar uma tarefa aparentemente impossível: plantar uma ideia na mente do herdeiro de um "
                            "império. Para realizar o crime perfeito, ele conta com a ajuda do parceiro Arthur, o discreto Eames e a arquiteta de sonhos Ariadne. "
                            "Juntos, eles correm para que o inimigo não antecipe seus passos.",
                "poster": "images/poster4.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=YoHD9XEInc0"
            },
            {
                "title": "Gladiador",
                "actors": ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"],
                "synopsis": "Maximus é um poderoso general romano, amado pelo povo e pelo imperador Marcus Aurelius. Antes de sua morte, o Imperador desperta a ira de seu filho "
                            "Commodus ao tornar pública a sua predileção em deixar o trono para Maximus. Sedento pelo poder, Commodus mata seu pai, assume a coroa e ordena a "
                            "morte de Maximus, que consegue fugir antes de ser pego, e passa a se esconder como um escravo e gladiador enquanto vai atrás de vingança.",
                "poster": "images/poster5.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=owK1qxDselE"
            },
            {
                "title": "Avatar",
                "actors": ["Sam Worthington", "Zoe Saldana", "Sigourney Weaver"],
                "synopsis": "No exuberante mundo alienígena de Pandora vivem os Na'vi, seres que parecem ser primitivos, mas são altamente evoluídos. Como o ambiente do planeta "
                            "é tóxico, foram criados os avatares, corpos biológicos controlados pela mente humana que se movimentam livremente em Pandora. "
                            "Jake Sully, um ex-fuzileiro naval paralítico, volta a andar através de um avatar e se apaixona por uma Na'vi. Esta paixão leva Jake a lutar pela "
                            "sobrevivência de Pandora.",
                "poster": "images/poster6.jpg",
                "trailer_url": "https://www.youtube.com/watch?v=5PSNL1qE6VY"
            }
        ]

        canvas = tk.Canvas(content_frame)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        # Configuração do canvas para permitir rolagem
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Exibindo informações dos filmes
        for movie in movies:
            movie_frame = ttk.Frame(scrollable_frame, padding=10)
            movie_frame.pack(fill="x", pady=5)

            # Carregando e ajustando a imagem do poster do filme
            poster_image = Image.open(movie["poster"])
            poster_image = poster_image.resize((100, 150), Image.Resampling.LANCZOS)
            poster_photo = ImageTk.PhotoImage(poster_image)

            poster_label = tk.Label(movie_frame, image=poster_photo)
            poster_label.image = poster_photo
            poster_label.pack(side="left", padx=10)

            # Informações do filme (título, atores, sinopse)
            info_frame = tk.Frame(movie_frame)
            info_frame.pack(side="left", fill="both", expand=True)

            title_label = tk.Label(info_frame, text=movie["title"], font=("Arial", 14, "bold"))
            title_label.pack(anchor="w")

            actors_label = tk.Label(info_frame, text="Atores: " + ", ".join(movie["actors"]), wraplength=400, justify="left")
            actors_label.pack(anchor="w", pady=5)

            synopsis_label = tk.Label(info_frame, text="Sinopse: " + movie["synopsis"], wraplength=400, justify="left")
            synopsis_label.pack(anchor="w", pady=5)

            # Abrindo o trailer do filme no browser
            trailer_btn = ttk.Button(info_frame, text="Assistir Trailer", command=lambda url=movie["trailer_url"]: webbrowser.open(url))
            trailer_btn.pack(anchor="w", pady=5)

if __name__ == "__main__":
    # Inicializa a janela principal do Tkinter
    root = tk.Tk()
    app = DesktopApp(root)
    root.mainloop()
