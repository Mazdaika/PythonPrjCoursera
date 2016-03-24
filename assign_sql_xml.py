import sqlite3
import xml.etree.ElementTree as et


def prepare_db(connct):
    cur = connct.cursor()
    cur.execute("DROP TABLE IF EXISTS Artist")
    cur.execute("DROP TABLE IF EXISTS Genre")
    cur.execute("DROP TABLE IF EXISTS Album")
    cur.execute("DROP TABLE IF EXISTS Track")
    connct.commit()
    print "deleted"
    cur.execute('''
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')
    cur.execute('''
CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);
''')
    cur.execute('''
CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);
''')
    cur.execute('''
CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')
    connct.commit()
    print "created"

def commitArtist(artist,connct):
    cur = connct.cursor()
    cur.execute("INSERT OR IGNORE INTO Artist (name) VALUES (?)", (artist,))

def commitGenre(artist,connct):
    cur = connct.cursor()
    cur.execute("INSERT OR IGNORE INTO Genre (name) VALUES (?)", (artist,))

def findArtists(elems,connct):
    for tags in elems:
        found = False
        for tag in tags:
            if not found:
                if tag.tag == "key" and tag.text == "Artist":
                    found = True
            else:
                commitArtist(tag.text, connct)
                found = False

def findGenres(elems, connct):
    for tags in elems:
        found = False
        for tag in tags:
            if not found:
                if tag.tag == "key" and tag.text == "Genre":
                    found = True
            else:
                commitGenre(tag.text, connct)
                found = False

def findAlbums(elems, connct):
    for tags in elems:
        found = False
        foundalb = False
        foundart = False
        artist = ""
        album = ""
        for tag in tags:
            if not found:
                if tag.tag == "key":
                    found = True
                    if  tag.text == "Album":
                        foundalb = True
                    if tag.text == "Artist":
                        foundart = True
            else:
                found = False
                if foundart:
                    artist = tag.text
                    foundart = False
                if foundalb:
                    album = tag.text
                    foundalb = False
            if album is not "" and artist is not "":
                commitAlbum(album, artist)

def commitAlbum(album, artist):
    cur = connct.cursor()
    cur.execute("SELECT id FROM Artist WHERE name = ?", (artist,))
    artist_id = cur.fetchone()[0]
    cur.execute("INSERT OR IGNORE INTO Album (artist_id, title) VALUES (?, ?)", (artist_id, album))


def findTracks(elems, connct):
    for tags in elems:
        found = False
        foundalb = False
        foundgenre = False
        foundname = False
        foundlen = False
        foundrate = False
        foundcount = False
        genre = ""
        album = ""
        name = ""
        length = ""
        rating = ""
        count = ""
        for tag in tags:
            if not found:
                if tag.tag == "key":
                    found = True
                    if tag.text == "Album":
                        foundalb = True
                    if tag.text == "Genre":
                        foundgenre = True
                    if tag.text == "Name":
                        foundname = True
                    if tag.text == "Total Time":
                        foundlen = True
                    if tag.text == "Rating":
                        foundrate = True
                    if tag.text == "Play Count":
                        foundcount = True
            else:
                found = False
                if foundgenre:
                    genre = tag.text
                    foundgenre = False
                if foundalb:
                    album = tag.text
                    foundalb = False
                if foundcount:
                    count = tag.text
                    foundcount = False
                if foundlen:
                    length = tag.text
                    foundlen = False
                if foundname:
                    name = tag.text
                    foundname = False
                if foundrate:
                    rating = tag.text
                    foundrate = False
            if album is not "" and genre is not "" and count is not "" and length is not "" and name is not "" and rating is not "":
                commitTrack(name, genre, album, length, rating, count)

def commitTrack(name, genre, album, length, rating, count):
    cur = connct.cursor()
    cur.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
    genre_id = cur.fetchone()[0]
    cur.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = cur.fetchone()[0]
    cur.execute("INSERT OR IGNORE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?, ?, ?, ?, ?, ?)", (name, album_id, genre_id, length, rating, count))

connct = sqlite3.connect("fromxml.sqlite")
fh = open("Library.xml")
str = fh.read()
extrxml = et.fromstring(str)

elems = extrxml.findall("dict/dict/")
prepare_db(connct)
findArtists(elems, connct)
findGenres(elems, connct)
findAlbums(elems, connct)
findTracks(elems, connct)

str = """
SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
"""
cur = connct.cursor()
cur.execute(str)
f = cur.fetchall()
print f

connct.commit()
connct.close()

