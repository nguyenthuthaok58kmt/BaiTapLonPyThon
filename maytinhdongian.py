#Khai báo thư viện tkinter(thư viện đồ họa GUI)
import tkinter as tk
from tkinter import messagebox
#Messengerbox để hiển thị thông báo khi thao tác lỗi

#Khai báo hàm tính kết quả
def tính_kết_quả():
    #try-except để tránh quá trình lỗi hệ thống và bị dừng chương trình
    try:
        #khai báo các biến: số 1 và 2 kiểu float, biến phép tính kiểu string
        sothunhat = float(Entry1.get())
        sothuhai = float(Entry2.get())
        pheptinh = biến_pheptinh.get()
    #Tạo radio lựa chọn các phép tính, kết quả được lưu vào biến kết_quả
        if pheptinh == "+":
            kết_quả = sothunhat + sothuhai
        elif pheptinh == "-":
            kết_quả = sothunhat - sothuhai
        elif pheptinh == "*":
            kết_quả = sothunhat * sothuhai
        elif pheptinh == "/":
            #Nếu số thứ 2 = 0 (chia cho 0) thì thông báo lỗi 
            if sothuhai == 0:
                raise ZeroDivisionError
            #Nếu khác 0 thì thực hiện chia bình thường
            kết_quả = sothunhat / sothuhai
        #Trường hợp nếu không chọn phép toán nào
        else:
            raise ValueError("Phép toán không hợp lệ.")
        #Cuối cùng biến kết quả được hiển thị 
        Nhãn_kết_quả.config(text=f"Kết quả: {kết_quả}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")
    except ZeroDivisionError:
        messagebox.showerror("Lỗi", "Không thể chia cho 0.")
#Hàm reset chương trình
def reset():
    #Xóa dữ liệu từ 2 ô entry số 1 và 2 đặt lại dữ liệu gốc là 0
    Entry1.delete(0, tk.END)
    Entry2.delete(0, tk.END)
    # Đặt biến phép tính về mặc định giá trị là "+"
    biến_pheptinh.set("+")
    #Xóa dữ liệu biến kết quả
    Nhãn_kết_quả.config(text="Kết quả:")

# Giao diện chính
Cửa_sổ = tk.Tk()
Cửa_sổ.title("Máy tính đơn giản")

#Phần còn lại là thiết kết layout sử dụng grid ( bao gồm dùng entry và label)
# Nhãn cho số thứ nhất
tk.Label(Cửa_sổ, text="Số thứ nhất:").grid(row=0, column=0)
 #Entry cho số thứ nhất
Entry1 = tk.Entry(Cửa_sổ)
Entry1.grid(row=0, column=1)

# Nhãn cho số thứ hai
tk.Label(Cửa_sổ, text="Số thứ hai:").grid(row=1, column=0)
 #Entry cho số thứ nhất
Entry2 = tk.Entry(Cửa_sổ)
Entry2.grid(row=1, column=1)

#Nói đến đây xong kéo nhanh xuống rồi chạy ctrinh
 #Chạy kết quả đúng
 #Chạy chia cho 0
 #Chạy 1 số là chữ
 
# Phép toán - Radio buttons
tk.Label(Cửa_sổ, text="Phép toán:").grid(row=2, column=0)
biến_pheptinh = tk.StringVar()
biến_pheptinh.set("+")

Khung_pheptinh = tk.Frame(Cửa_sổ)
Khung_pheptinh.grid(row=2, column=1)

for phép in ["+", "-", "*", "/"]:
    tk.Radiobutton(Khung_pheptinh, text=phép, variable=biến_pheptinh, value=phép).pack(side=tk.LEFT)

# Nút Tính và Làm mới
tk.Button(Cửa_sổ, text="Tính", command=tính_kết_quả).grid(row=3, column=0)
tk.Button(Cửa_sổ, text="Làm mới", command=reset).grid(row=3, column=1)

# Nhãn hiển thị kết quả 
Nhãn_kết_quả = tk.Label(Cửa_sổ, text="Kết quả:")
Nhãn_kết_quả.grid(row=4, column=0, columnspan=2)

# Bắt đầu vòng lặp giao diện
Cửa_sổ.mainloop()
