class Carro:
    def __init__ (self,marca,modelo,ano,cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar(self):
        return f'O carro {self.modelo} está ligado.'

    def acelerar(self):
        return f'Acelerar o {self.modelo}.'

    def desligar(self):
        return f'O {self.modelo} está desligado.'

if __name__ == '__main__':
    carro1= Carro("Volkswagen", "gol", "2016", "vermelho")
    carro2 = Carro("Renault", "kwid", "2018", "branco")
    carro3 = Carro("Volkswagen", "fox", "2008", "cinza")
    print(carro1.ligar())
    print(carro2.desligar())
    print(carro3.acelerar())
    