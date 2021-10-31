# kamus
# inisiasi variabel yang digunakan pada program yaitu sebagai berikut
# ganti_pin:
# pinlama = string yang digunakan sebagai variabel yang mengambil input user yang nantinya akan dicocokan dengan pin nasabah
# pinbaru = string yang digunakan sebagai variabel yang mengambil input user yang nantinya akan menjadi pin baru nasabah
# pinnasabah = string yang berisikan variabel yang mengambil pin nasabah yang terdapat pada data base pada saat itu
# transfer:
# rekening = string yang digunakan sebagai variabel yang mengambil input user berupa rekening tujuan
# nominal = string yang digunakan sebagai variabel yang mengambil input user berupa nominal yang ingin ditransfer kepada rekening tujuan
# penarikan tunai: 
# sumber = string yang digunakan sebagai variabel yang mengambil input user ketika memilih sumber dana yang akan digunakan untuk melakukan penarikan tunai
# penarikan = string yang digunakan sebagai variabel yang mengambil input user berupa nominal yang ingin ditarik dari sumber dana nasabah
# alasan = string yang digunakan untuk menentukan alasan gagalnya sebuah transaksi
# pembayaran:
# tujuan_pembayaran = string yang digunakan sebagai variabel yang mengambil input user berupa tujuan pembayaran seperti Pendidikan,PLN,atau Internet
# idpembayaran = string yang digunakan sebagai variabel yang mengambil input user berupa id yang dituju yang nantinya akan dicocokan dengan id yang ada pada data pembayaran
# alasan = string yang digunakan untuk menentukan alasan gagalnya sebuah transaksi
# button:
# numlist = berupa array yang menerima input dari button dan menyimpan setiap angka yang di input oleh tombol
# Condition = string yang berguna untuk menyatakan kondisi dari ui kepada button sehingga menyatakan fungsi dari button tersebut pada kondisi tertentu
# State = string yang berguna untuk menyatakan kondisi dari button kepada ui untuk mengganti tampilan
# i = integer yang berguna untuk menghitung panjangnya '*' yang diisikan pada ui ketika menginput password saat login
# n = integer yang berguna untuk menandakan bank tujuan pada menu transfer

# import library
import tkinter as tk
from tkinter import *
import Data_Id as id
from Data_Id import *
from Transfer_ import *
import pickle
import Data_Pembayaran as dp

# algoritma
# membuat tampilan utama
root=tk.Tk()
root.title('ATM Bank Ganesha')
root.geometry("1360x720")
bg = PhotoImage(file = ".\Assets\ATM_Ganesha_no_Menu.png")
canvas1 = Canvas( root, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
root.resizable('0','0')

# memasukkan photo kartu untuk UI
kart1=PhotoImage(file='.\Assets\Kartu-1.png')
kart2=PhotoImage(file='.\Assets\Kartu-2.png')
kart3=PhotoImage(file='.\Assets\Kartu-3.png')
kart4=PhotoImage(file='.\Assets\Kartu-4.png')
kart5=PhotoImage(file='.\Assets\Kartu-5.png')

# membuat tampilan pada layar
mainframe = tk.Frame(canvas1, width=480, height=400,bg='#ADD8E6')
mainframe.pack_propagate(0)
mainframe.pack(anchor=NW, padx=160, pady=110)
bg2 = PhotoImage(file = ".\Assets\layar.png")
canvas2 = Canvas( mainframe, width = 490,height = 410)
canvas2.pack(fill = "both", expand = True)
canvas2.create_image( 0, 0, image = bg2,anchor = "nw")

# inisiasi yang dibutuhkan untuk membantu jalannya program
# ganti_pin
pinlama=''
pinbaru=''
pinnasabah=''
# transfer
rekening=''
nominal=''
# penarikan tunai
sumber=''
penarikan=''
alasan=''
# pembayaran
tujuan_pembayaran=''
idpembayaran=''
alasan=''
# button
numlist=[]
Condition='belum dicantumkan'
State='menu1'
i=1
n=0

# code visual menu
def menu_kartu():
    global Condition
    canvas1.create_text(650,10,text="Pilih kartu", font='courier 20 bold', anchor='n', fill="white",tags='kartu')
    valkartu.set(0)
    Condition='kartu'
    kartu()
    return
def menu_login ():
    global numlist,Condition
    canvas2.create_text(240,10,text="Selamat Datang di\n" "ATM Bank Ganesha", font='courier 20 bold', anchor='n', fill="white", tags='password')
    canvas2.create_text(20,190,text="Silahkan Masukkan Nomor Pin Anda:", font='courier 15 bold', anchor='w', fill="white", tags='password')
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags='password')
    numlist.clear()
    Condition='login'
    button_numpad()
    button_samping()
    return
def menu_awal():
    # canvas2.create_text(240,10,text="Selamat Datang di\n" "ATM Bank Ganesha" , font='courier 20 bold', anchor='n', fill="white", tags='Menu awal')
    canvas2.create_text(240,25,text="Silahkan Pilih Menu\nyang Diinginkan", font='courier 20 bold',justify='center' ,anchor='n', fill="white", tags='menu_awal')
    global Condition
    Condition='menu awal'
    pilihan_menu_awal()
    button_samping()
    return

# code visual menu awal
def ganti_pin():
    global Condition,State,numlist,pinlama
    if State=='menu1':
        buatjudul(240,25,"Menu Ganti Pin",'ganti_pin')
        buattext(20,180,"Silahkan Masukkan Pin Lama Anda: ",'ganti_pin')
        buattext(375,280,"Benar-->",'ganti_pin') 
        textkeluar('ganti_pin')
        Condition='ganti pin'
        numlist.clear()
        button_numpad()
        button_samping()
        return
    if State=='menu2':
        # benar mulai nanya yang baru
        buatjudul(240,25,"Menu Ganti Pin",'pin_baru')
        buattext(20,180,"Silahkan Masukkan Pin Baru: ",'pin_baru')
        buattext(375,280,"Benar-->",'pin_baru') 
        textkeluar('pin_baru')
        Condition='pin baru'
        numlist.clear()
        button_numpad()
        button_samping()
        return
    if State =='menu3':
        numlist.clear()
        Condition='validasi pin'
        buattext(20,180,"Permintaan Anda Sedang Diproses...",'proses')
        if len(pinbaru) == 6:
            def pin_terganti():
                buatjudul(240,25,"Menu Ganti Pin",'validasi_pin')
                canvas2.delete('proses')
                buattext(20,180,"Ganti Pin Berhasil",'validasi_pin')
                id.nasabah[valkartu.get()-1]['pin'] = pinbaru
                pickle.dump(id.nasabah, open('nasabah.dat', 'wb'))
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
def transfer():
    global Condition,State,numlist,rekening,nominal,alasan,n
    if State== 'menu gagal':
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- ya ",'gagal')
        buattext(10,280,"<-- tidak ",'gagal')
        textkeluar('gagal')
        Condition='gagal'
        button_samping()
        return
    if State=='menu1':
        buatjudul(240,25,'Transfer','Transfer')
        buattext(10,125,"<-- Sesama Bank Ganesha ",'Transfer')
        buattext(10,200,"<-- Bank Lain ",'Transfer')
        buattext(10,280,"<-- Virtual Account ",'Transfer')
        textkeluar('Transfer')
        Condition='transfer'        
        button_samping()
        return
    if State=='menu2':
        buattext(10,125,"Anda Memilih untuk Transfer\nke "+bank_tujuan[n-1],'transfer2')
        buattext(10,200,'Masukkan No. Rekening Tujuan: ','transfer2')
        buattext(375,280,'Benar-->','transfer2')
        textkeluar('transfer2')
        numlist.clear()
        Condition='rekening transfer'
        button_numpad()
        return
    if State=='menu3':
        if no_rek_nasabah.count(rekening) > 0:
            buattext(10,125,"Anda Memilih untuk Transfer\nke "+bank_tujuan[n-1],'transfer3')
            buattext(10,200,'Masukkan nominal: ','transfer3')
            buattext(375,280,'Benar-->','transfer3')
            textkeluar('transfer3')
            numlist.clear()
            Condition='nominal transfer'
            button_numpad()
        else:
            State='menu gagal'
            alasan='Rekening Tidak Ada'
            numlist.clear()
            transfer()
            # ganti ini jadi menu gagal
            return
    if State=='menu4':
        id_tujuan = (no_rek_nasabah.index(rekening))
        canvas2.delete('nominal_isi')
        buattext(10,160,'Nama        : '+id.nasabah[id_tujuan]['nama'],'transfer4')
        buattext(10,200,'No.Rekening : '+id.nasabah[id_tujuan]['no-rek'],'transfer4')
        buattext(10,240,'Nominal     : '+nominal,'transfer4')
        buattext(375,280,'Benar-->','transfer4')
        textkeluar('transfer4')
        Condition= 'konfirmasi nominal'
        button_samping()
        return    
    if State=='menu5':
        id_tujuan = (no_rek_nasabah.index(rekening))
        buattext(140,200,'Transfer Sedang Diproses...','wait')
        if float(nominal) <= float(id.nasabah[valkartu.get()-1]['tabungan']):
            def transaksiberhasil():
                global Condition,alasan
                canvas2.delete('wait')
                buattext(15,180,'Transaksi Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='berhasil'
                button_samping()    
            root.after(2000,transaksiberhasil)
            id.nasabah[id_tujuan]['tabungan'] = str(float(id.nasabah[id_tujuan]['tabungan'])+float(nominal))
            id.nasabah[valkartu.get()-1]['tabungan'] = str(float(id.nasabah[valkartu.get()-1]['tabungan'])-float(nominal))
            pickle.dump(id.nasabah, open('nasabah.dat', 'wb'))
            return
        else:
            def transaksigagal():
                global State,numlist,alasan
                canvas2.delete('wait')
                State='menu gagal'
                alasan='Saldo Tidak Cukup'
                numlist.clear()
                canvas2.delete('nominal isi')
                transfer()
            root.after(2000,transaksigagal)
        return

    return
def info_rekening():
    global Condition,State
    if State=='menu1':
        buatjudul(240,10,'Info Rekening','info_rekening')
        buattext(10,125,'Pilih Sumber Dana','info_rekening')
        buattext(10,200,'<-- Tabungan','info_rekening')
        buattext(10,280,'<-- Giro','info_rekening')
        textkeluar('info_rekening')
        Condition='info_rekening'
        button_samping()
        return
    if State=='menu2':
        # menu tabungan
        buatjudul(240,10,'Tabungan','tabungan')
        buattext(20,125,'Nama           : '+id.nasabah[valkartu.get()-1]['nama'],'tabungan')
        buattext(20,175,'No. Rekening   : '+id.nasabah[valkartu.get()-1]['no-rek'],'tabungan')
        buattext(20,225,'Saldo Tabungan : '+id.nasabah[valkartu.get()-1]['tabungan'],'tabungan')
        textkeluar('tabungan')
        Condition='tabungan'
        button_samping()
        return
    if State=='menu3':
        # menu giro
        buatjudul(240,10,'Giro','giro')
        buattext(20,125,'Nama           : '+id.nasabah[valkartu.get()-1]['nama'],'giro')
        buattext(20,175,'No. Rekening   : '+id.nasabah[valkartu.get()-1]['no-rek'],'giro')
        buattext(20,225,'Saldo Giro     : '+id.nasabah[valkartu.get()-1]['giro'],'giro')
        textkeluar('giro')
        Condition='giro'
        button_samping()
        return
    return
def penarikan_tunai():
    global Condition,State,numlist,rekening,nominal,sumber,penarikan,alasan
    if State== 'menu gagal':
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- ya ",'gagal')
        buattext(10,280,"<-- tidak ",'gagal')
        textkeluar('gagal')
        Condition='penarikan gagal'
        button_samping()
        return
    if State== 'menu1':
        buatjudul(240,10,'Penarikan Tunai','penarikan_tunai')
        buattext(10,125,"Pilih Sumber Dana",'penarikan_tunai')
        buattext(10,200,"<-- Tabungan ",'penarikan_tunai')
        buattext(10,280,"<-- Giro ",'penarikan_tunai')
        textkeluar('penarikan_tunai')
        Condition='penarikan tunai'
        button_samping()
        return
    if State== 'menu2':
        buatjudul(240,10,'Penarikan Tunai','penarikan')
        buattext(10,125,'Sumber Dana'+sumber,'penarikan')
        buattext(10,200,'Masukkan Nominal','penarikan')
        buattext(375,280,'Benar-->','penarikan')
        textkeluar('penarikan')
        Condition='penarikan'
        numlist.clear()
        button_numpad()
        button_samping()
        return
    if State== 'menu3':
        # buat 2 kondisi kalo saldo ga cukup masuk ke gagal sama kalo berhasil kurangin tabungan
        buattext(140,200,'Transfer Sedang Diproses...','wait')
        if float(penarikan) <= float(id.nasabah[valkartu.get()-1][sumber]):
            def transaksiberhasil():
                global Condition,penarikan
                canvas2.delete('wait')
                buattext(15,180,'Transaksi Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='penarikan_berhasil'
                id.nasabah[valkartu.get()-1][sumber] = str(float(id.nasabah[valkartu.get()-1][sumber])-float(penarikan))
                pickle.dump(id.nasabah, open('nasabah.dat', 'wb'))
                button_samping()    
            root.after(2000,transaksiberhasil)
            return
        else:
            def transaksigagal():
                global State,numlist,alasan
                canvas2.delete('wait')
                State='menu gagal'
                alasan='Saldo Anda Tidak Cukup'
                numlist.clear()
                canvas2.delete('penarikan_isi')
                penarikan_tunai()
            root.after(2000,transaksigagal)
        return
    return
def pembayaran():
    global Condition,tujuan_pembayaran,numlist,alasan
    if State== 'menu gagal':
        buattext(10,125,"Batalkan transfer? ",'gagal')
        buattext(10,150,alasan,'gagal')
        buattext(10,200,"<-- ya ",'gagal')
        buattext(10,280,"<-- tidak ",'gagal')
        textkeluar('gagal')
        Condition='pembayaran gagal'
        button_samping()
    if State=='menu1':
        buatjudul(240,10,'Pembayaran','pembayaran')
        buattext(10,125,"Pilih Opsi Pembayaran: ",'pembayaran')
        buattext(10,200,"<-- PLN ",'pembayaran')
        buattext(10,280,"<-- Internet ",'pembayaran')
        buattext(10,360,"<-- Pendidikan ",'pembayaran')
        textkeluar('pembayaran')
        Condition='pembayaran'
        button_samping()
        return
    if State=='menu2':
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
    if State=='menu3':
        # sebutin nominal yang perlu di bayar terus tanyain apakah bener
        buatjudul(240,10,'Pembayaran','konfirmasi_pembayaran')
        buattext(10,175,"Tagihan yang Perlu Anda Bayar Sebesar\n "+str(dp.tagihan),'konfirmasi_pembayaran')
        buattext(375,280,'Benar-->','konfirmasi_pembayaran')
        textkeluar('konfirmasi_pembayaran')
        Condition='konfirmasi pembayaran'
        numlist.clear()
        button_samping()
        return
    if State=='menu4':
        buattext(140,200,'Transfer Sedang Diproses...','wait')
        if float(dp.tagihan) <= float(id.nasabah[valkartu.get()-1]['tabungan']):
            def transaksiberhasil():
                global Condition,penarikan
                canvas2.delete('wait')
                buattext(15,180,'Transaksi Berhasil','berhasil')
                buattext(15,220,'Silahkan ambil kartu Anda kembali','berhasil')
                textkeluar('berhasil')
                Condition='penarikan_berhasil'
                id.nasabah[valkartu.get()-1]['tabungan'] = str(float(id.nasabah[valkartu.get()-1]['tabungan'])-float(dp.tagihan))
                pickle.dump(id.nasabah, open('nasabah.dat', 'wb'))
                button_samping()    
            root.after(2000,transaksiberhasil)
            return
        else:
            def transaksigagal():
                global State,numlist,alasan
                canvas2.delete('wait')
                State='menu gagal'
                alasan='Saldo Anda Tidak Cukup'
                numlist.clear()
                pembayaran()
            root.after(2000,transaksigagal)
        return
    return



# code visual button dan text yang berulang untuk memudahkan penulisan command
def button_samping():
    button1 = Button( root, text = "1",command=lambda:options(1))
    button2 = Button( root, text = "2",command=lambda:options(2))
    button3 = Button( root, text = "3",command=lambda:options(3))
    button4 = Button( root, text = "4",command=lambda:options(4))
    button5 = Button( root, text = "5",command=lambda:options(5))
    button6 = Button( root, text = "6",command=lambda:options(6))
    button7 = Button( root, text = "7",command=lambda:options(7))
    button8 = Button( root, text = "8",command=lambda:options(8))

    # Display Buttons
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

    def options(entry):
        global i,n,State,sumber,tujuan_pembayaran,idpembayaran

        if Condition=='belum dicantumkan':
            return
        # login
        elif Condition=='login':
            if entry==8:
                i=1
                canvas2.delete('password')
                canvas2.delete('passwordisi')
                menu_kartu()
            else:
                return
        # menu awal
        elif Condition=='menu awal':
            if entry==1:
                menuju('menu_awal',ganti_pin())            
            if entry==2:
                State='menu1'
                menuju('menu_awal',transfer()) 
            if entry==3:
                State='menu1'
                menuju('menu_awal',info_rekening()) 
            if entry==5:
                State='menu1'
                menuju('menu_awal',penarikan_tunai())
            if entry==6:
                State='menu1'
                menuju('menu_awal',pembayaran())  
            if entry==8:
                i=1
                keluar('menu_awal',menu_kartu)    
        # ganti pin
        elif Condition=='ganti pin':
            if entry==7:
                if pinlama == pinnasabah:
                    State = 'menu2'
                    numlist.clear()
                    canvas2.delete('input_pin_lama')
                    canvas2.delete('ganti_pin')
                    ganti_pin()
                else:
                    State ='menu1'
                    canvas2.delete('input_pin_lama')
                    canvas2.delete('ganti_pin')
                    buattext(20,280,'Pin Lama Salah','ganti_pin')
                    numlist.clear()
                    ganti_pin()
            if entry==8:
                State='menu1'
                canvas2.delete('ganti_pin')
                canvas2.delete('input_pin_lama')
                keluar('ganti_pin',menu_awal)
                return       
        elif Condition == 'pin baru':
            if entry==7:
                State='menu3'
                canvas2.delete('pin_baru')
                canvas2.delete('input_pin_baru')
                ganti_pin()
            if entry==8:
                State='menu1'
                canvas2.delete('pin_baru')
                canvas2.delete('input_pin_baru')
                keluar('pin_baru',menu_awal)
                return
        elif Condition == 'validasi pin':
            if entry==8:
                State='menu1'
                keluar('validasi_pin',menu_awal)
        # transfer
        elif Condition=='gagal':
            if entry==2:
                i=0
                menuju('gagal',menu_login())            
            if entry==3:
                State='menu1'
                menuju('gagal',transfer())   
            return
        elif Condition=='transfer':
            if entry==8:
                State='menu1'
                keluar('Transfer',menu_awal)
            if entry==1:
                State='menu2'
                n=1
                menuju('Transfer',transfer)
                return
            if entry==2:                
                State='menu2'
                n=2
                menuju('Transfer',transfer)
                return
            if entry==3:
                State='menu2'
                n=3
                menuju('Transfer',transfer)
                return

            return
        elif Condition=='rekening transfer':
            if entry==8:
                State='menu1'
                keluar('transfer2',menu_awal)
                canvas2.delete('transfer_isi')
            return
        elif Condition=='konfirmasi transfer':
            if entry==8:
                State='menu1'
                keluar('transfer2',menu_awal)
                canvas2.delete('transfer_isi')

            if entry==7:
                State='menu3'
                menuju('transfer2',transfer)
                canvas2.delete('transfer_isi')
                return

            return
        elif Condition=='nominal transfer':
            if entry==8:
                State='menu1'
                keluar('transfer3',menu_awal)
                canvas2.delete('nominal_isi')
            if entry==7:
                State='menu4'
                menuju('transfer3',transfer)
                canvas2.delete('nominal_isi')
                return
            return
        elif Condition=='konfirmasi nominal':
            if entry==8:
                State='menu1'
                keluar('transfer4',menu_awal)
                canvas2.delete('nominal_isi')
            if entry==7:
                State='menu5'
                menuju('transfer4',transfer)
                canvas2.delete('nominal_isi')
                return
            return
        elif Condition=='berhasil':
            if entry==8:
                i=0
                menuju('berhasil',menu_kartu())
            return
        # info rekening
        elif Condition=='info_rekening':
            if entry==8:
                State='menu1'
                keluar('info_rekening',menu_awal)
            if entry==2:
                State='menu2'
                menuju('info_rekening',info_rekening)
            if entry==3:
                State='menu3'
                menuju('info_rekening',info_rekening)

            return
        elif Condition=='tabungan':
            if entry==8:
                State='menu1'
                keluar('tabungan',menu_awal)
        elif Condition=='giro':
            if entry==8:
                State='menu1'
                keluar('giro',menu_awal)
        # penarikan tunai
        elif Condition=='penarikan gagal':
            if entry==2:
                i=0
                menuju('gagal',menu_login())            
            if entry==3:
                State='menu1'
                menuju('gagal',penarikan_tunai())   
            return
        elif Condition=='penarikan tunai':
            if entry==8:
                State='menu1'
                keluar('penarikan_tunai',menu_awal)
            if entry==2:
                State='menu2'
                sumber='tabungan'
                menuju('penarikan_tunai',penarikan_tunai)
            if entry==3:
                State='menu2'
                sumber='giro'
                menuju('penarikan_tunai',penarikan_tunai)
            
            return
        elif Condition=='penarikan':
            if entry==8:
                State='menu1'
                numlist.clear()
                keluar('penarikan',menu_awal)
                canvas2.delete('penarikan_isi')
            if entry==7:
                State='menu3'
                menuju('penarikan',penarikan_tunai)
                canvas2.delete('penarikan_isi')
                return
        elif Condition=='penarikan_berhasil':
            if entry==8:
                i=0
                menuju('berhasil',menu_kartu())
            return
        # pembayaran
        elif Condition=='pembayaran gagal':
            if entry==2:
                i=0
                menuju('gagal',menu_login())            
            if entry==3:
                State='menu1'
                menuju('gagal',pembayaran())   
            return
        elif Condition=='pembayaran':
            if entry==8:
                State='menu1'
                keluar('pembayaran',menu_awal)
            if entry==2:
                State='menu2'
                tujuan_pembayaran='PLN'
                menuju('pembayaran',pembayaran)
            if entry==3:
                State='menu2'
                tujuan_pembayaran='Internet'
                menuju('pembayaran',pembayaran)
            if entry==4:
                State='menu2'
                tujuan_pembayaran='Pendidikan'
                menuju('pembayaran',pembayaran)
            
            return
        elif Condition=='id pembayaran':
            if entry==8:
                State='menu1'
                numlist.clear()
                keluar('pembayaran_',menu_awal)
                canvas2.delete('pembayaran_id')
            if entry==7:
                if len(idpembayaran)!=5:
                    buattext(10,250,'Masukkan 5 Digit id','pembayaran_')
                else:
                    dp.tagihan_(int(idpembayaran))
                    State='menu3'
                    numlist.clear()
                    menuju('pembayaran_',pembayaran)
                    canvas2.delete('pembayaran_id')
                return
            return
        elif Condition=='konfirmasi pembayaran':
            if entry==8:
                State='menu1'
                numlist.clear()
                keluar('konfirmasi_pembayaran',menu_awal)
            if entry==7:
                State='menu4'
                numlist.clear()
                menuju('konfirmasi_pembayaran',pembayaran)
                # kurangin saldo
                return
    
    return
def button_numpad():
    num1 = Button( root, text = "1",command=lambda:numbers(1))
    num2 = Button( root, text = "4",command=lambda:numbers(4))
    num3 = Button( root, text = "7",command=lambda:numbers(7))
    num4 = Button( root, text = "")
    num5 = Button( root, text = "2",command=lambda:numbers(2))
    num6 = Button( root, text = "5",command=lambda:numbers(5))
    num7 = Button( root, text = "8",command=lambda:numbers(8))
    num8 = Button( root, text = "0",command=lambda:numbers(0))
    num9 = Button( root, text = "3",command=lambda:numbers(3))
    num10 = Button( root, text = "6",command=lambda:numbers(6))
    num11 = Button( root, text = "9",command=lambda:numbers(9))
    num12 = Button( root, text = "")
    num13 = Button( root, text = "cancel",command=lambda:numbers(99))
    num14 = Button( root, text = "backspace",command=lambda:numbers(999))
    num15 = Button( root, text = "")
    num16 = Button( root, text = "accept",command=lambda:numbers(9999))

    # Display Buttons
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
        global i,numlist,Condition,rekening,nominal,pinlama, pinbaru, pinnasabah, State,penarikan,idpembayaran
        if Condition=='belum dicantumkan':
            return
        # login
        elif Condition=='login':
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('passwordisi')
                i=1
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
            if len(numlist)==6:
                
                strings = [str(num) for num in numlist]
                pin = "".join(strings)
                pinnasabah=id.nasabah[valkartu.get()-1]['pin']
                
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
                # print(numlist)
        # ganti pin
        elif Condition=='ganti pin':
            if entry==99:
                # cancel
                numlist.clear()
                canvas2.delete('input_pin_lama')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                pinlama = "".join(strings)
                canvas2.delete('input_pin_lama')
                buattext(20,225,pinlama,'input_pin_lama')
                pinnasabah=id.nasabah[valkartu.get()-1]['pin']
                if len(pinlama) == 6: 
                    if pinlama == pinnasabah:
                        State = 'menu2'
                        numlist.clear()
                        canvas2.delete('input_pin_lama')
                        canvas2.delete('ganti_pin')
                        ganti_pin()
                    else:
                        State ='menu1'
                        canvas2.delete('input_pin_lama')
                        canvas2.delete('ganti_pin')
                        buattext(20,280,'Pin Lama Salah','ganti_pin')
                        numlist.clear()
                        ganti_pin()
        elif Condition=='pin baru':
            
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('input_pin_baru')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                pinbaru = "".join(strings)
                canvas2.delete('input_pin_baru')
                buattext(20,225,pinbaru,'input_pin_baru')


            return    
        # transfer
        elif Condition=='rekening transfer':
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('transfer_isi')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
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
        elif Condition=='nominal transfer':
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('nominal_isi')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                nominal = "".join(strings)
                canvas2.delete('nominal_isi')
                buattext(10,225,nominal,'nominal_isi')
            return
        # penarikan tunai
        elif Condition=='penarikan':
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('penarikan_isi')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                penarikan = "".join(strings)
                canvas2.delete('penarikan_isi')
                buattext(10,225,penarikan,'penarikan_isi')
            return
        # pembayaran
        elif Condition=='id pembayaran':
            if entry==99:
                # cancle
                numlist.clear()
                canvas2.delete('pembayaran_id')
                return
            elif entry==999:
                # backspace
                return
            elif entry==9999:
                # enter
                return
            else:
                numlist.append(entry)
                strings = [str(num) for num in numlist]
                idpembayaran = "".join(strings)
                canvas2.delete('pembayaran_id')
                buattext(10,225,idpembayaran,'pembayaran_id')
            return
    return
def kartu():
        kartu1 = Button( root,image=kart1,highlightthickness = 0, bd = 0,command=lambda:value_kartu(1))
        kartu2 = Button( root,image=kart2,highlightthickness = 0, bd = 0,command=lambda:value_kartu(2))
        kartu3 = Button( root,image=kart3,highlightthickness = 0, bd = 0,command=lambda:value_kartu(3))
        kartu4 = Button( root,image=kart4,highlightthickness = 0, bd = 0,command=lambda:value_kartu(4))
        kartu5 = Button( root,image=kart5,highlightthickness = 0, bd = 0,command=lambda:value_kartu(5))
        
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
            if valkartu.get()>0:
                canvas1.delete('kartu')
                print('id yang terpilih adalah id ',valkartu.get())              
                (menu_login())                
            else:
                return
def pilihan_menu_awal():
    canvas2.create_text(10,125,text="<--Ganti pin", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(10,200,text="<--Transfer", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(10,280,text="<--Info Rekening", font='courier 15 bold', anchor='w', fill="white", tags='menu_awal')
    canvas2.create_text(470,125,text="Penarikan Tunai-->", font='courier 15 bold', anchor='e', fill="white", tags='menu_awal')
    canvas2.create_text(470,200,text="Pembayaran-->", font='courier 15 bold', anchor='e', fill="white", tags='menu_awal')
    textkeluar('menu_awal')
def buatjudul(x,y,teks,tag):
    canvas2.create_text(x,y,text=teks, font='courier 20 bold',justify='center' ,anchor='n', fill="white", tags=tag)
def buattext(x,y,teks,tag):
    canvas2.create_text(x,y,text=teks, font='courier 15 bold' ,anchor='w', fill="white", tags=tag)
def textkeluar(tag):
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags=tag)
def keluar(menuhapus,tujuan):
            canvas2.delete(menuhapus)
            tujuan()
def menuju(menuhapus,tujuan):
    canvas2.delete(menuhapus)
    tujuan()

# inisiasi loop
valkartu=tk.IntVar(0)
button_samping()
button_numpad()
menu_kartu()

root.mainloop()