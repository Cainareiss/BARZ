class Cliente:
    def __init__(self, nome, data_nascimento, telefone):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone
