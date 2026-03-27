import pytest
import string
from unittest.mock import patch
from src.passwd_generator import passwd


class TestPasswd():
    def setup_method(self):
        self.pm = passwd()

    def test_generate_passwd_valid_inputs(self):
        """Test valid password generation"""
        # Test different types
        for pwd_type in ['char', 'num', 'nchar']:
            pwd = self.pm.generate_passwd(8, pwd_type)
            assert len(pwd) == 8
            assert isinstance(pwd, str)

            # Verify characters are from correct set
            allowed_chars = {
                'char': self.pm.pass_char,
                'num': self.pm.pass_num,
                'nchar': self.pm.pass_all
            }
            for char in pwd:
                assert char in allowed_chars[pwd_type]

    def test_generate_passwd_invalid_length(self):
        """Test length validation"""
        with pytest.raises(ValueError, match="Password length must be between 4 and 128"):
            self.pm.generate_passwd(3, 'char')

        with pytest.raises(ValueError, match="Password length must be between 4 and 128"):
            self.pm.generate_passwd(129, 'char')

    def test_generate_passwd_invalid_type(self):
        """Test invalid type"""
        with pytest.raises(ValueError, match="Invalid type"):
            self.pm.generate_passwd(8, 'invalid')

    def test_validate_passwd_strong(self):
        """Test strong password validation"""
        strong_pwd = "A1b$CdEfG2h#"
        result = self.pm.validate_passwd(strong_pwd)

        assert result['valid'] is True
        assert result['strength'] == 'STRONG'
        assert result['score'] == 4
        assert result['length'] == 12

    def test_validate_passwd_weak(self):
        """Test weak password validation"""
        weak_pwd = "password"
        result = self.pm.validate_passwd(weak_pwd)

        assert result['valid'] is False
        assert result['strength'] == 'WEAK'
        assert result['score'] == 1

    def test_charset_estimation(self):
        """Test charset size estimation"""
        assert self.pm._estimate_charset("123456") == 10  # digits
        assert self.pm._estimate_charset("abcDEF") == 52  # letters
        assert self.pm._estimate_charset("abc123") == 62  # alphanum
        assert self.pm._estimate_charset("abc123$") == 95  # full

    @patch('passwd.passwd.RTX_4090_SPEED', 1000)  # Slow for testing
    def test_crack_time_calculation(self):
        """Test crack time calculations"""
        # Quick crack (<60s)
        assert 's' in self.pm._rtx_crack_time(3, 10)

        # Minutes
        assert 'm' in self.pm._rtx_crack_time(4, 10)

        # Hours
        assert 'h' in self.pm._rtx_crack_time(5, 10)

        # Days
        assert 'd' in self.pm._rtx_crack_time(6, 10)

        # Years
        assert 'y' in self.pm._rtx_crack_time(7, 10)

    def test_hashing_roundtrip(self):
        """Test hash and verify"""
        password = "MySecurePass123$"
        hashed = self.pm.hash_passwd(password)

        # Verify hash length and format
        assert len(hashed) == 64  # SHA-256 hex digest
        assert self.pm.verify_hash(password, hashed) is True
        assert self.pm.verify_hash("wrongpass", hashed) is False

    def test_hash_different_inputs(self):
        """Test hash uniqueness"""
        pwd1 = "password1"
        pwd2 = "Password1"

        hash1 = self.pm.hash_passwd(pwd1)
        hash2 = self.pm.hash_passwd(pwd2)

        assert hash1 != hash2

    def test_validate_edge_cases(self):
        """Test edge case validations"""
        # Minimum length
        result = self.pm.validate_passwd("A1b$", 4)
        assert result['valid'] is True

        # Exactly minimum length weak
        result = self.pm.validate_passwd("aaaa", 4)
        assert result['valid'] is False

        # Empty string
        result = self.pm.validate_passwd("")
        assert result['valid'] is False
        assert result['length'] == 0

    def test_realistic_crack_times(self):
        """Test realistic password crack times"""
        # Very weak
        weak = self.pm.validate_passwd("1234")
        assert float(weak['rtx_4090_crack_time'][:-1]) < 1000  # seconds

        # Strong
        strong = self.pm.validate_passwd("X7$kPq9mW2vR8nT4")
        assert 'e' in strong['rtx_4090_crack_time'] or 'y' in strong['rtx_4090_crack_time']


if __name__ == "__main__":
    pytest.main([__file__, "-v"])