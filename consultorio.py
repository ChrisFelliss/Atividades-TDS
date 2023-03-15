from datetime import datetime
from random import randint, choice


def verificar_str(texto):
    while 1:
        string = input(texto).lower() or None
        try:
            if string == None:
                print("Nome inválido")
            else:
                break
        except:
            pass
    return string


class Classe():
    def __init__(self, nome_paciente, nome_medico, medicos, id_consulta, id_bloqueada, data, especialidade, consulta):
        self.nome_paciente = nome_paciente
        self.nome_medico = nome_medico
        self.medicos = medicos
        self.id_consulta = id_consulta
        self.id_bloqueada = id_bloqueada
        self.data = data
        self.especialidade = especialidade
        self.consulta = consulta  # Dados da consulta em uma lista

    def __str__(self):
        return f'{self.nome_paciente.capitalize()}\n{self.nome_medico}'

    def get_nome_paciente(self):
        self.nome_paciente = verificar_str('Qual o nome completo do(a) paciente? ')
        return self.nome_paciente

    def get_nome_medico(self, medicos, especialidade):
        print('Lista de médicos disponíveis para a especialidade selecionada')
        medicos_lista = self.medicos[especialidade.capitalize()]
        for i in medicos_lista:
            print(i, medicos_lista[i])
            # print(i.keys(), i.values())
        while 1:
            nome = input('Tem preferencia por algum(a) médico(a)? [Opcional] ') or None
            print(list(medicos_lista.values()))
            if nome == None:
                nome = choice(list(medicos_lista.values()))
                print(nome)
                break
            elif nome not in (list(medicos_lista.values())):
                pass
            else:
                break

        self.nome_medico = nome
        return self.nome_medico

    def get_data(self):
        while 1:
            try:
                dia, mes, ano = verificar_str('Qual da data da consulta? [dd/mm/yyyy] ').split('/')
                date = datetime(int(ano), int(mes), int(dia))
                if datetime.now() > date:
                    raise
                date = date.strftime("%d/%m/%Y")
                break
            except:
                print('Data inválida')
        self.data = date

        return self.data

    def get_especialidade(self, medicos):
        print('Lista de especialidades ')
        for i in self.medicos:
            print(i)
        while 1:
            especialidade = verificar_str('Qual a especialidade? ')
            if especialidade.capitalize() in self.medicos.keys():
                break
            else:
                print('Opção inválida')
        self.especialidade = especialidade

        return self.especialidade

    def nova_consulta(self):
        self.get_nome_paciente()
        self.get_data()
        self.get_especialidade(self.medicos)
        self.get_nome_medico(self.medicos, self.especialidade)
        self.salvar_consulta(self.nome_paciente, self.nome_medico, self.id_bloqueada, self.data, self.especialidade, self.consulta)
        return


    def salvar_consulta(self, nome_paciente, nome_medico, id_bloqueada, data, especialidade, consulta):
        while 1:
            id_consulta = randint(100000, 999999)
            if id_consulta not in id_bloqueada:
                id_bloqueada.append(id_consulta)
                break

        self.consulta[id_consulta] = {
            'Nome do paciente': nome_paciente,
            'Nome do médico': nome_medico,
            'Data': data,
            'Especialidade': especialidade.capitalize()
        }
        return 'Consulta marcada'


    def mostrar_consulta(self, consulta):
        print('Lista de todas as consultas marcadas até o momento\n')
        for j in consulta:
            dados = consulta[j]
            print(f"Código da consulta:{j}\n{dados['Nome do paciente']}\n{dados['Data']}\n")
        indice = int(input('Qual o código da consulta que deseja ver?'))
        for i in consulta[indice]:
            print(f'\n{i}: {consulta[indice][i]}')
        return



    # def nova_consulta(self):
    #     return

    def comandos(self):
        comando = [
            lambda: print('Comando inválido'),
            lambda: self.nova_consulta(),
            lambda: self.mostrar_consulta(self.consulta)
        ]
        return comando


if __name__ == '__main__':
    lista_medicos = {
        "Cardiologia": {1: "Maria Silva", 2: "João Santos", 3: "Ana Oliveira", 4: "Pedro Pereira", 5: "Beatriz Alves"},
        "Dermatologia": {1: "Carlos Fernandes", 2: "Sofia Costa", 3: "Luís Sousa", 4: "Clara Coelho",
                         5: "Hugo Rodrigues"},
        "Ginecologia": {1: "Raquel Santos", 2: "Miguel Costa", 3: "Paula Oliveira", 4: "Bruno Silva",
                        5: "Catarina Pereira"},
        "Neurologia": {1: "Tiago Almeida", 2: "Mariana Carvalho", 3: "André Silva", 4: "Inês Sousa",
                       5: "Francisco Mendes"},
        "Oftalmologia": {1: "Carolina Santos", 2: "Gabriel Costa", 3: "Isabella Rodrigues", 4: "Vitor Oliveira",
                         5: "Luana Almeida"},
        "Oncologia": {1: "Gustavo Fernandes", 2: "Lívia Pereira", 3: "Marcelo Silva", 4: "Camila Sousa",
                      5: "Bruno Alves"},
        "Ortopedia": {1: "Fernanda Costa", 2: "Ricardo Pereira", 3: "Letícia Rodrigues", 4: "Eduardo Martins",
                      5: "Larissa Oliveira"},
        "Pediatria": {1: "Anderson Silva", 2: "Júlia Santos", 3: "Lucas Mendes", 4: "Bruna Carvalho",
                      5: "Felipe Rodrigues"},
        "Psiquiatria": {1: "Juliana Ferreira", 2: "Rafael Souza", 3: "Natália Oliveira", 4: "Marcos Lima",
                        5: "Jéssica Gomes"},
        "Urologia": {1: "Vinicius Ferreira", 2: "Luciana Costa", 3: "Diego Silva", 4: "Renata Pereira",
                     5: "Rodrigo Santos"}
    }

    consulta = Classe(
        nome_paciente="João Guilherme",
        nome_medico="Ketlin",
        medicos=lista_medicos,
        id_consulta="116359",
        id_bloqueada=[],
        data="11/05/2021",  # ddmmyyyy
        especialidade="Dermatologia",
        consulta={}
    )

    comando = consulta.comandos()
    while True:
        try:
            r = int(input(f'Seja bem-vindo ao hospital Paçoca!\n'
                          f'Em que posso ajudar?\n'
                          f'1 - Marcar nova consulta\n'
                          f'2 - Mostrar consultas pendentes\n'))
            if 1 <= r <= 2:
                comandos = consulta.comandos()
                comandos[r]()
            else:
                erro
        except:
            print('Comando Inválido')

# João
# 25/12/2023
# dermatologia
