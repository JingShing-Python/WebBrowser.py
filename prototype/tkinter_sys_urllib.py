import tkinter as tk
import sys
import urllib.request

class WebBrowser:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")

        self.url_label = tk.Label(master, text="URL:")
        self.url_label.pack(side=tk.LEFT)

        self.url_entry = tk.Entry(master, width=80)
        self.url_entry.pack(side=tk.LEFT)

        self.go_button = tk.Button(master, text="Go", command=self.load_page)
        self.go_button.pack(side=tk.LEFT)

        self.back_button = tk.Button(master, text="<", command=self.back_page)
        self.back_button.pack(side=tk.LEFT)

        self.forward_button = tk.Button(master, text=">", command=self.forward_page)
        self.forward_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(master, text="Quit", command=self.quit_browser)
        self.quit_button.pack(side=tk.LEFT)

        self.webview = tk.Text(master)
        self.webview.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.history = []
        self.current_page = 0

    def load_page(self):
        url = self.url_entry.get()
        try:
            response = urllib.request.urlopen(url)
            html = response.read().decode()
            self.webview.delete(1.0, tk.END)
            self.webview.insert(tk.END, html)
            self.history.append(url)
            self.current_page = len(self.history) - 1
        except Exception as e:
            self.webview.delete(1.0, tk.END)
            self.webview.insert(tk.END, str(e))

    def back_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            url = self.history[self.current_page]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(tk.END, url)
            self.load_page()

    def forward_page(self):
        if self.current_page < len(self.history) - 1:
            self.current_page += 1
            url = self.history[self.current_page]
            self.url_entry.delete(0, tk.END)
            self.url_entry.insert(tk.END, url)
            self.load_page()

    def quit_browser(self):
        sys.exit()

root = tk.Tk()
browser = WebBrowser(root)
root.mainloop()
