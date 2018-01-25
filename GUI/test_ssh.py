import paramiko
client = paramiko.SSHClient()
client.load_system_host_keys()
client.connect('10.111.49.27', username='svanderark', password='chaos')
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
  print('...' + line.strip('\n'))
client.close()



class FileSystemOverSSH(FileSystemAbstract):
    def listdir(self, fn):
        return listdir(fn)

    def getsize(self, fn):
        return getsize(fn)

    def is_hidden(self, fn):
        if platform == 'win':
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

        return basename(fn).startswith('.')

    def is_dir(self, fn):
        return isdir(fn)
