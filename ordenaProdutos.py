from Util import Util
from Produto import Produto
from Data import Data
import sys


#obtem os argumentos passados pelo terminal

file = str(sys.argv[1])
fileOutPut = str(sys.argv[2])

#instancias as classes
util = Util()
data = Data()
produto = Produto()
util.file = file

# verifica se existe o arquivo, recebe o retorno de True do metodo da classe Util
if util.existFile():
    data.initData(file)
    data.readDataOfFile()
    data.resultScore(fileOutPut)

# se nao existir manda uma mensagem de erro
else:
    print('Please send a new file')
