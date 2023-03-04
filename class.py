class Classe():
    def __init__(self, nome, duracao, genero, lancamento, diretor, class_indicativa, tela_cheia, pausado, volume):
        self.nome = nome
        self.duracao = duracao
        self.genero = genero
        self.lancamento = lancamento
        self.diretor = diretor
        self.class_indicativa = class_indicativa
        self.tela_cheia = tela_cheia
        self.pausado = pausado
        self.volume = volume

    def pausar(self, pausado):
        if not pausado:
            self.pausado = True
        return('Filme pausado')

    def continuar(self, pausado):
        if pausado:
            self.pausado = False
        return('Filme tocando')

    def avancar10(self, duracao):
        print(self.duracao)
        self.duracao = int(self.duracao) + 10
        return('→10s')

    def voltar10(self, duracao):
        print(self.duracao)
        self.duracao = int(self.duracao) - 10
        return('←10s')

    def telacheia(self, tela_cheia):
        if self.tela_cheia:
            self.tela_cheia = False
            return 'Tela Reduzida'
        else:
            self.tela_cheia = True
            return 'Tela Cheia'

    def aumentarVol(self, volume):
        print(volume)
        if self.volume < 10:
            self.volume += 1
        return '▬' * volume

    def diminuirVol(self, volume):
        print(volume)
        if self.volume > 0:
            self.volume -= 1
        return '▬' * volume

if __name__ == '__main__':
    filme1 = Classe(
        nome="Bts",
        duracao="108",
        genero="Documentário",
        lancamento="2022",
        diretor="Jung Cook",
        class_indicativa="12",
        tela_cheia=False,
        pausado=True,
        volume=10
    )
    
    print(filme1.nome)
    print(filme1.duracao)
    print(filme1.genero)
    print(filme1.lancamento)
    print(filme1.diretor)
    print(filme1.class_indicativa)
    print(filme1.tela_cheia)
    print(filme1.pausado)
    print(filme1.volume)
    
    print(filme1.diminuirVol(filme1.volume))
    print(filme1.diminuirVol(filme1.volume))
    print(filme1.diminuirVol(filme1.volume))
    print(filme1.diminuirVol(filme1.volume))
    
    print(filme1.aumentarVol(filme1.volume))
    print(filme1.aumentarVol(filme1.volume))
    print(filme1.aumentarVol(filme1.volume))
    print(filme1.aumentarVol(filme1.volume))
    
    print(filme1.voltar10(filme1.duracao))
    
    print(filme1.avancar10(filme1.duracao))
    
    print(filme1.telacheia(filme1.tela_cheia))
    print(filme1.telacheia(filme1.tela_cheia))
    print(filme1.telacheia(filme1.tela_cheia))
    
    print(filme1.pausar(filme1.pausado))
    print(filme1.pausar(filme1.pausado))
    
    print(filme1.continuar(filme1.pausado))
    print(filme1.continuar(filme1.pausado))
