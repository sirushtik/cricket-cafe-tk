from tkinter import *
import random
import time
import datetime
import tkinter.messagebox

def Cafe():
    root=Tk()
    root.geometry("1350x750+0+0")
    root.title("Cricket Stadium Cafe")
    root.configure(background='lightblue')

    Tops=Frame(root, width=1350, height=100, bd=14, relief="raise")
    Tops.pack(side=TOP)

    f1=Frame(root, width=900, height=650, bd=8, relief="raise")
    f1.pack(side=LEFT)

    f2=Frame(root, width=440, height=650, bd=8, relief="raise")
    f2.pack(side=RIGHT)

    f1a=Frame(f1, width=900, height=330, bd=8, relief="raise")
    f1a.pack(side=TOP)

    f2a=Frame(f1, width=900, height=320, bd=6, relief="raise")
    f2a.pack(side=BOTTOM)

    ft2=Frame(f2, width=440, height=450, bd=12, relief="raise")
    ft2.pack(side=TOP)
    fb2=Frame(f2, width=440, height=250, bd=16, relief="raise")
    fb2.pack(side=BOTTOM)

    f1aa=Frame(f1a, width=400, height=330, bd=16, relief="raise")
    f1aa.pack(side=LEFT)
    f1ab=Frame(f1a, width=400, height=330, bd=16, relief="raise")
    f1ab.pack(side=RIGHT)

    f2aa=Frame(f2a, width=450, height=330, bd=14, relief="raise")
    f2aa.pack(side=LEFT)

    f2ab=Frame(f2a, width=450, height=330, bd=14, relief="raise")
    f2ab.pack(side=RIGHT)

    Tops.configure(background='black')
    f1.configure(background='black')
    f2.configure(background='black')

    lblInfo=Label(Tops, font=('arial',70,'bold'),
                text="Cricket Stadium Cafe", bd=10)
    lblInfo.grid(row=0, column=0)

    #================================ Variables ====================================

    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    var4=IntVar()
    var5=IntVar()
    var6=IntVar()
    var7=IntVar()
    var8=IntVar()
    var9=IntVar()
    var10=IntVar()
    var11=IntVar()
    var12=IntVar()
    var13=IntVar()
    var14=IntVar()
    var15=IntVar()
    var16=IntVar()

    DateofOrder=StringVar()
    Receipt_Ref=StringVar()
    PaidTax=StringVar()
    SubTotal=StringVar()
    TotalCost=StringVar()
    CostofFast_Food=StringVar()
    CostofDrinks=StringVar()
    ServiceCharge=StringVar()

    E_Coke=StringVar()
    E_Pepsi=StringVar()
    E_Sprite=StringVar()
    E_Fanta=StringVar()
    E_Maaza=StringVar()
    E__7up=StringVar()
    E_Limca=StringVar()
    E_Mountain_Dew=StringVar()
    E_Hamburger=StringVar()
    E_French_Fries=StringVar()
    E_Pizza=StringVar()
    E_Sandwich=StringVar()
    E_Chicken_Legs=StringVar()
    E_Taco=StringVar()
    E_Hot_Dog=StringVar()
    E_Donut=StringVar()

    E_Coke.set("0")
    E_Pepsi.set("0")
    E_Sprite.set("0")
    E_Fanta.set("0")
    E_Maaza.set("0")
    E__7up.set("0")
    E_Limca.set("0")
    E_Mountain_Dew.set("0")
    E_Hamburger.set("0")
    E_French_Fries.set("0")
    E_Pizza.set("0")
    E_Sandwich.set("0")
    E_Chicken_Legs.set("0")
    E_Taco.set("0")
    E_Hot_Dog.set("0")
    E_Donut.set("0")

    DateofOrder.set(time.strftime("%d/%m/%Y"))
    var1.set("0")
    var2.set("0")
    var3.set("0")
    var4.set("0")
    var5.set("0")
    var6.set("0")
    var7.set("0")
    var8.set("0")
    var9.set("0")
    var10.set("0")
    var11.set("0")
    var12.set("0")
    var13.set("0")
    var14.set("0")
    var15.set("0")
    var16.set("0")

    #================================================= Functions ==============================================================
    def qExit():
        qExit = tkinter.messagebox.askyesno("Quit System","Do you want to quit")
        if qExit > 0:
            root.destroy()
            return

    def Reset():
        PaidTax.set("")
        SubTotal.set("")
        TotalCost.set("")
        CostofFast_Food.set("")
        CostofDrinks.set("")
        ServiceCharge.set("")
        txtReceipt.delete("1.0",END)


        E_Coke.set("0")
        E_Pepsi.set("0")
        E_Sprite.set("0")
        E_Fanta.set("0")
        E_Maaza.set("0")
        E__7up.set("0")
        E_Limca.set("0")
        E_Mountain_Dew.set("0")
        
        E_Hamburger.set("0")
        E_French_Fries.set("0")
        E_Pizza.set("0")
        E_Sandwich.set("0")
        E_Chicken_Legs.set("0")
        E_Taco.set("0")
        E_Hot_Dog.set("0")
        E_Donut.set("0")

        DateofOrder.set(time.strftime("%d/%m/%Y"))
        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        var13.set("0")
        var14.set("0")
        var15.set("0")
        var16.set("0")

        txtCoke.configure(state=DISABLED)
        txtPepsi.configure(state=DISABLED)
        txtSprite.configure(state=DISABLED)
        txtFanta.configure(state=DISABLED)
        txtMaaza.configure(state=DISABLED)
        txt_7up.configure(state=DISABLED)
        txtLimca.configure(state=DISABLED)
        txtMountain_Dew.configure(state=DISABLED)
        txtHamburger.configure(state=DISABLED)
        txtFrench_Fries.configure(state=DISABLED)
        txtPizza.configure(state=DISABLED)
        txtSandwich.configure(state=DISABLED)
        txtChicken_Legs.configure(state=DISABLED)
        txtTaco.configure(state=DISABLED)
        txtHot_Dog.configure(state=DISABLED)
        txtDonut.configure(state=DISABLED)

    #========================= Check Button ======================================================
    def chkbutton_value():
        if var1.get()==1:
            txtCoke.configure(state=NORMAL)
        elif var1.get()==0:
            txtCoke.configure(state=DISABLED)
            E_Coke.set("0")
            
        if var2.get()==1:
            txtPepsi.configure(state=NORMAL)
        elif var2.get()==0:
            txtPepsi.configure(state=DISABLED)
            E_Pepsi.set("0")
            
        if var3.get()==1:
            txtSprite.configure(state=NORMAL)
        elif var3.get()==0:
            txtSprite.configure(state=DISABLED)
            E_Sprite.set("0")
            
        if var4.get()==1:
            txtFanta.configure(state=NORMAL)
        elif var4.get()==0:
            txtFanta.configure(state=DISABLED)
            E_Fanta.set("0")
            
        
        if var5.get()==1:
            txtMaaza.configure(state=NORMAL)
        elif var5.get()==0:
            txtMaaza.configure(state=DISABLED)
            E_Maaza.set("0")
            
        if var6.get()==1:
            txt_7up.configure(state=NORMAL)
        elif var6.get()==0:
            txt_7up.configure(state=DISABLED)
            E__7up.set("0")

        if var7.get()==1:
            txtLimca.configure(state=NORMAL)
        elif var7.get()==0:
            txtLimca.configure(state=DISABLED)
            E_Limca.set("0")
            
        if var8.get()==1:
            txtMountain_Dew.configure(state=NORMAL)
        elif var8.get()==0:
            txtMountain_Dew.configure(state=DISABLED)
            E_Mountain_Dew.set("0")

        if var9.get()==1:
            txtHamburger.configure(state=NORMAL)
        elif var9.get()==0:
            txtHamburger.configure(state=DISABLED)
            E_Hamburger.set("0")
            
        if var10.get()==1:
            txtFrench_Fries.configure(state=NORMAL)
        elif var10.get()==0:
            txtFrench_Fries.configure(state=DISABLED)
            E_French_Fries.set("0")
            
        if var11.get()==1:
            txtPizza.configure(state=NORMAL)
        elif var11.get()==0:
            txtPizza.configure(state=DISABLED)
            E_Pizza.set("0")
            
        if var12.get()==1:
            txtSandwich.configure(state=NORMAL)
        elif var12.get()==0:
            txtSandwich.configure(state=DISABLED)
            E_Sandwich.set("0")
            
        if var13.get()==1:
            txtChicken_Legs.configure(state=NORMAL)
        elif var13.get()==0:
            txtChicken_Legs.configure(state=DISABLED)
            E_Chicken_Legs.set("0")
            
        if var14.get()==1:
            txtTaco.configure(state=NORMAL)
        elif var14.get()==0:
            txtTaco.configure(state=DISABLED)
            E_Taco.set("0")

        if var15.get()==1:
            txtHot_Dog.configure(state=NORMAL)
        elif var15.get()==0:
            txtHot_Dog.configure(state=DISABLED)
            E_Hot_Dog.set("0")

        if var16.get()==1:
            txtDonut.configure(state=NORMAL)
        elif var16.get()==0:
            txtDonut.configure(state=DISABLED)
            E_Donut.set("0")

    def CostofItem():
        Item1=float(E_Coke.get())
        Item2=float(E_Pepsi.get())
        Item3=float(E_Sprite.get())
        Item4=float(E_Fanta.get())
        Item5=float(E_Maaza.get())
        Item6=float(E__7up.get())
        Item7=float(E_Limca.get())
        Item8=float(E_Mountain_Dew.get())
        
        Item9=float(E_Hamburger.get())
        Item10=float(E_French_Fries.get())
        Item11=float(E_Pizza.get())
        Item12=float(E_Sandwich.get())
        Item13=float(E_Chicken_Legs.get())
        Item14=float(E_Taco.get())
        Item15=float(E_Hot_Dog.get())
        Item16=float(E_Donut.get())

        PriceofDrinks=(Item1*80)+(Item2*85)+(Item3*65)+(Item4*50)+\
        (Item5*75)+(Item6*80)+(Item7*40)+(Item8*70)

        PriceofFast_Food=(Item9*120)+(Item10*60)+(Item11*300)+(Item12*90)+\
        (Item13*180)+(Item14*160)+(Item15*140)+(Item16*30)

        DrinksPrice="₹",str("%.2f"%(PriceofDrinks))
        Fast_FoodPrice="₹",str("%.2f"%(PriceofFast_Food))
        CostofFast_Food.set(Fast_FoodPrice)
        CostofDrinks.set(DrinksPrice)
        SC="₹",str("%.2f"%(1.59))
        ServiceCharge.set(SC)

        SubTotalofITEMS="₹",str("%.2f"%(PriceofFast_Food+PriceofDrinks+1.59))
        SubTotal.set(SubTotalofITEMS)

        Tax="₹",str("%.2f"%((PriceofFast_Food+PriceofDrinks+1.59)*0.15))
        PaidTax.set(Tax)
        TT=(PriceofFast_Food+PriceofDrinks+1.59)*0.15
        TC="₹",str("%.2f"%(PriceofFast_Food+PriceofDrinks+1.59+TT))
        TotalCost.set(TC)
        
    def Receipt():
        txtReceipt.delete("1.0",END)
        x=random.randint(10908,500876)
        randomRef=str(x)
        Receipt_Ref.set("BILL"+randomRef)

        txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get()+"\t\t"+DateofOrder.get()+"\n")
        txtReceipt.insert(END,'Items\t\t\t\t\t'+"Cost of Items\n\n")
        txtReceipt.insert(END,'Coke:\t\t\t\t\t'+E_Coke.get()+"\n")
        txtReceipt.insert(END,'Pepsi:\t\t\t\t\t'+E_Pepsi.get()+"\n")
        txtReceipt.insert(END,'Sprite:\t\t\t\t\t'+E_Sprite.get()+"\n")
        txtReceipt.insert(END,'Fanta:\t\t\t\t\t'+E_Fanta.get()+"\n")
        txtReceipt.insert(END,'Maaza:\t\t\t\t\t'+E_Maaza.get()+"\n")
        txtReceipt.insert(END,'7up:\t\t\t\t\t'+E__7up.get()+"\n")
        txtReceipt.insert(END,'Limka:\t\t\t\t\t'+E_Limca.get()+"\n")
        txtReceipt.insert(END,'Mountain Dew:\t\t\t\t\t'+E_Mountain_Dew.get()+"\n")
        txtReceipt.insert(END,'Hamburger:\t\t\t\t\t'+E_Hamburger.get()+"\n")
        txtReceipt.insert(END,'French Fries:\t\t\t\t\t'+E_French_Fries.get()+"\n")
        txtReceipt.insert(END,'Pizza:\t\t\t\t\t'+E_Pizza.get()+"\n")
        txtReceipt.insert(END,'Sandwich:\t\t\t\t\t'+E_Sandwich.get()+"\n")
        txtReceipt.insert(END,'Chicken Legs:\t\t\t\t\t'+E_Chicken_Legs.get()+"\n")
        txtReceipt.insert(END,'Taco:\t\t\t\t\t'+E_Taco.get()+"\n")
        txtReceipt.insert(END,'Hot Dog:\t\t\t\t\t'+E_Hot_Dog.get()+"\n")
        txtReceipt.insert(END,'Donut:\t\t\t\t\t'+E_Donut.get()+"\n")
        txtReceipt.insert(END,'Cost of Drinks:\t\t'+CostofDrinks.get()+"\tTax Paid:\t\t"+PaidTax.get()+"\n")
        txtReceipt.insert(END,'Cost of Fast_Food:\t\t'+CostofFast_Food.get()+"\tSubTotal:\t\t"+SubTotal.get()+"\n")
        txtReceipt.insert(END,'Service Charge:\t\t'+ServiceCharge.get()+"\tTotal Cost:\t\t"+TotalCost.get()+"\n")    

                        
                                            

    #================================================= Drinks ==============================================================

    Coke=Checkbutton(f1aa, text="Coke \t\t", variable=var1, onvalue=1, offvalue=0,command=chkbutton_value,
                    font=('arial', 18, 'bold')).grid(row=0, sticky=W) #01
    Pepsi=Checkbutton(f1aa, text="Pepsi \t\t", variable=var2, onvalue=1, offvalue=0,command=chkbutton_value,
                        font=('arial', 18, 'bold')).grid(row=1, sticky=W) #02
    Sprite=Checkbutton(f1aa, text="Sprite \t", variable=var3, onvalue=1, offvalue=0,command=chkbutton_value,
                        font=('arial', 18, 'bold')).grid(row=2, sticky=W) #03 
    Fanta=Checkbutton(f1aa, text="Fanta \t", variable=var4, onvalue=1, offvalue=0,command=chkbutton_value,
                            font=('arial', 18, 'bold')).grid(row=3, sticky=W) #04
    Maaza=Checkbutton(f1aa, text="Maaza \t", variable=var5, onvalue=1, offvalue=0,command=chkbutton_value,
                        font=('arial', 18, 'bold')).grid(row=4, sticky=W) #05
    _7up=Checkbutton(f1aa, text="7up \t", variable=var6, onvalue=1, offvalue=0,command=chkbutton_value,
                            font=('arial', 18, 'bold')).grid(row=5, sticky=W) #06
    Limca=Checkbutton(f1aa, text="Limka \t", variable=var7, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=6, sticky=W) #07
    Mountain_Dew=Checkbutton(f1aa, text="Mountain Dew \t", variable=var8, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=7, sticky=W) #08

    #========================Fast_Food===============================================================================================

    Hamburger=Checkbutton(f1ab, text="Hamburger \t", variable=var9, onvalue=1, offvalue=0,command=chkbutton_value,
                        font=('arial', 18, 'bold')).grid(row=0, sticky=W) #09
    French_Fries=Checkbutton(f1ab, text="French Fries \t", variable=var10, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=1, sticky=W) #10
    Pizza=Checkbutton(f1ab, text="Pizza \t", variable=var11, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=2, sticky=W) #11 
    Sandwich=Checkbutton(f1ab, text="Sandwich \t", variable=var12, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=3, sticky=W) #12
    Chicken_Legs=Checkbutton(f1ab, text="Chicken Legs \t", variable=var13, onvalue=1, offvalue=0,command=chkbutton_value,
                                    font=('arial', 18, 'bold')).grid(row=4, sticky=W) #13
    Taco=Checkbutton(f1ab, text="Taco \t", variable=var14, onvalue=1, offvalue=0,command=chkbutton_value,
                                    font=('arial', 18, 'bold')).grid(row=5, sticky=W) #14
    Hot_Dog=Checkbutton(f1ab, text="Hot Dog \t", variable=var15, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=6, sticky=W) #15
    Donut=Checkbutton(f1ab, text="Donut \t", variable=var16, onvalue=1, offvalue=0,command=chkbutton_value,
                                font=('arial', 18, 'bold')).grid(row=7, sticky=W) #16

    #============================Enter Widget for Drinks================================================================================

    txtCoke=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Coke,
                justify='left', state=DISABLED)
    txtCoke.grid(row=0, column=1)

    txtPepsi=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Pepsi,
                    justify='left', state=DISABLED)
    txtPepsi.grid(row=1, column=1)

    txtSprite=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Sprite,
                        justify='left', state=DISABLED)
    txtSprite.grid(row=2, column=1)

    txtFanta=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Fanta,
                        justify='left', state=DISABLED)
    txtFanta.grid(row=3, column=1)

    txtMaaza=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Maaza,
                        justify='left', state=DISABLED)
    txtMaaza.grid(row=4, column=1)

    txt_7up=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E__7up,
                            justify='left', state=DISABLED)
    txt_7up.grid(row=5, column=1)

    txtLimca=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Limca,
                            justify='left', state=DISABLED)
    txtLimca.grid(row=6, column=1)

    txtMountain_Dew=Entry(f1aa, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Mountain_Dew,
                            justify='left', state=DISABLED)
    txtMountain_Dew.grid(row=7, column=1)

    #============================ Enter Widget for Fast_Food ================================================================================

    txtHamburger=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Hamburger,
                        justify='left', state=DISABLED)
    txtHamburger.grid(row=0, column=1)

    txtFrench_Fries=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_French_Fries,
                            justify='left', state=DISABLED)
    txtFrench_Fries.grid(row=1, column=1)

    txtPizza=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Pizza,
                            justify='left', state=DISABLED)
    txtPizza.grid(row=2, column=1)

    txtSandwich=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Sandwich,
                            justify='left', state=DISABLED)
    txtSandwich.grid(row=3, column=1)

    txtChicken_Legs=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Chicken_Legs,
                                justify='left', state=DISABLED)
    txtChicken_Legs.grid(row=4, column=1)

    txtTaco=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Taco,
                                    justify='left', state=DISABLED)
    txtTaco.grid(row=5, column=1)

    txtHot_Dog=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Hot_Dog,
                            justify='left', state=DISABLED)
    txtHot_Dog.grid(row=6, column=1)

    txtDonut=Entry(f1ab, font=('arial', 16, 'bold'), bd=8, width=6,textvariable=E_Donut,
                            justify='left', state=DISABLED)
    txtDonut.grid(row=7, column=1)

    #=========================Information======================================================

    lblReceipt = Label(ft2, font=('arial', 12, 'bold'), text="Receipt :", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(ft2, width=59, height=22, bg="white", bd=8, font=('arial', 11, 'bold'))
    txtReceipt.grid(row=1, column=0)

    #========================= Cost Items Information==========================================
    lblCostofDrinks=Label(f2aa,font=("arial",16,"bold"),text="Cost of Drinks",bd=8)
    lblCostofDrinks.grid(row=0,column=0,sticky=W)
    txtCostofDrinks=Entry(f2aa,font=("arial",16,"bold"),bd=8,justify="left",
                        insertwidth=2,textvariable=CostofDrinks)
    txtCostofDrinks.grid(row=0,column=1,sticky=W)

    lblCostofFast_Food=Label(f2aa,font=("arial",16,"bold"),text="Cost of Fast_Food",bd=8)
    lblCostofFast_Food.grid(row=1,column=0,sticky=W)
    txtCostofFast_Food=Entry(f2aa,font=("arial",16,"bold"),bd=8,justify="left",
                        insertwidth=2,textvariable=CostofFast_Food)
    txtCostofFast_Food.grid(row=1,column=1,sticky=W)

    lblServiceCharges=Label(f2aa,font=("arial",16,"bold"),text="Service Charges",bd=8)
    lblServiceCharges.grid(row=2,column=0,sticky=W)
    txtServiceCharges=Entry(f2aa,font=("arial",16,"bold"),bd=8,justify="left",
                            insertwidth=2,textvariable=ServiceCharge)
    txtServiceCharges.grid(row=2,column=1,sticky=W)
    
    #========================= Payment Information=============================================
    lblPaidTax=Label(f2ab,font=("arial",16,"bold"),text="Tax",bd=8)
    lblPaidTax.grid(row=0,column=0,sticky=W)
    txtPaidTax=Entry(f2ab,font=("arial",16,"bold"),bd=8,justify="left",
                    insertwidth=2,textvariable=PaidTax)
    txtPaidTax.grid(row=0,column=1)

    lblSubTotal=Label(f2ab,font=("arial",16,"bold"),text="Sub Total",bd=8)
    lblSubTotal.grid(row=1,column=0,sticky=W)
    txtSubTotal=Entry(f2ab,font=("arial",16,"bold"),bd=8,justify="left",
                    insertwidth=2,textvariable=SubTotal)
    txtSubTotal.grid(row=1,column=1)

    lblTotalCost=Label(f2ab,font=("arial",16,"bold"),text="Total",bd=8)
    lblTotalCost.grid(row=2,column=0,sticky=W)
    txtTotalCost=Entry(f2ab,font=("arial",16,"bold"),bd=8,justify="left",
                    insertwidth=2,textvariable=TotalCost)
    txtTotalCost.grid(row=2,column=1)


            
    #==========================Button==========================================================

    btnTotal = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16,'bold'), width=5, text="Total",command=CostofItem)
    btnTotal.grid(row=0, column=0)
    btnReceipt = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16,'bold'), width=5, text="Receipt",command=Receipt)
    btnReceipt.grid(row=0, column=1)
    btnReset = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16,'bold'), width=5, text="Reset",command=Reset)
    btnReset.grid(row=0, column=2)
    btnExit = Button(fb2, padx=16, pady=1, bd=4, fg="black", font=('arial', 16,'bold'), width=5, text="Exit",command=qExit)
    btnExit.grid(row=0, column=3)



    root.mainloop()

if __name__=='__main__':
    Cafe()