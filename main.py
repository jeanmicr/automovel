from veiculo import Veiculo
from carro import Carro



def main():
    carro1 = Carro('Honda', 'Civic Si','Vermelho')
    carro1.ligar()
    carro2 = Carro('Subaru', 'STI', 'Blue Micka')
    carro2.ligar()
    carro3 = Carro('Toyota', 'GR', 'Laranja')
    carro3.ligar()

    Carro.listar_veiculos()
    
if __name__ == '__main__':
    main()