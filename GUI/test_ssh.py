import kivy
from kivy.app import App

from kivy.uix.filechooser import FileChooserListView
from kivy.uix.filechooser import FileSystemAbstract

import os
from os import listdir
from os.path import (basename, getsize, isdir)

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

        #self.client = paramiko.SSHClient()
        #self.client.load_system_host_keys()
        #self.client.connect(target, username=username, password=password)
        host_keys = paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        t = paramiko.Transport((target, 22))
        t.connect(host_keys[target][host_keys[target].keys()[0]], username, password, )
        self.sftp = paramiko.SFTPClient.from_transport(t)


    def __del__(self):
        #self.sftp.close()
        self.sftp.close()
        print("end my life fam")

    def listdir(self, fn):
        #print(fn)
        #stdin, stdout, stderr = self.client.exec_command('python -c "from os import listdir; import sys; print(listdir(sys.argv[1]))" "' + fn[1:] + '"')
        #x = list(set(map(lambda x: x[:-1], [x for x in stdout])))
        #print(x)
        #print("\n\n")
        #s = self.client.open_sftp()
        x = self.sftp.listdir(fn)
        #s.close() #self.sftp.
        return x

    def getsize(self, fn):
        #print(fn[1:])
        #stdin, stdout, stderr = self.client.exec_command('python -c "from os.path import getsize; import sys; print(getsize(sys.argv[1]))" ' + fn[1:])
        #print("sjdklfjsldk")
        #print([x for x in stdout])
        #print("fjsdklfjl\n\n")
        #s = self.client.open_sftp()
        x = self.sftp.stat(fn).st_size #getsize(fn)
        #s.close()
        return x

    def is_hidden(self, fn):
        return False
        '''if platform == 'win':
            if not _have_win32file:
                return False
            try:
                return GetFileAttributesExW(fn)[0] & FILE_ATTRIBUTE_HIDDEN
            except error:
                # This error can occurred when a file is already accessed by
                # someone else. So don't return to True, because we have lot
                # of chances to not being able to do anything with it.
                Logger.exception('unable to access to <%s>' % fn)
                return True

        return basename(fn).startswith('.')'''

    def is_dir(self, fn):
        #stdin, stdout, stderr = self.client.exec_command('python -c "from os.path import isdir; import sys; print(isdir(sys.argv[1]))" "' + fn[1:] + '"')
        return False#list(map(lambda x: x[:-1], [x for x in stdout]))[-1] == "True"

if __name__ == '__main__':
    #comm = open("commands.dat", "r")
    #for i in comm:
    #    SetCommandButton.commandOptions.append(i.split(":")[0])

    MyApp().run()
