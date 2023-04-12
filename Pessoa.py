class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado="vivo", estado_civil="solteiro", conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge

    def envelhecer(self):
        if self.__estado == "vivo":
            self.__idade += 1
            if self.__idade < 21:
                self.__altura += 0.5
            print(f"{self.__nome} está com {maria.__idade} anos e {maria.__altura} cm de altura.")
        else:
            print(f"{self.__nome} está morto(a) e não pode envelhecer.")

    def engordar(self, valor):
        if self.__estado == "vivo":
            self.__peso += valor
            print(f"{self.__nome} engordou {valor} kg e agora pesa {self.__peso} kg.")
        else:
            print(f"Operação não realizada. {self.__nome} está morto(a).")

    def emagrecer(self, valor):
        if self.__estado == "vivo":
            self.__peso -= valor
            print(f"{self.__nome} emagreceu {valor} kg e agora pesa {self.__peso} kg.")
        else:
            print(f"{self.__nome} está morto(a) e não pode emagrecer.")

    def crescer(self, valor):
        if self.__estado == "vivo" and self.__idade < 21:
            self.__altura += valor
            print(f"{self.__nome} cresceu {valor} cm e agora tem {self.__altura} cm de altura.")
        elif self.__idade >= 21:
            print(f"{self.__nome} não pode mais crescer pois está com 21 anos ou mais.")
        else:
            print(f"{self.__nome} está morto(a) e não pode crescer.")

    def casar(self, pessoa):
        if pessoa.__estado == "morto" or self.__estado == 'morto':
            print(f"Casamento não realizado! {pessoa.__nome} está {pessoa.__estado} e {self.__nome} está {self.__estado}.")
        elif pessoa.__idade < 18 or self.__idade < 18:
            print(f"Casamento não realizado! {pessoa.__nome} tem {pessoa.__idade} anos e {self.__nome} tem {self.__idade} anos." )
        elif pessoa.__estado_civil == "casado" or self.__estado_civil == 'casado':
            print(f"Casamento não realizado! {pessoa.nome} está {pessoa.__estado_civil} e {self.__nome} está {self.__estado_civil}.")
        else:
            pessoa.__estado_civil = "casado"
            pessoa.__conjuge = self
            self.__conjuge = pessoa
            self.__estado_civil = "casado"
            print(f"{self.__nome} está casado com {pessoa.__nome}.")

    def morrer(self):
        if self.__estado == "vivo":
            self.__estado = "morto"
            print(f"{self.nome} morreu.")
            if self.__estado_civil == 'casado':
                self.__conjuge.__estado_civil = 'viúvo'
                self.__conjuge.__conjuge = None

        else:
            print(f"{self.nome} já está morto(a).")

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @property
    def peso(self):
        return self.__peso

    @property
    def altura(self):
        return self.__altura

    @property
    def sexo(self):
        return self.__sexo

    @property
    def estado(self):
        return self.__estado

    @property
    def estado_civil(self):
        return self.__estado_civil

    @property
    def conjuge(self):
        return self.__conjuge

    @nome.setter
    def nome(self, nome):
        return print('Sem permissão')

    @idade.setter
    def idade(self, idade):
        return print('Sem permissão')



maria = Pessoa('Maria', 5, 20, 100, 'F')
joao = Pessoa('João', 12, 40, 140, 'M')
pedro = Pessoa('Pedro', 22, 65, 170, 'M')
bia = Pessoa('Bia', 18, 55, 160, 'F')
julia = Pessoa('Julia', 30, 65, 170, 'F')
cadu = Pessoa('Carlos', 2, 11, 80, 'M')
jonas = Pessoa('Jonas', 34, 70, 180, 'M')


# a) atribua a idade de maria para o valor: 10
maria.idade = 10

# b) Maria fez aniversário. Chame o método necessário.
maria.envelhecer()

# c) Pedro quer crescer 2 cm. Chame o método necessário.
pedro.crescer(2)

# d) Bia quer casar com Carlos. Chame o método necessário.
bia.casar(cadu)

# e) Pedro quer casar com Maria. Chame o método necessário.
pedro.casar(maria)

# f) Pedro quer casar com Júlia.
pedro.casar(julia)

# g) Pedro quer casar com Bia.
pedro.casar(bia)

# h) Maria morreu.
maria.morrer()

# i) Maria quer engordar.
maria.engordar(2)

# j) Bia quer casar com Jonas.
bia.casar(jonas)

# k) Bia morreu.
bia.morrer()

# l) Pedro Morreu
pedro.morrer()

# m) Jonas quer casar com Júlia
jonas.casar(julia)

# n) Pedro quer casar com Bia
pedro.casar(bia)

