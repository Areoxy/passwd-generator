'''
Copyright 2021 © Envyre Development
All rights saved.

License:

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, modify, merge, distribute and sublicense,
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

'''


import random 
import hashlib


class passwd():
    def __init__(self):
        pass

    def make_passwd(self, len, type):
        self.pass_char = "abcdefghijklmnopqrstuvwxyzgwerqgjfABCDEFGHIJKLMNOPQRSTUVWXYZ+?$%/€"
        self.pass_num = "1234567890"
        self.pass_all = "1234abcdefghijklmno567pqrstuvwxyzgwerqgj890fABCDEFGHIJKLMNOPQRSTUVWXYZ+?$%/€"
        self.password = ""

        # Check type of the password
        if type == "char":
            # Generate password
            for x in range(0, len):
                passwd_w = random.choice(self.pass_char)
                self.password = self.password + passwd_w
            return self.password
        # Check type of the password
        elif type == "num":
            # Generate password
            for x in range(0, len):
                passwd_w = random.choice(self.pass_num)
                self.password = self.password + passwd_w
            return self.password
        # Check type of the password
        elif type == "nchar":
            # Generate password
            for x in range(0, len):
                passwd_w = random.choice(self.pass_all)
                self.password = self.password + passwd_w
            return self.password
    
    def hash_passwd(self, password):
        # Hash password
        self.hash_object = hashlib.md5(password.encode())
        # Return hashed password
        return self.hash_object.hexdigest()

    def check_passwd(self, type, password):
        if type == 1:
            re = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            checked = any(re in password for re in re)
            return checked
        elif type == 2:
            re = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            checked = any(re in password for re in re)
            return checked
        elif type == 3:
            re = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
            checked = any(re in password for re in re)
            return checked