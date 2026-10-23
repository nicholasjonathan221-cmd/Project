def jumlah (a, b):
    return a + b
def kurang (a, b):
    return a - b
def kali (a, b):
    return a * b    
def bagi (a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
print ("""kalkulator online
        1. Penjumlahan
        2. Pengurangan
        3. Perkalian
        4. Pembagian""")
pilih = int(input("Masukkan pilihan (1/2/3/4): "))
match pilih:
    case 1:
        x=int(input("Masukkan angka pertama: "))
        y=int(input("Masukkan angka kedua: "))
        print(f"{x} + {y} = {jumlah(x, y)}")
    case 2:
        x=int(input("Masukkan angka pertama: "))
        y=int(input("Masukkan angka kedua: "))
        print(f"{x} - {y} = {kurang(x, y)}")
    case 3:
        x=int(input("Masukkan angka pertama: "))
        y=int(input("Masukkan angka kedua: "))
        print(f"{x} * {y} = {kali(x, y)}")
    case 4:
        x=int(input("Masukkan angka pertama: "))
        y=int(input("Masukkan angka kedua: "))
        print(f"{x} / {y} = {bagi(x, y)}")