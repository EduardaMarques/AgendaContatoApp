
class Contato():
    def __init__(self,criacao, pessoa, telefones = []):
        self.criacao = criacao
        self.pessoa = pessoa 
        self.telefone = telefones

    def listarTelefones(self):
        return self.telefones
