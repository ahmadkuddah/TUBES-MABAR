# PROGRAM SIMULASI SISTEM ATM
# Spesifikasi Program: Program yang Mensimulasikan Sistem ATM dan Mensupport Beberapa Layanan Utama ATM,
# seperti Info Rekening, Penarikan Tunai, Transfer, Pembayaran, hingga Ganti PIN

# AUTHOR: Achmad N, Addin  M, Fathiya A, M Dzikri, M Naufal
# Jalankan Program Ini untuk Mulai Menggunakan Aplikasi

# KAMUS
# pinlama, pinbaru, pinnasabah : string  
# rekening, nominal : string 
# sumber, penarikan, alasan : string 
# tujuan_pembayaran, idpembayaran, alasan : string
# no_rek_nasabah, bank_tujuan : list
# numlist : list
# Condition, State  : string
# i, n : integer

# IMPORT LIBRARY
from tkinter import *           #Untuk Keperluan Graphic User Interface
from data import nasabah        #Import Tempat menyimpan data nasabah yang terhubung dengan database "nasabah.dat"
import pickle                   #Library untuk menyimpan data dalam bentuk .dat dan bisa permanent
import data_pembayaran as dp    #Import data untuk tagihan sesuai ID

# ALGORITMA
# Tampilan Windows Utama dengan Tkinter 
root= Tk()
root.title('ATM Bank Ganesha')
root.geometry("1360x720")
bg = PhotoImage(file = ".\Assets\ATM_Ganesha_no_Menu.png")
canvas1 = Canvas( root, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
root.resizable('0','0')

# Tampilan Kartu pada Menu Awal
kartu_img = [0 for i in range(5)]
for i in range(5):
    kartu_img[i] = PhotoImage(file=f'.\Assets\Kartu-{i+1}.png')

# Tampilan Layar/ Monitor ATM
# Membuat Frame
mainframe = Frame(canvas1, width=480, height=400,bg='#ADD8E6')
mainframe.pack_propagate(0)
mainframe.pack(anchor=NW, padx=160, pady=110)
# Menimpa Frame dengan Asset Gambar
bg2 = PhotoImage(file = ".\Assets\layar.png")
canvas2 = Canvas( mainframe, width = 490,height = 410)
canvas2.pack(fill = "both", expand = True)
canvas2.create_image( 0, 0, image = bg2, anchor = "nw")

# Inisiasi Variabel-Variabel
# Menu Ganti PIN
pinlama=''      #Variabel yang menyimpan input user untuk diverifikasi dengan pin asli nasabah
pinbaru=''      #Variabel yang menyimpan input user yang nantinya akan menjadi pin baru nasabah
pinnasabah=''   #Variabel yang menyimpan pin terakhir nasabah di database

# Menu Transfer
rekening=''     #Variabel yang menyimpan input user berupa rekening tujuan
nominal=''      #Variabel yang menyimpan input user berupa nominal yang ingin ditransfer kepada rekening tujuan
no_rek_nasabah = [nasabah[id]['no-rek'] for id in range(len(nasabah))]  #List yang berisi No. Rekening Nasabah di database
bank_tujuan = ["Sesama Bank Ganesha", "Bank Lain", "Virtual Account"]   #List bank tujuan yang bisa ditransfer
n = 0           #Indeks bank tujuan pada menu transfer

# Menu Penarikan Tunai
sumber=''       #Variabel yang menyimpan input user ketika memilih sumber dana yang akan digunakan untuk melakukan penarikan tunai
penarikan=''    #Variabel yang menyimpan input user berupa nominal yang ingin ditarik dari sumber dana nasabah
alasan=''       #Variabel yang menyimpan alasan gagalnya sebuah transaksi

# Menu Pembayaran
tujuan_pembayaran=''#Variabel yang menyimpan input user berupa tujuan pembayaran seperti Pendidikan, PLN, atau Internet
idpembayaran=''     #Variabel yang menyimpan input user berupa id yang dituju yang nantinya akan dicocokan dengan id yang ada pada data pembayaran

# Input dan Umum
numlist=[]          #List yang input dari button dan menyimpan setiap angka yang di input oleh tombol
Condition='belum dicantumkan'   #Kondisi dari Menu tertentu kepada button sehingga menyatakan fungsi dari button tersebut pada kondisi tertentu
State ='1'       #Menunjukkan sedang pada Menu/State  apa saat ini, agar UI yang muncul benar
i = 1               #Menghitung panjangnya '*' yang diisikan pada ui ketika menginput password saat login


# Kode Visual Menu Awal
def menu_kartu():   #Menu Pilih Kartu di Awal
    global Condition #Condition di set untuk mengubah fungsi button untuk menu tertentu, berlaku untuk seluruh condition
    canvas1.create_text(650, 10, text="Pilih kartu", font='courier 20 bold', 
    anchor='n', fill="white",tags='kartu')
    valkartu.set(0)
    Condition= 'kartu'   
    kartu()
    return
def menu_login ():  #Menu Login Setelah masukkan Kartu
    global numlist, Condition 
    canvas2.create_text(240,10,text="Selamat Datang di\n" "ATM Bank Ganesha", font='courier 20 bold', anchor='n', fill="white", tags='password')
    canvas2.create_text(20,190,text="Silahkan Masukkan Nomor Pin Anda:", font='courier 15 bold', anchor='w', fill="white", tags='password')
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags='password')
    numlist.clear()
    Condition='login'
    button_numpad()     #Button untuk menerima input dari keyboard, berlaku untuk semua button_numpad() di kode
    button_samping()    #Button untuk menerima masukan tombol di pinggir layar, berlaku untuk semua button_samping() di kode 
    return
def menu_awal():    #Menu Ketika Memilih Layanan
    canvas2.create_text(240,25,text="Silahkan Pilih Menu\nyang Diinginkan", font='courier 20 bold',justify='center' ,anchor='n', fill="white", tags='menu_awal')
    global Condition
    Condition='menu awal'
    pilihan_menu_awal()
    button_samping()
    return

# Menu Layanan-Layanan yang Tersedia
def ganti_pin():        #Menu Ganti PIN
    global Condition, State , numlist, pinlama
    #State  Menunjukkan dimana posisi nasabah dalam proses layanan tertentu. (1) -> (2) -> (3) -> dst.
    if State  == '1':    #Pin Lama
        #UI
        buatjudul(240,25,"Menu Ganti Pin",'ganti_pin')
        buattext(20,180,"Silahkan Masukkan Pin Lama Anda: ",'ganti_pin')
        buattext(375,280,"Benar-->",'ganti_pin') 
        textkeluar('ganti_pin')

        #Condition diperlukan untuk menyesuaikan fungsi button dengan menu
        Condition = 'ganti pin'
        numlist.clear()     #Clear Input
        button_numpad()
        button_samping()
        return

    if State  == '2':    #Pin Baru
        buatjudul(240,25,"Menu Ganti Pin",'pin_baru')
        buattext(20,180,"Silahkan Masukkan Pin Baru: ",'pin_baru')
        buattext(375,280,"Benar-->",'pin_baru') 
        textkeluar('pin_baru')
        Condition='pin baru'
        numlist.clear()
        button_numpad()
        button_samping()
        return

    if State  == '3':    #Validasi PIN, Berhasil atau Gagal
        numlist.clear()
        Condition='validasi pin'
        buattext(20,180,"Permintaan Anda Sedang Diproses...",'proses')

        if len(pinbaru) == 6:
            def pin_terganti():
                buatjudul(240,25,"Menu Ganti Pin",'validasi_pin')
                canvas2.delete('proses')
                buattext(20,180,"Ganti Pin Berhasil",'validasi_pin')
                nasabah[valkartu.get()-1]['pin'] = pinbaru
                pickle.dump(nasabah, open('nasabah.dat', 'wb'))
                textkeluar('validasi_pin')
                button_numpad()
                button_samping()
            root.after(2000, pin_terganti)

        else:
            def pin_salah():
                canvas2.delete('proses')
                buatjudul(240,25,"Menu Ganti Pin",'validasi_pin')
                buattext(20,180,'Pin Baru Anda Tidak Valid','validasi_pin')
                textkeluar('validasi_pin')
                button_numpad()
                button_samping()
            root.after(2000, pin_salah)
    return 
def transfer():         #Menu Transfer
    global Condition, State , numlist, rekening, nominal, alasan, n
    #State  Menunjukkan dimana posisi nasabah dalam proses layanan tertentu. (1) -> (2) -> (3) -> dst.
    if State  == 'menu gagal':   #Menu Jika Gagal atau dibatalkan karena Suatu Hal
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- Ya ",'gagal')
        buattext(10,280,"<-- Tidak ",'gagal')
        textkeluar('gagal')
        Condition='gagal'
        button_samping()
        return

    if State  == '1':    #Pilih Bank Tujuan
        buatjudul(240,25,'Transfer','Transfer')
        buattext(10,125,"<-- Sesama Bank Ganesha ",'Transfer')
        buattext(10,200,"<-- Bank Lain ",'Transfer')
        buattext(10,280,"<-- Virtual Account ",'Transfer')
        textkeluar('Transfer')
        Condition='transfer'        
        button_samping()
        return

    if State  == '2':    #Masukkan No. Rekening Tujuan
        buattext(10,125,"Anda Memilih untuk Transfer\nke "+bank_tujuan[n-1],'transfer2')
        buattext(10,200,'Masukkan No. Rekening Tujuan: ','transfer2')
        buattext(375,280,'Benar-->','transfer2')
        textkeluar('transfer2')
        numlist.clear()
        Condition='rekening transfer'
        button_numpad()
        return
        
    if State  == '3':    #Masukkan Nominal Transfer
        if no_rek_nasabah.count(rekening) > 0:
            buattext(10,125,"Anda Memilih untuk Transfer\nke "+bank_tujuan[n-1],'transfer3')
            buattext(10,200,'Masukkan nominal: ','transfer3')
            buattext(375,280,'Benar-->','transfer3')
            textkeluar('transfer3')
            numlist.clear()
            Condition='nominal transfer'
            button_numpad()
        else:
            State ='menu gagal'
            alasan='Rekening Tidak Ada'
            numlist.clear()
            transfer()
            # ganti ini jadi menu gagal
            return

    if State  == '4':    #Konfirmasi Rekening Tujuan
        id_tujuan = (no_rek_nasabah.index(rekening))
        canvas2.delete('nominal_isi')
        buattext(10,160,'Nama        : '+nasabah[id_tujuan]['nama'],'transfer4')
        buattext(10,200,'No.Rekening : '+nasabah[id_tujuan]['no-rek'],'transfer4')
        buattext(10,240,'Nominal     : '+nominal,'transfer4')
        buattext(375,280,'Benar-->','transfer4')
        textkeluar('transfer4')
        Condition= 'konfirmasi nominal'
        button_samping()
        return    

    if State =='5':      #Proses Transfer, Antara Berhasil atau Gagal
        id_tujuan = (no_rek_nasabah.index(rekening))
        buattext(140,200,'Transfer Sedang Diproses...','wait')
        if float(nominal) <= float(nasabah[valkartu.get()-1]['tabungan']):
            def transaksiberhasil():
                global Condition,alasan
                canvas2.delete('wait')
                buattext(15,180,'Transaksi Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='berhasil'
                button_samping()    
            root.after(2000,transaksiberhasil)
            nasabah[id_tujuan]['tabungan'] = str(float(nasabah[id_tujuan]['tabungan']) + float(nominal))
            nasabah[valkartu.get()-1]['tabungan'] = str(float(nasabah[valkartu.get()-1]['tabungan']) - float(nominal))
            pickle.dump(nasabah, open('nasabah.dat', 'wb'))
            return
        else:
            def transaksigagal():
                global State ,numlist,alasan
                canvas2.delete('wait')
                State ='menu gagal'
                alasan='Saldo Tidak Cukup'
                numlist.clear()
                canvas2.delete('nominal isi')
                transfer()
            root.after(2000,transaksigagal)
        return

    return
def info_rekening():    #Menu Info Rekening
    global Condition,State 
    if State  == '1':    #Pilih Sumber Dana
        buatjudul(240,10,'Info Rekening','info_rekening')
        buattext(10,125,'Pilih Sumber Dana','info_rekening')
        buattext(10,200,'<-- Tabungan','info_rekening')
        buattext(10,280,'<-- Giro','info_rekening')
        textkeluar('info_rekening')
        Condition='info_rekening'
        button_samping()
        return

    if State  == '2':    #Info Tabungan
        buatjudul(240,10,'Tabungan','tabungan')
        buattext(20,125,'Nama           : '+nasabah[valkartu.get()-1]['nama'],'tabungan')
        buattext(20,175,'No. Rekening   : '+nasabah[valkartu.get()-1]['no-rek'],'tabungan')
        buattext(20,225,'Saldo Tabungan : '+nasabah[valkartu.get()-1]['tabungan'],'tabungan')
        textkeluar('tabungan')
        Condition='tabungan'
        button_samping()
        return

    if State  == '3':    #Info Giro
        buatjudul(240,10,'Giro','giro')
        buattext(20,125,'Nama           : '+nasabah[valkartu.get()-1]['nama'],'giro')
        buattext(20,175,'No. Rekening   : '+nasabah[valkartu.get()-1]['no-rek'],'giro')
        buattext(20,225,'Saldo Giro     : '+nasabah[valkartu.get()-1]['giro'],'giro')
        textkeluar('giro')
        Condition='giro'
        button_samping()
        return
    return
def penarikan_tunai():  #Menu Penarikan Tunai
    global Condition,State ,numlist,rekening,nominal,sumber,penarikan,alasan
    if State  == 'menu gagal':   #Menu Jika Gagal atau dibatalkan karena Suatu Hal
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- ya ",'gagal')
        buattext(10,280,"<-- tidak ",'gagal')
        textkeluar('gagal')
        Condition='penarikan gagal'
        button_samping()
        return

    if State  == '1':    #Pilih Sumber Dana
        buatjudul(240,10,'Penarikan Tunai','penarikan_tunai')
        buattext(10,125,"Pilih Sumber Dana",'penarikan_tunai')
        buattext(10,200,"<-- Tabungan ",'penarikan_tunai')
        buattext(10,280,"<-- Giro ",'penarikan_tunai')
        textkeluar('penarikan_tunai')
        Condition='penarikan tunai'
        button_samping()
        return

    if State  == '2':    #Masukkan Nominal Penarikan
        buatjudul(240,10,'Penarikan Tunai','penarikan')
        buattext(10,125,'Sumber Dana'+ sumber,'penarikan')
        buattext(10,200,'Masukkan Nominal','penarikan')
        buattext(375,280,'Benar-->','penarikan')
        textkeluar('penarikan')
        Condition='penarikan'
        numlist.clear()
        button_numpad()
        button_samping()
        return

    if State == '3':     #Penarikan Diproses, Antara Berhasil atau Gagal
        buattext(140,200,'Penarikan Sedang Diproses...','wait')
        if float(penarikan) <= float(nasabah[valkartu.get()-1][sumber]):
            def transaksiberhasil():
                global Condition,penarikan
                canvas2.delete('wait')
                buattext(15,180,'Penarikan Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='penarikan_berhasil'
                nasabah[valkartu.get()-1][sumber] = str(float(nasabah[valkartu.get()-1][sumber])-float(penarikan))
                pickle.dump(nasabah, open('nasabah.dat', 'wb'))
                button_samping()    
            root.after(2000,transaksiberhasil)
            return
        else:
            def transaksigagal():
                global State ,numlist,alasan
                canvas2.delete('wait')
                State ='menu gagal'
                alasan='Saldo Anda Tidak Cukup'
                numlist.clear()
                canvas2.delete('penarikan_isi')
                penarikan_tunai()
            root.after(2000,transaksigagal)
        return
    return
def pembayaran():       #Menu Pembayaran
    global Condition,tujuan_pembayaran,numlist,alasan
    if State  == 'menu gagal':   #Menu Jika Gagal atau dibatalkan karena Suatu Hal
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- ya ",'gagal')
        buattext(10,280,"<-- tidak ",'gagal')
        textkeluar('gagal')
        Condition='pembayaran gagal'
        button_samping()

    if State  == '1':        #Pilih Keperluan/Instansi Penagih
        buatjudul(240,10,'Pembayaran','pembayaran')
        buattext(10,125,"Pilih Opsi Pembayaran: ",'pembayaran')
        buattext(10,200,"<-- PLN ",'pembayaran')
        buattext(10,280,"<-- Internet ",'pembayaran')
        buattext(10,360,"<-- Pendidikan ",'pembayaran')
        textkeluar('pembayaran')
        Condition='pembayaran'
        button_samping()
        return

    if State  == '2':        #Jika Gagal atau dibatalkan karena Suatu Hal
        buatjudul(240,10,'Pembayaran','pembayaran_')
        buattext(10,125,"Anda Memilihi pembayaran "+tujuan_pembayaran,'pembayaran_')
        buattext(10,175,"Silahkan Masukkan 5 digit \nID pelanggan: ",'pembayaran_')
        buattext(375,280,'Benar-->','pembayaran_')
        textkeluar('pembayaran_')
        Condition='id pembayaran'
        numlist.clear()
        button_samping()
        button_numpad()
        return

    if State  == '3':        #Nominal Tagihan muncul di Layar
        buatjudul(240,10,'Pembayaran','konfirmasi_pembayaran')
        buattext(10,175,"Tagihan yang Perlu Anda Bayar Sebesar\n "+str(dp.tagihan),'konfirmasi_pembayaran')
        buattext(375,280,'Benar-->','konfirmasi_pembayaran')
        textkeluar('konfirmasi_pembayaran')
        Condition='konfirmasi pembayaran'
        numlist.clear()
        button_samping()
        return

    if State  == '4':        #Pembayaran Diproses, antara Berhasil atau Gagal
        buattext(140,200,'Pembayaran Sedang Diproses...','wait')
        if float(dp.tagihan) <= float(nasabah[valkartu.get()-1]['tabungan']):
            def transaksiberhasil():
                global Condition,penarikan
                canvas2.delete('wait')
                buattext(15,180,'Transaksi Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='penarikan_berhasil'
                nasabah[valkartu.get()-1]['tabungan'] = str(float(nasabah[valkartu.get()-1]['tabungan'])-float(dp.tagihan))
                pickle.dump(nasabah, open('nasabah.dat', 'wb'))
                button_samping()    
            root.after(2000,transaksiberhasil)
            return
        else:
            def transaksigagal():
                global State ,numlist,alasan
                canvas2.delete('wait')
                State ='menu gagal'
                alasan='Saldo Anda Tidak Cukup'
                numlist.clear()
                pembayaran()
            root.after(2000,transaksigagal)
        return
    return

# Visual Button dan Handle Input Button ataupun Numpad
def button_samping(): #Button untuk menerima masukan tombol di pinggir layar, berlaku untuk semua button_samping() di kode 
    button1 = Button( root, text = "1",command=lambda:options(1))
    button2 = Button( root, text = "2",command=lambda:options(2))
    button3 = Button( root, text = "3",command=lambda:options(3))
    button4 = Button( root, text = "4",command=lambda:options(4))
    button5 = Button( root, text = "5",command=lambda:options(5))
    button6 = Button( root, text = "6",command=lambda:options(6))
    button7 = Button( root, text = "7",command=lambda:options(7))
    button8 = Button( root, text = "8",command=lambda:options(8))

    # Display Buttons UI
    canvas1.create_window( 80, 210,
                            anchor = "nw",
                            window = button1,
                            height = 50,
                            width  =30)
    canvas1.create_window( 80, 290,
                            anchor = "nw",
                            window = button2,
                            height = 50,
                            width  =30)
    canvas1.create_window( 80, 370, 
                            anchor = "nw",
                            window = button3,
                            height = 50,
                            width  =30)
    canvas1.create_window( 80, 450, 
                            anchor = "nw",
                            window = button4,
                            height = 50,
                            width  =30)
    canvas1.create_window( 690, 210,
                            anchor = "nw",
                            window = button5,
                            height = 50,
                            width  =30)
    canvas1.create_window( 690, 290,
                            anchor = "nw",
                            window = button6,
                            height = 50,
                            width  =30)
    canvas1.create_window( 690, 370, 
                            anchor = "nw",
                            window = button7,
                            height = 50,
                            width  =30)
    canvas1.create_window( 690, 450, 
                            anchor = "nw",
                            window = button8,
                            height = 50,
                            width  =30)

    def options(entry): #Logic Utama Dari Button, Adaptif sesuai Menu yang Ada
        global i,n,State ,sumber,tujuan_pembayaran,idpembayaran

        if Condition == 'belum dicantumkan':
            return
        
        # MENU AWAL
        # Login
        elif Condition == 'login':
            if entry == 8:
                i=1
                canvas2.delete('password')
                canvas2.delete('passwordisi')
                menu_kartu()
            else:
                return

        # Menu Awal
        elif Condition == 'menu awal':
            if entry == 1:
                menuju('menu_awal',ganti_pin())            
            if entry == 2:
                State ='1'
                menuju('menu_awal',transfer()) 
            if entry == 3:
                State ='1'
                menuju('menu_awal',info_rekening()) 
            if entry == 5:
                State ='1'
                menuju('menu_awal',penarikan_tunai())
            if entry == 6:
                State ='1'
                menuju('menu_awal',pembayaran())  
            if entry == 8:
                i=1
                keluar('menu_awal',menu_kartu) 
        
        # GANTI PIN
        elif Condition == 'ganti pin':
            if entry == 7:
                if pinlama == pinnasabah:
                    State  = '2'
                    numlist.clear()
                    canvas2.delete('input_pin_lama')
                    canvas2.delete('ganti_pin')
                    ganti_pin()
                else:
                    State  ='1'
                    canvas2.delete('input_pin_lama')
                    canvas2.delete('ganti_pin')
                    buattext(20,280,'Pin Lama Salah','ganti_pin')
                    numlist.clear()
                    ganti_pin()
            if entry == 8:
                State ='1'
                canvas2.delete('ganti_pin')
                canvas2.delete('input_pin_lama')
                keluar('ganti_pin',menu_awal)
                return   

        # PIN Baru
        elif Condition == 'pin baru':
            if entry == 7:
                State ='3'
                canvas2.delete('pin_baru')
                canvas2.delete('input_pin_baru')
                ganti_pin()
            if entry == 8:
                State ='1'
                canvas2.delete('pin_baru')
                canvas2.delete('input_pin_baru')
                keluar('pin_baru',menu_awal)
                return

        # Validasi PIN       
        elif Condition == 'validasi pin':
            if entry == 8:
                State ='1'
                keluar('validasi_pin',menu_awal)

        # TRANSFER
        # Menu Gagal
        elif Condition == 'gagal':
            if entry == 2:
                i=0
                menuju('gagal',menu_login())            
            if entry == 3:
                State ='1'
                menuju('gagal',transfer())   
            return
        # Menu Transfer
        elif Condition == 'transfer':
            if entry == 8:
                State ='1'
                keluar('Transfer',menu_awal)
            if entry == 1:
                State ='2'
                n=1
                menuju('Transfer',transfer)
                return
            if entry == 2:                
                State ='2'
                n=2
                menuju('Transfer',transfer)
                return
            if entry == 3:
                State ='2'
                n=3
                menuju('Transfer',transfer)
                return
            return
        # Input Rekening Transfer
        elif Condition == 'rekening transfer':
            if entry == 8:
                State ='1'
                keluar('transfer2',menu_awal)
                canvas2.delete('transfer_isi')
            return
        # Konfirmasi Rekening Transfer
        elif Condition == 'konfirmasi transfer':
            if entry == 8:
                State ='1'
                keluar('transfer2',menu_awal)
                canvas2.delete('transfer_isi')
            if entry == 7:
                State ='3'
                menuju('transfer2',transfer)
                canvas2.delete('transfer_isi')
                return
            return
        # Input Nominal Transfer
        elif Condition == 'nominal transfer':
            if entry == 8:
                State ='1'
                keluar('transfer3',menu_awal)
                canvas2.delete('nominal_isi')
            if entry == 7:
                State ='4'
                menuju('transfer3',transfer)
                canvas2.delete('nominal_isi')
                return
            return
        # Konfirmasi Rekening Tujuan
        elif Condition == 'konfirmasi nominal':
            if entry == 8:
                State ='1'
                keluar('transfer4',menu_awal)
                canvas2.delete('nominal_isi')
            if entry == 7:
                State ='5'
                menuju('transfer4',transfer)
                canvas2.delete('nominal_isi')
                return
            return
        # Transfer Berhasil
        elif Condition == 'berhasil':
            if entry == 8:
                i=0
                menuju('berhasil',menu_kartu())
            return
        # INFO REKENING
        # Pilih Sumber Dana
        elif Condition == 'info_rekening':
            if entry == 8:
                State ='1'
                keluar('info_rekening',menu_awal)
            if entry == 2:
                State ='2'
                menuju('info_rekening',info_rekening)
            if entry == 3:
                State ='3'
                menuju('info_rekening',info_rekening)
            return
        # Sumber Dana Tabungan
        elif Condition == 'tabungan':
            if entry == 8:
                State ='1'
                keluar('tabungan',menu_awal)
        # Sumber Dana Giro
        elif Condition == 'giro':
            if entry == 8:
                State ='1'
                keluar('giro',menu_awal)
        # PENARIKAN TUNAI
        # Menu jika Gagal karena suatu Hal
        elif Condition == 'penarikan gagal':
            if entry == 2:
                i=0
                menuju('gagal',menu_login())            
            if entry == 3:
                State ='1'
                menuju('gagal',penarikan_tunai())   
            return
        # Menu Awal Penarikan Tunai, Pilih Sumber Dana dan Nominal
        elif Condition == 'penarikan tunai':
            if entry == 8:
                State ='1'
                keluar('penarikan_tunai',menu_awal)
            if entry == 2:
                State ='2'
                sumber='tabungan'
                menuju('penarikan_tunai',penarikan_tunai)
            if entry == 3:
                State ='2'
                sumber='giro'
                menuju('penarikan_tunai',penarikan_tunai)
            return
        # Menu Awal Penarikan Tunai, Pilih Sumber Dana
        elif Condition == 'penarikan':
            if entry == 8:
                State ='1'
                numlist.clear()
                keluar('penarikan',menu_awal)
                canvas2.delete('penarikan_isi')
            if entry == 7:
                State ='3'
                menuju('penarikan',penarikan_tunai)
                canvas2.delete('penarikan_isi')
                return
        # Penarikan Berhasil
        elif Condition == 'penarikan_berhasil':
            if entry == 8:
                i=0
                menuju('berhasil',menu_kartu())
            return
        # PEMBAYARAN
        # Menu jika Gagal karena suatu Hal
        elif Condition == 'pembayaran gagal':
            if entry == 2:
                i=0
                menuju('gagal',menu_login())            
            if entry == 3:
                State ='1'
                menuju('gagal',pembayaran())   
            return
        # Menu Awal Pembayaran
        elif Condition == 'pembayaran':
            if entry == 8:
                State ='1'
                keluar('pembayaran',menu_awal)
            if entry == 2:
                State ='2'
                tujuan_pembayaran='PLN'
                menuju('pembayaran',pembayaran)
            if entry == 3:
                State ='2'
                tujuan_pembayaran='Internet'
                menuju('pembayaran',pembayaran)
            if entry == 4:
                State ='2'
                tujuan_pembayaran='Pendidikan'
                menuju('pembayaran',pembayaran)
            return
        # Masukkan ID Pembayaran
        elif Condition == 'id pembayaran':
            if entry == 8:
                State ='1'
                numlist.clear()
                keluar('pembayaran_',menu_awal)
                canvas2.delete('pembayaran_id')
            if entry == 7:
                if len(idpembayaran)!=5:
                    buattext(10,250,'Masukkan 5 Digit id','pembayaran_')
                else:
                    dp.tagihan_(int(idpembayaran))
                    State ='3'
                    numlist.clear()
                    menuju('pembayaran_',pembayaran)
                    canvas2.delete('pembayaran_id')
                return
            return
        # Konfirmasi Pembayaran
        elif Condition == 'konfirmasi pembayaran':
            if entry == 8:
                State ='1'
                numlist.clear()
                keluar('konfirmasi_pembayaran',menu_awal)
            if entry == 7:
                State ='4'
                numlist.clear()
                menuju('konfirmasi_pembayaran',pembayaran)
                # kurangin saldo
                return
    return
def button_numpad():  #Button untuk menerima input dari keyboard, berlaku untuk semua button_numpad() di kode
    num1    = Button( root, text = "1",command=lambda:numbers(1))
    num2    = Button( root, text = "4",command=lambda:numbers(4))   #UI Button
    num3    = Button( root, text = "7",command=lambda:numbers(7))
    num4    = Button( root, text = "")
    num5    = Button( root, text = "2",command=lambda:numbers(2))
    num6    = Button( root, text = "5",command=lambda:numbers(5))
    num7    = Button( root, text = "8",command=lambda:numbers(8))
    num8    = Button( root, text = "0",command=lambda:numbers(0))
    num9    = Button( root, text = "3",command=lambda:numbers(3))
    num10   = Button( root, text = "6",command=lambda:numbers(6))
    num11   = Button( root, text = "9",command=lambda:numbers(9))
    num12   = Button( root, text = "")
    num13   = Button( root, text = "Cancel",command=lambda:numbers(99))
    num14   = Button( root, text = "Backspace",command=lambda:numbers(999))
    num15   = Button( root, text = "")
    num16   = Button( root, text = "Accept",command=lambda:numbers(9999))

    # Display Buttons UI
    canvas1.create_window( 830, 310,
                            anchor = "nw",
                            window = num1,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 830, 380,
                            anchor = "nw",
                            window = num2,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 830, 450,
                            anchor = "nw",
                            window = num3,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 830, 520,
                            anchor = "nw",
                            window = num4,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 930, 310,
                            anchor = "nw",
                            window = num5,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 930, 380,
                            anchor = "nw",
                            window = num6,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 930, 450,
                            anchor = "nw",
                            window = num7,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 930, 520,
                            anchor = "nw",
                            window = num8,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 1030, 310,
                            anchor = "nw",
                            window = num9,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 1030, 380,
                            anchor = "nw",
                            window = num10,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 1030, 450,
                            anchor = "nw",
                            window = num11,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 1030, 520,
                            anchor = "nw",
                            window = num12,
                            height = 50,
                            width  = 90)
    canvas1.create_window( 1130, 310,
                            anchor = "nw",
                            window = num13,
                            height = 50,
                            width  = 120)
    canvas1.create_window( 1130, 380,
                            anchor = "nw",
                            window = num14,
                            height = 50,
                            width  = 120)
    canvas1.create_window( 1130, 450,
                            anchor = "nw",
                            window = num15,
                            height = 50,
                            width  = 120)
    canvas1.create_window( 1130, 520,
                            anchor = "nw",
                            window = num16,
                            height = 50,
                            width  = 120)
    
    def numbers(entry):
        global i, numlist, Condition, rekening, nominal, pinlama, pinbaru, pinnasabah, State, penarikan, idpembayaran
        if Condition == 'belum dicantumkan':
            return
        # LOGIN
        elif Condition == 'login':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('passwordisi')
                i=1
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else: #Input Button Angka
                numlist.append(entry)
            if len(numlist)==6:
                strings = [str(num) for num in numlist]
                pin = "".join(strings)
                pinnasabah=nasabah[valkartu.get()-1]['pin']
                
                if pin == pinnasabah:
                    canvas2.delete('password')
                    canvas2.delete('passwordisi')
                    menu_awal()
                    return
                else:
                    canvas2.create_text(20,245,text="Nomor Pin Salah", font='courier 15 bold', anchor='w', fill="#da4545", tags='password')
                    canvas2.delete('passwordisi')
                    menu_login()
                    i=1
                    return
            else:
                bintang=canvas2.create_text(10,220,text="", font='courier 15 bold', anchor='w', fill="white", tags='passwordisi')
                canvas2.insert(bintang,'end'," *"*i)
                i+=1                
                
        #GANTI PIN
        elif Condition == 'ganti pin':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('input_pin_lama')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                pinlama = "".join(strings)
                canvas2.delete('input_pin_lama')
                buattext(20,225,pinlama,'input_pin_lama')
                pinnasabah=nasabah[valkartu.get()-1]['pin']
                if len(pinlama) == 6: 
                    if pinlama == pinnasabah:
                        State  = '2'
                        numlist.clear()
                        canvas2.delete('input_pin_lama')
                        canvas2.delete('ganti_pin')
                        ganti_pin()
                    else:
                        State  ='1'
                        canvas2.delete('input_pin_lama')
                        canvas2.delete('ganti_pin')
                        buattext(20,280,'Pin Lama Salah','ganti_pin')
                        numlist.clear()
                        ganti_pin()
        #PIN Baru          
        elif Condition == 'pin baru':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('input_pin_baru')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                pinbaru = "".join(strings)
                canvas2.delete('input_pin_baru')
                buattext(20,225,pinbaru,'input_pin_baru')
            return 

        # TRANSFER
        elif Condition == 'rekening transfer':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('transfer_isi')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                rekening = "".join(strings)
                # print(numlist)
                if len(numlist)==8:
                    canvas2.delete('transfer_isi')
                    buattext(10,225,rekening,'transfer_isi')
                    Condition=('konfirmasi transfer')
                    return
                else:
                    canvas2.delete('transfer_isi')
                    buattext(10,225,rekening,'transfer_isi')
            return
        #Nominal Transfer
        elif Condition == 'nominal transfer':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('nominal_isi')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                nominal = "".join(strings)
                canvas2.delete('nominal_isi')
                buattext(10,225,nominal,'nominal_isi')
            return
        # Penarikan Tunai
        elif Condition == 'penarikan':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('penarikan_isi')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                penarikan = "".join(strings)
                canvas2.delete('penarikan_isi')
                buattext(10,225,penarikan,'penarikan_isi')
            return
        # Pembayaran
        elif Condition == 'id pembayaran':
            if entry == 99:
                # CANCLE
                numlist.clear()
                canvas2.delete('pembayaran_id')
                return
            elif entry == 999:
                # BACKSPACE
                return
            elif entry == 9999:
                # ENTER
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                idpembayaran = "".join(strings)
                canvas2.delete('pembayaran_id')
                buattext(10,225,idpembayaran,'pembayaran_id')
            return
    return
def kartu():    #UI dan Logic Kartu
        #UI
        kartu1 = Button( root,image=kartu_img[0], highlightthickness = 0, bd = 0,command=lambda:value_kartu(1))
        kartu2 = Button( root,image=kartu_img[1], highlightthickness = 0, bd = 0,command=lambda:value_kartu(2))
        kartu3 = Button( root,image=kartu_img[2], highlightthickness = 0, bd = 0,command=lambda:value_kartu(3))
        kartu4 = Button( root,image=kartu_img[3], highlightthickness = 0, bd = 0,command=lambda:value_kartu(4))
        kartu5 = Button( root,image=kartu_img[4], highlightthickness = 0, bd = 0,command=lambda:value_kartu(5))
        
        canvas1.create_window( 800, 3,
                                anchor = "n",
                                window = kartu1,
                                tags='kartu'
                                )
        canvas1.create_window( 910, 3,
                                anchor = "n",
                                window = kartu2,
                                tags='kartu'
                                )
        canvas1.create_window( 1020,3, 
                                anchor = "n",
                                window = kartu3,
                                tags='kartu'
                                )
        canvas1.create_window( 1130,3, 
                                anchor = "n",
                                window = kartu4,
                                tags='kartu'
                                )
        canvas1.create_window( 1240,3, 
                                anchor = "n",
                                window = kartu5,
                                tags='kartu'
                                )
                                
        def value_kartu(entry):
            valkartu.set(entry)
            if valkartu.get() > 0:
                canvas1.delete('kartu')
                print('id yang terpilih adalah id ', valkartu.get())              
                (menu_login())                
            else:
                return
def pilihan_menu_awal(): #UI Pilihan Menu
    canvas2.create_text(10,125,text="<--Ganti pin", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(10,200,text="<--Transfer", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(10,280,text="<--Info Rekening", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(470,125,text="Penarikan Tunai-->", font='courier 15 bold', anchor='e', fill="white", tags='menu_awal')
    canvas2.create_text(470,200,text="Pembayaran-->", font='courier 15 bold', anchor='e', fill="white", tags='menu_awal')
    textkeluar('menu_awal')
def buatjudul(x,y,teks,tag): #Function Buat UI Judul
    canvas2.create_text(x,y,text=teks, font='courier 20 bold',justify='center' ,anchor='n', fill="white", tags=tag)
def buattext(x,y,teks,tag):  #Function Buat UI Text
    canvas2.create_text(x,y,text=teks, font='courier 15 bold' ,anchor='w', fill="white", tags=tag)
def textkeluar(tag):        #Function Buat UI Text Keluar
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags=tag)
def keluar(menuhapus,tujuan):   #Function Untuk Keluar ke suatu menu
            canvas2.delete(menuhapus)
            tujuan()
def menuju(menuhapus,tujuan):   #Function Untuk Menuju ke suatu menu
    canvas2.delete(menuhapus)
    tujuan()

# INISIASI LOOP
valkartu = IntVar(0) #Mengambil ID Pelanggan berdasarkan Pilihan Kartu
button_samping()
button_numpad()
menu_kartu()

root.mainloop()