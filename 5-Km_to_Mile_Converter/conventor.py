while True:
    choose = int(input("""Select your action: 
    [1] Km to Mile
    [2] Mile to Km
    """))

    if choose == 1:
        km = int(input('Enter km:\n'))
        print('Mile: ',str(km*0.621371192))
    if choose == 2:
        mile = int(input('Enter Mile:\n'))
        print('Km: ',mile*1.609344)
    else:
        print('Please enter a valid value')

    cont = str(input('Do you want to do it again ? \n[Y]es \n[N]o\n'))
    if cont.lower() == "y":
        continue
    else:
        break


