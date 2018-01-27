import kivy
from kivy.app import App

from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileSystemAbstract

import os
from os import listdir
from os.path import (basename, getsize, isdir)

import stat

'''have_win32file = False
if platform == 'win':
    try:
        from win32file import FILE_ATTRIBUTE_HIDDEN, GetFileAttributesExW, error
        _have_win32file = True
    except ImportError:
        Logger.error('filechooser: win32file module is missing')
        Logger.error('filechooser: we cant check if a file is hidden or not')'''



import paramiko

class MyApp(App):

    def build(self):
        return FileChooserListView(file_system=FileSystemOverSSH('10.111.49.27', 'svanderark', 'chaos'))


class FileSystemOverSSH(FileSystemAbstract):

    def __init__(self, target, username, password):
        super().__init__()

        self.client = paramiko.SSHClient()
        self.client.load_system_host_keys()
        self.client.connect(target, username=username, password=password)
        self.sftp = self.client.open_sftp()

    def __del__(self):
        self.sftp.close()
        self.client.close()

    def listdir(self, fn):
        return self.sftp.listdir(fn)

    def getsize(self, fn):
        return self.sftp.stat(fn).st_size

    def is_hidden(self, fn):
        #return False
        #assuming the robot runs linux not windows.
        return basename(fn).startswith('.')

    def is_dir(self, fn):
        return stat.S_ISDIR(self.sftp.stat(fn).st_mode)


if __name__ == '__main__':
    #comm = open("commands.dat", "r")
    #for i in comm:
    #    SetCommandButton.commandOptions.append(i.split(":")[0])

    MyApp().run()
