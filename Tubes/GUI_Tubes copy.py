from os import stat
import tkinter as tk
from tkinter import *
import Data_Id as id
from Data_Id import *
from Tubes.GUI_Tubes import transfer

# membuat tampilan utama
root=tk.Tk()
root.title('ATM Bank Ganesha')
root.geometry("1360x720")
bg = PhotoImage(file = "Tubes\Assets\ATM_Ganesha_no_Menu.png")
canvas1 = Canvas( root, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
root.resizable('0','0')

# photo kartu
kart1=PhotoImage(file='Tubes\Assets\Kartu-1.png')
kart2=PhotoImage(file='Tubes\Assets\Kartu-2.png')
kart3=PhotoImage(file='Tubes\Assets\Kartu-3.png')
kart4=PhotoImage(file='Tubes\Assets\Kartu-4.png')
kart5=PhotoImage(file='Tubes\Assets\Kartu-5.png')

# membuat tampilan pada layar
mainframe = tk.Frame(canvas1, width=480, height=400,bg='#ADD8E6')
mainframe.pack_propagate(0)
mainframe.pack(anchor=NW, padx=160, pady=110)
bg2 = PhotoImage(file = "Tubes\Assets\layar.png")
canvas2 = Canvas( mainframe, width = 490,height = 410)
canvas2.pack(fill = "both", expand = True)
canvas2.create_image( 0, 0, image = bg2,anchor = "nw")

# inisiasi yang dibutuhkan untuk membantu jalannya program
id_nasabah=[]
numlist=[]
pinbaru=[]
pinlama=[]
state='pinlama'
Condition='belum dicantumkan'
i=1

# code visual menu
def menu_kartu():
    canvas1.create_text(650,10,text="Pilih kartu", font='courier 20 bold', anchor='n', fill="white",tags='kartu')
    valkartu.set(0)
    global Condition
    Condition='kartu'
    kartu()
    return
def menu_login ():
    canvas2.create_text(240,10,text="Selamat Datang di\n" "ATM Bank Ganesha", font='courier 20 bold', anchor='n', fill="white", tags='password')
    canvas2.create_text(20,190,text="Silahkan Masukkan Nomor Pin Anda:", font='courier 15 bold', anchor='w', fill="white", tags='password')
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags='password')
    global numlist
    numlist=[]
    global Condition
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
    canvas2.create_text(240,25,text="Ganti Pin", font='courier 20 bold',justify='center' ,anchor='n', fill="white", tags='ganti_pin')
    canvas2.create_text(20,180,text="pin lama: ", font='courier 15 bold',anchor='w', fill="white", tags='ganti_pin')
    canvas2.create_text(20,220,text="pin baru: ", font='courier 15 bold',anchor='w', fill="white", tags='ganti_pin')
    canvas2.create_text(470,280,text="benar-->", font='courier 15 bold', anchor='e', fill="white", tags='ganti_pin') 
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags='ganti_pin')
    global Condition
    Condition='ganti pin'
    button_numpad()
    button_samping()
    return


# code visual button dan text yang berulang
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
        global i
        if Condition=='belum dicantumkan':
            return
        elif Condition=='login':
            if entry==8:
                i=1
                canvas2.delete('password')
                canvas2.delete('passwordisi')
                menu_kartu()
            else:
                return
        elif Condition=='menu awal':
            if entry==1:
                canvas2.delete('menu_awal')
                ganti_pin()
            if entry==8:
                i=1
                canvas2.delete('menu_awal')
                menu_kartu()
            
            
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
        global i
        global state
        if Condition=='belum dicantumkan':
            return
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
                # tambahin kondisi pin bener sama salah disini
                strings = [str(num) for num in numlist]
                pin = "".join(strings)
                pinnasabah=id.nasabah[valkartu.get()-1]['pin']
                # print('ini number yang di terima',pin)
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
        elif Condition=='ganti pin':
            # if entry==99:
            #     # cancle
            #     pinlama.clear()
            #     pinbaru.clear()
            #     if state=='pinlama':
            #         canvas2.delete('pinlama')
            #     else:  
            #         canvas2.delete('pinbaru')
            #     i=1
            #     return
            # elif entry==999:
            #     # backspace
            #     return
            # elif entry==9999:
            #     # enter
            #     return
            # else:
            #     i=1
            #     if state=='pinlama':
            #         pinlama.append(entry)
            #         if len(pinlama)==6:    
            #             strings = [str(num) for num in pinlama]
            #             pinlama1 = "".join(strings)
            #             pinnasabah=id.nasabah[valkartu.get()-1]['pin']
            #             if pinlama1==pinnasabah:
            #                 state='pinbaru'
            #                 i=1
            #             else:
            #                 canvas2.create_text(20,245,text="Nomor Pin Salah", font='courier 15 bold', anchor='w', fill="#da4545", tags='ganti_pin')
            #                 canvas2.delete('pinlama')
            #         else:
            #             bintang=canvas2.create_text(100,180,text="", font='courier 15 bold', anchor='w', fill="white", tags='pinlama')
            #             canvas2.insert(bintang,'end'," *"*i)
            #             i+=1  
            #     else:
            #         i=1
            #         pinbaru.append(entry)
            #         if len(pinbaru)==6:    
            #             strings = [str(num) for num in pinbaru]
            #             pinbaru1 = "".join(strings)
            #             pinnasabah=id.nasabah[valkartu.get()-1]['pin']
            #             if pinbaru1!=pinnasabah:
            #                 state='pinlama'
            #                 id.nasabah[valkartu.get()-1]['pin']=pinbaru1
            #                 i=1
            #                 menu_awal()
            #                 return
            #         else:
            #             bintang=canvas2.create_text(100,220,text="", font='courier 15 bold', anchor='w', fill="white", tags='pinlama')
            #             canvas2.insert(bintang,'end'," *"*i)
            #             i+=1

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
    canvas2.create_text(470,360,text="Keluar-->", font='courier 15 bold', anchor='e', fill="white", tags='menu_awal')


# inisiasi loop
valkartu=tk.IntVar(0)
button_samping()
button_numpad()
menu_kartu()

root.mainloop()