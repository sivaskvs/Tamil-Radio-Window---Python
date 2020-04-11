#!/usr/bin/python
import tkinter as tk
import json
import urllib.request as urllib

from bs4 import BeautifulSoup
import re
import os



def print_selection(name,val,freq):
    print(name,val,freq)
    pyscript = "python playTamilRadio.py {} {} {}"
    os.system(pyscript.format(val, name, freq))


def main():
    print(1)
    web = urllib.urlopen("https://www.tamilradios.com/Suryan")
    pattern = re.compile(
        'src=\'(?:(?:https?|ftp|file):\/\/|www\.|ftp\.)(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[-A-Z0-9+&@#\/%=~_|$?!:,.])*(?:\([-A-Z0-9+&@#\/%=~_|$?!:,.]*\)|[A-Z0-9+&@#\/%=~_|$])\';')

    soup = BeautifulSoup(web.read(), "html.parser")
    scripts = soup.find_all('script')
    src_scripts = scripts[len(scripts) - 1]
    found = ''
    m = re.search('src=\'(.+?)\';', src_scripts.string)
    if m:
        found = m.group(1)
        found = found[:-1]

    window = tk.Tk()
    window.title("Tamil Radio From Tamilradios.com")
    window.geometry('300x100')
    with open('radioInfo.json') as json_file:
        data = json.load(json_file)
        for p in data['radio']:
            B = tk.Button(window, text=p['Name'], command=lambda j=p:print_selection(j['Name'], found+j['Value'], j['Frequency']))
            # B.pack()
            B.grid(row=p['Grid1'], column=p['Grid2'])

    # sys.exit(app.exec_())
    window.mainloop()


if __name__ == "__main__":
    main()