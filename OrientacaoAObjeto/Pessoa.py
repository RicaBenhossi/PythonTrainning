"""
Orientação a Objeto:

Hierarquia 
    Classe
    Atributo
    Método
    Herança
    Instância
"""


# class Pessoa_sem_construtor:
#     nome = ""  # Atributo da Classe PESSOA. O seu valor é denominado ESTADO.
#     idade = ""  # Outro atributo da Classe PESSOA

#     """
#         Método da Classe PESSOA que retorna se ela está caminhando ou parada. O primeiro parâmetro deve sempre ser SELF que instancia o prórpio 
#         método
#     """

#     def caminhar(self, caminhando):
#         if (caminhando):
#             print("Pessoa caminhando...")
#         else:
#             print("Pesso parada...")


class Pessoa:
    nome = ""  # Atributo da Classe PESSOA. O seu valor é denominado ESTADO.
    idade = ""  # Outro atributo da Classe PESSOA

    """
        Método Construtor - Esse método é o responsável por inicializar um objeto, atribuindo estados aos seus atibutos.
                            Nesse exemplo ao instanciar (chamar) o objeto, é obrigatório passar os estados como parâmetro
    """

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Caminhar(self):
        print("Pessoa está caminhando...")

    def Dormir(self):
        print("Está na hora de dormir!")


# p = Pessoa()  # Para chamar a Classe, deve-se obrigatoriaente usar os ().
# p.nome = "João"
# p.idade = 12
# print("Nome: ", p.nome)
# print("Idade: ", p.idade)
# p.caminhar(False)

# r = Pessoa_com_construtor("Maria", 7)
# print("Nome (construtor): ", r.nome)
# print("Idade (construtor): ", r.idade)
# r.caminhar(False)
