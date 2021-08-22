class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    raquelly = Pessoa(nome='Raquelly')
    marco = Pessoa(raquelly, nome='Marco')
    print(Pessoa.cumprimentar(marco))
    print(id(marco))
    print(marco.cumprimentar())
    print(marco.nome)
    print(marco.idade)
    for filho in marco.filhos:
        print(filho.nome)
    marco.sobrenome = 'Bentancor'
    del marco.filhos
    print(marco.__dict__)
    print(raquelly.__dict__)

