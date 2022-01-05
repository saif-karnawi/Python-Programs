from tkinter import*
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.myWindow = Tk()

        self.myWindow.geometry("300x500+100+100")
        self.myWindow.title("Currency Exchange")

        self.choice = StringVar()
        self.choice.set("0")
        self.rb1 = Radiobutton(self.myWindow,text= "USD", font = 14,
                          variable = self.choice, value = "USD")
        self.rb1.place(x=20,y=90)
        self.rb2 = Radiobutton(self.myWindow,text= "AUD", font = 14,
                          variable = self.choice, value = "AUD")
        self.rb2.place(x=20,y=120)
        self.rb3 = Radiobutton(self.myWindow,text= "GBP", font = 14,
                          variable = self.choice, value = "GBP")
        self.rb3.place(x=20,y=150)
        self.rb4 = Radiobutton(self.myWindow,text= "JPY", font = 14,
                          variable = self.choice, value = "JPY")
        self.rb4.place(x=20,y=180)
        
        self.label = Label(self.myWindow, text="Amount in CAD:" , font= 14)
        self.label.place(x=25,y=20)
        self.entry= Entry(self.myWindow , width = 10, font = 14)
        self.entry.place(x=150,y=20)
        self.label2 = Label(self.myWindow, text="Currency to convert to:" , font= 14)
        self.label2.place(x=25,y=60)
        
        self.button1 = Button(self.myWindow, text = "Display Results" , command=self.do_this)
        self.button1.place(x=65,y=215)
        self.button2 = Button(self.myWindow, text = "Quit" , font = 16 , command= self.myWindow.destroy)
        self.button2.place(x=175,y=215)
        
        self.enteredText = StringVar()
        self.label = Label(self.myWindow, textvariable = self.enteredText, font =30)
        self.label.place(x=45,y=310)
        

        
        mainloop()
        
    def do_this(self):
        
        if float(self.entry.get()) < 0:
            tkinter.messagebox.showinfo("Error" , "Please enter a positive number for the amount of CAD.")
            self.enteredText.set("")
        else:
                              
            dictionary = {"USD": 0.75 , "AUD": 1.02 , "GBP": 0.59 , "JPY": 88.14 , "0": "Error"}
            myRate = dictionary[(self.choice.get())]
            
            currency = self.choice.get()
            total = myRate * float(self.entry.get())
            self.enteredText.set("Current Exchange rate is : " + str(myRate) \
                               + "\nThe money in " + currency + " is : " + str(format(total, '.2f')))
              
            
        
my_gui = MyGUI()



