import webbrowser,sys,email
print(email.__file__)
webbrowser.open("https://inventwithpython.com/")
if len(sys.argv)>1:
    address = ''.join(sys.argv[1:])
