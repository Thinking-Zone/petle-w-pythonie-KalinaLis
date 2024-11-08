zgaduj = True

while zgaduj:
    odpowiedz = input("Czy pada? (t/n) ")
    if (pada == True):
        if odpowiedz == 't':
            print("zgadłeś, pada")
            zgaduj == break
        elif odpowiedz == 'n':
            print("nie, nie pada")
        else:
            print("odpowiedz na pytanie")
    elif (pada == False):
        if odpowiedz == 'n':
            print("zgadłeś, pada")
        elif odpowiedz == 't':
            print("nie, nie pada")
            break
