from Produto import Produto
from Util import Util
class Data:
    #construtor
    def __init__(self):
        self._lista = []
        self._file = None
        self._orderedList = None
        self._produto = None

    # properties getters and setters
    @property
    def lista(self):
        return self._lista

    @lista.setter
    def lista(self, value):
        self._lista = value


    @property
    def file(self):
        return self.file

    @file.setter
    def file(self, value):
        self.file = value

    @property
    def orderedList(self):
        return self._orderedList

    @orderedList.setter
    def orderedList(self, value):
        self._orderedList = value


    # inicializa os dados a serem utilizados na classe
    def initData(self, file):
        self._file = file

    def readDataOfFile(self):
        # abre o arquivo para leitura
        files = open(self._file, 'r')
        self._produto = Produto()
        for data in files:
            # remove \n
            data = self._removeBreakWord(data)

            # data um split nos dados tirando ;
            elements = data.split(';')

            # preenche a classe produto
            produto = self._produto.setProduct(elements)

            self._orderedList = self._makeResultOrdered(produto)

        # fecha arquivo
        files.close()
        return self._orderedList


    # metodo que seta produtos
    def _setProduct(self, data):
        product = Produto()
        product.idProd      = data[0]
        product.venda       = data[1]
        product.qtdVisita   = data[2]
        return product


    # metodo privado que cria o resultado e ordena
    def _makeResultOrdered(self, data):
        # calcula o Pscore
        data.ScoreProduct()

        # cria uma tupla
        listNorOrdered = (data.idProd, data.Pscore)

        # adiciona as tuplas em uma lista
        self._lista.append(listNorOrdered)

        # ordena de forma decrescente
        self._lista.sort(key=lambda x: x[1], reverse=True)

        return self._lista


    # cria o arquivo contendo todos os resultados
    def resultScore(self, file):

        listOfProducts = self._orderedList

        util = Util()
        util.newFile = file
        # cria um arquivo
        fileWrite = util.makeFile(util.newFile)

        # le a lista de produtos com os Pscore ordernado e imprime o resultado em um novo arquivo passado pelo terminal
        for i in range(len(listOfProducts)):
            fileWrite.writelines('ID-{};{}\n'.format(listOfProducts[i][0], listOfProducts[i][1]))

        # fecha arquivo
        fileWrite.close()


    # metodo que remove a \n
    @staticmethod
    def _removeBreakWord(word):
        x = word.rstrip()
        return x





