devmod = 1

def printdev(x):
    if devmod == 1:
        print(x)

import os

def clr():
    os.system("cls")

gravity = 10

def valid_value():
    if lang.lower() == "tr":
        print('Lütfen geçerli bir değer giriniz!')
    elif lang.lower() == "en":
        print('Please enter a valid value!')


def mt_to_time(x):
    x = x/gravity*0.5
    print(x)

def time_to_mt(a):
    a = a**2*gravity*0.5
    print(a)

########################################################################################################################
def tr_choose():
    choose = input("""
            [1]- Serbest düşüş

            [00]- Ayarlar (Çalışmıyor)
            [0]- Çıkış
            İşlem seçiniz: """)
    clr()
    if choose == "1":
        tr_choose_1()
    elif choose == "00":
        tr_settings()
    elif choose == "0":
        exit()
    else:
        valid_value()
        tr_choose()

def tr_settings():
    settings = input("""
                [1]- Yer çekimi

                [0]- Geri 
                İşleminizi seçin: """)
    clr()
    if settings == "1":
        tr_settings_1()
    elif settings == "0":
        tr_choose()
    else:
        valid_value()
        tr_settings()


def tr_settings_1():
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
        tr_settings()
    elif settings_gravity == "2":
        #gravity = gravity - 0.193
        gravity = 9.807
        tr_settings()
    elif settings_gravity == "3":
        gravity = 1.62
        tr_settings()
    elif settings_gravity == "4":
        gravity = 3.721
        tr_settings()
    elif settings_gravity == "5":
        gravity = 24.79
        tr_settings()
    elif settings_gravity == "9":
        custom_gravity = int(input('Lütfen bir değer giriniz:\t'))
        gravity = custom_gravity
        tr_settings()
    elif settings_gravity == "0":
        tr_settings()
    else:
        valid_value()
        tr_settings_1()


def tr_choose_1():
    freefall = input("""
                [1]- Metreden saniye bulma
                [2]- Saniyeden metre bulma

                [0]- Geri
                İşleminizi seçin: """)
    clr()
    if freefall == "1":
        x = int(input('Lütfen metre değerini gir:\t'))
        mt_to_time(x)
        tr_choose()
    elif freefall == "2":
        a = int(input('Lütfen saniye\'yi giriniz:\t'))
        time_to_mt(a)
        tr_choose()
    elif freefall == "0":
        tr_choose()
    else:
        valid_value()
        tr_choose_1()

########################################################################################################################

def en_choose():
    choose = input("""
            [1]- Free fall

            [00]- Settings (Not working)
            [0]- Exit
            Select your action: """)
    clr()
    if choose == "1":
        en_choose_1()
    elif choose == "00":
        en_settings()

def en_settings():
    settings = input("""
                [1]- Gravity

                [0]- Back
                Select your action: """)
    clr()
    if settings == "1":
        en_settings_1()
    elif settings == "0":
        en_choose()
    else:
        valid_value()
        en_settings()

def en_settings_1():
    settings_gravity = input("""
                    [1]- 10
                    [2]- 9,807 (Earth)
                    [3]- 1,62 (Moon)
                    [4]- 3,721 (Anthem)
                    [5]- 24,79 (Jupiter)

                    [9]- Custom
                    [0]- Back
                    Select your action: """)

    if settings_gravity == "1":
        gravity = 10
        en_settings()
    elif settings_gravity == "2":
        #gravity = gravity - 0.193
        gravity = 9.807
        en_settings()
    elif settings_gravity == "3":
        gravity = 1.62
        en_settings()
    elif settings_gravity == "4":
        gravity = 3.721
        en_settings()
    elif settings_gravity == "5":
        gravity = 24.79
        en_settings()
    elif settings_gravity == "9":
        custom_gravity = int(input('Please enter a value :\t'))
        gravity = custom_gravity
        en_settings()
    elif settings_gravity == "0":
        en_settings()
    else:
        valid_value()
        en_settings_1()

def en_choose_1():
    freefall = input("""
                [1]- Metre to second
                [2]- Second to metre

                [0]- Back
                Select your action: """)
    clr()
    if freefall == "1":
        x = int(input('Please enter the meter value:\t'))
        mt_to_time(x)
        en_choose()
    elif freefall == "2":
        a = int(input('Please enter the second:\t'))
        time_to_mt(a)
        en_choose()
    elif freefall == "0":
        en_choose()
    else:
        valid_value()
        en_choose_1()

########################################################################################################################

while True:
    lang = input('Select your language  [TR/EN]\n')
    clr()
    if lang.lower() == "tr":
        tr_choose()
        break
    elif lang.lower() == "en":
        en_choose()
        break
    else:
        print('Lütfen geçerli bir değer giriniz!\t / \tPlease enter a valid value! \n')
        continue


