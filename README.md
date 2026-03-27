[![Downloads](https://static.pepy.tech/badge/passwd-generator)](https://pepy.tech/project/passwd-generator) [![Downloads](https://static.pepy.tech/badge/passwd-generator/month)](https://pepy.tech/project/passwd-generator)

# passwd-generator

passwd-generator is a simple Python library to generate, hash, and verify secure passwords with modern crack time analysis.

## Documentation

Install the Package with 

`pip install passwd-generator` 
or install the Development Version with 
`pip install git+`

### **Generate a password**

```python
from passwd_generator import passwd

# available types: 'char' (letters+symbols), 'num' (numbers only), 'nchar' (all chars)
password = passwd().generate_passwd(length=12, type="nchar")
```

### **Validate a password**

```python
from passwd_generator import passwd

print(passwd().validate_passwd(password="text", min_length=4))
```

Example Ouput:
```commandline
{
    'valid': True,
    'length': 11,
    'score': 4,
    'cracktime' 24y
    'requirements': {
        'digits': True,
        'upper': True,
        'lower': True,
        'special': True
    }
}
```

### **Hash a password/text**
```python
from passwd_generator import passwd

password_hash = passwd().hash_passwd("text")
```

### **Verify a hash**
```python
from passwd_generator import passwd

password_hash = passwd().verify_hash("new_hash", "old_hash")
```
