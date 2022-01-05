from tkinter import* 
import tkinter.messagebox 
class MyGUI: 
 def __init__(self): 
     self.myWindow = Tk() 
     self.myWindow.geometry("325x300+100+100") #width times height - initial value x + inital y  self.myWindow.title("Investment Calculator") 
  
     self.label = Label(self.myWindow, text="Investment Amount:" , font= 14)
     self.label.place(x=10,y=10) 
     self.entry= Entry(self.myWindow , width = 10, font = 14) 
     self.entry.place(x=200,y=10) 
  
     self.label2 = Label(self.myWindow, text="Years:" , font= 14) 
     self.label2.place(x=10,y=50) 
     self.entry2= Entry(self.myWindow , width = 10, font = 14) 
     self.entry2.place(x=200,y=50) 
  
     self.label3 = Label(self.myWindow, text="Annual Interest Rate:" , font= 14)
     self.label3.place(x=10,y=90) 
     self.entry3= Entry(self.myWindow , width = 10, font = 14) 
     self.entry3.place(x=200,y=90) 
  
     self.label4 = Label(self.myWindow, text="Future Value:" , font= 14)
     self.label4.place(x=10,y=130) 
  
     self.enteredText = StringVar() 
     self.label = Label(self.myWindow, textvariable = self.enteredText, font =30)
     self.label.place(x=200,y=130) 
  
  
     self.button1 = Button(self.myWindow, text = "Calculate" , command=self.do_this)
     self.button1.place(x=95,y=220) 
     self.button1 = Button(self.myWindow, text = "Quit" , command= self.myWindow.destroy)
     self.button1.place(x=170,y=220) 
  
  
 def do_this(self): 
  
  
  
     invest_amt = float(self.entry.get()) 
     years = float(self.entry2.get()) 
     interest_rate = float(self.entry3.get()) 
  
     if invest_amt < 0 or years < 0 or interest_rate < 0: 
             tkinter.messagebox.showinfo("Error" , "All numbers entered must be positive")
             self.enteredText.set("") 
     else: 
         future_value = invest_amt * ( 1 + (interest_rate / 100)) ** years
         self.enteredText.set(str(format(future_value, '.2f'))) 
  
  
  
my_gui = MyGUI()
