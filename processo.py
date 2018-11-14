
class Processo():

    def __init__(self,id,vizinho1,vizinho2):
        self.id = id
        self.vizinho = vizinho1
        self.prox_vizinho = vizinho2
        self.isLider = False
        self.falha = False
        self.comecou_eleicao = False #Identifica quem iniciou a eleicao
