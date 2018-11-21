
class Processo():

    def __init__(self,id,vizinho1,vizinho2):
        self.id = id #Id do processo
        self.vizinho = vizinho1 #Primeiro vizinho
        self.prox_vizinho = vizinho2 #Segundo vizinho
        self.isLider = False
        self.falha = False
        self.comecou_eleicao = False #Identifica quem iniciou a eleicao
        self.id_lider = 0
