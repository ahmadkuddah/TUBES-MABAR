from Data_Id import nasabah    #Import data
from time import sleep  #Untuk memberi delay print agar lebih realistis
import pickle   #Untuk save dan load data secara permanen

no_rek_nasabah = [nasabah[id]['no-rek'] for id in range(len(nasabah))]    #List no rekening dari data
bank_tujuan = ["Sesama Bank Ganesha", "Bank Lain", "Virtual Account"]     #List bank tujuan


def restart_transfer(): #Fungsi untuk mengulang transfer jika ada kesalahan di saat transfer
    print("Batalkan transfer? Ketik: \n"
          "1 - Jika Ya\n"
          "2 - Jika Tidak\n")
    i = int(input("Batal?(1/2): ")) 
    if i == "2":    #Jika tidak batal transfer, maka menu transfer akan kembali dijalankan (asumsi masukan user benar)
        transfer_()
    else:
        print("Silahkan ambil kartu Anda kembali")
        #Transfer batal dan kembali ke main menu awal

def transfer_(no_rektujuan): 
    id = 1 #Id pengirim, dari awal sudah di-define

    print("Transfer ATM\nPilih bank yang ingin dituju. Ketik: \n"   #Interface menu awal transfer
          "1 - Untuk ke Sesama Bank Ganesha\n"
          "2 - Untuk ke Bank Lain\n"
          "3 - Untuk ke Virtual Account")
    n = int(input("Masukkan angka menu yang ingin dituju (1/2/3): "))   
    #Input dari user untuk memilih menu bank tujuan
    #Di GUI, input akan berupa tombol

    print(f"\nAnda Memilih untuk Transfer ke {bank_tujuan[n-1]}")
    no_rek_tujuan = input("Masukkan no. rekening yang ingin dituju: ") #Input no. rekening tujuan

    if no_rek_nasabah.count(no_rek_tujuan) > 0: #Jika no. rekening tujuan ada di data (count > 0), maka transfer berlanjut
        nominal_transfer = float(input("Masukkan nominal transfer: "))  #Nominal transfer dari masukan user
        
        id_tujuan = no_rek_nasabah.index(no_rek_tujuan) #Variable untuk menyimpan index/ id dari rekening tujuan. Fungsinya untuk mengakses data
        
        print("\nKonfirmasi Tujuan Transfer\n" #Interface untuk mengonfirmasi tujuan transfer yang diambil dari data id tujuan
        f"Nama : {nasabah[id_tujuan]['nama']}\n"
        f"No. Rekening : {nasabah[id_tujuan]['no-rek']}\n"
        f"Jumlah Transfer : {nominal_transfer}\n"
        "Ketik: \n"
          "1 - Jika Benar\n"
          "2 - Jika Salah\n")
        
        n = int(input("Benar(1)/ Salah(2): "))  #Masukan user berupa apakah tujuan transfer benar/salah
        if n == 1:
            print("Transfer Sedang Diproses...") #Memproses Transaksi
            sleep(2)    #Sleep (dari library time) digunakan untuk memberi delay agar realistis

            if float(nasabah[id]['tabungan']) < nominal_transfer:   #Mengecek apakah saldo cukup atau tidak
                print("Maaf, saldo anda tidak cukup\n")   #Jika tidak, transfer bisa di-restart
                restart_transfer()
            else:   #Jika cukup, maka tabungan dari rekening pengirim akan dipindah ke tabungan rekening tujuan
                nasabah[id]['tabungan'] = str(float(nasabah[id]['tabungan']) - nominal_transfer) #Datanya belom bisa kesimpen permanen
                nasabah[id_tujuan]['tabungan'] = str(float(nasabah[id_tujuan]['tabungan']) + nominal_transfer)
                pickle.dump(nasabah, open("nasabah.dat", "wb"))
                print("\nTransfer berhasil\nSilahkan ambil kartu Anda kembali") #Transaksi selesai
            
        else:
           restart_transfer() #Jika rekening tujuan salah, maka user diberi opsi untuk me-restart

    else:   #Jika no. rekening tidak tersedia di database, maka akan diberikan pilihan untuk restart transfer
        print("\nNo. Rekening yang anda tuju tidak tersedia.")
        restart_transfer()