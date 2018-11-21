from datetime import date
from Carros import Carro
import os


def main():
    hoje=date.today()
    repeat = "0"
    car=Carro()
    while repeat == "0":

        print("                   data atual: " + str(hoje))
        print("--------------escolha uma das opções abaixo:----------------")

        print("1)consultar veículos\n")

        print("2)adicionar veículos\n")

        print("3)alugar/reservar veículos\n")

        print("4)devolver/liberar veículos\n")

        print("5)excluir veículos\n")

        print("6)avançar data atual\n")

        print("7)sair\n")

        print("[quantidade de atrasos: " + str(car.getatraso()) + "              ]")

        print("[quantidade de veículos cadastrados: " + str(car.getCarros()) + " ]")

        print("[quantidade de vaículos alugados: " + str(car.getResAlg()) + "    ]")

        try:
            a = int(input())

        except ValueError as e:
            print("Digite um número inteiro positivo")
            a = int(input())

        if a == 1:
            car.consulta()
            input("aperte qualquer tecla para voltar ao menu: ")

        elif a == 2:
            marca = input("Marca do carro: \n")
            modelo = input("Modelo do carro: \n")
            ano = input("Ano do carro: \n")
            diaria = float(input("Aluguel do carro: \n"))
            car.add_car(marca,modelo,ano,diaria)
            input("aperte qualquer tecla para voltar ao menu: ")


        elif a == 3:
            escolha = int(input("O senhor deseja (1)Alugar ou (2)Reservar um veiculo: "))

            if escolha == 1:
                car.alugar()
                input("aperte qualquer tecla para voltar ao menu: ")


            elif escolha == 2:
                car.reservar()
                input("aperte qualquer tecla para voltar ao menu: ")


        elif a == 4:
            escolha = int(input("O senhor deseja (1)Devolver ou (2)Liberar um veiculo: "))

            if escolha == 1:
                car.devolver()
                input("aperte qualquer tecla para voltar ao menu: ")


            elif escolha == 2:
                car.liberar()
                input("aperte qualquer tecla para voltar ao menu: ")


        elif a == 5:
            car.delete_car()
            input("aperte qualquer tecla para voltar ao menu: ")

        elif a == 6:
            c = int(input("deseja avançar quantos dias? "))
            hoje = date.fromordinal(hoje.toordinal()+c)
            print("data alterada com sucesso!")
            input("aperte qualquer tecla para voltar ao menu: ")

        elif a == 7:
            repeat = "1"


main()