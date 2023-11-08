from guizero import App, Box, Combo, Picture, PushButton, Text, Window

# declarations
menu_manage = ['Enter Stats','Manage Events']
menu_stats = ['Individual Stats','Team Stats' ]


# methods
def open_window():
    window_2.show()
    # window_2.show(wait = True)

def close_window():
    window_2.hide()

def go_home():
	lbl_debug.value = "Home Function"

def do_manage():
	lbl_debug.value = combo_manage.value

def do_stats():
	lbl_debug.value = combo_stats.value

def do_calendar():
	lbl_debug.value = "Calendar Function"

def do_quit():
	app.destroy()

JCCOLORS = {'PURPLE':'#4b3048',
'DARK_BLUE':'#1b365d',
'GOLD':'#a89968',
'FLAT_BLUE':'#9bb8d3',
'COOL_GRAY':'#53565a'}

app = App(title="Swimming App", height=500, width=800,bg=JCCOLORS['FLAT_BLUE'])
box0 = Box(app, layout="auto",height=75, width=500)
box1 = Box(app, layout="grid",border=2)
box2 = Box(app, layout="auto",height=320, width=625)

# BOX 0
lbl_title = Text(box0,text="Juniata Swimming App",font="Roboto Slab Bold",size=36,width="fill",height="fill",align="bottom",color=JCCOLORS['DARK_BLUE'])

# BOX 1
# Row 0 
lbl_debug = Text(box1,text="Debug",color=JCCOLORS['COOL_GRAY'],grid=[0,0])
# Row 1
lbl_nme = Text(box1,text="Home",color=JCCOLORS['FLAT_BLUE'],grid=[0,1])
# grid=[1,1]
# grid=[2,1]
# grid=[3,1]
lbl_manage = Text(box1,text="Manage",color=JCCOLORS['COOL_GRAY'],grid=[4,1])
lbl_stats= Text(box1,text="Stats",color=JCCOLORS['COOL_GRAY'],grid=[5,1])
lbl_cal = Text(box1,text="Calendar",color=JCCOLORS['COOL_GRAY'],grid=[6,1,])
lbl_roster = Text(box1,text="Roster",color=JCCOLORS['COOL_GRAY'],grid=[7,1])

# Row 2
button_home=PushButton(box1,text="Home",command=go_home,grid=[0,2])
# grid=[1,2]
# grid=[2,2]
# grid=[3,2]
combo_manage = Combo(box1, options=menu_manage,command=do_manage,grid=[4,2])
combo_stats  = Combo(box1, options=menu_stats,command=do_stats,grid=[5,2])
button_calendar = PushButton(box1,text="Calendar",command=do_calendar,grid=[6,2])
button_roster=PushButton(box1, text="Roster", command=open_window, grid=[7,2])
button_exit=PushButton(box1, text="Exit", command=do_quit, grid=[8,2])

# BOX 2
applogo = Picture(box2,image="app-logo.png")


window_2 = Window(app, title="Swimmer Roster", height=500, width=600)
#box to group objects
box = Box(window_2, layout="grid")

# First Name
col0_0 = Text(box, text="First Name", size=18, color="blue", font="Arial", align="left", grid=[0,0])
# Last Name
col1_0 = Text(box, text="Last Name", size=18, color="blue", font="Arial", align="left", grid=[1,0])
# School Year
col2_0 = Text(box, text="Year", size=18, color="blue", font="Arial", align="left", grid=[2,0])
# Email
col3_0 = Text(box, text="Email", size=18, color="blue", font="Arial", align="left", grid=[3,0])

col0_1 = Text(box, text="Brad", size=14, color="red", font="Arial", align="left", grid=[0,1])
col1_1 = Text(box, text="Newman", size=14, color="red", font="Arial", align="left", grid=[1,1])
col2_1 = Text(box,text="Senior", size=14, color="red", font="Arial", align="left", grid=[2,1])
col3_1 = Text(box, text="brad.newman@juniata.edu", size=14, color="red", font="Arial", align="left", grid=[3,1])


col0_2 = Text(box, text="Mark", size=14, color="red", font="Arial", align="left", grid=[0,2])
col1_2 = Text(box, text="Beekey", size=14, color="red", font="Arial", align="left", grid=[1,2])
col2_2 = Text(box,text="Senior", size=14, color="red", font="Arial", align="left", grid=[2,2])
col3_2 = Text(box, text="mark.beeky@juniata.edu", size=14, color="red", font="Arial", align="left", grid=[3,2])

footer = Box(window_2,layout="auto")
swimlogo=Picture(footer,image="swim-use.png",align="right")

close_da_door = PushButton(window_2, text="close a window", command=close_window)

window_2.hide()

app.display()