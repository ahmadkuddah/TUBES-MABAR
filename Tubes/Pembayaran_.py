def opsi_pembayaran():
  print("Opsi Pembayaran:")
  print("1. PLN ")
  print("2. Internet")
  print("3. Pendidikan")
  print(" ")
  return
tagihan=''
def tagihan_(ID):
    global tagihan
    if 0 <= ID < 10000:
        tagihan='50000'
        print("Nilai Tagihan Pembayaran: 50000")
    elif 10000 <= ID < 20000:
        tagihan='75000'
        print("Nilai Tagihan Pembayaran: 75000")
    elif 20000 <= ID < 30000:
        tagihan='100000'
        print("Nilai Tagihan Pembayaran: 100000")
    elif 30000 <= ID < 40000:
        tagihan='150000'
        print("Nilai Tagihan Pembayaran: 150000")
    elif 40000 <= ID < 50000:
        tagihan='250000'
        print("Nilai Tagihan Pembayaran: 250000")
    elif 50000 <= ID < 60000:
        tagihan='500000'
        print("Nilai Tagihan Pembayaran: 500000")
    elif 60000 <= ID < 70000:
        tagihan='750000'
        print("Nilai Tagihan Pembayaran: 750000")
    elif 70000 <= ID < 80000:
        tagihan='1000000'
        print("Nilai Tagihan Pembayaran: 1000000")
    elif 80000 <= ID < 90000:
        tagihan='1500000'
        print("Nilai Tagihan Pembayaran: 1500000")
    elif 90000 <= ID < 99999:
        tagihan='2000000'
        print("Nilai Tagihan Pembayaran: 2000000")
    return


opsi = input("Pilih pembayaran (1/2/3): ")
if opsi == "1":
  while True:
    ID = input("Masukkan ID Pembayaran (5-digit): ")
    if len(ID) == 5:
        ID = int(ID)
        tagihan()
    else:
        continue
    konfirmasi = input("Apakah tagihan Anda sudah benar? [y/n] ")
    if konfirmasi == "y":
        print("Pembayaran Berhasil")
        break
    else: 
        print("ID pembayaran yang dimasukkan salah.")
        continue
if opsi == "2":
  while True:
    ID = input("Masukkan ID Pembayaran (5-digit): ")
    if len(ID) == 5:
        ID = int(ID)
        tagihan()
    else:
        print("ID pembayaran yang dimasukkan salah.")
        continue
    konfirmasi = input("Apakah tagihan Anda sudah benar? [y/n] ")
    if konfirmasi == "y":
        print("Pembayaran Berhasil")
        break
    else: 
        continue
if opsi == "3":
  while True:
    ID = input("Masukkan ID Pembayaran (5-digit): ")
    if len(ID) == 5:
        ID = int(ID)
        tagihan()
    else:
        print("ID pembayaran yang dimasukkan salah.")
        continue
    konfirmasi = input("Apakah tagihan Anda sudah benar? [y/n] ")
    if konfirmasi == "y":
        print("Pembayaran Berhasil")
        break
    else: 
        continue
