from tkinter import * 
from tkinter import messagebox
from datetime import datetime
import csv
import pandas as pd

name = Tk()
name.title('Thông tin nhân viên')
name.geometry('1024x400')

day = datetime.now()

ttin = {
    'ma': '',
    'ten': '',
    'gioi tinh': '',
    'ngay sinh': datetime.today(),
    'chuc vu': '',
    'don vi': '',
    'so cmnd': '',
    'ngay cap': '',
    'noi cap': '',
}

entries = {}

title = Label(name, text = 'THÔNG TIN NHÂN VIÊN', font = ('arial', 15, 'bold'))
title.place(x = 200, y = 1)
# Ma
ma = Label(name, text = 'Mã*', font = ('arial', 11, 'bold'))
ma.place(x = 10, y = 50)
ma1 = Entry(name, width= 20, font = ('arial', 9))
ma1.place(x = 10, y = 75)

# Ten
ten = Label(name, text = 'Tên*', font = ('arial', 11, 'bold'))
ten.place(x = 200, y = 50)
ten1 = Entry(name, width= 30, font = ('arial', 9))
ten1.place(x = 200, y = 75)

# Ngay sinh
ngaysinh = Label(name, text = 'Ngày sinh', font = 'arial 11 bold')
ngaysinh.place(x = 500, y = 50)
ngaysinh1 = Entry(name, width= 20, font = 'arial 9')
ngaysinh1.place(x = 500, y = 75)

# Gioi tinh
sex = Label(name, text = 'Giới tính', font = 'arial 11 bold')
sex.place(x = 670, y = 50)
select_opt = IntVar(value= 5)
sex1 = Radiobutton(name, text = 'Nam', font = 'arial 9', variable= select_opt, value= 0)
sex2 = Radiobutton(name, text = 'Nữ', font = 'arial 9', variable= select_opt, value= 1)
sex1.place(x = 670, y = 75)
sex2.place(x = 770, y = 75)

# Don vi 
donvi = Label(name, text = 'Đơn vị*', font = ('arial', 11, 'bold'))
donvi.place(x = 10, y = 100)
donvi1 = Entry(name, width= 57, font = ('arial', 9))
donvi1.place(x = 10, y = 125)

# Chuc danh
chuc = Label(name, text= 'Chức danh', font = ('arial', 11, 'bold'))
chuc.place(x = 10, y = 155)
chuc1 = Entry(name, width= 57, font = 'arial 9')
chuc1.place(x = 10, y = 180)

# So CMND
so = Label(name, text = 'Số CMND', font = 'arial 11 bold')
so.place(x = 500, y = 100)
so1 = Entry(name, width= 30, font = 'arial 9')
so1.place(x = 500, y = 125)

# Ngay cap
ngay = Label(name, text = 'Ngày cấp', font = 'arial 11 bold')
ngay.place(x = 723, y = 100)
ngay1 = Entry(name, width= 20, font = 'arial 9')
ngay1.place(x = 723, y = 125)

# Noi cap
noi = Label(name, text = 'Nơi cấp', font = 'arial 11 bold')
noi.place(x = 500, y = 150)
noi1 = Entry(name, width= 52, font = 'arial 9')
noi1.place(x = 500, y = 175)

def save_info():
    ttin['ma'] = ma1.get()
    ttin['ten'] = ten1.get()
    date_str = ngaysinh1.get()
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    formatted_date = date_obj.strftime('%d/%m/%Y')
    ttin['ngay sinh'] = formatted_date
    if select_opt.get() == 0 :
        ttin['gioi tinh'] = 'Nam'
    if select_opt.get() == 1 :
        ttin['gioi tinh'] = "Nu"
    ttin['chuc vu'] = chuc1.get()
    ttin['don vi'] = donvi1.get()
    ttin['so cmnd'] = so1.get()
    ttin['ngay cap'] = ngay1.get()
    ttin['noi cap'] = noi1.get()
    with open('employees.csv', 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames= ttin.keys())
        writer.writerow(ttin)
    messagebox.showinfo("Thông báo", "Lưu dữ liệu thành công!")

def show_birthdays():
    today = datetime.today().strftime('%d/%m/%Y')
    with open('employees.csv', 'r') as f:
        reader = csv.DictReader(f)
        birthdays = [row for row in reader if row['ngay sinh'] == today]
    if birthdays:
        messagebox.showinfo("Sinh nhật hôm nay", "\n".join([f"{row['ten']} {row['ma']}" for row in birthdays]))
    else:
        messagebox.showinfo("Sinh nhật hôm nay", "Không có nhân viên nào sinh nhật hôm nay.")

def export_data():
    try:
        df = pd.read_csv('employees.csv')
        df['ngay sinh'] = pd.to_datetime(df['ngay sinh'], format='%d/%m/%Y')
        df = df.sort_values(by='ngay sinh', ascending=False)
        df.to_excel('employees.xlsx', index=False)
        messagebox.showinfo("Thông báo", "Xuất dữ liệu thành công!")
    except FileNotFoundError:
        messagebox.showerror("Lỗi", "File employees.csv không tồn tại.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# Nut
nut = Button(name, text = 'Xác nhận', font = 'arial 10 bold', command= save_info)
nut.place(x = 200, y = 220)
nut1 = Button(name, text = 'Sinh nhật ngày hôm nay', font = 'arial 10 bold', command= show_birthdays)
nut1.place(x = 280, y = 220)
nut3 = Button(name, text = 'Xuất toàn bộ danh sách', font = 'arial 10 bold', command= export_data)
nut3.place(x = 460, y = 220)
name.mainloop()
