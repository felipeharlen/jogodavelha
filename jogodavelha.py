class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [" "] * 9
        self.jogador_atual = "X"
        self.celulas_vitoriosas = None

    def imprimir_tabuleiro(self):
        for i in range(0, 9, 3):
            print(self.tabuleiro[i], "|", self.tabuleiro[i + 1], "|", self.tabuleiro[i + 2])
            if i < 6:
                print("---------")

    def fazer_jogada(self, posicao):
        if 1 <= posicao <= 9 and self.tabuleiro[posicao - 1] == " ":
            self.tabuleiro[posicao - 1] = self.jogador_atual

            if self.verificar_vitoria():
                print(f"Jogador {self.jogador_atual} venceu!")
                return f"Jogador {self.jogador_atual} venceu!"
            elif " " not in self.tabuleiro:
                print("Empate!")
                return "Empate!"
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
            return None
        else:
            print("Jogada inválida. Tente novamente.")
            return None


    def verificar_vitoria(self):
        # Verifica linhas, colunas e diagonais
        for i in range(0, 9, 3):
            if self.tabuleiro[i] == self.tabuleiro[i + 1] == self.tabuleiro[i + 2] != " ":
                return True
        for i in range(3):
            if self.tabuleiro[i] == self.tabuleiro[i + 3] == self.tabuleiro[i + 6] != " ":
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != " ":
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != " ":
            return True
        return False

