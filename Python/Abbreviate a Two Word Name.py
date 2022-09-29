"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""

def abbrev_name(name):
    text = name.upper().split(" ")
    return text[0][0] + '.' + text[1][0]

abbrev_name("Vasily Keytiyev")

# Best solution
"""
def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()
"""
# Second Best
"""
def abbrevName(name):
    first, last = name.upper().split(' ')
    return first[0] + '.' + last[0]
"""