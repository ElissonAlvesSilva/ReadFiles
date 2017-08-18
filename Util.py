class Util:
    #construtor
    def __init__(self):
        self._file = ''
        self._newFile = ''

    #   properties getters and setters
    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value

    @property
    def newFile(self):
        return self._newFile

    @newFile.setter
    def newFile(self, value):
        self._newFile = value


    # funcao que verifica se existe o arquivo para leitura
    def existFile(self):
        try:
            with open(self.file, 'r'):
                return True
        except IOError:
            print("No such file in the directory.\nPlease verify if the file it's  in the directory")
            return False


    # funcao quer cria um novo arquivo
    def makeFile(self, newFile):
        self._newFile = open(newFile, 'w+')
        return self._newFile


