# Pong - Jogo Clássico

Este é um jogo clássico de Pong desenvolvido em Python usando a biblioteca `pygame`.

## Como Jogar

- O jogador 1 controla a raquete da esquerda usando as teclas W (para cima) e S (para baixo).
- O jogador 2 controla a raquete da direita usando as teclas Seta para Cima e Seta para Baixo.
- A bola se move automaticamente e rebaterá nas raquetes e nas bordas superiores e inferiores da tela.
- Cada vez que a bola ultrapassa um jogador, o outro ganha 1 ponto.
- O placar é exibido na tela.
- Quando o jogo é encerrado, as pontuações são salvas no arquivo `pontuacoes.txt`.

## Requisitos

- Python 3.x
- Biblioteca `pygame`

Para instalar o `pygame`, execute:

pip install pygame


## Como Executar

1. Certifique-se de estar no diretório onde o arquivo `jogopong.py` está localizado.
2. Execute o jogo com o comando:

python jogopong.py


## Estrutura do Projeto

projeto_pong/
│-- jogopong.py        # Código do jogo
│-- pontuacoes.txt     # Arquivo que armazena as pontuações
│-- README.txt         # Este arquivo


Divirta-se jogando Pong!

