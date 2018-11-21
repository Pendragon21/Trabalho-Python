from datetime import datetime

class Carro(object):
    def __init__(self):
        self.carro = []
        self.tempo = []
        self.atraso=[]

#------------------------------------------------Metodo para adicionar um carro-------------------------------------------------
    def add_car(self,marca,modelo,ano,diaria):
        carro = "Carro: " + str(len(self.carro) + 1) + " Modelo: " + modelo + " Marca: " + marca + " Ano: " + str(ano) + " Aluguel por dia: " + str(diaria)

        self.carro.append(carro)
# ------------------------------------------------Metodo para deletar um carro-------------------------------------------------
    def delete_car(self, diaria):
        excluir = int(input("digite o codigo do carro a ser removido"))
        excluir -= 1

        if self.carro[excluir][-1] == '1':
            self.carro.remove(self.carro[excluir])
        else:
            print("Carro reservado, por favor, insira outro carro ou espere o tempo do aluguel acabar")

# ------------------------------------------------Metodo para ver o numero de veiculos cadastrados-------------------------------------------------
    def getCarros(self):
        return len(self.carro)

# ------------------------------------------------Metodo para ver o numero de veiculos cadastrados-------------------------------------------------
    def getatraso(self):
        return len(self.atraso)


# ------------------------------------------------Metodo para ver a quantidade de veiculos alugados ou rezervados------------------------------
    def getResAlg(self):
        return len(self.tempo)


# -----------------------------------------------------Metodo para consultar os carros---------------------------------------------------------
    def consulta(self):

        i = 0
        while i < len(self.carro):

            aux = self.carro[i].find("Marca")
            print(self.carro[i][:aux - 1])

            if self.veiculo[i][-1::] == '1':
                print("Veiculo disponível")

            else:
                print("Veiculo indisponível")
            i += 1

        ver = input("Para mais detalhes digite v: ")

        if ver == 'v':
            j = 0
            while j < len(self.veiculo):

                print(self.veiculo[j])

                if self.veiculo[j][-1::] == '1':
                    print("Veiculo disponível")

                else:
                    print("Veiculo indisponível")
                j += 1
# -----------------------------------------------------Metodo para alugar/reservar carros---------------------------------------------------------
    def alugar(self):
        loc=input("nome do locatário:")
        tempo=int(input("Deseja alugar o Carro por quantos dias?"))

        now = datetime.now()
        dia = now.day + tempo
        mes = now.month
        ano = now.year

        if dia>30:
            dia-=30
            mes=now.month + 1

            if mes>12:
                mes-=12
                ano=now.year+1

        if len(self.carro)==0:
            print ("não temos Carros disponíveis no momento")
        elif tempo>30:
            print ("aluguel e reservas só poderão ser feitas em 30 dias")

        else:
            choose=input("Escolha um carro a ser alugado:")
            choose=choose-1
            help=int(self.carro[choose][-1::])

        if help!=1:
            print ("Carro indisponível")

        else:
            self.carro[choose]=self.carro[choose].replace(self.carro[choose][-1::],'0')
            vencimento=choose,str(dia)+'//' + str(mes) + "//" + str(ano), loc,tempo
            self.tempo.append(vencimento)

    def reservar(self):
        loc = input("Nome do Locatario: ")
        tempo = int(input("Deseja reservar o Carro por quantos dias?"))

        if tempo > 30:
            print("aluguel e reservas só poderão ser feitas em 30 dias")

        else:
            choose = int(input("Qual carro deseja rerservar: "))
            choose =choose-1

            data_da_reserva = input("Selecione data para a reserva(d/m/a): ")
            reserva=data_da_reserva.split('/')

            dia=int(reserva[0])
            mes=int(reserva[1])
            ano=int(reserva[2])
            i=0

            while i<len(self.tempo):
                if self.tempo[i][0]==choose:
                    reservacar=self.tempo[i][1].split('/')
                    diaC=int(reservacar[0])
                    mesC=int(reservacar[1])
                    anoC=int(reservacar[2])

                    if ano==anoC:
                        if mes == mesC:
                            if dia >= diaC:

                                vencimento=choose, str(dia) + "/" + str(mes) + "/" + str(ano)
                                self.prazos.append(vencimento)
                                self.carro[choose] = self.carro[choose].replace(self.carro[choose][-1::], '0')
                            else:
                                print("Veiculo indisponível")
                        else:
                            vencimento=choose, str(dia) + "/" + str(mes) + "/" + str(ano)
                            self.prazos.append(vencimento)
                            self.carro[choose] = self.carro[choose].replace(self.carro[choose][-1::], '0')
                    else:
                        vencimento=choose, str(dia) + "/" + str(mes) + "/" + str(ano)
                        self.prazos.append(vencimento)
                        self.carro[choose] = self.carro[choose].replace(self.carro[choose][-1::], '0')

                i += 1

            if i == len(self.prazos):
                vencimento=choose, str(dia) + "/" + str(mes) + "/" + str(ano), loc, tempo
                self.prazos.append(vencimento)
                self.carro[choose]=self.carro[choose].replace(self.carro[choose][-1::], '0')

# -----------------------------------------------------Metodo para devolver/liberar carros---------------------------------------------------------

    def devolver(self,dia,mes,ano):

        carro=int(input("Carro que deve ser devolvido"))
        carro=carro-1

        i=0
        while i<len(self.tempo):
            print ("Carro alugado %d"+(self.tempo[i][0]+1))
            input()

            if self.tempo[i][0]==carro:
                TCar=self.tempo[i][1].split('/')
                diaC = int(TCar[0])
                mesC = int(TCar[1])
                help=self.carro[i].find("Auguel por dia")
                help+=10

                valor=float(self.carro[i][help:-2])

                if mes == mesC:
                    if dia == diaC:
                        print("Nome do Locatario: %s" % (self.tempo[i][2]))
                        print("Pagar: %d" % (valor * self.tempo[i][3]))
                        self.tempo.remove(self.tempo[i])
                        self.carro[carro] = self.carro[carro].replace(self.carro[carro][-1::], '1')

                    else:
                        print("Nome do Locatario: %s" % (self.tempo[i][2]))
                        print("Veiculo está atrasado, Pagar: %d" % (valor * self.tempo[i][3] + (valor * (dia - diaC))))
                        self.tempo.remove(self.tempo[i])
                        self.carro[carro] = self.carro[carro].replace(self.carro[carro][-1::], '1')
                        self.atraso[i]

                else:

                    mesA = mes - mesC
                    diasA = 30 - diaC + 30 * (mesA - 1) + dia
                    print("Nome do Locatario: %s" % (self.tempo[i][2]))
                    print("Veiculo está atrasado, Pagar: %d" % (valor * self.tempo[i][3] + (valor * (diasA))))
                    self.tempo.remove(self.tempo[i])
                    self.carro[carro] = self.carro[carro].replace(self.carro[carro][-1::], '1')
            i += 1

    def liberar(self):
        carro=int(input("qual carro deseja liberar?"))
        carro=carro-1
        i=0
        while i<len(self.tempo):
            print ("Carro alugado: %d"+(self.tempo[i][0]+1))
            input()

            if self.tempo[i][0] == carro:
                self.tempo.remove(self.tempo[carro])
                self.carro[carro] = self.carro[carro].replace(self.carro[carro][-1::], '1')
                i += 1