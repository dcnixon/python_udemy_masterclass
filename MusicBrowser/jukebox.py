# Code is for a simple browser for the music database

import sqlite3
try:
    import tkinter
except ImportError:      # python 2
    import Tkinter as tkinter

conn = sqlite3.connect('music.db', )


class Scrollbox(tkinter.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


def get_albums(event):
    """ get the artist ID from the database row. Uses the result to query the albums and set the Album list box to display the result """
    lb = event.widget
    index = lb.curselection()[0]
    artist_name = lb.get(index),

    # get the artist ID from the database row. Use the result to query the albums and set the Album list box to display the result
    artist_id = conn.execute("SELECT artists._id FROM artists WHERE artists.name = ?", artist_name).fetchone()
    alist = []
    for row in conn.execute("SELECT name FROM albums WHERE albums.artist = ? ORDER BY name", artist_id):
        alist.append(row[0])
    albumLV.set(tuple(alist))
    songLV.set(("Choose an album", ))

def get_songs(event):
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name=?", album_name).fetchone()
    alist = []
    for row in conn.execute("SELECT songs.title, songs.track FROM songs WHERE songs.album = ? ORDER BY track", album_id):
        alist.append(row[0])
    songLV.set(tuple(alist))


# albumScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=albumList.yview)
# albumScroll.grid(row=1, column=1, sticky='nse')
# albumList['yscrollcommand'] = albumScroll.set


mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

# configure the columns
mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)     # space column on the right

# configure the rows weight gives a % of the geometry to the row/column
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ====== labels ======
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ====== Artists Listbox =====
artistList = Scrollbox(mainWindow)
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

for artist in conn.execute('SELECT artists.name FROM artists ORDER BY artists.name'):
    artistList.insert(tkinter.END, artist[0])

artistList.bind('<<ListboxSelect>>', get_albums)

# ===== Albums Listbox ======
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

albumList.bind('<<ListboxSelect>>', get_songs)

# ===== Songs Listbox =====
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')


# ===== Main Loop =====
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("Closing database connection")
conn.close()

# can put the scrollbar in their own column, but we will put them with the Listbox
# since the listbox doesn't know if there is a column available for its scrollbar

# tkinter variables are tracked variables - anything using them is notified of the change
