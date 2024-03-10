from datetime import datetime
import customtkinter as ctk


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    time_label.configure(text=current_time)
    app.after(1000, update_time)
def update_date():
    current_date = datetime.today().strftime("%m-%d-%y")
    date_label.configure(text=current_date)
    app.after(1000, update_date)
#Start CTK GUI
app = ctk.CTk()
app.geometry("480x320")
#Tab View
tabview = ctk.CTkTabview(app)
tabview.pack(padx=10,pady=10)


clock_tab = tabview.add("Home")
info_tab = tabview.add("Info")
tabview.set("Home")
#Widgets
t1 = ctk.CTkLabel(clock_tab,text="Welcome",font=('Times New Roman',35))
t1.pack(padx=20,pady=20)

time_label = ctk.CTkLabel(clock_tab,text_color="blue",text="00:00:00", font=('Helvetica',32))
time_label.pack(padx=10,pady=10)

date_label = ctk.CTkLabel(clock_tab,text_color="red",text="date",font=("Helvetica",30))
date_label.pack(padx=10,pady=10)



update_time()
update_date()
app.mainloop()