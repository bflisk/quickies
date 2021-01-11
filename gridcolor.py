#
# Brendan Flisk
# This program creates a graphics windown with a grid
# and allows the user to fill in rectangles by
# clicking on them
#

# imports the necessary libraries
from graphics import *

# creates a specfied amount of rectangles
class RectVar:
	def __init__(self,name,value):
		self.name = name
		self.value = value

# searches for the rectangles the user clicked on
def search(click,plist,xlist,ylist,xframe,yframe):
	found = []

	# finds closest x value to the click
	for x in xlist[:xframe]:
		if abs(click.getX() - x) < 5:
			found.append(x)
			break
		else:
			pass

	# finds the closest y value to the mouseclick
	y = 0
	while y < len(ylist):
		if abs(click.getY() - ylist[y]) > 5:
			y += yframe
		else:
			found.append(ylist[y])
			break

	# searches through plist for the correct rectangle to change to black
	py = 0
	while py < len(plist):
		try:
			if found[1] == plist[py].value.getCenter().getY():
				for px in plist[py:py+xframe]:
					if found[0] == px.value.getCenter().getX():
						px.value.setFill('black')
						break
					else:
						pass
				break
			else:
				pass
			py += yframe
		except:
			print('excepted')
			break

	return found

def main():
	#width = eval(input('Width: '))
	#height = eval(input('Height: '))
	width = 1000
	height = 500

	win = GraphWin('Test',width,height)
	plist = []

	# dynamically creates a grid for the graphics window
	for p in range(int(win.getHeight()/10)):
		y = 0+10*p
		for i in range(int(win.getWidth()/10)):
			plist.append(RectVar('Rect'+str(i),Rectangle(Point(0+10*i,0+y),Point(10+10*i,10+y))))
			plist[-1].value.draw(win)

	# stores the x and y values of the centerpoints of each rectangle
	xlist,ylist = [],[]

	for i in plist:
		xlist.append(i.value.getCenter().getX())
		ylist.append(i.value.getCenter().getY())

	# checks for mouseclick in the graphics window
	ifclick = False
	found = False
	while ifclick == False:
		click = win.checkMouse()
		if click != None:
			while found == False:
				found = search(click,plist,xlist,ylist,width//10,height//10)
		else:
			pass
		found = False

	win.close()

main()
