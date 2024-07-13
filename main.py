# def mainMenu():
from aritmatika import bangunRuang, bangunDatar, interface_kubus, interface_karucut, interface_tabung, interface_balok



def mainMenu():
    print('''Selamat datang di program Python 
      1. Integral
      2. Turunan
      3. Aritmatika
      4. Logaritma
      5. Translate
      6. Exit''')
    
    pilihan = int(input("Masukkan pilihan anda: "))
    if pilihan == 1:
        integral()
    elif pilihan == 2:
        turunan()
    elif pilihan == 3:
        aritmatika()
    elif pilihan == 4:
        logaritma()
    elif pilihan == 5:
        translate()
    elif pilihan == 6:
        exit()
    else:
        print("Pilihan tidak valid")
        mainMenu()


def aritmatika():
    print('''Selamat datang di program Python 
      1. Bangun Ruang
      2. Bangun Datar
      3. Operasi Aritmatika
    ''')
    pilihan = int(input("Masukkan operasi yang anda inginkan: "))
    if pilihan == 1:
        bangunRuang()
    elif pilihan == 2:
        bangunDatar()
    elif pilihan == 3:
        operasiAritmatika()

def bangunRuang():
    while True:
        print('''Menu Bangun Ruang
            1. Kubus
            2. Balok
            3. Tabung
            4. Kerucut
            0. Main menu
            ''')
        pilihan = int(input("Masukkan operasi yang anda inginkan: "))

        if pilihan == 1:
            interface_kubus()
        elif pilihan == 2:
            interface_balok()
        elif pilihan == 3:
            interface_tabung()
        elif pilihan == 4:
            interface_karucut()
        elif pilihan == 0:
            mainMenu()
        else:
            print("Menu tidak ada pada pilihan, masukkan 0 - 4")
        ValueError("masukan Angka")




def integral():
    while True:
        print('''Silahkan pilih jenis integral: 
        1. Integral Tentu
        2. Integral Tak Tentu''')
        pilihan = int(input('Masukkan operasi integral: '))
        if pilihan == 1:
            integralTentu()
        elif pilihan == 2:
            integralTakTentu()





def turunan():
    pass


def integralTentu():
    base = int(input('masukkan base number: '))
    power = int(input('masukkan power number: '))
    result = base**power

    test = base*('x')

    # integralEquation = (base/power+1)*(base)*

    print(test)






def integralTakTentu():
    pass


# def aritmatika():
#     print('''Selamat datang di program Python
#       1. Bangun Ruang
#       2. Bangun Datar
#       3. Operasi Aritmatika
#     ''')
#     pilihan = int(input("Masukkan operasi yang anda inginkan: "))
#     if pilihan == 1:
#         bangunRuang()
#     elif pilihan == 2:
#         bangunDatar()
#     elif pilihan == 3:
#         operasiAritmatika()
        

## put ALL the function below here

# def bangunRuang():
#     while True:
#         print('''Menu Bangun Ruang
#             1. Kubus
#             2. Balok
#             3. Tabung
#             4. Kerucut
#             0. Main menu
#             ''')
#         pilihan = int(input("Masukkan operasi yang anda inginkan: "))
#
#         if pilihan == 1:
#             interface_kubus()
#         elif pilihan == 2:
#             interface_balok()
#         elif pilihan == 3:
#             interface_tabung()
#         elif pilihan == 4:
#             interface_karucut()
#         elif pilihan == 0:
#             mainMenu()
#         else:
#             print("Menu tidak ada pada pilihan, masukkan 0 - 4")
#         ValueError("masukan Angka")

def operasiAritmatika():
    pass


def bangunDatar():
    pass


def logaritma():
    pass


def translate():
    pass




# def interface_kubus():
#     while True:
#         s = float(input("Masukkan sisi : "))
#         if s > 0:
#             print(f"Luas kubus adalah : {calculate_kubus(s)}")
#             break
#         else:
#             print("input yang dimasukkan tidak sesuai")
#         ValueError("Masukan input dalam angka")
#
#
# def interface_balok():
#     while True:
#         p = float(input("Masukkan panjang balok : "))
#         l = float(input("Masukkan lebar balok : "))
#         t = float(input("Masukkan tinggi balok : "))
#
#         if p > 0 and l > 0 and t > 0 :
#             print(f"Luas balok adalah {calculate_balok(p,l,t)}")
#             break
#         else:
#             print("input yang dimasukkan3 tidak sesuai")
#         ValueError("Masukan input dalam angka")
#
# def interface_tabung():
#     while True:
#         r = float(input("Masukkan Jari -jari : "))
#         t = float(input("Masukkan tinggi tabung : "))
#
#         if r > 0 and t > 0:
#              print(f"Luas tabung adalah {calculate_tabung(r,t)}")
#              break
#         else:
#             print("input yang dimasukkan tidak sesuai")
#         ValueError("Masukan input dalam angka")
#
#
# def interface_karucut():
#     while True:
#         r = float(input("Masukkan Jari -jari : "))
#         t = float(input("Masukkan tinggi tabung : "))
#
#         if r > 0  and t > 0:
#              print(f"Luas kerucut adalah {calculate_kerucut(r,t)}")
#              break
#         else:
#             print("input yang dimasukkan tidak sesuai")
#         ValueError("Masukan input dalam angka")
#
#
# def calculate_kubus(s):
#     luas_kubus = s ** 3
#     return(luas_kubus)
#
# def calculate_balok(p,l,t):
#     luas_balok = p * l * t
#     return(luas_balok)
#
# def calculate_tabung(r,t):
#     v = 3.14
#     luas_tabung= v*r*r*t
#     return(luas_tabung)
#
# def calculate_kerucut(r,t):
#     v = 3.14
#     a = 1/3
#     luas_kerucut = a * v * r * r *t
#     return(luas_kerucut)
#
#
mainMenu()

def exit():
    pilihan = int(input("Masukkan kembali pilihan anda: "))