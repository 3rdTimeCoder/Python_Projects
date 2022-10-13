'''
Author: Nomah S.
Desc: This script takes files inside a given directory and sorts them into album folders by type.
'''

import os
import shutil
from time import sleep


def sort_files():
    '''
    sorts files inside a given directory. i.e. Into pdfs, epubs, videos, etc.
    '''
    music_ext = ['.mp3', '.m4a', '.flac', '.wav', '.wma', '.aac' ]
    image_ext = ['.jpg', '.JPG', '.jpeg', '.png', '.gif', '.psd', '.ai', '.eps']
    video_ext = ['.mp4', '.mov', '.wmv', '.avi', '.mkv', '.webm', '.flv', '.mts']
    ext_dict = {
        '.pdf': 'PDFs',
        '.epub': 'Ebooks',
        '.mp4': 'Videos',
        '.zip': 'ZIPs',
        '.exe': 'Executables',
        '.txt': 'Text Documents',
        '.csv': 'Excel Documents',
        '.docx': 'Word Documents',
        }
        
    for file in os.listdir():

        try:
            #if file ext not pre-defined ext, skip:
            ext = os.path.splitext(file)[1]
            if ext not in music_ext and ext not in image_ext and ext not in video_ext and ext not in ext_dict.keys():
                continue

            #create file path
            file_path = os.path.join(os.getcwd(), file)

            #create folder path
            if ext in ext_dict.keys():
                folder_name = ext_dict[ext]
                folder_path = os.path.join(os.getcwd(), ext_dict[ext])
            elif ext in image_ext:
                folder_name = 'Images'
                folder_path = os.path.join(os.getcwd(), 'Images')
            elif ext in video_ext:
                folder_name = 'Videos'
                folder_path = os.path.join(os.getcwd(), 'Videos')
            elif ext in music_ext:
                folder_name = 'Music'
                folder_path = os.path.join(os.getcwd(), 'Music')

            #create folder if it dosen't exist
            if os.path.exists(folder_path) == False:
                os.mkdir(folder_name)

            #move file into folder:
            try: 
                shutil.move(file_path, folder_path, copy_function=shutil.copy2)
            except:
                print("File Already Exists in Folder.")
                continue
        
        except:
            print('An Error Occured!')
            quit()
    
    print('Files Successfully Sorted!')
    sleep(5)



if __name__ == '__main__':
    dr = input('Enter Directory: ')

    if os.path.exists(dr):
        os.chdir(dr) 
    else:
        print('Invalid Directory Entered!')
        quit()

    sort_files()