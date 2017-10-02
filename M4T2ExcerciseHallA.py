# CTI 110
# M4T2 Python Exercise
# Hall, Airelle
# Mr. Norris
# 1 Oct 2017


# ask user for tag from HTML
# code will print what tag is

htmlTag = input('Enter tag:')

# variables

# P = Indicates a Paragraph. Example: <p>This is paragraph</p>
# H = Header One. Most Important header. Example: <h1>Header</h1>
# b = Bold. Example: <b>BOLD</b>
# d = Divides paragraphs. Example: <div>paragraph 1</div>

if htmlTag == 'p':
    print ('Indicates a Paragraph. Example: <p>This is paragraph</p>')
elif htmlTag == 'h':
    print ('Header One. Most Important header. Example: <h1>Header</h1>')
elif htmlTag == 'b':
    print ('Bold. Example: <b>BOLD</b>')
elif htmlTag == 'd':
    print ('Divides paragraphs. Example: <div>paragraph 1</div>')
else:
    print ('Error 4080: Tag not found')

# Code will print to corresponding tag. If no tag is found. Code
# will print error: No Tag Found
