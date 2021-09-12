# passwd-generator

Passwd_generator is an easy way to generate, hash and check passwords.

## Install

Install the Package with 

`pip install passwd-generator` 
or install the Development Version with 
`pip install git+`

### Documentation

Read the Docs here:
[Link](https://github.com/Envyre-Development/passwd-generator)

### Example

```python
import passwd_generator

generator = passwd() # Define the password-generator
password = generator.make_passwd(10, "char") # Generates the password 
print(password)
```

> The 10 means the length of the password. You can change it freely 
