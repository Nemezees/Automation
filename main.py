# Automação passos
# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: abrir base de dados
# Passo 4: cadastrar um produto
# Passo 5: repetir o passo 4 até terminar
# pyautogui automatiza mouse teclado e outras funções
# pyautogui.click() - Clica com o mouse
# pyautogui.write() - escrever um texto
# pyautogui.press() - clica em algo do teclado
# pyautogui.hotkey() - combinação de teclas 'Ctrl + c'
# pyautogui.scroll() - scrolla a tela
# pyautogui.PAUSE = 0.5 - Dá uma pausa
# Passo 1: Entrar no sistema da empresa
    # 1.1 Abrir o navegador
    #mouse = 1051, 605
    # Entrar no link (https://dlp.hashtagtreinamentos.com/python/intensivao/login)
import pyautogui
import time
pyautogui.PAUSE = 0.5
pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

pyautogui.doubleClick(1051, 605)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('Enter')
time.sleep(1.5)

# Passo 2: Fazer login no Sistema
    # Digitar email e senha

pyautogui.click(958, 375)
pyautogui.write('brenoemaildeteste@gmail.com')
pyautogui.click(969, 466)
pyautogui.write('qualquersenhavale')
pyautogui.click(954, 533)
time.sleep(1.5)

# Passo 3: Importar base de dados

import pandas
tabela = pandas.read_csv('produtos.csv')
for linha in tabela.index:
# Passo 4: cadastrar o produto
#codigo do produto
    pyautogui.click(871, 255)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo)
    #marca do produto
    pyautogui.press('tab')
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    #tipo do produto
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    #categoria do produto
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    #preço unitario
    pyautogui.press('tab')
    preco_u = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_u)
    #custo do produto
    pyautogui.press('tab')
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    #obs
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    #botao de enviar
    pyautogui.press('tab')
    pyautogui.press('Enter')

    #scrollar de volta
    pyautogui.scroll(1000)

# Passo 5: repetir para toda tabela
