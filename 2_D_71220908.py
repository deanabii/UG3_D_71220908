plat = input("Masukkan Plat Nomor : ").split()

try:
    nomor_plat = int(plat[1])
    if nomor_plat >= 0 and nomor_plat <= 3000:
        print("Plat nomor tersebut diperuntukan untuk mobil")
    elif nomor_plat >= 3001 and nomor_plat <= 4000:
        print("Print nomor tersebut diperuntukan untuk motor")
    elif nomor_plat >= 4001 and nomor_plat <= 5000:
        print("Plat nomor tersebut diperuntukan untuk angkutan umum")
    else:
        print("Plat nomor tidak terindikasi ketiga angkutan tersebut")
except:
    print('Plat Nomor Tidak Terindikasi, setelah kode daerah harus berupa nomor kendaraan')