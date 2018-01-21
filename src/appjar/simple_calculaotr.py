# import the library
from appJar import gui

# create a GUI variable called app
app = gui("Simple Calculator")


# calculator function
def calculator(key):
    val = app.getLabel("calculator")
    if key == "C":
        app.setLabel("calculator","")
    elif key == "=":
        app.setLabel("calculator", val+key+str(eval(val)))
    else:
        app.setLabel("calculator", val + key)


app.setIPadX(5)
app.setIPadY(5)
app.addEmptyLabel("calculator")
app.setLabelBg("calculator", "grey")
app.setLabelRelief("calculator", "sunken")
app.setLabelAlign("calculator", "e")
buttons=[["1", "2", "3", "C"],
         ["4", "5", "6", "+"],
         ["7", "8", "9", "-"],
         ["0", "*", "/", "="]]

app.addButtons(buttons, calculator)
app.setButtonWidths(buttons, 6)
app.setButtonHeights(buttons, 3)


# start the GUI
app.go()