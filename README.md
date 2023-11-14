# Jogo da Velha com Flask

Este é um simples jogo da velha implementado em Python usando o framework Flask para criar uma aplicação web. Os jogadores podem se divertir jogando alternadamente em um ambiente amigável.

![Jogo da Velha](img/printscreen.png)

## Como Usar

### Pré-requisitos
- Python instalado
- Pip (gerenciador de pacotes do Python)

### Passos para Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/felipeharlen/jogodavelha.git
   cd jogodavelha
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o aplicativo:
   ```bash
   python app.py
   ```

4. Abra o navegador e visite [http://localhost:5000](http://localhost:5000).

### Acesso Externo
Se desejar acessar de um dispositivo externo, certifique-se de estar na mesma rede Wi-Fi e execute:
   ```bash
   python app.py --host=0.0.0.0
   ```

Abra o navegador e visite `<seu-endereco-ip>:5000`. Encontre seu endereço IP usando `ipconfig` no Windows ou `ifconfig` no Linux/Mac.

---
