'''
Copyright 2021-Present © Areo
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
import hashlib
import secrets
import string
from typing import Optional

class passwd:
    def __init__(self):
        self.pass_char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+?$%/€"
        self.pass_num = "1234567890"
        self.pass_all = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+?$%/€"

        self._sets = {
            1: string.digits,  # "0123456789"
            2: string.ascii_letters,  # "a-zA-Z"
            3: string.ascii_letters + string.digits,  # "a-zA-Z0-9"
            4: string.ascii_letters + string.digits  # Same as type 3 (numbers + letters)
        }

        self.RTX_4090_SPEED = 1_000_000_000  # 1B guesses/sec

        self.CHARSET_SIZES = {
            1: 10,  # digits
            2: 52,  # letters
            3: 62,  # alphanum
            4: 95  # printable
        }

    def generate_passwd(self, length: int, type: str) -> str:
        """
        Generate secure password with specified type and length

        Args:
            length: Password length (min 4, max 128)
            type: 'char' (letters+symbols), 'num' (numbers only), 'nchar' (all chars)

        Returns:
            Generated password string
        """
        if not 4 <= length <= 128:
            raise ValueError("Password length must be between 4 and 128")

        # Map type to character set
        char_sets = {
            'char': self.pass_char,
            'num': self.pass_num,
            'nchar': self.pass_all
        }

        if type not in char_sets:
            raise ValueError(f"Invalid type: {type}. Use 'char', 'num', or 'nchar'")

        # Generate
        password = ''.join(secrets.choice(char_sets[type]) for _ in range(length))

        return password

    def validate_passwd(self, password: str, min_length: int = 4) -> dict:
        """
                Validate password with specified min_length and calculate overall strength and safety without saving or caching anything

                Args:
                    password: Password String
                    min_length: Minimumn length

                Returns:
                    Calculated security rating
        """
        length = len(password)
        charset_size = self._estimate_charset(password)
        crack_time = self._rtx_crack_time(length, charset_size)
        has_digit = any(c.isdigit() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_special = any(not c.isalnum() for c in password)

        score = sum([has_digit, has_upper, has_lower, has_special])
        valid = length >= min_length and score >= 3

        return {
            'valid': valid,
            'length': length,
            'score': score,
            'strength': 'STRONG' if valid else 'WEAK',
            'rtx_4090_crack_time': f"{crack_time}",
            'charset_size': charset_size,
            'requirements': {
                'digits': has_digit,
                'upper': has_upper,
                'lower': has_lower,
                'special': has_special
            }
        }
    
    # Hash password
    def hash_passwd(self, text: str) -> str:
        hash_object = hashlib.sha256(text.encode("utf-8"))
        m = hash_object.hexdigest()
        return m

    # Verfify hash
    def verify_hash(self, input_hash: str, stored_hash: str) -> bool:
        hashed_input = hashlib.sha256(input_hash.encode("utf-8")).hexdigest()
        return hashed_input == stored_hash

    def _estimate_charset(self, password: str) -> int:
        """Smart charset size detection"""
        chars = set(password)
        if all(c.isdigit() for c in chars): return 10
        if all(c.isalpha() for c in chars): return 52
        if all(c.isalnum() for c in chars): return 62
        return 95

    def _rtx_crack_time(self, length: int, charset_size: int) -> str:
        """RTX 4090 crack time"""
        total_combos = charset_size ** length
        seconds = total_combos / self.RTX_4090_SPEED

        if seconds < 60:
            return f"{seconds:.1f}s"
        elif seconds < 3600:
            return f"{seconds / 60:.0f}m"
        elif seconds < 86400:
            return f"{seconds / 3600:.0f}h"
        elif seconds < 31536000:
            return f"{seconds / 86400:.0f}d"
        else:
            years = seconds / 31536000
            return f"{years:.1e}y" if years > 1e6 else f"{years:.0f}y"

