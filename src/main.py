from tkinter import *
from tkinter import messagebox
import platform
import webbrowser

def app():
    window = Tk()
    window.geometry("700x440")
    window.resizable(False, False)
    window.iconbitmap("C:\\Users\\Ashwin\\Desktop\\Programming Portfolio\\Python\\loanCalc\\icon\\favicon.ico")
    window.title("Loan Calculator")

    def showHelp():
        webbrowser.open("https://www.google.com/search?q=What+is+a+loan&sxsrf=ALiCzsaxhjy3WnFSx3MumB-6is7TrqAuLw%3A1655323787397&ei=izyqYoHzF4ehptQP7ZCHyAQ&ved=0ahUKEwjB5NfSobD4AhWHkIkEHW3IAUkQ4dUDCA4&uact=5&oq=What+is+a+loan&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyCggAEIAEEIcCEBQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoHCCMQsQIQJzoECAAQCkoECEEYAEoECEYYAFDhB1jvCWCgDWgBcAF4AIABygGIAbsCkgEFMC4xLjGYAQCgAQHIAQrAAQE&sclient=gws-wiz")

    def showAbout():
        os = platform.platform()
        messagebox.showinfo(title="About", message=f"Loan Calculator                                          \nAuthor: Ashwin Ravuru Kalyan\nVersion: 1.0.0\nOperating System: {os}")  
    
    menubar = Menu(window)
    
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New Window                          ", command=newWindow)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.destroy)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Show Help                        ", command=showHelp)
    helpmenu.add_separator()
    helpmenu.add_command(label="About", command=showAbout)
    
    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_cascade(label="Help", menu=helpmenu)
    
    titleLabel = Label(window, text="Loan Calculator", font=("Times New Roman", 25)).place(x=250, y=30)
    loanAmountLabel = Label(window, font=("Times New Roman", 11), text="Loan Amount ($)").place(x=140, y=100)
    interestRateLabel = Label(window, font=("Times New Roman", 11), text="Interest Rate (%)").place(x=140, y=125)
    loanTermLabel = Label(window, font=("Times New Roman", 11), text="Loan Term (yrs)").place(x=140, y=150)
    compoundedLabel = Label(window, font=("Times New Roman", 11), text="Compounded (#/yr)").place(x=140, y=173)
    paymentsLabel = Label(window, font=("Times New Roman", 11), text="Payments per year").place(x=140, y=198)
    
    loanAmountEntry = Entry(window, width=35)
    loanAmountEntry.insert(0, "100000")
    loanAmountEntry.place(x=253, y=100)

    interestRateEntry = Entry(window, width=35)
    interestRateEntry.insert(0, "6")
    interestRateEntry.place(x=253, y=125)

    loanTermEntry = Entry(window, width=35)
    loanTermEntry.insert(0, "10")
    loanTermEntry.place(x=253, y=150)

    compoundedEntry = Entry(window, width=33)
    compoundedEntry.insert(0, "12")
    compoundedEntry.place(x=265, y=175)

    paymentsEntry = Entry(window, width=33)
    paymentsEntry.insert(0, "12")
    paymentsEntry.place(x=265, y=200)

    def loanCalc():
        try:
            P = float(loanAmountEntry.get())
            r = float(interestRateEntry.get())/100
            n = int(compoundedEntry.get())
            t = int(loanTermEntry.get())
            b = int(paymentsEntry.get())
            a = t * b
        except ValueError:
            messagebox.showerror(title="Error", message="Please enter a valid number.                                                ")
       
        try:
            res = P*(1+(r/n))**(n*t)
            res2 = res/(b*t)
            interestAmount = res-P 
            resRounded = round(res, 2)
            res2Rounded = round(res2, 2)
            intAmRounded = round(interestAmount, 2)
        except ZeroDivisionError:
            messagebox.showerror(title="Error", message="Please enter a number above zero in the Compounded and/or Payments Per Year input boxes.                                                ")
        except OverflowError:
            messagebox.showerror(title="Error", message="Please enter a reasonable number.                                                ")

        f = "{:,}".format(resRounded)
        f2 = "{:,}".format(res2Rounded)
        f3 = "{:,}".format(intAmRounded)
        f4 = "{:,}".format(a)

        final = Label(window, font=("Times New Roman", 15), text=f"${f}                                                                             ").place(x=328, y=285)
        final2 = Label(window, font=("Times New Roman", 15), text=f"${f2}                                                                             ").place(x=359, y=315)
        final3 = Label(window, font=("Times New Roman", 15), text=f"${f3}                                                                             ").place(x=319, y=345)
        final4 = Label(window, font=("Times New Roman", 15), text=f"{f4}                                                                             ").place(x=394, y=375)
    
    calcButton = Button(window, text="        Calculate        ", background="#f71661", foreground="#ffffff", activebackground="#cc1452", activeforeground= "#ffffff", command=loanCalc).place(x=300, y=241)
    resultLabel = Label(window, font=("Times New Roman", 15), text="Your total payment is:").place(x=130, y=285)
    resultLabel2 = Label(window, font=("Times New Roman", 15), text="Your periodic payment is:").place(x=130, y=315)
    resultLabel3 = Label(window, font=("Times New Roman", 15), text="Your total interest is:").place(x=130, y=345)
    resultLabel4 = Label(window, font=("Times New Roman", 15), text="Your total number of payments:").place(x=130, y=375)

    window.config(menu=menubar)
    window.mainloop()

def newWindow():
    app()

app()