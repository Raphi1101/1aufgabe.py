#Module importieren
import mariadb
import sys
import tkinter as tk
from tkinter import ttk
#Connect to MariaDB platform

try:
    conn = mariadb.connect(
        user="Raphi1101",
        password="Joel1902",
        host="localhost",
        port=3306,
        database="schlumpfshop3"
    ) 

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cur = conn.cursor()

class Artikel:
    def __init__(self,name,bestand,lieferant):
        self.name = name
        self.bestand = bestand
        self.lieferant = lieferant

#Funktion wenn Button gedrückt wird
def artikel_suchen():
    try:
        grenze = int(eingabe.get()) #zahl vom benutzer einholen
    
    except ValueError:
        meldung.config(text="Bitte gib eine Zahl ein: ")
        return
    

    #Alte zeilen in der Tabelle löschen
    for zeile in tabelle.get_children():
        tabelle.delete(zeile)

    #Daten aus der Datenbank holen
    try: 
        cur.execute("SELECT artikel.artikelname, artikel.Lagerbestand, artikel.Lieferant FROM artikel WHERE artikel.Lagerbestand < ?", (grenze,))
        ergebnisse = cur.fetchall()
        for eintrag in ergebnisse:
            #Jeden Artikel in der Tabelle anzeigen
            tabelle.insert("","end", values=eintrag)
        meldung.config(text=f"{len(ergebnisse)} Artikel gefunden.")

    except mariadb.Error as e:
        meldung.config(text="Fehler bei der Abfrage")

#Fenster erstellen
fenster = tk.Tk()
fenster.title("Bestellung prüfen")

#Text + eingabefeld
tk.Label(fenster, text="Zeig mir alle Artikel mit weniger als: ").pack()
eingabe = tk.Entry(fenster)
eingabe.pack()

#Button
tk.Button(fenster, text="Artikel anzeigen", command=artikel_suchen).pack()

#Tabelle erstellen
tabelle = ttk.Treeview(fenster, columns=("Bezeichnung", "Bestand", "Lieferant"), show ="headings")
tabelle.heading("Bezeichnung", text="Bezeichnung")
tabelle.heading("Bestand", text="Bestand")
tabelle.heading("Lieferant", text="Lieferant")
tabelle.pack()

#meldung unten
meldung = tk.Label(fenster, text="")
meldung.pack()

#Fenster anzeigen
fenster.mainloop()



