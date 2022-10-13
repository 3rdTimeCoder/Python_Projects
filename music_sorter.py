'''
Author: Nomah S.
Desc: This script takes music in a folder and sorts them into album folders or artist folders
'''

import os
import shutil
import mutagen as mt


def remove_illegal_chars(string):
    '''
    remove illegal characters from string
    --> Returns a new string without the illegal characters.
    '''

    ILLEGAL_CHARS = "#%&\}\{<>*?$!'+|=;/:"
    str_list = list(string)

    for element in str_list:
        if element in ILLEGAL_CHARS:
            str_list.remove(element)
    
    return "".join(str_list)



def sort_by_album():
    '''
    sorts songs into albums folders
    '''
    for song in os.listdir():

        #if file not mp3, ignore/skip:
        ext = os.path.splitext(song)[1]
        if ext != '.mp3':
            continue
        
        try:
            song_metadata = mt.File(song) 
            
            #if album metatag exists set it to album, else set album to unknown:
            if 'TPE1' in song_metadata.keys():
                album = song_metadata['TALB'].text[0]
            else:
                album = 'Unknown'

            #remove illegal char '|' and everything after it:
            if '|' in album:
                album = album.split('|')[0].strip()

            album = remove_illegal_chars(album)

            #create album path, used create album folder + song_path:
            album_path = os.path.join(os.getcwd(), album)
            song_path = os.path.join(os.getcwd(), song)

            # if album folder doesn't exist, create it:
            if os.path.exists(album_path) == False:
                os.mkdir(album)

            #move song to correct folder (the one just created or the one already there):
            shutil.move(song_path, album_path, copy_function=shutil.copy2)
        
        except:
            print('An Error Occured!')


    print('Music Succesfully Sorted!')


def sort_by_artist():
    '''
    sorts songs into artist folders
    '''
    for song in os.listdir():

        #if file not mp3, ignore/skip:
        ext = os.path.splitext(song)[1]
        if ext != '.mp3':
            continue

        try:
            song_metadata = mt.File(song) #get song metadata:

            #if artist metatag exists set it to album, else set album to unknown:
            if 'TPE1' in song_metadata.keys():
                artist = song_metadata['TPE1'].text[0]
            else:
                artist = 'Unknown'

            #remove illegal characters from artist string:
            artist = remove_illegal_chars(artist)

            #remove excess info from artist name, i.e. '|' or '-' and anything after these chars:
            #This is not working for whatever reason:
            if '|' in artist:
                artist = artist.split('|')[0]
            elif '-' in artist:
                artist = artist.split('-')[0]
            

            #create album path, used create album folder + song_path:
            artist_path = os.path.join(os.getcwd(), artist.strip())
            song_path = os.path.join(os.getcwd(), song)

            # if album folder doesn't exist, create it:
            if os.path.exists(artist_path) == False:
                os.mkdir(artist)

            #move song to correct folder (the one just created or the one already there):
            shutil.move(song_path, artist_path, copy_function=shutil.copy2)

        except:
            print('An Error Occured!')
            # quit()

    print('Music Successfully Sorted!')


if __name__ == '__main__':
    
    try:
        dr = input('Enter Directory: ')
        if os.path.exists(dr):
            os.chdir(dr) # move to the entered directory
        else:
            print('Invalid Directory Entered!')
            quit()
            
        action = input('1.Sort Music By Album\n2.Sort Music By Artist\nEnter Action: ')

        if action == '1':
            sort_by_album()
        elif action == '2':
            sort_by_artist()
        else: 
            print('Ivalid Input!')
    
    except:
        print('An Error Occured!')


    


