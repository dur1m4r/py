import string

example_dict = {'key' : 'value'}

example_template = string.Template("$key is here but $missing is not provided")

try:
    print('substitute()     :', example_template.substitute(example_dict))
except KeyError as err:
    print('ERROR:', str(err))

print('safe_sutbstitute(): ', example_template.safe_substitute(example_dict))