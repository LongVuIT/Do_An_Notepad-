import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import scrolledtext

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        text.delete(1.0, tk.END)
        text.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        file.write(text.get(1.0, tk.END))

def format_text():
    font = simpledialog.askstring("Font", "Nhập font chữ (ví dụ: Arial)", parent=root)
    size = simpledialog.askinteger("Size", "Nhập kích thước font chữ (ví dụ: 12)", parent=root)
    text.tag_configure("format", font=(font, size))

def word_count():
    words = text.get(1.0, tk.END).split()
    messagebox.showinfo("Đếm từ", f"Tổng số từ: {len(words)}")

def search_text():
    search = simpledialog.askstring("Tìm kiếm", "Nhập từ cần tìm", parent=root)
    start = 1.0
    while True:
        start = text.search(search, start, stopindex=tk.END)
        if not start:
            break
        end = f"{start}+{len(search)}c"
        text.tag_add("search", start, end)
        start = end

def about():
    messagebox.showinfo("Thông tin", "Notepad\nContact to Vũ")

root = tk.Tk()
root.title("Notepad")
root.configure(background="lightblue")

text = scrolledtext.ScrolledText(root, wrap="word")
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Tạo mới", command=new_file)
file_menu.add_command(label="Mở", command=open_file)
file_menu.add_command(label="Lưu", command=save_file)
menu_bar.add_cascade(label="Tệp", menu=file_menu)

edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Định dạng văn bản", command=format_text)
edit_menu.add_command(label="Đếm từ", command=word_count)
edit_menu.add_command(label="Tìm kiếm văn bản", command=search_text)
menu_bar.add_cascade(label="Chỉnh sửa", menu=edit_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Thông tin", command=about)
menu_bar.add_cascade(label="Trợ giúp", menu=help_menu)

text.tag_configure("search", background="yellow")
root.config(menu=menu_bar)
root.mainloop()