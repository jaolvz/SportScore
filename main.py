import customtkinter as ck
import tkinter as tk
from tkinter import ttk
import scrips
from datetime import datetime ,timedelta
from PIL import Image, ImageTk
import requests
from io import BytesIO

ck.set_appearance_mode("System")
ck.set_default_color_theme("dark-blue")

class Aplicativo(ck.CTk):


    def __init__(self, *args , **kwargs):
        super().__init__()
        self.geometry("800x800")
        self.configure(fg_color = "#3489eb")
        self.title("SportScore")
        self.resizable(False, False)
        self.frame_atual = self.telaInicial()


    def telaInicial(self):

        telaInicial = ck.CTkFrame(self, fg_color="#3489eb")

        self.nomeApp = ck.CTkLabel(telaInicial, text='SportScore', text_color="white", font=("LEMON MILK", 40)).place(
            relx=0.28, rely=0.06)

        self.btnBrasileiro = ck.CTkButton(telaInicial, text="Brasileirão", fg_color="red", font=("Arial", 14),
                                          border_spacing=10, text_color="white",
                                          command=lambda: self.abrir_nova_janela_de_liga("BSA")).place(relx=0.1,
                                                                                                       rely=0.3)

        self.btnPremierLeague = ck.CTkButton(telaInicial, text="Premier League", fg_color="red", font=("Arial", 14),
                                             border_spacing=10, text_color="white",
                                             command=lambda: self.abrir_nova_janela_de_liga("PL")).place(relx=0.67,
                                                                                                         rely=0.3)

        self.btnEspanhol = ck.CTkButton(telaInicial, text="Espanhol", fg_color="red", font=("Arial", 14),
                                        border_spacing=10, text_color="white",
                                        command=lambda: self.abrir_nova_janela_de_liga("PD")).place(relx=0.1, rely=0.5)

        self.btnBundesliga = ck.CTkButton(telaInicial, text="Bundesliga", fg_color="red", font=("Arial", 14),
                                          border_spacing=10, text_color="white",
                                          command=lambda: self.abrir_nova_janela_de_liga("BL1")).place(relx=0.67,
                                                                                                       rely=0.5)

        self.btnEredivise = ck.CTkButton(telaInicial, text="Eredivise", fg_color="red", font=("Arial", 14),
                                         border_spacing=10, text_color="white",
                                         command=lambda: self.abrir_nova_janela_de_liga("DED")).place(relx=0.1,
                                                                                                      rely=0.7)

        self.btnSerieA = ck.CTkButton(telaInicial, text="Serie A", fg_color="red", font=("Arial", 14),
                                      border_spacing=10, text_color="white",
                                      command=lambda: self.abrir_nova_janela_de_liga("SA")).place(relx=0.67, rely=0.7)

        self.btnLigue1 = ck.CTkButton(telaInicial, text="Ligue 1", fg_color="RED", font=("Arial", 14),
                                      border_spacing=10, text_color="WHITE",
                                      command=lambda: self.abrir_nova_janela_de_liga("FL1")).place(relx=0.4, rely=0.9)

        self.toplevel_window = None

        telaInicial.place(relwidth=1, relheight=1)




    def abrir_nova_janela_de_liga(self, liga_cod):


        self.dados_tabela = scrips.pegando_tabela_por_cod(liga_cod)
        self.title(self.dados_tabela['competition']['name'])

        liga_frame = ck.CTkFrame(self, fg_color="#3489eb")
        btnVoltar = ck.CTkButton(liga_frame,text="Voltar", command=lambda: self.telaInicial())
        btnVoltar.place(y=-3,x=-5)
        # Criando a árvore (tabela)

        self.tree = ttk.Treeview(liga_frame, show="headings")
        # Definindo colunas
        self.tree["columns"] = ["Posição", "Classificação", ["P"], ["J"], ["V"], ["E"], ["D"], ["GP"], ["GC"]]

        # Formatando colunas
        self.tree.column("Posição", anchor=tk.CENTER, width=40)
        self.tree.column("Classificação", anchor=tk.CENTER, width=100)
        self.tree.column("P", anchor=tk.CENTER, width=30)
        self.tree.column("J", anchor=tk.CENTER, width=30)
        self.tree.column("V", anchor=tk.CENTER, width=30)
        self.tree.column("E", anchor=tk.CENTER, width=30)
        self.tree.column("D", anchor=tk.CENTER, width=30)
        self.tree.column("GP", anchor=tk.CENTER, width=30)
        self.tree.column("GC", anchor=tk.CENTER, width=30)

        # Dando título
        self.tree.heading("Posição", text="#")
        self.tree.heading("Classificação", text="Time")
        self.tree.heading("P", text="P")
        self.tree.heading("J", text="J")
        self.tree.heading("V", text="V")
        self.tree.heading("E", text="E")
        self.tree.heading("D", text="D")
        self.tree.heading("GP", text="GP")
        self.tree.heading("GC", text="GC")

        self.tabela = self.dados_tabela['standings'][0]['table']
        for equipe in self.tabela:
            id_time =  equipe['team']['id']
            posicao = equipe['position']
            nome_equipe = equipe['team']['shortName']
            pontos = equipe['points']
            partidas = equipe["playedGames"]
            vitorias = equipe['won']
            empate = equipe['draw']
            derrota = equipe['lost']
            gols_Pro = equipe['goalsFor']
            gols_Contra = equipe["goalsAgainst"]
            #depois passar isso para uma função que organize liga por liga
            if liga_cod=="BSA":
                if posicao <= 4:
                    tags = ("libertadores",)
                elif posicao > 4 and posicao <= 6:
                    tags = ("prelibertadores",)
                elif posicao > 6 and posicao <= 12:
                    tags = ("sulamericana",)
                elif posicao > 16:
                    tags = ("rebaixamento",)
                else:
                    tags = ""
            else:
                tags=""

            self.tree.insert("", tk.END,iid=id_time, values=(
            posicao, nome_equipe, pontos, partidas, vitorias, empate, derrota, gols_Pro, gols_Contra), tags=tags)
        self.tree.configure(height=20)
        self.tree.tag_configure("libertadores", background="#1cd437")
        self.tree.tag_configure("prelibertadores", background="#026625")
        self.tree.tag_configure("sulamericana", background="#5b7ff5")
        self.tree.tag_configure("rebaixamento", background="#ff0000")
        self.tree.place(x=30, y=35, anchor="nw")
        self.tree.bind("<Button-1>",lambda event: buscar3jogo(self.tree.focus()))

        frame_proxJogos = ck.CTkFrame(liga_frame, fg_color="white" , width=350, height=300)
        frame_proxJogos.pack_propagate(0)
        frame_proxJogos.place(x=30, y=770, anchor="sw")

        def buscar3jogo(id):


            proxsjogos = scrips.pegar_proximo3jogos(id)
            font_bold = ck.CTkFont(weight="bold")

            for indice, jogo in enumerate(proxsjogos):
                frame_jogo = tk.Frame(frame_proxJogos,background="white" , width=330, height=80)
                print(jogo)
                mandantejogo = ck.CTkLabel(frame_jogo,text_color="black", text=jogo['homeTeam']['shortName'])
                mandantejogo.place(x=15,rely=0.5, anchor='w')

                responseMandante = requests.get(jogo['homeTeam']['crest'])
                imageMandante = ck.CTkImage(light_image=Image.open(BytesIO(responseMandante.content)),
                                            dark_image=Image.open(BytesIO(responseMandante.content)), size=(25, 25))
                label_img_Mandante = ck.CTkLabel(frame_jogo, image=imageMandante, text="")
                label_img_Mandante.place( x=40, rely=0.8, anchor='center')





                rodada = ck.CTkLabel(frame_jogo, text_color="#72767d", text=f"Rodada {jogo['matchday']}")
                rodada.place(relx=0.5, rely=0.8, anchor='center')

                dataFormatada = datetime.fromisoformat(jogo['utcDate'][:-1])
                dataFormatada = dataFormatada - timedelta(hours=3)
                dataFormatada = dataFormatada.strftime("%d/%m - %H:%M")

                data = ck.CTkLabel(frame_jogo, text_color="#72767d", text=f"{dataFormatada}")
                data.place(relx=0.5, rely=0.2, anchor='center')


                versus = ck.CTkLabel(frame_jogo,text_color="black",font=font_bold, text="X")
                versus.place(relx =0.5, rely=0.5, anchor='center')

                visitantejogo = ck.CTkLabel(frame_jogo,text_color="black", text=jogo['awayTeam']['shortName'])
                visitantejogo.place(x=315, rely=0.5, anchor='e')

                responseVisitante = requests.get(jogo['awayTeam']['crest'])
                imageVisitante = ck.CTkImage(light_image=Image.open(BytesIO(responseVisitante.content)),
                                            dark_image=Image.open(BytesIO(responseVisitante.content)), size=(25, 25))
                label_img_Visitante = ck.CTkLabel(frame_jogo, image=imageVisitante, text="")
                label_img_Visitante.place(x=290, rely=0.8, anchor='center')

                frame_jogo.place(y=100*indice+10, relx=0.5, anchor="n")


        label_Artilheiros = ck.CTkLabel(liga_frame,text="Artilheiros")
        label_Artilheiros.place(x=595, y=15, anchor='center')


        frame_Artilheiros = ck.CTkFrame(liga_frame,width=350, height=430)
        frame_Artilheiros.place(x=595, y=35, anchor="n")
        frame_Artilheiros.pack_propagate(0)
        artilheiros = scrips.artilheiros_Campeonato(liga_cod)
        for jogador in artilheiros:
            print(jogador)
            frame_jogador = ck.CTkFrame(frame_Artilheiros,width=350, height=43)
            frame_jogador.pack_propagate(0)
            frame_jogador.pack()
            nome_jogador = ck.CTkLabel(frame_jogador, text=jogador['player']['name'])
            nome_jogador.place(relx=0.5, rely=0.5, anchor='center')
            sigla_time_jogador = ck.CTkLabel(frame_jogador, text=jogador['team']['tla'])
            sigla_time_jogador.place(relx=0.1, rely=0.5, anchor='center')
            gols_jogador = ck.CTkLabel(frame_jogador, text=jogador ['goals'])
            gols_jogador.place(relx=0.85, rely=0.5, anchor='center')



        liga_frame.place(relwidth=1, relheight=1)








app = Aplicativo()
app.mainloop()
