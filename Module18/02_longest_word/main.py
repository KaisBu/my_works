text = input('Enter the text: ').split()

print('The word:', max(text, key=len))
print('Word length:', len(max(text, key=len)))
