class Classe():
    def __init__(self, nome, duracao_total, duracao_atual, genero, lancamento, diretor, class_indicativa, tela_cheia, pausado, volume):
        self.nome = nome
        self.duracao_total = duracao_total
        self.duracao_atual = duracao_atual
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

    def avancar10(self, duracao_atual, duracao_total):
        print(self.duracao_total, self.duracao_atual)
        if int(self.duracao_atual) < int(self.duracao_total):
            self.duracao_atual = int(self.duracao_atual) + 10
        return('→10s')

    def voltar10(self, duracao_atual):
        if self.duracao_atual > 0:
            self.duracao_atual = int(self.duracao_atual) - 10
        else:
            self.duracao_atual = 0
        return('←10s')

    def telacheia(self, tela_cheia):
        if self.tela_cheia:
            self.tela_cheia = False
            return 'Tela Reduzida'
        else:
            self.tela_cheia = True
            return 'Tela Cheia'

    def aumentarVol(self, volume):
        if self.volume < 10:
            self.volume += 1
        return '▬' * volume, volume

    def diminuirVol(self, volume):
        if self.volume > 0:
            self.volume -= 1
        return '▬' * volume, volume


    def comandos(self):
        comando = [
            lambda: print('Comando inválido'),
            lambda: self.continuar(self.pausado),
            lambda: self.pausar(self.pausado),
            lambda: self.telacheia(self.tela_cheia),
            lambda: self.avancar10(self.duracao_atual, self.duracao_atual),
            lambda: self.voltar10(self.duracao_atual),
            lambda: self.aumentarVol(self.volume),
            lambda: self.diminuirVol(self.volume)
        ]
        return comando

if __name__ == '__main__':
    filme1 = Classe(
        nome="Bts",
        duracao_total="108",
        duracao_atual="0",
        genero="Documentário",
        lancamento="2022",
        diretor="Jung Cook",
        class_indicativa="12",
        tela_cheia=False,
        pausado=True,
        volume=10
    )
    print('Genero:', filme1.genero)
    print('Data de lançamento:', filme1.lancamento)
    print('Diretor:', filme1.diretor)
    print('Classificação indicativa:', filme1.class_indicativa)
    while True:
        try:
            r = int(input(f'Filme: {filme1.nome}\n'
                          f'Duração: {int(filme1.duracao_atual) // 60}:{int(filme1.duracao_atual) % 60}\n'
                          f'Volume: {filme1.volume}/10\n'
                          'Filme já disponível para assistir!\n'
                          '1 - Play\n'
                          '2 - Pause\n'
                          '3 - Tela cheia\n'
                          '4 - Avançar 10 segundos\n'
                          '5 - Voltar 10 segundos\n'
                          '6 - Aumentar volume\n'
                          '7 - Diminuir volume\n'))
            if 1 <= r <= 7:
                comandos = filme1.comandos()
                print(f'\033[32m{comandos[r]()}\033[0m')
            else:
                erro
        except:
            print('\033[31mComando Inválido\033[0m')

