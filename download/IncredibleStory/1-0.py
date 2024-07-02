import tkinter as tk
from tkinter import filedialog, messagebox
from random import *

# 窗口类
class Window(tk.Tk):
    # 变量
    width, height = 400, 410
    label1, entry, label2, text, button, button_again = None, None, None, None, None, None
    main, names, married = None, None, None
    # 初始化
    def __init__(self):
        super().__init__()
        self.title("炸裂情感史")
        # self.geometry("%sx%s" % (self.width, self.height))
        self.input()

    # 输入数据
    def input(self):
        # 主角
        self.label1 = tk.Label(self, text="请输入主角名：")
        self.label1.pack(anchor="nw")
        self.entry = tk.Entry(self)
        self.entry.pack(fill="x")
        # 配角
        self.label2 = tk.Label(self, text="请输入配角名（一行一个）：")
        self.label2.pack(anchor="nw")
        self.text = tk.Text(self)
        self.text.pack(fill="both")
        # 确定
        self.button = tk.Button(self, text="确定", command=self.get)
        self.button.pack(fill="both")

    # 读取数据
    def get(self):
        # 读取
        self.main = self.entry.get()
        self.names = self.text.get("1.0", tk.END)
        # 配角名称列表
        self.names = self.names.split('\n')
        if self.names[len(self.names)-1] == "":
            self.names.pop()
        self.clear()
        self.output()

    # 输出生成结果
    def output(self):
        # 文本
        self.text = tk.Text(self, state="disable")
        self.text.pack(fill="both")
        # 保存按钮
        self.button.config(text="保存", command=self.save)
        self.button.pack(fill="x")
        # 重来按钮
        self.button_again = tk.Button(self, text="再来一次", command=self.again)
        self.button_again.pack(fill="x")
        # 生成算法部分
        self.result()

    # 生成算法
    def result(self):
        self.write(self.main+"从小喜欢"+choice(self.names))
        self.write(self.main+"和"+choice(self.names)+"是青梅竹马")
        self.write(self.main+"的白月光是"+choice(self.names))
        self.write(self.main+"的初恋是"+choice(self.names))
        self.names.append(self.main)
        while len(self.names) > 1:
            self.a, self.b = None, None
            while (self.a == self.b):
                self.a = randint(0, len(self.names)-1)
                self.b = randint(0, len(self.names)-1)
            self.sentence(self.names[self.a], self.names[self.b])
        self.write(self.names[0]+"是最后赢家")

    # 单次剧情生成
    def sentence(self, x, y):
        self.c = randint(0, 7)
        if self.c == 0:
            self.write(x+"和"+y+"结婚了")
        elif self.c == 1:
            self.write(x+"爱上了"+y)
        elif self.c == 2:
            self.write(x+"绿了"+y)
        elif self.c == 3:
            self.write(x+"失手杀了"+y)
            self.names.remove(y)
        elif self.c == 4:
            self.write(x+"因爱生恨，杀了"+y)
            self.names.remove(y)
        elif self.c == 5:
            self.write(x+"爱上了错误的人，自杀了")
            self.names.remove(x)
        elif self.c == 6:
            self.write(x+"抢婚了"+y+"的婚礼")
        elif self.c == 7:
            self.write(x+"发现"+y+"绿了他，于是和他离婚了")

    # 保存为txt
    def save(self):
        # 文件路径
        self.path = tk.filedialog.asksaveasfilename(title='保存文件', filetypes=[("文本文件", "*.txt")])
        self.file_text = self.text.get("1.0", tk.END)
        # 写入内容
        if self.path != "":
            with open(file=self.path, mode="a+", encoding="utf-8") as self.file:
                self.file.write(self.file_text)
            messagebox.showinfo(title="提示", message="保存成功！")

    # 重来
    def again(self):
        self.button_again.pack_forget()
        self.clear()
        self.input()

    # 清空
    def clear(self):
        self.label1.pack_forget()
        self.label2.pack_forget()
        self.text.pack_forget()
        self.button.pack_forget()
        self.entry.pack_forget()

    # 写入
    def write(self, text):
        self.text.config(state="normal")
        self.text.insert("end", text+"\n")
        self.text.config(state="disable")

if __name__ == "__main__":
    win = Window()
    win.mainloop()
