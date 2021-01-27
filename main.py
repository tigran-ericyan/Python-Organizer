import os
import shutil

video_files = ['.webm', '.mkv', '.vob', '.gif', '.avi', '.amv', '.mp4',]

audio_files = ['.aif','.cda', '.mid', '.mp3', '.mpa', '.ogg', ]

image_files = ['.tif', '.tiff', '.bmp', '.jpg', '.jpeg', '.gif', '.png', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.ico']

setup_files = ['.exe', '.msi', ]

disc_files = ['.iso', ]

code_files = ['.py', '.html', '.css', '.js', '.whl', ]

archive_files = ['.zip', '.rar', '.tar', '.tgz', '.tar.gz', ]

torrent_files = ['.torrent']

path = str(input('Input path: '))

if path == 'download':
    path = 'C:\\Users\\tiko1\\Downloads\\'
elif path == 'e':
    path = 'E:\\'
elif path == 'c':
    path = 'C:\\'
else:
    if os.path.exists(path):
        pass
    else:
        print('Your path doesn\'t exists')

all_files = os.listdir(path)

for file_name in all_files:
    ext = os.path.splitext(file_name)[-1].lower()
    for audio in audio_files:
        if ext == audio:
            if not os.path.exists(path + 'audio\\'):
                os.mkdir(path + 'audio\\')
            shutil.move(path + file_name, path + 'audio\\')
    for video in video_files:
        if ext == video:
            if not os.path.exists(path + 'video\\'):
                os.mkdir(path + 'video\\')
            shutil.move(path + file_name, path + 'video\\')
    for image in image_files:
        if ext == image:
            if not os.path.exists(path + 'image\\'):
                os.mkdir(path + 'image\\')
            shutil.move(path + file_name, path + 'image\\')
    for setup in setup_files:
        if ext == setup:
            if not os.path.exists(path + 'setup\\'):
                os.mkdir(path + 'setup\\')
            shutil.move(path + file_name, path + 'setup\\')
    for code in code_files:
        if ext == code:
            if not os.path.exists(path + 'code\\'):
                os.mkdir(path + 'code\\')
            shutil.move(path + file_name, path + 'code\\')
    for archive in archive_files:
        if ext == archive:
            if not os.path.exists(path + 'archive\\'):
                os.mkdir(path + 'archive\\')
            shutil.move(path + file_name, path + 'archive\\')
    for torrent in torrent_files:
        if ext == torrent:
            if not os.path.exists(path + 'torrent\\'):
                os.mkdir(path + 'torrent\\')
            shutil.move(path + file_name, path + 'torrent\\')
    for disc in disc_files:
        if ext == disc:
            if not os.path.exists(path + 'disc\\'):
                os.mkdir(path + 'disc\\')
            shutil.move(path + file_name, path + 'disc\\')