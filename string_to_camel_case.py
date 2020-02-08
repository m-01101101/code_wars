# Convert string to camel case

# my attempt
def to_camel_case(text):    
    final = ''
    for i in text.replace('_', '-').split('-'):
        final += i.capitalize()
    
    if text == '':
        final
    elif text[0].islower():
        final = final.replace(final[0], text[0])
    
    return final
    
# list comprehension version
def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
    
# something i could have doen
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

# lambda
import re
def to_camel_case(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)
