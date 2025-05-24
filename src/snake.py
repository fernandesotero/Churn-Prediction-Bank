
'''
Importing library.
'''
import sys
import re

def camel_to_snake(name):
    return re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', name).lower()

    '''
    Transform the columns name from camel case to snake_case.
    '''
