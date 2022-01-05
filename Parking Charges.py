from tkinter import*
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.myWindow = Tk()
        self.myWindow.geometry("300x300+100+100") #width times height - initial value x + inital y
        self.myWindow.title("tk")
        self.choice = StringVar()
        self.choice.set(0)
        self.rb1 = Radiobutton(self.myWindow,text= "Daytime (6:00am - 5:59pm)", font = 14,
                               variable = self.choice, value = 0.07)
        self.rb1.place(x=10,y=40)
        self.rb2 = Radiobutton(self.myWindow,text= "Evening (6:00pm - 11:59pm)", font = 14,
                               variable = self.choice, value = 0.12)
        self.rb2.place(x=10,y=75)
        self.rb3 = Radiobutton(self.myWindow,text= "Off-Peak (12:00am - 5:59am)", font = 14,
                               variable = self.choice, value = 0.05)
        self.rb3.place(x=10,y=110)
        self.label = Label(self.myWindow, text="Number of minutes: " , font= 14)
        self.label.place(x=25,y=155)
        self.entry= Entry(self.myWindow , width = 10, font = 14)
        self.entry.place(x=155,y=155)
        self.button1 = Button(self.myWindow, text = "Display Changes" , command=self.do_this)
        self.button1.place(x=55,y=190)
        self.button2 = Button(self.myWindow, text = "Quit" , font = 16 , command= self.myWindow.destroy)
        self.button2.place(x=165,y=190)

        mainloop()

    def do_this(self):
            if float(self.entry.get()) < 0:
                tkinter.messagebox.showinfo("Error" , "Please enter a positive number for minutes.")
            else:
                rate = float(self.choice.get())
                charge = rate * float(self.entry.get())
                tkinter.messagebox.showinfo("Total Charges" , "Your total charges = $" + str(format(charge, '.2f')))
        
my_gui = MyGUI()
