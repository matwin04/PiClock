from datetime import datetime
import customtkinter as ctk

def btn1():
    print("BTN1")
    t1.configure(text='penis')
def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000, update_time)
def update_date():
    current_date = datetime.today().strftime("%m-%d-%y")
    date_label.configure(text=current_date)
    app.after(1000, update_date)
app = ctk.CTk()
app.geometry("480x320")
t1 = ctk.CTkLabel(app,text_color="white",text="Welcome")
t1.pack(padx=20,pady=20)

time_label = ctk.CTkLabel(app,text_color="blue",text="00:00:00", font=('Helvetica',32))
time_label.pack(padx=10,pady=10)

date_label = ctk.CTkLabel(app,text_color="red",text="date",font=("Helvetica",30))
date_label.pack(padx=10,pady=10)

b1 = ctk.CTkButton(app,text="Button 1", command=btn1)
b1.pack(padx=10,pady=10)
update_time()
update_date()
app.mainloop()