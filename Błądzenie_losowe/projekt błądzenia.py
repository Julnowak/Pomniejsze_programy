import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    odp = input('Czy chcesz wygenerować błądzenie losowe jeszcze raz? (t/n)')
    if odp == 'n':
        break
