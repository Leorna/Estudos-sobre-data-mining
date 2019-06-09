from random import randint
import matplotlib.pyplot as plt


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        
    def __roll(self):
        return randint(1, self.sides)
    
    def gen_results(self, times=1000):
        for _ in range(times):
            result = self.__roll()
            yield result
            
    
    
die = Die()

times = 10**6

results = [value for value in die.gen_results(times)]

frequencies = [results.count(value) for value in range(1, die.sides+1)]

x = [1, 2, 3, 4, 5, 6]

plt.scatter(x, frequencies, s=40, edgecolor='none')

plt.title('Lançamento de um dado de 6 lados ' + str(times) + ' vezes', fontsize=24)
plt.xlabel('Resultado', fontsize=14)
plt.ylabel('Frequencia do Resultado', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.show()



