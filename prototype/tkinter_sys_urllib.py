import sys
import urllib.request
import tkinter as tk
from tkinter import messagebox


class Browser:

    def __init__(self, root):
        self.root = root
        self.root.title("Python Browser")

        self.back_btn = tk.Button(self.root, text="<", command=self.back)
        self.back_btn.pack(side="left")

        self.forward_btn = tk.Button(self.root, text=">", command=self.forward)
        self.forward_btn.pack(side="left")

        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(side="left", padx=5)

        self.go_btn = tk.Button(self.root, text="Go", command=self.go)
        self.go_btn.pack(side="left")

        self.webview = tk.Text(self.root, wrap="word")
        self.webview.pack(side="top", fill="both", expand=True)

        self.history = []
        self.current = -1

    def back(self):
        if self.current > 0:
            self.current -= 1
            url = self.history[self.current]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.update_webview()

    def forward(self):
        if self.current < len(self.history) - 1:
            self.current += 1
            url = self.history[self.current]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(0, url)
            self.update_webview()

    def go(self):
        url = self.url_entry.get()
        if url:
            try:
                response = urllib.request.urlopen(url)
                html = response.read().decode()
                self.webview.delete("1.0", tk.END)
                self.webview.insert("1.0", html)
                if url != self.get_current_url():
                    self.history = self.history[:self.current+1]
                    self.history.append(url)
                    self.current += 1
            except:
                messagebox.showerror("Error", "Invalid URL")

    def update_webview(self):
        url = self.history[self.current]
        self.url_entry.delete(0, tk.END)
        self.url_entry.insert(0, url)
        self.go()

    def get_current_url(self):
        return self.history[self.current] if self.history else ""


if __name__ == "__main__":
    root = tk.Tk()
    browser = Browser(root)
    root.mainloop()
