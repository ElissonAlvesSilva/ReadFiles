from Util import Util
class Produto:
    # construtor
    def __init__(self):
        self._idProd     = 0
        self._venda      = 0
        self._qtdVisita  = 0
        self._Pscore     = 0


    # properties getter and setters

    @property
    def idProd(self):
        return self._idProd

    @idProd.setter
    def idProd(self, value):
        self._idProd = value

    @property
    def venda(self):
        return self._venda

    @venda.setter
    def venda(self, value):
        self._venda = value

    @property
    def qtdVisita(self):
        return self._qtdVisita

    @qtdVisita.setter
    def qtdVisita(self, value):
        self._qtdVisita = value


    @property
    def Pscore(self):
        return self._Pscore

    @Pscore.setter
    def Pscore(self, value):
        self._Pscore = value

    # calculo do score dos produtos

    def ScoreProduct(self):
        self.Pscore = (2*int(self.venda) + int(self.qtdVisita))

    # seta os produtos
    def setProduct(self, data):

        produto = Produto()

        produto.idProd = data[0]
        produto.venda = data[1]
        produto.qtdVisita = data[2]
        return produto






