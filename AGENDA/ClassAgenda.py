Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import datetime

class Contato():
    def __init__(self, pessoa, telefone):
        self.criacao = str(datetime.date.today())
        self.pessoa = pessoa
        self.telefone = telefone

    def listarTelefones(self):
        pass
