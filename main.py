import pyautogui
from time import sleep
import colorama
from colorama import Fore
from pathlib import Path

colorama.init(autoreset=True)

ROOT_PATH = Path(__file__).parent
MENU_IMG_PATH = str(ROOT_PATH / 'recursos/menu.jpg')
NEXT_IMG_PATH = str(ROOT_PATH / 'recursos/next.jpg')

cordenadas = {
    "BOTAO_JOGAR": [963, 981],
    "DIFICULDADE_EXPERT": [1321, 1004],
    "FASE_INFERNAL": [1316, 585],
    "DIFICULDADE_FACIL": [628, 497],
    "MODO_ESVAZIAMENTO": [1263, 496],
    "SELECIONA_MACACO_ATIRADOR": [1817, 658],
    "SELECIONA_MACACO_MAGO": [1699, 344],
    "POSICIONA_MACACO_ATIRADOR": [1583, 533],
    "POSICIONA_MACACO_MAGO": [832, 731],
    "SELECIONA_MACACO_ATIRADOR_MAPA": [1583, 533],
    "SELECIONA_MACACO_MAGO_MAPA": [832, 731],
    "UPGRADE_3_ESQUERDA": [336, 807],
    "UPGRADE_2_ESQUERDA": [352, 655],
    "UPGRADE_1_DIREITA": [1569, 508],
    "UPGRADE_3_DIREITA": [1515, 806],
    "INICIAR|DEIXAR_RAPIDO": [1828, 1032],
    "BOTAO_OK": [939, 777],
    "BOTAO_PROXIMO": [944, 941],
    "BOTAO_HOME": [724, 871],
}


def click(local, delay=0.9):
    pyautogui.click(cordenadas[local])
    sleep(delay)


def scroll_repetido(vezes=20, passo=-800):
    print(f'{Fore.BLUE}Scrollando a lista de torres...')
    pyautogui.moveTo(1817, 658)
    sleep(0.3)
    for _ in range(vezes):
        pyautogui.scroll(passo)
        sleep(0.1)


def checa_tela_inicial():
    while True:
        try:
            if pyautogui.locateOnScreen(
                MENU_IMG_PATH, grayscale=True, confidence=0.9
            ):
                print(
                    f'{Fore.GREEN}Tela do Jogo encontrada. '
                    'Iniciando o bot...'
                )
                return
        except pyautogui.ImageNotFoundException:
            pass
        print(f'{Fore.YELLOW}Tela não detectada, tentando novamente...')
        sleep(2)


def posicionar_macaco(tipo, pos, upgrades):
    click(tipo)
    click(pos)
    click(pos)
    for upgrade in upgrades:
        for _ in range(upgrade["vezes"]):
            click(upgrade["local"], delay=0.3)


def posicionamento_macacos():
    print(f'{Fore.MAGENTA}Posicionando macacos...')

    posicionar_macaco(
        "SELECIONA_MACACO_ATIRADOR",
        "POSICIONA_MACACO_ATIRADOR",
        [
            {"local": "UPGRADE_3_ESQUERDA", "vezes": 4},
            {"local": "UPGRADE_2_ESQUERDA", "vezes": 2}
        ]
    )

    scroll_repetido()

    posicionar_macaco(
        "SELECIONA_MACACO_MAGO",
        "POSICIONA_MACACO_MAGO",
        [
            {"local": "UPGRADE_1_DIREITA", "vezes": 4},
            {"local": "UPGRADE_3_DIREITA", "vezes": 2}
        ]
    )

    click("INICIAR|DEIXAR_RAPIDO", delay=0.5)
    click("INICIAR|DEIXAR_RAPIDO", delay=0.5)
    sleep(2)


def Main():
    checa_tela_inicial()
    print(f'{Fore.CYAN}Selecionando o mapa do farm...')
    sleep(5)
    click("BOTAO_JOGAR")
    click("DIFICULDADE_EXPERT")
    click("FASE_INFERNAL")
    click("DIFICULDADE_FACIL")
    click("MODO_ESVAZIAMENTO")
    sleep(7)
    click("BOTAO_OK")
    sleep(3)
    posicionamento_macacos()


def Exit():
    print(f'{Fore.CYAN}Esperando botão Próximo aparecer...')
    while True:
        try:
            botao = pyautogui.locateOnScreen(
                NEXT_IMG_PATH, grayscale=True, confidence=0.9
            )
            if botao:
                print(
                    f'{Fore.CYAN}Botão Próximo encontrado. '
                    'Clicando e voltando '
                    'ao menu...'
                )
                click("BOTAO_PROXIMO")
                sleep(2)
                click("BOTAO_HOME")
                sleep(6)
                break
        except pyautogui.ImageNotFoundException:
            pass
        print(f'{Fore.YELLOW}Aguardando botão Próximo...')
        sleep(2)

    checa_tela_inicial()


if __name__ == '__main__':
    print(f'{Fore.BLUE}Aguardando 5 segundos para você organizar a tela...')
    sleep(5)

    while True:
        Main()
        Exit()
