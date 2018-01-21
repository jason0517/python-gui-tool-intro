from appJar import gui

app = gui("School Management System", "400x300")

def Edit():
    pass

def add_student(data):
    app.addGridRow("g1", data)


def Add(btn):
    app.showSubWindow("create_pop")


# ----------------------Main Tab Frame----------------------------
app.startTabbedFrame("TopTabbedFrame")

app.startTab("Student")
# app.setStretch("both")
app.setSticky("news")

# app.setIPadX(-30)
# app.setIPadY(-30)
app.setFont(12)
g_data =[
    ["Name", "Age", "Gender", "Grade"],
    ["Fred", 16, "Male", "G11"],
    ["Tina", 15, "Female", "G12"],
    ["Clive", 18, "Male", "G10"],
    ["Betty", 20, "Female", "G12"]
]

app.addGrid("g1",
            g_data, action=Edit, addRow=Add)

app.stopTab()

app.startTab("Teacher")
app.addLabel("l2", "Tab 2 Label")
app.stopTab()

app.startTab("Employee")
app.addLabel("l3", "Tab 3 Label")
app.stopTab()

app.stopTabbedFrame()

# ------------------------Create Student Form Window-------------------------

def on_submit_new_student(btn):
    d = [app.getEntry("Name"), app.getEntry("Age"), app.getEntry("Gender"), app.getEntry("Grade")]
    add_student(d)
    app.hideSubWindow("create_pop")

def on_new_student_cancel(btn):
    app.hideSubWindow("create_pop")

app.startSubWindow("create_pop", modal=True)

app.startLabelFrame("Add a New Student")
# these only affect the labelFrame
app.setSticky("ew")
app.setFont(12)

app.addLabel("csf_l1", "Name", 0, 0)
app.addEntry("Name", 0, 1)

app.addLabel("csf_l2", "Age", 1, 0)
app.addEntry("Age", 1, 1)

app.addLabel("csf_l3", "Gender", 2, 0)
app.addEntry("Gender", 2, 1)

app.addLabel("csf_l4", "Grade", 3, 0)
app.addEntry("Grade", 3, 1)

app.addButtons(["Ok", "Cancel"], [on_submit_new_student, on_new_student_cancel], 4, 0, 2)
app.stopLabelFrame()

app.stopSubWindow()





app.go()