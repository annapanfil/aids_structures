import random
def generate(n: int):
    #losuje n niepowtarzalnych liczb z zakresu 0 do 1,5n
    data = random.sample(range(int(1.5*n)), n)
    return data

if __name__ == "__main__":
    generate(10)
