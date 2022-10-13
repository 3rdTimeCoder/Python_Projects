import os
import shutil
import mutagen as mt

#this script takes music in a folder and sorts them into album folders.
dr = input('Enter Diectory: ')

# os.chdir('C:/Users/User/Videos/Star vs the forces of evil/Download/albums')
os.chdir(dr)

for song in os.listdir():
    #get song metadata:
    song_metadata = mt.File(song)

    #extact title, track_number and album from metadata
    title, album, track_number = song_metadata['TIT2'].text[0], song_metadata['TALB'].text[0], song_metadata['TRCK'].text[0]

    #remove illegal char '|' and everything after it:
    if '|' in album:
        album = album.split('|')[0].strip()
        # print(album)

    #create album path, used create album folder + song_path:
    album_path = os.path.join(os.getcwd(), album)
    song_path = os.path.join(os.getcwd(), song)
    # print(song_path)

    # if album folder doesn't exist, create it:
    if os.path.exists(album_path) == False:
        os.mkdir(album)
        # print(album)

    #move song to correct folder (the one just created or the one already there):
    shutil.move(song_path, album_path, copy_function=shutil.copy2)

print('Done!')

# shutil.move(source, destination, copy_function=shutil.copy2)



#Short Documentation
# print(t["TIT2"]) #tittle
# print(t["TALB"]) #album
# print(t["TRCK"]) #track number
# tags["TIT2"] = TIT2(encoding=3, text=title)
# tags["TALB"] = TALB(encoding=3, text=u'mutagen Album Name')
# tags["TPE2"] = TPE2(encoding=3, text=u'mutagen Band')
# tags["COMM"] = COMM(encoding=3, lang=u'eng', desc='desc', text=u'mutagen comment')
# tags["TPE1"] = TPE1(encoding=3, text=u'mutagen Artist')
# tags["TCOM"] = TCOM(encoding=3, text=u'mutagen Composer')
# tags["TCON"] = TCON(encoding=3, text=u'mutagen Genre')
# tags["TDRC"] = TDRC(encoding=3, text=u'2010')
# tags["TRCK"] = TRCK(encoding=3, text=u'track_number')