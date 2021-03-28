#------------------------------------------------------------TABLE OF CONTENTS:--------------------------------------------------------------------------------------
#                                                          1.Import Module
#                                                          2.HTML CODE SECTION   
#                                                          3.POSSIBLY USELESS SECTION -EXTRA REMINDER HTML FILE STUFF
#                                                          4.DEFINITONS SECTION  ****THIS IS WHERE I WORK AFTER THE EVENT LOOP WORK****
#                                                          5.GUI LAYOUT
#                                                          6.START OF WINDOW
#                                                          7.EVENT LOOP  ***THIS IS WHERE I NEED TO WORK NEXT***
#                                                          8.-THE END-
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------Import any modules----------------------------------------------------------------------------
import PySimpleGUI as sg

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------Html code section---------------------------------------------------------------------------------------------
# The triple " is important.  ---leave this header alone for now, later may break it up too---
header = """  
<!DOCTYPE html>
<html>
<head>
<title>This is a title</title>
</head>
<body>
<h1>This is a header</h1>
<p>
"""  #leave header alone for now---

#-------------------------------------------------HTML CODE CONTINUED  (THIS IS THE WEIRD STUFF)------------------------------------------------------------------------
m0 = """This is a paragraph"""  #this is what will show on the page  
m1 = """<ul>"""  #this line only happens once
m2 = """
<li><input type="checkbox" id="checkbox1" name="checkbox1" value="checkbox1"/>"""  # this line has to happen for every checkbox
m3 = 'this is a checkbox'  # this needs to be a variable values[1] through values[18]
m4 = """</li>""" # this line has to happen for every checkbox
m5 = """
<li><a href=""" # this line has to happen for every link
m6 = "blah.html"  # this needs to be a variable:values  [20,22,24,26,28,30]
m7 = """>"""
m8 = 'I am a link'   # this needs to be a variable:values [19,21,23,25,27,29]
m9 = """</a></li>"""  # this line has to happen for every link
m1a = """</ul>""" # this line only happens once
footer = """</p></body>
</html>"""

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------Possibly useless section---------------------------------------------------------------------------
#next we give the HTML code for the reminder page...this -might not be part- of the final program- sort of like a type of exception handling

blahmessage = """<!DOCTYPE html>
<html>
<head>
<title>Success!</title>
</head>
<body>
<h1>You linked to blah.html  !!!  Success!!!  Yay!!!</h1>
</body>
</html>"""

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------Definitions section-------------------------------------------------------------------------------------
#                                                              ----THIS IS WHERE I WORK AFTER I WORK THE EVENT LOOP----
def htmlwriter():  # This defines what will be written to html files using the read/write python module(this module doesn't need to be imported-native)
    #nmof = 'example' #this is the name of the file you are making
    FileType = '.html' #type of file you are making
    FinishedFileName = nmof + FileType # way that the program will add the type of file to the name of the file
    f = open(FinishedFileName,'w') #opens FinishedFileName
    f1 = open('blah.html','w') #reminder page to remind you to link your files to new file names
    f.write(header)  #lets start writing to this file! yay!!
    # needs if-then conditional statements adding the checkboxes and the links if there is a value for them
#begin writing checkboxes to the html file
    if values[1]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx1)  # variable checkbox label
        f.write(m4)
    if values[2]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx2)  # variable checkbox label
        f.write(m4)
    if values[3]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx3)  # variable checkbox label
        f.write(m4)
    if values[4]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx4)  # variable checkbox label
        f.write(m4)
    if values[5]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx5)  # variable checkbox label
        f.write(m4)
    if values[6]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx6)  # variable checkbox label
        f.write(m4)
    if values[7]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx7)  # variable checkbox label
        f.write(m4)
    if values[8]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx8)  # variable checkbox label
        f.write(m4)
    if values[9]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx9)  # variable checkbox label
        f.write(m4)
    if values[10]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx10)  # variable checkbox label
        f.write(m4)
    if values[11]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx11)  # variable checkbox label
        f.write(m4)
    if values[12]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx12)  # variable checkbox label
        f.write(m4)
    if values[13]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx13)  # variable checkbox label
        f.write(m4)
    if values[14]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx14)  # variable checkbox label
        f.write(m4)
    if values[15]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx15)  # variable checkbox label
        f.write(m4)
    if values[16]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx16)  # variable checkbox label
        f.write(m4)
    if values[17]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx17)  # variable checkbox label
        f.write(m4)
    if values[18]:  #example of how to write checkbox
        f.write(m2)
        f.write(chbx18)  # variable checkbox label
        f.write(m4)
        
#begin writing links to the html file
    if values[19] and values[20]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile1) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk1) # needs to be replaced with link label
        f.write(m9)
    if values[21] and values[22]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile2) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk2) # needs to be replaced with link label
        f.write(m9)
    if values[23] and values[24]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile3) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk3) # needs to be replaced with link label
        f.write(m9)
    if values[25] and values[26]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile4) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk4) # needs to be replaced with link label
        f.write(m9)
    if values[27] and values[28]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile5) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk5) # needs to be replaced with link label
        f.write(m9)
    if values[29] and values[30]:  #example of how to write link
        f.write(m5)
        f.write(Lnkfile6) # needs to be replaced with link file
        f.write(m7)
        f.write(Lnk6) # needs to be replaced with link label
        f.write(m9)
    f.write(footer) #more writing
    f.close()#closes the page you are creating...ALWAYS CLOSE THE FILES YOU OPEN!!!!!!!!!!!!!!
    f1.write(blahmessage) #reminder page open - may not make final cut-
    f1.close()#reminder page close -may not make final cut
    #print(g)  #prints to the shell so i know i'm not going crazy.  won't be part of the final cut
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------Graphic user interface(GUI) layout---------------------------------------------------------------------
    
layout = [[sg.Text("Name the file"), sg.Input(), sg.Button('Ok'), sg.Button('Cancel'),sg.Text("This will add .html on and overwrite the file ***caution***")],  # values[0] - name of the file
           [sg.Text("Select the Widgets:")],
           [sg.Text("Checkbox with label:"), sg.Input()], # values[1]          -checkboxes-
           [sg.Text("Checkbox with label:"), sg.Input()], # values[2]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[3]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[4]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[5]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[6]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[7]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[8]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[9]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[10]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[11]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[12]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[13]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[14]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[15]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[16]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[17]
           [sg.Text("Checkbox with label:"), sg.Input()], # values[18]
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to(include full file name. ex: blah.html):"), sg.Input()], # values[19] and values[20]        -links-
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to:"), sg.Input()], # values[21] and values[22]
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to:"), sg.Input()], # values[23] and values[24]
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to:"), sg.Input()], # values[25] and values[26]
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to:"), sg.Input()], # values[27] and values[28]
           [sg.Text("Link with label:"), sg.Input(),sg.Text("File to link to:"), sg.Input()]] # values[29] and values[30]
           #[sg.Text("result:")],
           #[sg.Text(size=(30,1), key='-OUTPUT-')],
           #[sg.Button('Ok'), sg.Button('Cancel')]]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

window = sg.Window('''Welcome to Lesley's HTML Maker''', layout)  # the start of the window

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------Event loop----------------------------------------------------------------------------------------------------
#                                 

while True:  #loop that  checks buttons for events and then if 'Ok' button event it checks input boxes for input values and assigns them to variables
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  #checking if the program needs to close
        break
    if event == 'Ok':  #checking if the program needs to pull the input values and assign them to variables
        nmof = values[0]  #assigning values to names
        chbx1 = values[1]
        chbx2 = values[2]
        chbx3 = values[3]
        chbx4 = values[4]
        chbx5 = values[5]
        chbx6 = values[6]
        chbx7 = values[7]
        chbx8 = values[8]
        chbx9 = values[9]
        chbx10 = values[10]
        chbx11 = values[11]
        chbx12 = values[12]
        chbx13 = values[13]
        chbx14 = values[14]
        chbx15 = values[15]
        chbx16 = values[16]
        chbx17 = values[17]
        chbx18 = values[18]
        Lnk1 = values[19]
        Lnk2 = values[21]
        Lnk3 = values[23]
        Lnk4 = values[25]
        Lnk5 = values[27]
        Lnk6 = values[29]
        Lnkfile1 = values[20]
        Lnkfile2 = values[22]
        Lnkfile3 = values[24]
        Lnkfile4 = values[26]
        Lnkfile5 = values[28]
        Lnkfile6 = values[30]
        createfeedback = nmof + ".html created"  # feedback in the window to let you know something happened
        if values[0]:
            print (createfeedback)   #this is incomplete...need to add some more if-then conditions probably, heck if i know
#            window['-OUTPUT-'].update(g2)
                  
            htmlwriter()  
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
window.close()  # now we are done.