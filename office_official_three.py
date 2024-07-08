import customtkinter as ctk
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import office_official_four
from Dictionary import Word
import sqlite3

def page():
    global counter
    counter = 0
    app = ctk.CTk()
    app.title('Founders Information')
    window_width = 1115
    window_height = 550
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
    app.config(bg = '#161C25')
    app.resizable(False , False)
    def validate_input(action, value):
        # Check if the input is empty or if it's a digit
        if action == '1':  # Insertion or deletion (1 means the text is being inserted/deleted)
            return value.isdigit() or value == ""
        return True
    validation = app.register(validate_input)
    font1 = ('Arial' , 20 , 'bold')
    font2 = ('Arial' , 14 , 'bold')
    name_label = ctk.CTkLabel(app, font = font1, text = 'Name:', text_color='yellow', bg_color='#161C25')
    name_label.place(x = 20 , y = 20)
    name_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180)
    name_entry.place(x = 180 , y = 20)
    specialization_label = ctk.CTkLabel(app, font = font1, text = 'Specialization:', text_color='yellow', bg_color='#161C25')
    specialization_label.place(x = 20 , y = 80)
    specialization_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180)
    specialization_entry.place(x = 180 , y = 80)
    registration_number_label = ctk.CTkLabel(app, font = font1, text = 'Registration number:', text_color='yellow', bg_color='#161C25')
    registration_number_label.place(x = 480 , y = 20)
    registration_number_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180, validate="key", validatecommand=(validation, '%d', '%S'))
    registration_number_entry.place(x = 700 , y = 20)
    graduation_year_label = ctk.CTkLabel(app, font = font1, text = 'Graduation year:', text_color='yellow', bg_color='#161C25')
    graduation_year_label.place(x = 520 , y = 80)
    graduation_year_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180, validate="key", validatecommand=(validation, '%d', '%S')) 
    graduation_year_entry.place(x = 700 , y = 80)
    founder_id_label = ctk.CTkLabel(app, font = font1, text = 'Founder ID:', text_color='yellow', bg_color='#161C25')
    founder_id_label.place(x = 300 , y = 140)
    founder_id_entry = ctk.CTkEntry(app, font = font1, text_color = 'red' , bg_color ='#161C25', border_color='#161C25', border_width=2, width = 180, validate="key", validatecommand=(validation, '%d', '%S'))
    founder_id_entry.place(x = 430, y = 140)
    def add_to_treeview():
        nm = name_entry.get()
        sp = specialization_entry.get()
        rg = registration_number_entry.get()
        gu = graduation_year_entry.get()
        id = founder_id_entry.get()
        
        # Get all item identifiers in the Treeview
        item_ids = tree.get_children()
        for item_id in item_ids:
            # Retrieve the values from the specified columns ('registration number' and 'Founder ID')
            registration_number = tree.item(item_id, 'values')[2]  # index 2 corresponds to the 'registration number' column
            founder_id = tree.item(item_id, 'values')[4]  # index 4 corresponds to the 'Founder ID' column
            if (rg == registration_number) or (id == founder_id):
                messagebox.showerror(title='Registered Founder', message='The founder already exists!')
                return 
        global counter
        counter = counter + 1
        tree.insert('', "end", values=(nm,sp,rg,gu,id))
        name_entry.delete(0,'end')
        specialization_entry.delete(0,'end')
        registration_number_entry.delete(0,'end')
        graduation_year_entry.delete(0,'end')
        founder_id_entry.delete(0,'end')
        
    def insert_button_function():
        name = name_entry.get()
        spe = specialization_entry.get()
        reg_temp = registration_number_entry.get()
        gru_temp = graduation_year_entry.get()
        id_temp = founder_id_entry.get()
        '''if (name == '' and id_temp == '') or (name == '' and spe == '' and  reg_temp == '' and gru_temp == '') or (spe == '' and  reg_temp == '' and gru_temp == '' and id_temp == ''):
            messagebox.showwarning(title='Empty Field', message='There is a field(s) missing, please fill them in')
            return'''
        '''if id_temp == '':
            if(name == '' or spe == '' or  reg_temp == '' or gru_temp == ''):
                messagebox.showwarning(title='Empty Field', message='There is a field(s) missing, please fill them in')
                return'''
        

        if id_temp != '': # if the entered values related to normal founder (not eng)
                File = 'DataBase.db'
                connection = sqlite3.connect(File)
                cursor = connection.cursor()
                if id_temp != '':
                    fid = int(id_temp)
                cursor.execute("""select * from Founders where F_ID = ?""",(fid,))
                find = cursor.fetchone()

                if find == None:
                    messagebox.showerror(title='Invalid input', message='please check the entered Founder ID/name')
                    return
                
                else:
                    fname = find[0] + ' ' + find[1] + ' ' + find[2]
                    if fname != name:
                        messagebox.showerror(title='Invalid input', message='please check the entered name')
                        return   
        else: #if the entered values related to founder engineer
            
            if name == '' or spe == '' or reg_temp == '' or gru_temp == '':
                messagebox.showwarning(title='Empty Field', message='There is a field(s) missing, please fill them in')
                return
            if reg_temp != '':
                reg = int(reg_temp)
            if gru_temp != '':
                gru = int(gru_temp)
            File = 'DataBase.db'
            connection = sqlite3.connect(File)
            cursor = connection.cursor()
            cursor.execute("""select * from Eng_Fnd where Eng_Registration_Number = ?""",(reg,))
            pr = cursor.fetchone()
            if pr == None:
                print('here')
                messagebox.showerror(title='Invalid input', message='please check the entered data for engineer founder')
                return
            
            cursor.execute("""select * from Engineers where Registration_Number = ?""",(reg,))
            find = cursor.fetchone()

            if find == None:
                messagebox.showerror(title='Invalid input', message='please check the entered registration number')
                return
                
            fname = find[1] + ' ' + find[2] + ' ' + find[3]
            if fname != name:
                messagebox.showerror(title='Invalid input', message='please check the entered name')
                return  
            elif find[4] != spe:
                messagebox.showerror(title='Invalid input', message='please check the entered specialization')
                return
            elif find[5] != gru:
                messagebox.showerror(title='Invalid input', message='please check the entered graduation year')
                return
        add_to_treeview()
    def on_enter(event):
        insert_button.invoke()
    insert_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Insert Data', fg_color='#05A312', hover_color='#00850B', bg_color='#161C25', cursor = 'hand2', corner_radius=15,width = 260, command = insert_button_function)
    insert_button.place(x =17 ,y =500)
    app.bind("<Return>", on_enter)
    def nextPage():
        classification_num = Word["classification_num"]
        File = 'DataBase.db'
        connection = sqlite3.connect(File)
        cursor = connection.cursor()
        cursor.execute(""" select * from Founders where Classification_Number = ?""" , (classification_num,))
        find = cursor.fetchall()
        if counter < len(find):
            messagebox.showwarning(title='Incomplete entry', message='You need to enter all of your office founders ')
            return
        
        app.destroy()
        office_official_four.page()
    next_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Next Page', fg_color='#161C25', hover_color='#FF5002', bg_color='#161C25',border_color='#F15704',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = nextPage)
    next_button.place(x =320 ,y =500)
    def finishing():
        app.destroy()
    close_button = ctk.CTkButton(app, font = font1, text_color='#fff', text = 'Close', fg_color='#E40404', hover_color='#AE0000', bg_color='#161C25',border_color='#E40404',border_width=2, cursor = 'hand2', corner_radius=15, width = 260, command = finishing)
    close_button.place(x =623 ,y =500)
    style = ttk.Style(app)
    style.theme_use('clam')
    style.configure('Treeview', font = font2, foreground = '#fff', background = '#000',fieldbackground = '#313837', rowheight=40)# Increase font size for Treeview structure via rowheight
    style.configure('Treeview.Heading', font=('Arial', 18))# Increase the font size for column names
    style.map('Treeview', background = [('selected', '#1A8F2D')])
    tree = ttk.Treeview(app,height = 5)
    tree['columns'] = ('name', 'specialization' , 'registration number', 'Graduation year','Founder ID')
    tree.column('#0', width = 0, stretch= tk.NO) # to hide the default first column of the treeview
    tree.column('name', anchor = tk.CENTER, width = 280)
    tree.column('specialization', anchor = tk.CENTER, width = 200)
    tree.column('registration number', anchor = tk.CENTER, width = 220)
    tree.column('Graduation year', anchor = tk.CENTER, width = 200)
    tree.column('Founder ID', anchor = tk.CENTER, width = 180)
    tree.heading('name',text = 'name')
    tree.heading('specialization',text = 'specialization')
    tree.heading('registration number',text = 'registration number')
    tree.heading('Graduation year',text = 'Graduation year')
    tree.heading('Founder ID',text = 'Founder ID')
    tree.place(x =22, y = 230)
    app.mainloop()