# passwd-generator

Passwd_generator is an easy way to generate, hash and check passwords.

**Documentation**

Install the Package with 

`pip install passwd-generator` 
or install the Development Version with 
`pip install git+`

Generate a password from numbers and special characters.

```py
from passwd_generator import passwd

generator = passwd()
password = generator.make_passwd(10, "char") # Generate the password 
print(password)
```

Generate a password from numbers.

```py
from passwd_generator import passwd

generator = passwd() # Define the passwd generator
password = generator.make_passwd(10, "num") # Generate the password
print(password)
```

Generate a password from numbers, letters and special charakters.

```py
from passwd_generator import passwd

generator = passwd() # Define the passwd generator
password = generator.make_passwd(10, "nchar") # Generate the password
print(password)
```

The 10 means the length of the password. You can change this freely
