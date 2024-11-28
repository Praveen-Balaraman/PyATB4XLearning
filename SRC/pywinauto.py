#from subprocess import Popen
#from pywinauto import
#from time import sleep

#Popen('calc.exe',shell=True)
from pywinauto 

app = application.Application().start("notepad.exe")
app.Notepad.edit.TypeKeys("Hello, pywinauto!")

