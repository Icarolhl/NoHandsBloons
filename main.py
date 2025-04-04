import pyautogui
from time import sleep
import colorama
from colorama import Fore
from pathlib import Path

colorama.init(autoreset=True)

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
MENU_IMG_PATH = str(CAMINHO_RAIZ / 'recursos/menu.jpg')
NEXT_IMG_PATH = str(CAMINHO_RAIZ / 'recursos/next.jpg')

"""
Dicionário contendo as coordenadas para auto clicker.

Obs: Toda vez que novos mapas e macacos são adicionados, por consequência essas
coordenadas também são alteradas. Pode ser que na sua versão do jogo esteja
diferente e você precise mudar.
"""
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


def click(local):
    pyautogui.click(cordenadas[local])
    sleep(0.9)


def checa_tela_inicial():
    while True:
        try:
            pyautogui.locateOnScreen(
                MENU_IMG_PATH, grayscale=True, confidence=0.9
            )
            print(
                f'{Fore.GREEN}Tela do Jogo encontrada. '
                'Iniciando o bot...'
            )
            return
        except pyautogui.ImageNotFoundException:
            print(
                f'{Fore.RED}Imagem menu.jpg não encontrada. '
                'Tentando novamente...'
            )
        sleep(2)


def scrollar_lista_torres():
    print(f'{Fore.BLUE}Scrollando a lista de torres...')
    pyautogui.moveTo(1817, 658)
    sleep(0.3)
    for _ in range(20):
        pyautogui.scroll(-800)
        sleep(0.1)


def posicionamento_macacos():
    print(f'{Fore.MAGENTA}Posicionando macacos...')

    click("SELECIONA_MACACO_ATIRADOR")
    click("POSICIONA_MACACO_ATIRADOR")
    click("SELECIONA_MACACO_ATIRADOR_MAPA")
    click("UPGRADE_3_ESQUERDA")
    click("UPGRADE_3_ESQUERDA")
    click("UPGRADE_3_ESQUERDA")
    click("UPGRADE_3_ESQUERDA")
    click("UPGRADE_2_ESQUERDA")
    click("UPGRADE_2_ESQUERDA")

    scrollar_lista_torres()

    click("SELECIONA_MACACO_MAGO")
    click("POSICIONA_MACACO_MAGO")
    click("SELECIONA_MACACO_MAGO_MAPA")
    click("UPGRADE_1_DIREITA")
    click("UPGRADE_1_DIREITA")
    click("UPGRADE_1_DIREITA")
    click("UPGRADE_1_DIREITA")
    click("UPGRADE_3_DIREITA")
    click("UPGRADE_3_DIREITA")
    click("INICIAR|DEIXAR_RAPIDO")
    click("INICIAR|DEIXAR_RAPIDO")
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
    try:
        botao = pyautogui.locateOnScreen(
            NEXT_IMG_PATH, grayscale=True, confidence=0.9
        )
        while botao is None:
            sleep(2)
            print(f'{Fore.YELLOW}Botão Próximo não encontrado.')
            botao = pyautogui.locateOnScreen(
                NEXT_IMG_PATH, grayscale=True, confidence=0.9
            )
        print(f'{Fore.CYAN}Fase Terminada. Começando Novamente...')
    except pyautogui.ImageNotFoundException:
        print(f'{Fore.RED}Imagem next.jpg não encontrada.')
    checa_tela_inicial()


if __name__ == '__main__':
    print(f'{Fore.BLUE}Aguardando 5 segundos para você organizar a tela...')
    sleep(5)

    while True:
        Main()
