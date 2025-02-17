from cmu_graphics import *
from tree import *
from tod import *

def onAppStart(app):
    app.background = "lightblue"
    app.width = 540
    app.height = 860
    app.timeOfDay = get_current_datetime()

def onStep(app):
    app.stepsPerSecond = 60
    app.timeOfDay = get_current_datetime()



def redrawAll(app):
    drawRect(0, 0, app.width, app.height,  fill = app.background)
    drawLabel(app.timeOfDay.time, app.width/2, app.height/2, font = "Arial", size = 40, fill = "black")

def get_current_time():
    """
    Get the current date and time from the system.

    :return: A DateTime object with the current date and time.
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")  # Format: HH:MM:SS
    return DateTime(current_time)

runApp(width=540, height=860)