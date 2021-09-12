from distutils.core import setup
import re
from codecs import open
from os import path, environ


with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()


setup(
  name = 'passwd-generator',         
  packages = ['passwd-generator'], 
  version = '0.1',     
  license='MIT',        
  description = 'passwd_generator is a easy way to generate passwords, hash passwords and check passwords.',   
  author = 'Areo',                   
  author_email = 'areo@envyre.de',      
  url = 'https://github.com/Envyre-Development/passwd-generator',  
  download_url = 'https://github.com/Envyre-Development/passwd-generator/archive/refs/tags/passwd-generator.tar.gz',    
  keywords = ['Generator', 'Password', 'passwd_generator'],   
  long_description=README,
  long_description_content_type='text/markdown',
  classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
