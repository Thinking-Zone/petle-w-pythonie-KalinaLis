pada = False
licznik_nie = 0
while not pada:
    print("Nie pada! yaaay")
    odpowiedz = input("Czy pada? (tak/nie) ")
    if odpowiedz == 'nie':
        licznik_nie += 1 
    elif odpowiedz == 'tak':
        print(f"powiedziałeś 'nie'{licznik_nie}")
        pada == True
    elif odpowiedz == 'niewiem':
        print("to sie dowiedz")
    else: 
        print("huh")
