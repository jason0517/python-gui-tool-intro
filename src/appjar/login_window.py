# import the library
from appJar import gui

def on_button_click(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        app.infoBox("Success", "Congratulations "+usr +", you are logged in!")


app=gui()

app.startLabelFrame("Login Details")
# these only affect the labelFrame
app.setSticky("ew")
app.setFont(14)

app.addLabel("l1", "Username", 0, 0)
app.addEntry("Username", 0, 1)

app.addLabel("l2", "Password", 1, 0)
app.addEntry("Password", 1, 1)

app.addButtons(["Submit", "Cancel"], on_button_click, 2, 0, 2)
app.stopLabelFrame()

app.go()