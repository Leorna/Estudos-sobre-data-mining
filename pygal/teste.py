from pygal import Bar
from random import randint


class Moeda:
    def __init__(self):
        self.lados = 2
        
    def lancar_moeda(self, vezes):
        for _ in range(vezes):
            yield randint(1, self.lados)
    
    
moeda = Moeda()

vezes = 1000000

resultados = [face for face in moeda.lancar_moeda(vezes)]

frequencia_cara = resultados.count(1)
frequencia_coroa = resultados.count(2)

h = Bar()

h.title = 'Lançamento de uma moeda ' + str(vezes) + ' vezes'
h.x_title = 'Faces'
h.y_title = 'Frequencia da face'

h.add('Cara', frequencia_cara)
h.add('Coroa', frequencia_coroa)
h.render_to_file('teste.svg')