import customtkinter as ck

ck.set_appearance_mode("System")
ck.set_default_color_theme("dark-blue")


class Aplicativo(ck.CTk):

    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.title("SportScore")
        self.configure(fg_color="#3489eb")
        self.resizable(False, False)

        self.nomeApp = ck.CTkLabel(self, text='SportScore', text_color="white", font=("LEMON MILK", 40))
        self.nomeApp.grid(row=0, column=1)

        self.btnBrasileiro = ck.CTkButton(self, text="Brasileirão", fg_color="white",font=("Arial",14),
                                         border_spacing=10, text_color="black")
        self.btnBrasileiro.grid(row=1, column=0, )

        self.btnPremierLeague = ck.CTkButton(self, text="Premier League", fg_color="white",font=("Arial",14),
                                         border_spacing=10, text_color="black")
        self.btnPremierLeague.grid(row=1, column=2)

        self.btnEspanhol = ck.CTkButton(self, text="Espanhol", fg_color="white",font=("Arial",14),
                                         border_spacing=10, text_color="black")
        self.btnEspanhol.grid(row=2, column=2)

        self.btnBundesliga = ck.CTkButton(self, text="Bundesliga", fg_color="white",font=("Arial",14),
                                         border_spacing=10, text_color="black")
        self.btnBundesliga.grid(row=2, column=0)

        self.btnEredivise = ck.CTkButton(self, text="Eredivise", fg_color="white", font=("Arial", 14),
                                          border_spacing=10, text_color="black")
        self.btnEredivise.grid(row=3, column=0)

        self.btnSerieA = ck.CTkButton(self, text="Serie A", fg_color="white", font=("Arial", 14),
                                         border_spacing=10, text_color="black")
        self.btnSerieA.grid(row=3, column=2)

        self.btnLigue1 = ck.CTkButton(self, text="Ligue 1", fg_color="white", font=("Arial", 14),
                                      border_spacing=10, text_color="black")
        self.btnLigue1.grid(row=4, column=1)












        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)


        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)



app = Aplicativo()
app.mainloop()
