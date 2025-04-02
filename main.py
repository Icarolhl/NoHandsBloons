import pyautogui
from time import sleep
import colorama
from colorama import Fore
from pathlib import Path
colorama.init(autoreset=True)

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
# VICTORY_IMG_PATH = "recursos\\victory.png"
# DEFEAT_IMG_PATH = "recursos\\defeat.png"
MENU_IMG_PATH = CAMINHO_RAIZ / 'recursos/menu.jpg'
NEXT_IMG_PATH = CAMINHO_RAIZ / "recursos/next.jpg"

print(MENU_IMG_PATH)
print(NEXT_IMG_PATH)

"""
Dicionario Contendo as infomações de cordenada para auto clicker.

Obs: Toda vez que novos mapas e macacos são adicionados por consequencia essas
cordenadas também são alteradas pode ser que na sua versão de jogo esteja
diferente e você precise mudar as coisas.
"""
cordenadas = {
    "BOTAO_JOGAR": [963, 981],
    "DIFICULDADE_EXPERT": [1321, 1004],
    "FASE_INFERNAL": [1316, 585],
    "DIFICULDADE_FACIL": [628, 497],
    "MODO_ESVAZIAMENTO": [1263, 496],
    "BOTAO_OK": [939, 777],
}


def click(local):
    pyautogui.click(cordenadas[local])
    sleep(0.5)


def checa_tela_inicial():
    while True:  # Verifica se está na tela inicial do jogo
        tela_certa = pyautogui.locateOnScreen(
            MENU_IMG_PATH, grayscale=True, confidence=0.9)
        if tela_certa is not None:
            print(f'{Fore.GREEN}Tela do Jogo encontrada. Iniciando o bot...')
        else:
            print(f'{Fore.GREEN}A tela não foi encontrada. Procurando novamente...')  # noqa: E501
            sleep(2)


def posicionamento_macacos():
    ...


def Main():
    checa_tela_inicial()
    print(f'{Fore.CYAN}Selecionando o mapa do farm...')
    sleep(5)
    click("BOTAO_JOGAR")
    click("DIFICULDADE_EXPERT")
    click("FASE_INFERNAL")
    click("DIFICULDADE_FACIL")
    click("MODO_ESVAZIAMENTO")
    click("BOTAO_OK")
    sleep(3)
    posicionamento_macacos()


def Exit():
    botao = pyautogui.locateOnScreen(
        NEXT_IMG_PATH, grayscale=True, confidence=0.9)

    while botao is None:
        sleep(2)
        print('Botão Proximo não encontrado.')
        botao = pyautogui.locateOnScreen(
            NEXT_IMG_PATH, grayscale=True, confidence=0.9)

    print(f'{Fore.CYAN}Fase Terminada. Começando Novamente...')
    # Botar abaixo o caminho do fim da fase até o menu inicial
    # pyautogui.click(x=960, y=910)
    # sleep(2)
    # # pyautogui.click(x=790, y=850)
    # sleep(6)

    checa_tela_inicial()


while True:
    Main()
