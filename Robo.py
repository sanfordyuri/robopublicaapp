# -*- coding: utf-8 -*-
import pyautogui as cmd
import os
import time


os.system('color a')

print '                   ___                  '
print '                  (   )                 '
print '                   | |                  '
print '     /=============| |==============\    '
print '     [                               ]                   Bem vindo(a), eu sou o PublisherRobot'
print '     |       _____       _____       |             Sou capaz de publicar todos os 3 aplicativos,'
print '     |     ||     ||   ||     ||     |             Necessarios para o cliente usar o ambiente nuvem'
print '    [|     ||  o  ||   ||  o  ||     |]                    Sendo eles: AC, PATRIO e AGENTE'
print '    [|     ||_____||   ||_____||     |] '
print '    [|                               |]          Caso eu apresente algum erro, informe ao meu desenvolvedor'
print '    [|                               |]                   Entre em contato pelos seguintes meios:'
print '     |     /-------------------\     |                         WhatsApp: (85) 9 86002685 '
print '     |    /                     \    |                  Email: yurisanford@fortestecnologia.com.br'
print '     |                               |  '
print '     \===============================/     Para cancelar meu processamento basta usar: [CTRL + C] (Aqui no cmd)'
print ' '
print ' '
os.system('echo              Ola! %USERNAME%')
pasta  = input('      Insira o nome da pasta do cliente: ')
print ' '

cortado = pasta.split('_')

def mapeiaPastaDoCliente():
    os.system('net use F: \\\FORTES-RPS-02\\Share\\sistemas\\' + pasta)
    print ' PublisherRobot: Pasta do cliente mapeada com sucesso. [' + time.ctime() + ']'

def openPushPage():
    
    cmd.hotkey('winleft', 'd')
    cmd.sleep(0.5)
    cmd.press('winleft')
    cmd.sleep(0.5)	
    cmd.write('Auto.Sky Platform')
    cmd.sleep(0.5)
    cmd.press('dow')
    cmd.press('enter')
    cmd.sleep(1)
    cmd.click('asserts/AppImg.png')
    cmd.sleep(10)
    cmd.click('asserts/PublicarImg.png')
    cmd.sleep(3)

def publicaAc():
    print ' PublisherRobot: Iniciando Publicacao do AC [' + time.ctime() + ']'
    cmd.press('tab')
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('\\\FORTES-RPS-02\\Share\\sistemas\\' + pasta + '\\AC\\AC.exe')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write(cortado[0].upper() + ' ' + cortado[1].upper())
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','c')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write('AC ' + cortado[0].upper())
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','v')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/mostrarOpcoesImg.png')
    cmd.sleep(0.2)
    cmd.move(100, 0)
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('AC ' + cortado[0].upper())
    cmd.sleep(0.5)
    for i in range(13):
        cmd.sleep(0.2)
        cmd.press('tab')

    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.write('F_' + cortado[0].upper() + '_' + cortado[1].upper())
    cmd.sleep(0.2)
    cmd.press('tab')
    cmd.sleep(0.2)
    cmd.write('\\\FORTES-RPS-02\\Share\\sistemas\\' + pasta)
    cmd.sleep(0.2)
    cmd.press('tab')
    cmd.write('F')
    cmd.sleep(0.4)
    cmd.press('tab')
    cmd.sleep(0.2)
    cmd.write('RE')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.keyDown('ctrl')
    for i in range(40):
        cmd.press('pagedown')
    cmd.sleep(0.1)
    cmd.press('space')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/okImg.png')
    cmd.sleep(0.1)
    cmd.press('ctrl')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('down')
    cmd.sleep(0.1)
    cmd.press('down')
    cmd.sleep(0.1)
    cmd.press('down')
    cmd.sleep(0.1)
    cmd.press('space')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('enter')
    for i in range(5):
        cmd.sleep(0.1)
        cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('enter')
    print ' PublisherRobot: AC publicado com sucesso. [' + time.ctime() + ']'

def publicaPatrio():
    cmd.sleep(15)
    print ' PublisherRobot: Iniciando Publicacao do PATRIO [' + time.ctime() + ']'
    cmd.click('asserts/PublicarImg.png')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('\\\FORTES-RPS-02\\Share\\sistemas\\' + pasta + '\\PATRIO\\PATRIO.exe')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write(cortado[0].upper() + ' ' + cortado[1].upper())
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','c')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write('PATRIO ' + cortado[0].upper())
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','v')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/mostrarOpcoesImg.png')
    cmd.sleep(0.2)
    cmd.move(100, 0)
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('PATRIO ' + cortado[0].upper())
    cmd.sleep(0.5)
    for i in range(13):
        cmd.sleep(0.2)
        cmd.press('tab')
    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.keyDown('ctrl')
    for i in range(40):
        cmd.press('pagedown')
    cmd.sleep(0.1)
    cmd.press('space')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/okImg.png')
    cmd.sleep(0.1)
    cmd.press('ctrl')
    for i in range(6):
        cmd.sleep(0.1)
        cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('enter')
    print ' PublisherRobot: PATRIO publicado com sucesso. [' + time.ctime() + ']'

def publicaAgente():
    cmd.sleep(15)
    print ' PublisherRobot: Iniciando Publicacao do AGENTE [' + time.ctime() + ']'    
    cmd.click('asserts/PublicarImg.png')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('F:\\AC\\Agente_'+ pasta +'\\Agente\\Agente.exe')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write(cortado[0].upper() + ' ' + cortado[1].upper())
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','c')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','a')
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.write('AGENTE ' + cortado[0].upper())
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.5)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('del')
    cmd.sleep(0.1)
    cmd.hotkey('ctrl','v')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/mostrarOpcoesImg.png')
    cmd.sleep(0.2)
    cmd.move(100, 0)
    cmd.sleep(0.2)
    cmd.click()
    cmd.write('AGENTE ' + cortado[0].upper())
    cmd.sleep(0.5)
    for i in range(13):
        cmd.sleep(0.2)
        cmd.press('tab')
    cmd.press('enter')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('tab')
    cmd.sleep(0.1)
    cmd.keyDown('ctrl')
    for i in range(40):
        cmd.press('pagedown')
    cmd.sleep(0.1)
    cmd.press('space')
    cmd.sleep(0.1)
    cmd.doubleClick('asserts/okImg.png')
    cmd.sleep(0.1)
    cmd.press('ctrl')
    for i in range(6):
        cmd.sleep(0.1)
        cmd.press('tab')
    cmd.sleep(0.1)
    cmd.press('enter')
    print ' PublisherRobot: AGENTE publicado com sucesso. [' + time.ctime() + ']'


mapeiaPastaDoCliente()
openPushPage()
publicaAc()
publicaPatrio()
publicaAgente()

print '                   ___                  '
print '                  (   )                 '
print '                   | |                  '
print '     /=============| |==============\    '
print '     [                               ]                   Ok, meu trabalho terminou por aqui'
print '     |       _____       _____       |                   Fico no aguardo de novos chamados'
print '     |     ||     ||   ||     ||     |                 Ate a proxima, qualquer coisa so chamar.'
print '    [|     ||  ^  ||   ||  ^  ||     |]         '
print '    [|     ||_____||   ||_____||     |] '
print '    [|                               |]          '
print '    [|                               |]          '
print '     |     /-------------------\     |    '
print '     |                               | '
print '     |                               |  '
print '     \===============================/   '
print ' '
print ' '
input("Pressione <enter> para encerrar!")

