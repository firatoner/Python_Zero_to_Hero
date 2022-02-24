devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

gravity = 10
def tr():
    printdev('Lang: TR')

    def p_choose():
        choose = input("""
        [1]- Serbest düşüş
        
        [0]- Ayarlar
           
        İşlem seçiniz: """)
        if choose == "1":
            freefall = input("""
            [1]- Metreden saniye bulma
            [2]- Saniyeden metre bulma
                
            [0]- Geri
            İşleminizi seçin: """)

            if freefall == "1":
                x = int(input('Lütfen metre değerini gir:\t'))
                mt_to_time(x)
            elif freefall == "2":
                a = int(input('Lütfen saniye\'yi giriniz:\t'))
                time_to_mt(a)
            else:
                valid_value()
        elif choose == "0":
            settings = input("""
            [1]- Yer çekimi
            
            [0]- Geri 
            İşleminizi seçin: """)

            if settings == "1":
                settings_gravity = input("""
            [1]- 10
            [2]- 9,807 (Dünya)
            [3]- 1,62 (Ay)
            [4]- 3,721 (Mars)
            [5]- 24,79 (Jüpiter)
            
            [9]- Özel değer
            [0]- Geri 
            İşleminizi seçin: """)

                if settings_gravity == "1":
                    gravity = 10
                    p_choose()
                elif settings_gravity == "2":
                    gravity = 9.807
                    p_choose()
                elif settings_gravity == "3":
                    gravity = 1.62
                    p_choose()
                elif settings_gravity == "4":
                    gravity = 3.721
                    p_choose()
                elif settings_gravity == "5":
                    gravity = 24.79
                    p_choose()
                elif settings_gravity == "9":
                    custom_gravity = int(input('Lütfen bir değer giriniz:\t'))
                    gravity = custom_gravity
                    p_choose()
                else:
                    valid_value()
                    p_choose()


            elif settings == "0":
                exit()




def valid_value():
    if lang.lower() == "tr":
        print('Lütfen geçerli bir değer giriniz!')
    elif lang.lower() == "en":
        print('Please enter a valid value!')






def en():
    printdev('Lang: EN')
    choose = input("""
    [1]- Free fall
    
    [0]- Back 
    [00]- Settings

    Select your action: """)
    if choose == "1":
        freefall = input("""
        [1]- Metre to time
        [2]- Time to metre
        
        [0]- Back 
        Select your action: """)
        if freefall == "1":
            x = int(input('Please enter meters :\n'))
            x = x/gravity*0.5
            printdev(x)

def mt_to_time(x):
    x = x/gravity*0.5
    print(x)

def time_to_mt(a):
    a = a**2*gravity*0.5
    print(a)

while True:
    lang = input('Select your language  [TR/EN]\n')
    if lang.lower() == "tr":
        tr()
        break
    elif lang.lower() == "en":
        en()
        break
    else:
        print('Lütfen geçerli bir değer giriniz!\t / \tPlease enter a valid value! \n')
        continue
