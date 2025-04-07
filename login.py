 
import webbrowser
import os

new = 2 # open in a new tab, if possible

path = os.path.abspath(r'C:\Users\timra\OneDrive\Documents\work\code\project-main\project-main\cgi-bin\index.html')
url = 'file://' + path
webbrowser.open(url,new=new)