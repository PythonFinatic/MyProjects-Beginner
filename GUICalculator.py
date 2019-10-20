from tkinter import *

root = Tk()

frame = Frame(root)

def clear():
	outputNumber.delete(0, END)

def button_click(num):
	current = outputNumber.get()
	outputNumber.delete(0, END)
	outputNumber.insert(0, str(current) + str(num))

def add_button():
	first_number = outputNumber.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	outputNumber.delete(0, END)

def equal_button():
	second_number = outputNumber.get()
	outputNumber.delete(0, END)

	# if math != "decimal":

	if math == "addition":
		outputNumber.insert(0, f_num + int(second_number))

	elif math == "subtract":
		outputNumber.insert(0, f_num - int(second_number))
	
	elif math == "multiply":
		outputNumber.insert(0, f_num * int(second_number))

	# if math == "decimal":
	# 	if math == "addition":
	# 		outputNumber.insert(0, f_num + float(second_number))

	# 	elif math == "subtract":
	# 		outputNumber.insert(0, f_num - float(second_number))
		
	# 	elif math == "multiply":
	# 		outputNumber.insert(0, f_num * float(second_number))

def subtract_button():
	first_number = outputNumber.get()
	global f_num
	global math
	math = "subtract"
	f_num = int(first_number)
	outputNumber.delete(0, END)

def multiply_button():
	first_number = outputNumber.get()
	global f_num
	global math
	math = "multiply"
	f_num = int(first_number)
	outputNumber.delete(0, END)

# def decimal_button():
# 	first_number = outputNumber.get()
# 	global f_num
# 	global math
# 	math = "decimal"
# 	f_num = str(first_number)
# 	f_num + "."
# 	f_num = int(first_number)
	

class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        

    def on_leave(self, e):
        self['background'] = self.defaultBackground


outputNumber = Entry(root, width=30, borderwidth=5)
button0 = HoverButton(root, fg="white", bg="black", text="0", padx=60, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(0))
button1 = HoverButton(root, fg="white", bg="black", text="1", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(1))
button2 = HoverButton(root, fg="white", bg="black", text="2", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(2))
button3 = HoverButton(root, fg="white", bg="black", text="3", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(3))
button4 = HoverButton(root, fg="white", bg="black", text="4", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(4))
button5 = HoverButton(root, fg="white", bg="black", text="5", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(5))
button6 = HoverButton(root, fg="white", bg="black", text="6", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(6))
button7 = HoverButton(root, fg="white", bg="black", text="7", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(7))
button8 = HoverButton(root, fg="white", bg="black", text="8", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(8))
button9 = HoverButton(root, fg="white", bg="black", text="9", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=lambda : button_click(9))
buttonAdd = HoverButton(root, fg="white", bg="orange", text="+", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=add_button)
buttonSubtract = HoverButton(root, fg="white", bg="orange", text="-", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=subtract_button)
buttonMultiply = HoverButton(root, fg="white", bg="orange", text="x", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=multiply_button)
# buttonDecimal = HoverButton(root, fg="white", bg="black", text=".", padx=20, pady=10, borderwidth=5, activebackground="yellow", command=decimal_button)
buttonEqual = HoverButton(root, fg="white", bg="orange", text="=", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=equal_button)
buttonClear = HoverButton(root, fg="black", bg="white", text="C", padx=25, pady=10, borderwidth=5, activebackground="yellow", command=clear)


outputNumber.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=0, columnspan=2)
buttonMultiply.grid(row=1, column=3)
buttonEqual.grid(row=4, column=2)
buttonSubtract.grid(row=2, column=3)
# buttonDecimal.grid(row=4, column=1)
buttonAdd.grid(row=3, column=3)
buttonClear.grid(row=4, column=3)



root.title("GUI Calculator")









root.mainloop()