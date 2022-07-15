def menu():
    print('\nWitaj w programie, do tworzenia list rzeczy do zrobienia!')
    print()
    print('1. Sprawdź swoje zadania')
    print('2. Dodaj nowe zadanie')
    print('3. Usuń zadanie z listy')
    print('4. Zapisz do pliku')
    print('5. Wyjdź z programu')


def sprawdz(lista):
    i = '1'
    for zadanie in lista:
        print(i + '. ' + zadanie)
        now = int(i)
        u = now + 1
        i = str(u)


def dodaj():
    p = 'tak'
    while p == 'tak':
        task = input('Wprowadź nowe zadanie:\n')
        lis.append(task)
        print('\nZadanie zostało dodane!')
        p = input('Czy chcesz dodać jeszcze jedno zadanie? \n')
        while p != 'tak' and p != 'nie':
            print('Wpisz poprawnie!')
            p = input('Czy chcesz dodać jeszcze jedno zadanie? \n')


def usun():
    y = int(input('Podaj numer zadania, które chcesz usunąć: '))
    if 0 < y <= len(lis):
        print('UWAGA! Zadanie o traści "' + lis[y - 1] + '" zostanie zaraz usunięte! Czy jesteś pewny swojej decyzji? ')
        odp = input('')
        if odp == 'tak':
            lis.pop(y - 1)
            y = str(y)
            print('Zadanie nr ' + y + ' zostało usunięte.\n')
        elif odp == 'nie':
            print('Zadanie nie zostało usunięte.')
        else:
            print('Proszę wpisać poprawnie!')
    else:
        print('Nie można usunąć zadania - podaj inny numer.')


def do_pliku():
    f = open('lista.txt', "a", encoding='UTF-8')
    c = '1'
    for i in lis:
        f.write(c + '. ' + i + '\n')
        b = int(c)
        c = b + 1
        c = str(c)
    f.close()


def enter():
    input("\nProszę wcisnąć ENTER, aby kontynuować")


m = open('lista.txt', "r", encoding='UTF-8')
lista = list(m)
lis = []
wybor = 1
while wybor != 5:
    menu()
    try:
        inp = input('Wybierz jedną z opcji, aby rozpocząć:\n')
        wybor = int(inp)
        if wybor == 1:
            sprawdz(lis)
            enter()
        elif wybor == 2:
            dodaj()
            enter()
        elif wybor == 3:
            usun()
            enter()
        elif wybor == 4:
            do_pliku()
            enter()
    except:
        print('Proszę wybrać jedną z podanych opcji!')
m.close()
print('\nDziękujemy i życzymy miłego dnia!')

# musisz nad tym popracować
