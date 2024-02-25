import tkinter as tk

class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")
        self.ans = "" #curr exp
        self.res = "" #total exp
        self.dispfr = self.display_frame()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.totalLabel, self.label = self.dislabel()
        self.btnfr = self.button_frame()
        self.btnfr.rowconfigure(0,weight=1)
        for i in range(1,5):
            self.btnfr.rowconfigure(i,weight=1)
            self.btnfr.columnconfigure(i,weight=1)
        self.crDigiButtons()
        self.crOperButtons()
        self.crSpecialButtons()
        self.bind()

    def dislabel(self):
        totalLabel = tk.Label(self.dispfr, text=self.res, anchor=tk.E, bg="#1a1a1a", fg="#66b3ff", padx=24, font=("Arial", 16))
        totalLabel.pack(expand=True, fill="both")

        label = tk.Label(self.dispfr, text=self.ans, anchor=tk.E, bg="#1a1a1a", fg="#66b3ff", padx=24, font=("Arial", 40, "bold"))
        label.pack(expand=True, fill="both")   
        return totalLabel, label
    
    def add(self,value):
        self.ans+=str(value)
        self.update_label()
    def display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#000000")
        frame.pack(expand=True, fill="both")
        return frame
    def crSpecialButtons(self):
        self.crClearButton()
        self.crEqualButton()
    def crDigiButtons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.btnfr, text=str(digit), bg="#000000", fg="#66b3ff",font=("Arial",24,"bold"),borderwidth=0,command=lambda x=digit:self.add(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def addop(self,op):
        self.ans+=op
        self.res+=self.ans
        self.ans=""
        self.update_total_label()
        self.update_label()
    def crOperButtons(self):
        i=0
        for op,sym in self.operations.items():
            button=tk.Button(self.btnfr,text=sym,bg="#000000",fg="#b3ff99",font=("Arial",20),borderwidth=0,command=lambda x=op:self.addop(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    
    def clear(self):
        self.ans=""
        self.res=""
        self.update_label()
        self.update_total_label()
    
    def evalex(self):
        self.res+=self.ans
        self.update_total_label()
        try:
            self.ans=str(eval(self.res))
            self.res=""
        except Exception as e:
            self.ans="Error"
        finally:
            self.update_label()
    def crClearButton(self):
        button = tk.Button(self.btnfr, text="C", bg="#000000", fg="#00ff00",font=("Arial",20,"bold"),borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,columnspan=3,sticky=tk.NSEW)

    def crEqualButton(self):
        button = tk.Button(self.btnfr, text="=", bg="#99ffff", fg="#006666",font=("Arial",20),borderwidth=0,command=self.evalex)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def bind(self):
        self.window.bind("<Return>",lambda ev:self.evalex())
        for i in self.digits:
            self.window.bind(str(i),lambda ev,digit=i:self.add(digit))
        for i in self.operations:
            self.window.bind(i,lambda ev,op=i:self.addop(op))
    def button_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_total_label(self):
        temp=self.res
        for op,sym in self.operations.items():
            temp=temp.replace(op,f'{sym}')
        self.totalLabel.config(text=temp)

    def update_label(self):
        self.label.config(text=self.ans[:11])
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    cal = Calc()
    cal.run()
