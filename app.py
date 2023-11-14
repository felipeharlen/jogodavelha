from flask import Flask, render_template, request
from jogodavelha import JogoDaVelha

app = Flask(__name__)
jogo = JogoDaVelha()

@app.route('/')
def index():
    return render_template('index.html', tabuleiro=jogo.tabuleiro, jogador_atual=jogo.jogador_atual)

@app.route('/fazer_jogada', methods=['POST'])
def fazer_jogada():
    if jogo.verificar_vitoria() or " " not in jogo.tabuleiro:
        mensagem = "O jogo já foi concluído. Reinicie para jogar novamente."
        return render_template('index.html', tabuleiro=jogo.tabuleiro, jogador_atual=jogo.jogador_atual, mensagem=mensagem)

    posicao = int(request.form['posicao'])
    vitoria_ou_empate = jogo.fazer_jogada(posicao)

    if vitoria_ou_empate:
        return render_template('index.html', tabuleiro=jogo.tabuleiro, jogador_atual=jogo.jogador_atual, mensagem=vitoria_ou_empate)
    return render_template('index.html', tabuleiro=jogo.tabuleiro, jogador_atual=jogo.jogador_atual)

@app.route('/reiniciar_jogo', methods=['POST'])
def reiniciar_jogo():
    jogo.__init__()
    return render_template('index.html', tabuleiro=jogo.tabuleiro, jogador_atual=jogo.jogador_atual)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
