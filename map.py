#launches map in the webbrowser from the commandline argument
#or from clipbord
import webbrowser, sys, pyperclip

addr = ''

if len(sys.argv) > 1:
	addr = ' '.join(sys.argv[1:])
else:
	addr = pyperclip.paste()

#print addr

webbrowser.open('http://google.co.in/search?q=' + addr)
