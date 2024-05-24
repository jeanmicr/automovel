from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self,marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self.veiculos.append(self)

    @abstractmethod
    def ligar(self):
        print(f'O carro {self._modelo} está ligado')
        