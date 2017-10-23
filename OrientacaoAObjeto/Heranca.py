"""
    HERANÇA - A classe filha herda da classe pai/mãe os seus métodos, atributos, estados e comportamento, podendo especializar
              uma classe.
"""
# Para usar a herança é necessário importa o módulo getcwd de OS para que a classe mãe possa ser trazisa para o contexo do programa
# Evitar usar o import BIBLIOTECA pois tratrá TODAS os métodos da bibiloteca, carregando desnecessiariamente o sistema.
from Pessoa import Pessoa


# A Classe PessoaFisica recebe como parâmetros a Classe Mãe Pessoa.
class PessoaFisica(Pessoa):
    # Novo atributo da classe PessoaFisica
    cpf = ""

    # Novo méodo inicializador.
    # **kwargs traz o dicionário da classe herdada, nesse caso alé mdo CPF, será obrigatório preencher nome, idade, referente
    # à contrução da classe Pessoa.
    def __init__(self, cpf, **kwargs):
        # A Função SUPER faz a referencia ao método INIT da classe Pessoa. Rcebe como primeiro parâmetro o nome da classe 
        # que e aestá chamando e depois self, seguida da chamada do .__init__, passano os atributos da classe mãe (**wargs)
        super(PessoaFisica, self).__init__(**kwargs)
        # Atribuição do CPF da Classe PessoaFisica à classe Pessoa.
        self.cpf = cpf

    def Aniversario(self):
        self.idade = self.idade + 1
        print("Fez aniversário de: " + str(self.idade) + " ano(s) de vida.")


pf = PessoaFisica(nome="Paulo", idade=36, cpf="123")
print("Nome: ", pf.nome)
print("Idade: ", pf.idade)
pf.Caminhar()
pf.Dormir()
pf.Aniversario()