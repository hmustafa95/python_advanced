try:
    text_file = open('~/Desktop/text.rtf', 'r')
    print('File found')
except FileNotFoundError:
    print('File not found')