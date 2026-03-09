👾 Cyberpunk Tetris

Um Tetris estilizado em tema Cyberpunk desenvolvido com HTML5 Canvas + JavaScript no Front-end e Python no Back-end para servir a aplicação localmente.

O projeto combina visual neon futurista, animações em tempo real e um servidor simples em Python para rodar o jogo no navegador.
<img width="1315" height="605" alt="image" src="https://github.com/user-attachments/assets/dfd6de33-c784-43f2-bc77-70bb28d5a308" />

⚡ Ideal para estudos de:

Canvas API

Lógica de jogos

Integração entre Front-end e Back-end

Servidores HTTP simples em Python

🕹️ Demonstração do Jogo

O jogo funciona diretamente no navegador e possui:

✨ Interface Cyberpunk Neon
🎮 Controles simples de teclado
📈 Sistema de pontuação e níveis
🧠 Lógica completa de colisão, rotação e limpeza de linhas

🏗️ Estrutura do Projeto
Cyberpunk-Tetris
│
├── Front.html   # Interface do jogo (HTML + CSS + JavaScript)
└── back.py      # Servidor Python que executa o jogo
🎨 Front-end (Front.html)

O Front-end é responsável por toda a parte visual e lógica do jogo.

Ele utiliza:

HTML5 Canvas → renderização do tabuleiro

CSS → estilo Cyberpunk (neon, glow, scanlines)

JavaScript → lógica completa do Tetris

⚙️ Principais funcionalidades
🎮 Sistema de jogo

O JavaScript controla:

Criação das peças (T, O, L, J, I, S, Z)

Movimento e rotação

Detecção de colisão

Queda automática das peças

Limpeza de linhas completas

Funções importantes:

createPiece() → cria as peças do jogo

collide() → detecta colisões

merge() → fixa a peça no tabuleiro

arenaSweep() → remove linhas completas

playerRotate() → rotaciona peças

🧠 Sistema de Pontuação e Nível

Quando linhas são completadas:

A pontuação aumenta

O nível sobe

A velocidade do jogo aumenta

player.level = Math.floor(player.lines / 5) + 1

Isso faz o jogo ficar cada vez mais rápido e desafiador.

🎨 Renderização no Canvas

O jogo utiliza o Canvas API para desenhar:

Tabuleiro

Peças

Grade de fundo

Efeitos neon

Cada peça possui:

✨ Glow neon
🧩 Detalhes internos
🟦 Bordas estilizadas

⌨️ Controles
Tecla	Ação
⬅	mover para esquerda
➡	mover para direita
⬇	acelerar queda
⬆	rotacionar peça
Enter	reiniciar após Game Over
🖥️ Back-end (back.py)

O Back-end é um servidor HTTP simples em Python que serve os arquivos do jogo.

Ele utiliza apenas bibliotecas padrão do Python:

http.server

socketserver

webbrowser

Ou seja, não precisa instalar nenhuma dependência externa.

⚙️ Como o servidor funciona

O servidor:

1️⃣ Inicia na porta 8000

http://localhost:8000

2️⃣ Serve automaticamente o arquivo:

Front.html

quando o usuário acessa /.

if self.path == '/':
    self.path = '/Front.html'

3️⃣ Abre o navegador automaticamente quando inicia.

webbrowser.open(f'http://localhost:{PORT}')
🚀 Vantagens desse servidor

✔ Muito leve
✔ Não precisa de frameworks
✔ Ideal para projetos pequenos
✔ Fácil de rodar localmente

▶️ Como Executar o Projeto
1️⃣ Baixe o repositório
git clone <repo>
cd Cyberpunk-Tetris
2️⃣ Execute o servidor
python back.py
3️⃣ O navegador abrirá automaticamente
http://localhost:8000

Se não abrir automaticamente, basta acessar manualmente.

🎨 Estilo Visual

O jogo possui um tema Cyberpunk futurista, incluindo:

🌌 Fundo escuro
💡 Glow neon nas peças
📺 Efeito de scanlines estilo CRT
🔳 Grade tecnológica no fundo

Fonte utilizada:

Orbitron

Muito usada em interfaces futuristas.

🧠 Conceitos Aplicados

Este projeto utiliza diversos conceitos importantes de programação:

🎮 Game Loop com requestAnimationFrame
📐 Matrizes para representar peças
🧮 Algoritmos de colisão
🧱 Estruturas de tabuleiro (arena)
⌨️ Captura de eventos do teclado
🌐 Servidor HTTP simples

🚀 Possíveis Melhorias

Ideias para evoluir o projeto:

🔊 adicionar efeitos sonoros

🧠 salvar highscore

👥 modo multiplayer

🎨 animações de destruição de linha

📱 versão mobile

🏆 ranking online

👨‍💻 Autor

Projeto desenvolvido para estudo de:

JavaScript

Canvas API

Python HTTP Server

Lógica de jogos
