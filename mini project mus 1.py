# User dan Pw untuk login
User = 2409116027
Pw = 12345

# Proses Login
while True: 
    try: #untuk menangani jika ada salah dalam input nya
        Username = int(input("Masukan Username anda: "))
        Password = int(input("Masukan Password anda: "))
        
        if Username == User and Password == Pw:
            print("Yeay Login Berhasil")
            break #untuk menghentikan proses looping
        else:
            print("Username dan Password tidak tersedia")
    except ValueError: #sudah sepaket dengan try
        print("Masukan Username dan Password dengan benar")

while True:
    Jam_Kerja = float(input("Masukan jam kerja: "))
    Tarif_perjam = float(input("Masukan Tarif kerja per jam: "))
    Gaji = Jam_Kerja * Tarif_perjam #menghitung gaji dengan cara mengkali
    
    Bonus = 0
    if Jam_Kerja > 160:
        Bonus = 0.1 * Gaji #menghitung bonus dengan 0.1/10%
        Gaji += Bonus
    else:
        Jam_Kerja <= 160
        Gaji = Jam_Kerja * Tarif_perjam
    
    print("Bonus = RP", Bonus)
    print("Gaji Total = Rp", Gaji)

    #kondisi apabila ingin menghitung kembali
    Kembali = input("Apakah Anda Ingin Menghitung Gaji Kembali? (ya/Tidak): ")
    if Kembali.lower() != "ya": #untuk kalau huruf kapital atau tidak tetap bisa
        print("-------Selesai-------")
        break