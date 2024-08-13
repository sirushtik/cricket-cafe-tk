from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time
from Cafe import Cafe

class Cricket() :
    def __init__(self,root) :
        def iExit():
            iExit = tkinter.messagebox.askyesno("Cricket Match Ticket Booking System","Confirm if you want to quit")
            if iExit > 0:
                root.destroy()
                return

        #=================================================================Ticket=====================================================================


        self.root = root
        self.root.title = ("Cricket Match Ticket Booking System")
        self.root.geometry("1350x600+0+0")
        self.root.configure(background = 'lightblue')

        MainFrame = Frame(self.root , bd = 10, width = 1340, height = 700, bg = 'lightblue', relief = RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame , bd = 10, width = 1340, height = 100, bg = 'lightblue', relief = RIDGE)
        TopFrame1.grid()

        TopFrame2 = Frame(MainFrame, bd = 10, width = 1300, height = 500, bg = 'lightblue', relief = RIDGE)
        TopFrame2.grid()

        f1 = Frame(TopFrame2, width = 890, height = 600, bd = 5, relief = RIDGE)
        f1.grid(row = 1, column = 0)

        f2 = Frame(TopFrame2, width = 400, height = 600, pady = 2, bd = 5, relief = RIDGE)
        f2.grid(row = 1, column = 1)

        frametopRight = Frame(f2, width = 404, height = 420, bd = 5, relief = RIDGE) #Ticketing Receipt
        frametopRight.pack(side = TOP)

        frameBottomRight = Frame(f2, width = 408, height = 100, bd = 5, pady = 15, relief = RIDGE) #Buttons pady=10
        frameBottomRight.pack(side = BOTTOM)

        f1a = Frame(f1, width = 900, height = 330, bd=5, relief = RIDGE)
        f1a.pack(side = TOP)
        f2a = Frame(f1, width = 900, height = 320, bd = 5, relief = RIDGE)
        f2a.pack(side = BOTTOM)

        topLeft1 = Frame(f1a, width = 300, height = 200, bd = 5, padx = 25, pady = 1, relief = RIDGE)
        topLeft1.pack(side = LEFT)
        topLeft2 = Frame(f1a, width = 300, height = 200, bd = 5, padx = 25, pady = 1, relief = RIDGE)
        topLeft2.pack(side = LEFT)
        topLeft3 = Frame(f1a, width = 300, height = 200, bd = 5, padx = 25, pady = 1, relief = RIDGE)
        topLeft3.pack(side = LEFT)
        topLeft4 = Frame(f2a, width = 350, height = 200, bd = 5, padx = 5, pady = 12, relief = RIDGE) 
        topLeft4.pack(side = LEFT)
        topLeft5 = Frame(f2a, width = 350, height = 200, bd = 5, padx=5, pady = 12, relief = RIDGE) 
        topLeft5.pack(side = LEFT)
        topLeft6 = Frame(f2a, width = 350, height = 200, bd = 5, padx=5, pady = 12, relief = RIDGE) 
        topLeft6.pack(side = LEFT)

#======================================================================================================================================

        lblTitle = Label(TopFrame1, font = ('arial',40,'bold'), text = "Cricket Match Ticket Booking System", bd = 5, width = 41,padx = 4, justify = 'center')
        lblTitle.grid(row = 0,column = 0)

#======================================================================================================================================

        Date = StringVar()
        Time = StringVar()
        Block = StringVar()
        Num_Ticket = StringVar()
        State_Tax = IntVar()
        Sub_Total = IntVar()
        Total_Price = IntVar()
        Ref_No = StringVar()

        text_Input = StringVar()
        global operator
        operator = ""

        Block.set("")
        Num_Ticket.set("")
        State_Tax.set("") 
        Sub_Total.set("")
        Total_Price.set("")
        Ref_No.set("")

        varA1 = IntVar()
        varA2 = IntVar()
        varA3 = IntVar()
        varB1 = IntVar()
        varB2 = IntVar()
        varB3 = IntVar()
        varC1 = IntVar()
        varC2 = IntVar()
        varC3 = IntVar()
        varD1 = IntVar()
        varD2 = IntVar()
        varD3 = IntVar()
        varE1 = IntVar()
        varE2 = IntVar()
        varE3 = IntVar()
        varF1 = IntVar()
        varF2 = IntVar()
        varF3 = IntVar()

        A1 = IntVar()
        A2 = IntVar()
        A3 = IntVar()
        B1 = IntVar()
        B2 = IntVar()
        B3 = IntVar()
        C1 = IntVar()
        C2 = IntVar()
        C3 = IntVar()
        D1 = IntVar()
        D2 = IntVar()
        D3 = IntVar()
        E1 = IntVar()
        E2 = IntVar()
        E3 = IntVar()
        F1 = IntVar()
        F2 = IntVar()
        F3 = IntVar()

        Tax = StringVar()
        SubTotal = StringVar()
        Total = StringVar()

        varA1.set("0")
        varA2.set("0")
        varA3.set("0")
        varB1.set("0")
        varB2.set("0")
        varB3.set("0")
        varC1.set("0")
        varC2.set("0")
        varC3.set("0")
        varD1.set("0")
        varD2.set("0")
        varD3.set("0")
        varE1.set("0")
        varE2.set("0")
        varE3.set("0")
        varF1.set("0")
        varF2.set("0")
        varF3.set("0")


        A1.set("")
        A2.set("")
        A3.set("")
        B1.set("")
        B2.set("")
        B3.set("")
        C1.set("")
        C2.set("")
        C3.set("")
        D1.set("")
        D2.set("")
        D3.set("")
        E1.set("")
        E2.set("")
        E3.set("")
        F1.set("")
        F2.set("")
        F3.set("")

#==========================================================Booking Code Continuation==========================================
                
        def Reset():
            varA1.set("0")
            varA2.set("0")
            varA3.set("0")
            varB1.set("0")
            varB2.set("0")
            varB3.set("0")
            varC1.set("0")
            varC2.set("0")
            varC3.set("0")
            varD1.set("0")
            varD2.set("0")
            varD3.set("0")
            varE1.set("0")
            varE2.set("0")
            varE3.set("0")
            varF1.set("0")
            varF2.set("0")
            varF3.set("0")

            A1.set("")
            A2.set("")
            A3.set("")
            B1.set("")
            B2.set("")
            B3.set("")
            C1.set("")
            C2.set("")
            C3.set("")
            D1.set("")
            D2.set("")
            D3.set("")
            E1.set("")
            E2.set("")
            E3.set("")
            F1.set("")
            F2.set("")
            F3.set("")
            Block.set("")
            Num_Ticket.set("")
            State_Tax.set("") 
            Sub_Total.set("")
            Total_Price.set("")
            Ref_No.set("")
            chkbutton_A1_Value()
            chkbutton_A2_Value()
            chkbutton_A3_Value()
            chkbutton_B1_Value()
            chkbutton_B2_Value()
            chkbutton_B3_Value()
            chkbutton_C1_Value()
            chkbutton_C2_Value()
            chkbutton_C3_Value()
            chkbutton_D1_Value()
            chkbutton_D2_Value()
            chkbutton_D3_Value()
            chkbutton_E1_Value()
            chkbutton_E2_Value()
            chkbutton_E3_Value()
            chkbutton_F1_Value()
            chkbutton_F2_Value()
            chkbutton_F3_Value()


        def chkbutton_A1_Value() :
            if varA1.get() == 1 :
                A1.set("")
                entA1.configure(state = NORMAL)
            elif varA1.get() == 0 :
                A1.set("")
                entA1.configure(state = DISABLED)

        def chkbutton_B1_Value() :
            if varB1.get() == 1 :
                B1.set("")
                entB1.configure(state = NORMAL)
            elif varB1.get() == 0 :
                B1.set("")
                entB1.configure(state = DISABLED)

        def chkbutton_C1_Value() :
            if varC1.get() == 1 :
                C1.set("")
                entC1.configure(state = NORMAL)
            elif varC1.get() == 0 :
                C1.set("")
                entC1.configure(state = DISABLED)

        def chkbutton_A2_Value() :
            if varA2.get() == 1 :
                A2.set("")
                entA2.configure(state = NORMAL)
            elif varA2.get() == 0 :
                A2.set("")
                entA2.configure(state = DISABLED)

        def chkbutton_B2_Value() :
            if varB2.get() == 1 :
                B2.set("")
                entB2.configure(state = NORMAL)
            elif varB2.get() == 0 :
                B2.set("")
                entB2.configure(state = DISABLED)

        def chkbutton_C2_Value() :
            if varC2.get() == 1 :
                C2.set("")
                entC2.configure(state = NORMAL)
            elif varC2.get() == 0 :
                C2.set("")
                entC2.configure(state = DISABLED)

        def chkbutton_A3_Value() :
            if varA3.get() == 1 :
                A3.set("")
                entA3.configure(state = NORMAL)
            elif varA3.get() == 0 :
                A3.set("")
                entA3.configure(state = DISABLED)

        def chkbutton_B3_Value() :
            if varB3.get() == 1 :
                B3.set("")
                entB3.configure(state = NORMAL)
            elif varB3.get() == 0 :
                B3.set("")
                entB3.configure(state = DISABLED)

        def chkbutton_C3_Value() :
            if varC3.get() == 1 :
                C3.set("")
                entC3.configure(state = NORMAL)
            elif varC3.get() == 0 :
                C3.set("")
                entC3.configure(state = DISABLED)

        def chkbutton_D2_Value() :
            if varD2.get() == 1 :
                D2.set("")
                entD2.configure(state = NORMAL)
            elif varD2.get() == 0 :
                D2.set("")
                entD2.configure(state = DISABLED)

        def chkbutton_D1_Value() :
            if varD1.get() == 1 :
                D1.set("")
                entD1.configure(state = NORMAL)
            elif varD1.get() == 0 :
                D1.set("")
                entD1.configure(state = DISABLED)

        def chkbutton_D3_Value() :
            if varD3.get() == 1 :
                D3.set("")
                entD3.configure(state = NORMAL)
            elif varD3.get() == 0 :
                D3.set("")
                entD3.configure(state = DISABLED)

        def chkbutton_E1_Value() :
            if varE1.get() == 1 :
                E1.set("")
                entE1.configure(state = NORMAL)
            elif varE1.get() == 0 :
                E1.set("")
                entE1.configure(state = DISABLED)

        def chkbutton_E2_Value() :
            if varE2.get() == 1 :
                E2.set("")
                entE2.configure(state = NORMAL)
            elif varE2.get() == 0 :
                E2.set("")
                entE2.configure(state = DISABLED)

        def chkbutton_E3_Value() :
            if varE3.get() == 1 :
                E3.set("")
                entE3.configure(state = NORMAL)
            elif varE3.get() == 0 :
                E3.set("")
                entE3.configure(state = DISABLED)

        def chkbutton_F1_Value() :
            if varF1.get() == 1 :
                F1.set("")
                entF1.configure(state = NORMAL)
            elif varF1.get() == 0 :
                F1.set("")
                entF1.configure(state = DISABLED)

        def chkbutton_F2_Value() :
            if varF2.get() == 1 :
                F2.set("")
                entF2.configure(state = NORMAL)
            elif varF2.get() == 0 :
                F2.set("")
                entF2.configure(state = DISABLED)

        def chkbutton_F3_Value() :
            if varF3.get() == 1 :
                F3.set("")
                entF3.configure(state = NORMAL)
            elif varF3.get() == 0 :
                F3.set("")
                entF3.configure(state = DISABLED)

        

        def Total_Cost() :
            if varA1.get()==1 :
                a1=A1.get()
                tax=float('%.2f' %(200*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*a1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("A1-"+randomRef)

                Block.set("Block-A1")
                Num_Ticket.set(a1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varB1.get()==1 :
                b1=B1.get()
                tax=float('%.2f' %(200*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*b1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("B1-"+randomRef)

                Block.set("Block-B1")
                Num_Ticket.set(b1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varC1.get()==1 :
                c1=C1.get()
                tax=float('%.2f' %(200*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*c1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("C1-"+randomRef)

                Block.set("Block-C1")
                Num_Ticket.set(c1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)
            
            if varD1.get()==1 :
                d1=D1.get()
                tax=float('%.2f' %(700*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*d1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("D1-"+randomRef)

                Block.set("Block-D1")
                Num_Ticket.set(d1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varE1.get()==1 :
                e1=E1.get()
                tax=float('%.2f' %(800*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*e1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("E1-"+randomRef)

                Block.set("Block-E1")
                Num_Ticket.set(e1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varF1.get()==1 :
                f1=F1.get()
                tax=float('%.2f' %(1000*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*f1

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("F1-"+randomRef)

                Block.set("Block-F1")
                Num_Ticket.set(f1)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            

            if varA2.get()==1 :
                a2=A2.get()
                tax=float('%.2f' %(400*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+400)*a2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("A2-"+randomRef)

                Block.set("Block-A2")
                Num_Ticket.set(a2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varB2.get()==1 :
                b2=B2.get()
                tax=float('%.2f' %(400*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+400)*b2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("B2-"+randomRef)

                Block.set("Block-B2")
                Num_Ticket.set(b2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varC2.get()==1 :
                c2=C2.get()
                tax=float('%.2f' %(400*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+400)*c2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("C2-"+randomRef)

                Block.set("Block-C2")
                Num_Ticket.set(c2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varD2.get()==1 :
                d2=D2.get()
                tax=float('%.2f' %(700*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*d2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("D2-"+randomRef)

                Block.set("Block-D2")
                Num_Ticket.set(d2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varE2.get()==1 :
                e2=E2.get()
                tax=float('%.2f' %(800*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*e2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("E2-"+randomRef)

                Block.set("Block-E2")
                Num_Ticket.set(e2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varF2.get()==1 :
                f2=F2.get()
                tax=float('%.2f' %(1000*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*f2

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("F2-"+randomRef)

                Block.set("Block-F2")
                Num_Ticket.set(f2)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)


            if varA3.get()==1 :
                a3=A3.get()
                tax=float('%.2f' %(500*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+600)*a3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("A3-"+randomRef)

                Block.set("Block-A3")
                Num_Ticket.set(a3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varB3.get()==1 :
                b3=B3.get()
                tax=float('%.2f' %(500*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+600)*b3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("B3-"+randomRef)

                Block.set("Block-B3")
                Num_Ticket.set(b3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varC3.get()==1 :
                c3=C3.get()
                tax=float('%.2f' %(500*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+600)*c3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("C3-"+randomRef)

                Block.set("Block-C3")
                Num_Ticket.set(c3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varD3.get()==1 :
                d3=D3.get()
                tax=float('%.2f' %(700*0.12))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*d3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("D3-"+randomRef)

                Block.set("Block-D3")
                Num_Ticket.set(d3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varE3.get()==1 :
                e3=E3.get()
                tax=float('%.2f' %(800*0.14))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*e3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("E3-"+randomRef)

                Block.set("Block-E3")
                Num_Ticket.set(e3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)

            if varF3.get()==1 :
                f3=F3.get()
                tax=float('%.2f' %(1000*0.16))
                subt=float('%.2f' %(tax+10))
                tot=float(tax+subt+200)*f3

                x=random.randint(100,6000)
                randomRef=str(x)
                Ref_No.set("F3-"+randomRef)

                Block.set("Block-F3")
                Num_Ticket.set(f3)
                Tax.set(tax)
                SubTotal.set(subt)
                Total.set(tot)
                State_Tax.set(tax)
                Sub_Total.set(subt)
                Total_Price.set(tot)
    
        #=====================================Entry Widget=============================================================================

        lblBlock = Label(topLeft1,font=('arial',20, 'bold'),text="Block (₹200)", bd = 8) .grid(row =0,column =0, sticky =W)

        chkA1 = Checkbutton(topLeft1,font=('arial',20, 'bold'),text="Block A1", variable = varA1, onvalue = 1, offvalue = 0, command = chkbutton_A1_Value) .grid(row =1,column =0, sticky =W)
        entA1=Entry(topLeft1,font=('arial',20, 'bold'), textvariable=A1,bd=2,width=5,state=DISABLED)
        entA1.grid(row=1,column=1,sticky=W)

        chkB1 = Checkbutton(topLeft1,font=('arial',20, 'bold'),text="Block B1", variable = varB1, onvalue = 1, offvalue = 0, command = chkbutton_B1_Value) .grid(row =2,column =0, sticky =W)
        entB1=Entry(topLeft1,font=('arial',20, 'bold'), textvariable=B1,bd=2,width=5,state=DISABLED)
        entB1.grid(row=2,column=1,sticky=W)

        chkC1 = Checkbutton(topLeft1,font=('arial',20, 'bold'),text="Block C1", variable = varC1, onvalue = 1, offvalue = 0, command = chkbutton_C1_Value) .grid(row =3,column =0, sticky =W)
        entC1=Entry(topLeft1,font=('arial',20, 'bold'), textvariable=C1,bd=2,width=5,state=DISABLED)
        entC1.grid(row=3,column=1,sticky=W)

        #---------------------------------------------------------------------

        lblBlock = Label(topLeft2,font=('arial',20, 'bold'),text="Block (₹400)", bd = 8) .grid(row =0,column =0, sticky =W)

        chkA2 = Checkbutton(topLeft2,font=('arial',20, 'bold'),text="Block A2", variable = varA2, onvalue = 1, offvalue = 0, command = chkbutton_A2_Value) .grid(row =1,column =0, sticky =W)
        entA2=Entry(topLeft2,font=('arial',20, 'bold'), textvariable=A2,bd=2,width=5,state=DISABLED)
        entA2.grid(row=1,column=1,sticky=W)

        chkB2 = Checkbutton(topLeft2,font=('arial',20, 'bold'),text="Block B2", variable = varB2, onvalue = 1, offvalue = 0, command = chkbutton_B2_Value) .grid(row =2,column =0, sticky =W)
        entB2=Entry(topLeft2,font=('arial',20, 'bold'), textvariable=B2,bd=2,width=5,state=DISABLED)
        entB2.grid(row=2,column=1,sticky=W)

        chkC2 = Checkbutton(topLeft2,font=('arial',20, 'bold'),text="Block C2", variable = varC2, onvalue = 1, offvalue = 0, command = chkbutton_C2_Value) .grid(row =3,column =0, sticky =W)
        entC2=Entry(topLeft2,font=('arial',20, 'bold'), textvariable=C2,bd=2,width=5,state=DISABLED)
        entC2.grid(row=3,column=1,sticky=W)

        #---------------------------------------------------------------------

        lblBlock = Label(topLeft3,font=('arial',20, 'bold'),text="Block (₹500)", bd = 8) .grid(row =0,column =0, sticky =W)
        chkA3 = Checkbutton(topLeft3,font=('arial',20, 'bold'),text="Block A3", variable = varA3, onvalue = 1, offvalue = 0, command = chkbutton_A3_Value) .grid(row =1,column =0, sticky =W)
        entA3=Entry(topLeft3,font=('arial',20, 'bold'), textvariable=A3,bd=2,width=5,state=DISABLED)
        entA3.grid(row=1,column=1,sticky=W)
        
        chkB3 = Checkbutton(topLeft3,font=('arial',20, 'bold'),text="Block B3", variable = varB3, onvalue = 1, offvalue = 0, command = chkbutton_B3_Value) .grid(row =2,column =0, sticky =W)
        entB3=Entry(topLeft3,font=('arial',20, 'bold'), textvariable=B3,bd=2,width=5,state=DISABLED)
        entB3.grid(row=2,column=1,sticky=W)

        chkC3 = Checkbutton(topLeft3,font=('arial',20, 'bold'),text="Block C3", variable = varC3, onvalue = 1, offvalue = 0, command = chkbutton_C3_Value) .grid(row =3,column =0, sticky =W)
        entC3=Entry(topLeft3,font=('arial',20, 'bold'), textvariable=C3,bd=2,width=5,state=DISABLED)
        entC3.grid(row=3,column=1,sticky=W)

        #===============================================================================================================================

        lblBlock = Label(topLeft4,font=('arial',20, 'bold'),text="Block (₹700)", bd = 8) .grid(row =0,column =0, sticky =W)

        chkD1 = Checkbutton(topLeft4,font=('arial',20, 'bold'),text="Block D1", variable = varD1, onvalue = 1, offvalue = 0, command = chkbutton_D1_Value) .grid(row =1,column =0, sticky =W)
        entD1=Entry(topLeft4,font=('arial',20, 'bold'), textvariable=D1,bd=2,width=5,state=DISABLED)
        entD1.grid(row=1,column=1,sticky=W)

        chkD2= Checkbutton(topLeft4,font=('arial',20, 'bold'),text="Block E1", variable = varD2, onvalue = 1, offvalue = 0, command = chkbutton_D2_Value) .grid(row =2,column =0, sticky =W)
        entD2=Entry(topLeft4,font=('arial',20, 'bold'), textvariable=D2,bd=2,width=5,state=DISABLED)
        entD2.grid(row=2,column=1,sticky=W)

        chkD3 = Checkbutton(topLeft4,font=('arial',20, 'bold'),text="Block F1", variable = varD3, onvalue = 1, offvalue = 0, command = chkbutton_D3_Value) .grid(row =3,column =0, sticky =W)
        entD3=Entry(topLeft4,font=('arial',20, 'bold'), textvariable=D3,bd=2,width=5,state=DISABLED)
        entD3.grid(row=3,column=1,sticky=W)

        #---------------------------------------------------------------------

        lblBlock = Label(topLeft5,font=('arial',20, 'bold'),text="Block (₹800)", bd = 8) .grid(row =0,column =0, sticky =W)

        chkE1 = Checkbutton(topLeft5,font=('arial',20, 'bold'),text="Block D2", variable = varE1, onvalue = 1, offvalue = 0, command = chkbutton_E1_Value) .grid(row =1,column =0, sticky =W)
        entE1=Entry(topLeft5,font=('arial',20, 'bold'), textvariable=E1,bd=2,width=5,state=DISABLED)
        entE1.grid(row=1,column=1,sticky=W)

        chkE2 = Checkbutton(topLeft5,font=('arial',20, 'bold'),text="Block E2", variable = varE2, onvalue = 1, offvalue = 0, command = chkbutton_E2_Value) .grid(row =2,column =0, sticky =W)
        entE2=Entry(topLeft5,font=('arial',20, 'bold'), textvariable=E2,bd=2,width=5,state=DISABLED)
        entE2.grid(row=2,column=1,sticky=W)

        chkE3 = Checkbutton(topLeft5,font=('arial',20, 'bold'),text="Block F2", variable = varE3, onvalue = 1, offvalue = 0, command = chkbutton_E3_Value) .grid(row =3,column =0, sticky =W)
        entE3=Entry(topLeft5,font=('arial',20, 'bold'), textvariable=E3,bd=2,width=5,state=DISABLED)
        entE3.grid(row=3,column=1,sticky=W)

        #---------------------------------------------------------------------

        lblBlock = Label(topLeft6,font=('arial',20, 'bold'),text="Block (₹1000)", bd = 8) .grid(row =0,column =0, sticky =W)
        chkF1 = Checkbutton(topLeft6,font=('arial',20, 'bold'),text="Block D3", variable = varF1, onvalue = 1, offvalue = 0, command = chkbutton_F1_Value) .grid(row =1,column =0, sticky =W)
        entF1=Entry(topLeft6,font=('arial',20, 'bold'), textvariable=F1,bd=2,width=5,state=DISABLED)
        entF1.grid(row=1,column=1,sticky=W)
        
        chkF2 = Checkbutton(topLeft6,font=('arial',20, 'bold'),text="Block E3", variable = varF2, onvalue = 1, offvalue = 0, command = chkbutton_F2_Value) .grid(row =2,column =0, sticky =W)
        entF2=Entry(topLeft6,font=('arial',20, 'bold'), textvariable=F2,bd=2,width=5,state=DISABLED)
        entF2.grid(row=2,column=1,sticky=W)

        chkF3 = Checkbutton(topLeft6,font=('arial',20, 'bold'),text="Block F3", variable = varF3, onvalue = 1, offvalue = 0, command = chkbutton_F3_Value) .grid(row =3,column =0, sticky =W)
        entF3=Entry(topLeft6,font=('arial',20, 'bold'), textvariable=F3,bd=2,width=5,state=DISABLED)
        entF3.grid(row=3,column=1,sticky=W)

        #===========================================================================================================================================

        #=====================================Lable Widget=============================================================================

        lblReceipt=Label(frametopRight,font=('arial',18, 'bold'),text="Receipt",bd=5, pady=10, padx=4, width = 28,justify='center')
        lblReceipt.grid(row=0,column=0)

        lblBlock1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Block", width = 10, relief = 'sunken', justify='center')
        lblBlock1.grid(row=0,column=1)
    
        lblBlock2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 10, relief = 'sunken', textvariable=Block, justify='center')
        lblBlock2.grid(row=1,column=1)

        lblTicket1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Ticket", width = 10, relief = 'sunken', justify='center')
        lblTicket1.grid(row=0,column=2)

        lblTicket2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 10, relief = 'sunken',textvariable=Num_Ticket,justify='center')
        lblTicket2.grid(row=1,column=2)

        #=====================================Space====================================================================================

        lblsp=Label(frameBottomRight,font=('arial',14, 'bold'), width = 40)
        lblsp.grid(row=2,column=0, columnspan=4) 

        lblsp=Label(frameBottomRight,font=('arial',14, 'bold'), width = 40)
        lblsp.grid(row=6,column=0, columnspan=4) 


        #===============================================================================================================================

        lblSTax1=Label(frameBottomRight,font=('arial',14, 'bold'),text="State Tax", width = 10, relief = 'sunken', justify='center')
        lblSTax1.grid(row=3,column=1)
        lblSTax2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 10, relief = 'sunken', textvariable=State_Tax, justify='center')
        lblSTax2.grid(row=3,column=2)
        
        lblSTol1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Sub Total", width = 10, relief = 'sunken', justify='center')
        lblSTol1.grid(row=4,column=1)
        lblSTol2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 10, relief = 'sunken', textvariable=Sub_Total, justify='center')
        lblSTol2.grid(row=4,column=2)
        
        lblPrice1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Total", width = 10, relief = 'sunken', justify='center')
        lblPrice1.grid(row=5,column=1)
        lblPrice2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 10, relief = 'sunken', textvariable=Total_Price, justify='center')
        lblPrice2.grid(row=5,column=2)

        #===============================================================================================================================

        lblRefNo1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Ref No", width = 10, relief = 'sunken', justify='center')
        lblRefNo1.grid(row=7,column=0,padx=5, pady=5)
        lblRefNo2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 8, relief = 'sunken',textvariable=Ref_No, justify='center')
        lblRefNo2.grid(row=8,column=0)

        lblTime1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Time", width = 10, relief = 'sunken', justify='center')
        lblTime1.grid(row=7,column=1)
        lblTime2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 8, relief = 'sunken',textvariable=Time, justify='center')
        lblTime2.grid(row=8,column=1)

        lblDate1=Label(frameBottomRight,font=('arial',14, 'bold'),text="Date", width = 10, relief = 'sunken', justify='center')
        lblDate1.grid(row=7,column=2)
        lblDate2=Label(frameBottomRight,font=('arial',14, 'bold'), width = 8, relief = 'sunken',textvariable=Date, justify='center')
        lblDate2.grid(row=8,column=2)
        
        #===============================================================================================================================

        Date.set(time.strftime("%d/%m/%Y")) 
        Time.set(time.strftime("%H:%M:%S")) 
        
        #------------------------------------------------------------------------------------------------


        lblsp=Label(frameBottomRight,font=('arial',14, 'bold'), width = 40)
        lblsp.grid(row=10,column=0, columnspan=4) 

        btnTotal = Button(frameBottomRight,font=('arial',14, 'bold'),text="Total", width = 8, height = 1, padx=2, pady=16, bd =2, command = Total_Cost)
        btnTotal.grid(row=11,column=0)
        btnCafe = Button(frameBottomRight,font=('arial',14, 'bold'),text="Cafe", width = 8, height = 1, padx=2, pady=16, bd =2, command = Cafe)
        btnCafe.grid(row=11,column=1)
        btnReset = Button(frameBottomRight,font=('arial',14, 'bold'),text="Reset", width = 8, height = 1, padx=2, pady=16, bd =2, command = Reset)
        btnReset.grid(row=11,column=2)
        btnExit = Button(frameBottomRight,font=('arial',14, 'bold'),text="Exit", width = 8, height = 1, padx=2, pady=16, bd =2, command = iExit)
        btnExit.grid(row=11,column=3)

#======================================================================================================================================

if __name__=='__main__':
    root = Tk()
    application = Cricket(root)
    root.mainloop()
