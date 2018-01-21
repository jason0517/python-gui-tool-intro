# import the library
from appJar import gui

# create a GUI variable called app
app = gui("Hello World", "400x200")

# add a label control
app.addLabel("lbl1", "Hello,world!")

# window.setLabel("label1", "123")

# start the GUI
app.go()

