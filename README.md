# NoHandsBloons

![Python](https://img.shields.io/badge/Python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-working-brightgreen)

> Um bot totalmente automatizado para jogar Bloons TD6

---

## 🧠 O que é?

**NoHandsBloons** é um bot escrito em Python que automatiza partidas do Bloons TD6 usando PyAutoGUI. Ele realiza:

- Seleção automática de mapas e modos  
- Posicionamento de torres (macacos)  
- Aplicação de upgrades  
- Detecção visual de progresso (via screenshots)  
- Ciclo infinito de farming  

---

## ⚙️ Requisitos

- Python 3.9+
- Sistema operacional com suporte a PyAutoGUI
- Resolução 1920x1080 (pode precisar ajustar coordenadas)
- Biblioteca OpenCV instalada (para `confidence` funcionar)
- Ter a fase Inferno desbloqueada

---

## 📦 Instalação

```bash
git clone https://github.com/Icarolhl/NoHandsBloons.git
cd NoHandsBloons
pip install -r requirements.txt
```

---

## 🚀 Como usar

1. Abra o Bloons TD6 no modo janela com a resolução recomendada  
2. Certifique-se que o menu inicial do jogo está visível  
3. Execute o bot com o comando:

```bash
python main.py
```

O bot fará todo o processo: iniciar partida, posicionar torres, clicar "Próximo", repetir...

---

## 📂 Estrutura

```
NoHandsBloons/
├── main.py               # Código principal do bot
├── requirements.txt      # Dependências Python
├── LICENSE               # Licença MIT
├── README.md             # Este arquivo
└── recursos/             # Imagens usadas para reconhecimento de tela
    ├── menu.jpg
    └── next.jpg
```

---

## 🛠️ Tecnologias usadas

- `pyautogui`
- `colorama`
- `pillow`
- `opencv-python`

---

## 📄 Licença

Distribuído sob a licença MIT.  
Sinta-se livre para usar, modificar, adaptar ou expandir como quiser.
