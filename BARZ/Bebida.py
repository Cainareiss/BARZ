import Produto

class Bebida(Produto):
    def __init__(self, nome, preco, codigo, marca, volume, alcoolica):
        super().__init__(nome, preco, codigo)
        self.marca = marca
        self.volume = volume
        self.alcoolica = alcoolica

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_volume(self):
        return self.volume

    def set_volume(self, volume):
        self.volume = volume

    def get_alcoolica(self):
        return self.alcoolica

    def set_alcoolica(self, alcoolica):
        self.alcoolica = alcoolica
