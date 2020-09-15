import string

values = {'var' : 'foo', 'pip' : 'shmik', 'pounce' : 'zapikanos'}

t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable 
""")

print('TEMPLATE:', t.substitute(values))

s = """
Variable        : %(pip)s
Escape          : %%
Variable in text: %(pip)siable
"""

print('INTERPOLATION:', s % values)

s = """
Varialbe        : {pounce}
Escape          : {{}}
Variable in text: {pounce}iable
"""

print('FORMAT:', s.format(**values))