# Text Editor

from appJar import gui

def load():
    fileName=app.openBox()
    f=open(fileName, 'r')
    text=f.read()
    show(text)
    f.close()

def show(text=""):
    app.setTextArea("t1", text)

def save():
    fileName=app.saveBox()
    f=open(fileName, 'w')
    text=app.getTextArea("t1")
    f.write(text)
    f.close()

app=gui('Text Editor',"800x600")
app.addScrolledTextArea("t1")
app.addMenuItem("file", "open", load)
app.addMenuItem("file", "save", save)
#app.showSplash("TEXT EDIT ++", fill='red', stripe='black', fg='white', font=44)
app.go()
    
    
    

