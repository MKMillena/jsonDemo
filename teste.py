import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i%2 == 0] # i variando de 10 até 36 e retorna apenas valores divisíveis por 2
        self.porta_halteres = {} # dicionário_1 vazio para poder receber valores
        self.reiniciar_o_dia() # função_2 a ser criada e apresentada a seguir

    def reiniciar_o_dia(self): # função_2 criada
        self.porta_halteres = {i: i for i in self.halteres} # vai aplicar valores em dicionário_1, onde i (posição): i (peso)

    def listar_halteres(self): # retorna todos os halteres disponíveis
        return [i for i in self.porta_halteres.values() if i != 0]

    def listar_espacos(self): # retorna todos os halteres disponíveis
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegar_haltere(self, peso):
        halt_posit = list(self.porta_halteres.values()).index(peso) # retorna o valor do índice em que está alocado o peso. Ex: 14 -> índice 2
        key_halt = list(self.porta_halteres.keys())[halt_posit] # retorna em qual posição o peso está. Ex: peso 14 está na posição 14
        self.porta_halteres[key_halt] = 0 # para indicar que o peso foi pego e deixou espaço vazio
        return peso # o peso que o usuário pegou

    def devolver_haltere(self, posit, peso): # função para devolver na posição e qual peso estou devolvendo
        self.porta_halteres[posit] = peso


    def calcular_caos(self): # vai calcular quantos halteres estão fora do lugar em percentual
        caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(caos) / len(self.porta_halteres)

class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo # tipo 1 é normal e tipo 2 é bagunçeiro
        self.academia = academia
        self.peso = 0

    def iniciar_treino(self):
        lista_pesos = self.academia.listar_halteres()
        self.peso = random.choice(lista_pesos)
        self.academia.pegar_haltere(self.peso)

    def finalizar_treino(self):
        espacos = self.academia.listar_espacos()
        if self.peso == 0: # Se o usuário não pegou peso, não faz nada
            return

        espacos_vazios = self.academia.listar_espacos()
        if not espacos_vazios: # Se não há espaços, não é possível devolver
            return

        if self.tipo == 1:
            # Verifica se o lugar correto do peso está na lista de espaços vazios
            if self.peso in espacos_vazios:
                self.academia.devolver_haltere(self.peso, self.peso)
            else:
                # Se o lugar correto está ocupado, devolve em um lugar aleatório vago
                posit = random.choice(espacos_vazios)
                self.academia.devolver_haltere(posit, self.peso)

        # Lógica para o usuário bagunceiro (fora do if do tipo 1)
        elif self.tipo == 2:
            # Sempre devolve em um lugar aleatório vago
            posit = random.choice(espacos_vazios)
            self.academia.devolver_haltere(posit, self.peso)

        self.peso = 0



academia = Academia()

usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]

for i in usuarios:
    print(i.tipo) # 1 1 1 1 1 1 1 1 1 1 2, os tipos dos usuários

random.shuffle(usuarios) # misturar usuários para trocar a posição do usuário 2 aleatoriamente

# todos os usuários vão passar por 10 sessões de treino

list_caos = []

for k in range(50):
    academia.reiniciar_o_dia()
    for i in range(10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciar_treino()
        for user in usuarios:
            user.finalizar_treino()
    list_caos += [academia.calcular_caos()]

import seaborn
seaborn.displot(list_caos) # Gráfico da distribuição das variáveis
