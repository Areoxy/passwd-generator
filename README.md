[![Downloads](https://static.pepy.tech/badge/passwd-generator)](https://pepy.tech/project/passwd-generator) [![Downloads](https://static.pepy.tech/badge/passwd-generator/month)](https://pepy.tech/project/passwd-generator)

# passwd-generator

passwd-generator is a python package to generate, hash, and check passwords in many different formats like only text or text&numbers.

## Documentation

Install the Package with 

`pip install passwd-generator` 
or install the Development Version with 
`pip install git+`

**Generate a password from numbers and special characters.**

```python
from passwd_generator.functions import passwd

generator = passwd()
password = generator.make_passwd(10, "char") # Generates the password 
print(password)
```

**Generate a password from numbers.**

```python
from passwd_generator.functions import passwd

generator = passwd() # Define the passwd generator
password = generator.make_passwd(10, "num") # Generates the password
print(password)
```

**Generate a password from numbers, letters and special charakters.**

```python
from passwd_generator.functions import passwd

generator = passwd() # Define the passwd generator
password = generator.make_passwd(10, "nchar") # Generates the password
print(password)
```

> The 10 means the length of the password. You can change this freely


**Hash a Passwort**

```python
from passwd_generator.functions import passwd

generator = passwd() # Define the passwd generator
hashed_password = generator.hash_passwd("yourpassword") # Hashs the password
print(hashed_password)
```

**Check if a password contains numbers.**

```python
from passwd_generator.functions import passwd


generator = passwd() # Define the passwd generator
hashed_password = generator.check_passwd(1, "yourpasswort") # Checks the password
print(hashed_password)
```

**Check if a password contains letters.**

```python
from passwd_generator.functions import passwd


generator = passwd() # Define the passwd generator
hashed_password = generator.check_passwd(2, "yourpasswort") # Checks the password
print(hashed_password)
```

**Check if a password contains numbers and letters.**

```python
from passwd_generator.functions import passwd


generator = passwd() # Define the passwd generator
hashed_password = generator.check_passwd(3, "yourpasswort") # Checks the password
print(hashed_password)
```

> Note that the check returns true if the password contains the requirements and false if ot.
