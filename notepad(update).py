import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import scrolledtext
from tkinter import font as tkfont
import os

def new_file():
    if text.get(1.0, tk.END) != '\n':  # Kiểm tra xem có thay đổi chưa
        if messagebox.askyesno("Xác nhận", "Bạn có muốn lưu thay đổi trước khi tạo file mới?"):
            save_file()
    text.delete(1.0, tk.END)
    root.title("Notepad - Mới")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(1.0, file.read())
        root.title(f"Notepad - {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END).strip())
        root.title(f"Notepad - {file_path}")

def format_text():
    font = simpledialog.askstring("Font", "Nhập font chữ (ví dụ: Arial)", parent=root)
    size = simpledialog.askinteger("Size", "Nhập kích thước font chữ (ví dụ: 12)", parent=root)
    text.configure(font=(font, size))

def word_count():
    words = text.get(1.0, tk.END).split()
    messagebox.showinfo("Đếm từ", f"Tổng số từ: {len(words)}")

def search_text():
    search = simpledialog.askstring("Tìm kiếm", "Nhập từ cần tìm", parent=root)
    if search:
        start = 1.0
        text.tag_remove("search", 1.0, tk.END)  # Xóa các kết quả tìm kiếm cũ
        while True:
            start = text.search(search, start, stopindex=tk.END, nocase=True)  # Tìm kiếm không phân biệt chữ hoa chữ thường
            if not start:
                break
            end = f"{start}+{len(search)}c"
            text.tag_add("search", start, end)
            start = end
        text.tag_configure("search", background="yellow")

def replace_text():
    search = simpledialog.askstring("Tìm kiếm", "Nhập từ cần tìm", parent=root)
    replace = simpledialog.askstring("Thay thế", "Nhập từ thay thế", parent=root)
    if search and replace:
        content = text.get(1.0, tk.END)
        updated_content = content.replace(search, replace)
        text.delete(1.0, tk.END)
        text.insert(1.0, updated_content)

def change_background_color():
    color = simpledialog.askstring("Màu nền", "Nhập mã màu Hex (ví dụ: #f0f0f0):")
    if color:
        text.configure(bg=color)

def undo():
    text.edit_undo()

def redo():
    text.edit_redo()

def exit_program():
    if text.get(1.0, tk.END) != '\n':  # Kiểm tra nếu có thay đổi
        if messagebox.askyesno("Xác nhận", "Bạn có muốn lưu thay đổi trước khi thoát?"):
            save_file()
    root.quit()

def about():
    messagebox.showinfo("Thông tin", "Notepad\nLiên hệ với Vũ")

root = tk.Tk()
root.title("Notepad")
root.configure(background="lightblue")

# Tạo text widget và bật tính năng undo/redo
text = scrolledtext.ScrolledText(root, wrap="word", undo=True)
text.pack(expand=True, fill="both")

menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Tạo mới", command=new_file)
file_menu.add_command(label="Mở", command=open_file)
file_menu.add_command(label="Lưu", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Thoát", command=exit_program)
menu_bar.add_cascade(label="Tệp", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Định dạng văn bản", command=format_text)
edit_menu.add_command(label="Đếm từ", command=word_count)
edit_menu.add_command(label="Tìm kiếm văn bản", command=search_text)
edit_menu.add_command(label="Thay thế văn bản", command=replace_text)
edit_menu.add_separator()
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
menu_bar.add_cascade(label="Chỉnh sửa", menu=edit_menu)

# View menu
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Thay đổi màu nền", command=change_background_color)
menu_bar.add_cascade(label="Xem", menu=view_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Thông tin", command=about)
menu_bar.add_cascade(label="Trợ giúp", menu=help_menu)

text.tag_configure("search", background="yellow")

root.config(menu=menu_bar)
root.protocol("WM_DELETE_WINDOW", exit_program)  # Xử lý khi đóng cửa sổ
root.mainloop()
