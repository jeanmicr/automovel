from veiculo import Veiculo

class Carro(Veiculo):
    
    veiculos = []
    
    def __init__(self, marca, modelo, cor):
        super().__init__(marca,modelo)
        self._cor = cor
        
    @classmethod
    def listar_veiculos(cls):
        for veiculo in cls.veiculos:
            print(f'Marca: {veiculo._marca} | Modelo: {veiculo._modelo} | Cor: {veiculo._cor}')
        
    def ligar(self):
        return super().ligar()