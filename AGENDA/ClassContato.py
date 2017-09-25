
class Contato():
    def __init__(self, pessoa, telefones = []):
        self.criacao = str(datetime.date.today())
        self.pessoa = pessoa
        self.telefone = telefones

    def listarTelefones(self):
        return self.telefones
