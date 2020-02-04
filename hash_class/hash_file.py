from filehash import FileHash
from os import chmod
from os import path
from os import stat
from time import ctime
from stat import S_IREAD, S_IRGRP, S_IROTH

class FileHasher():
    """
    Class to hold methods to hash a file
    """

    def __init__(self):
        """
        Initialise the class
        """
        pass

    def hash_file(self,filepath):
        """
        Sets the file to be read only
        Creates the hash for the file given in the filepath
        Uses hash SHA-256
        Returns the hash
        """
        sha256hasher = FileHash('sha256')
        chmod(filepath, S_IREAD|S_IRGRP|S_IROTH)
        # See https://docs.python.org/3/library/stat.html for definitions of S_IREAD, S_IRGRP, S_IROTH
        hashed_output = sha256hasher.hash_file(filepath)
        return hashed_output

    def save_to_txt(self,file_path,hashed_file):
        """
        Saves file name, extension, size, date the file was last modified, and the hash 
        to a .txt file in the same location as the original file
        """
        file_name = path.basename(file_path)
        file_directory = path.dirname(file_path)
        file_size = stat(file_path).st_size
        file_modified = ctime(path.getmtime(file_path))
        txt_file_path = path.join(file_directory, file_name + '_HASH.txt')
        try:
            with open(txt_file_path,'w+') as f:
                f.write('Filename: ' + file_name)
                f.write('\nDirectory: ' + file_directory)
                f.write('\nFile size: ' + str(file_size) + 'bytes')
                f.write('\nDate last modified: ' + file_modified)
                f.write('\nSHA-256 hash: ' + hashed_file)
            return True
        except:
            return False