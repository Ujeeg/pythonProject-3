# from main import mainMenu
def interface_kubus():
    while True:
        try :
            s = float(input("Masukkan sisi : "))
            if s > 0:
                print(f"Luas kubus adalah : {calculate_kubus(s)}")
                if not yes_or_no_interface():
                    break 
            else:
                print("input yang dimasukkan tidak sesuai")
        except ValueError:
            print("Masukan input dalam angka")


def interface_balok():
    while True:
        try :
            p = float(input("Masukkan panjang balok : "))
            l = float(input("Masukkan lebar balok : "))
            t = float(input("Masukkan tinggi balok : "))

            if p > 0 and l > 0 and t > 0:
                print(f"Luas balok adalah {calculate_balok(p, l, t)}")
                if not yes_or_no_interface():
                    break
            else:
                print("input yang dimasukkan3 tidak sesuai")
        except ValueError:
            print("Masukan input dalam angka")


def interface_tabung():
    while True:
        try :
            r = float(input("Masukkan Jari -jari : "))
            t = float(input("Masukkan tinggi tabung : "))

            if r > 0 and t > 0:
                print(f"Luas tabung adalah {calculate_tabung(r, t)}")
                if not yes_or_no_interface():
                    break 
            else:
                print("input yang dimasukkan tidak sesuai")
        except ValueError:
            print("Masukan input dalam angka")


def interface_karucut():
    while True:
        try :
            r = float(input("Masukkan Jari -jari : "))
            t = float(input("Masukkan tinggi tabung : "))

            if r > 0 and t > 0:
                print(f"Luas kerucut adalah {calculate_kerucut(r, t)}")
                if not yes_or_no_interface():
                    break 
            else:
                print("input yang dimasukkan tidak sesuai")
        except ValueError:
            print("Masukan input dalam angka")


def calculate_kubus(s):
    luas_kubus = s ** 3
    return (luas_kubus)


def calculate_balok(p, l, t):
    luas_balok = p * l * t
    return (luas_balok)


def calculate_tabung(r, t):
    v = 3.14
    luas_tabung = v * r * r * t
    return (luas_tabung)


def calculate_kerucut(r, t):
    v = 3.14
    a = 1 / 3
    luas_kerucut = a * v * r * r * t
    return (luas_kerucut)


def bangunDatar():
    pass


def operasiAritmatika():
    pass


def yes_or_no_interface():
    while True:
        try :
            print("Apakah ada akan menghitung kembali (y/n) :")
            pilihan = input("Masukan Input : ").strip().lower()
            if pilihan == "y":
                return True
            elif pilihan == "n":
                return False
            else:
                print("masukan y / n")
        except ValueError:
            print("Masukan y / n")