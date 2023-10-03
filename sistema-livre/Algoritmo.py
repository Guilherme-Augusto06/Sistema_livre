# Importe as classes dos animais terrestres
from Classes import *

import os

def main():
    a = 1
    while a == 1:
        try:
            print("Bem vindo ao Animalpedia.")
            print("[01] - Leão")
            print("[02] - Elefante")
            print("[03] - Girafa")
            print("[04] - Tigre")
            print("[05] - Urso Panda")
            print("[06] - Zebra")
            print("[07] - Rinoceronte")
            print("[08] - Hipopótamo")
            print("[09] - Koala")
            print("[10] - Panda Vermelho")
            print("[11] - Canguru")
            print("[12] - Tatu")
            print("[13] - Coala")
            print("[14] - Orangotango")
            print("[15] - Sair")
            menu = input("Digite o número correspondente ao animal que gostaria de visitar. \n -")

            # Tratamento das escolhas
            match menu:
                case "1":
                    print("Aqui estão algumas informações sobre leões para você! \n")
                    leao = Leão()
                    leao.botarOvo()
                    leao.pele()
                    leao.patas()
                    leao.correr()
                    leao.informações()
                    os.system("pause")
                    os.system("cls")
                case "2":
                    print("Aqui estão algumas informações sobre elefantes para você! \n")
                    elefante = Elefante()
                    elefante.botarOvo()
                    elefante.pele()
                    elefante.patas()
                    elefante.correr()
                    elefante.informações()
                    os.system("pause")
                    os.system("cls")
                case "3":
                    print("Aqui estão algumas informações sobre girafas para você! \n")
                    girafa = Girafa()
                    girafa.botarOvo()
                    girafa.pele()
                    girafa.patas()
                    girafa.correr()
                    girafa.informações()
                    os.system("pause")
                    os.system("cls")
                case "4":
                    print("Aqui estão algumas informações sobre tigres para você! \n")
                    tigre = Tigre()
                    tigre.botarOvo()
                    tigre.pele()
                    tigre.patas()
                    tigre.correr()
                    tigre.informações()
                    os.system("pause")
                    os.system("cls")
                case "5":
                    print("Aqui estão algumas informações sobre ursos pandas para você! \n")
                    ursopanda = ursopanda()
                    ursopanda.botarOvo()
                    ursopanda.pele()
                    ursopanda.patas()
                    ursopanda.correr()
                    ursopanda.informações()
                    os.system("pause")
                    os.system("cls")
                case "6":
                    print("Aqui estão algumas informações sobre zebras para você! \n")
                    zebra = Zebra()
                    zebra.botarOvo()
                    zebra.pele()
                    zebra.patas()
                    zebra.correr()
                    zebra.informações()
                    os.system("pause")
                    os.system("cls")
                case "7":
                    print("Aqui estão algumas informações sobre rinocerontes para você! \n")
                    rinoceronte = Rinoceronte()
                    rinoceronte.botarOvo()
                    rinoceronte.pele()
                    rinoceronte.patas()
                    rinoceronte.correr()
                    rinoceronte.informações()
                    os.system("pause")
                    os.system("cls")
                case "8":
                    print("Aqui estão algumas informações sobre hipopótamos para você! \n")
                    hipopotamo = Hipopótamo()
                    hipopotamo.botarOvo()
                    hipopotamo.pele()
                    hipopotamo.patas()
                    hipopotamo.correr()
                    hipopotamo.informações()
                    os.system("pause")
                    os.system("cls")
                case "9":
                    print("Aqui estão algumas informações sobre coalas para você! \n")
                    koala = Koala()
                    koala.botarOvo()
                    koala.pele()
                    koala.patas()
                    koala.correr()
                    koala.informações()
                    os.system("pause")
                    os.system("cls")
                case "10":
                    print("Aqui estão algumas informações sobre pandas vermelhos para você! \n")
                    pandavermelho = PandaVermelho()
                    pandavermelho.botarOvo()
                    pandavermelho.pele()
                    pandavermelho.patas()
                    pandavermelho.correr()
                    pandavermelho.informações()
                    os.system("pause")
                    os.system("cls")
                case "11":
                    print("Aqui estão algumas informações sobre cangurus para você! \n")
                    canguru = Canguru()
                    canguru.botarOvo()
                    canguru.pele()
                    canguru.patas()
                    canguru.correr()
                    canguru.informações()
                    os.system("pause")
                    os.system("cls")
                case "12":
                    print("Aqui estão algumas informações sobre tatus para você! \n")
                    tatu = Tatu()
                    tatu.botarOvo()
                    tatu.pele()
                    tatu.patas()
                    tatu.correr()
                    tatu.informações()
                    os.system("pause")
                    os.system("cls")
                case "13":
                    print("Aqui estão algumas informações sobre coalas para você! \n")
                    coala = Coala()
                    coala.botarOvo()
                    coala.pele()
                    coala.patas()
                    coala.correr()
                    coala.informações()
                    os.system("pause")
                    os.system("cls")
                case "14":
                    print("Aqui estão algumas informações sobre orangotangos para você! \n")
                    orangotango = Orangotango()
                    orangotango.botarOvo()
                    orangotango.pele()
                    orangotango.patas()
                    orangotango.correr()
                    orangotango.informações()
                    os.system("pause")
                    os.system("cls")
                case "15":
                    a = 0
                    print("Obrigado por usar o Animalpedia. Até a próxima!")
                case _:
                    print("Opção inválida. Por favor, selecione um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {str(e)}")
            os.system("pause")
            os.system("cls")