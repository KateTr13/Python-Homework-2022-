text = 'hello\tworld'
text = text.expandtabs(10)
print(text)

text = '----hello----'
print(text.lstrip('-'))

text = 'hello'
print(text.removeprefix('he'))

text = 'world'
print(text.center(10, '_'))

text = 'world'
print(text.zfill(20))

text = 'hello'
print(text.ljust(10, '_'))


