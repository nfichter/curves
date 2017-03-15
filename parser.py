from display import *
from matrix import *
from draw import *
import math
import time
from random import randint

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""

#note, also added "color" which takes 3 args (r, g, b) from 0,255 or "random" for random
#"displaynoclr" to display without clear_screen, "savenoclr"
def parse_file( fname, points, transform, screen, color ):
    lines = open(fname).readlines()
    lineNum = 0
    while lineNum < len(lines):
    	add = 2
    	cmd = lines[lineNum][:-1]
    	print cmd
    	if cmd == "line":
    		args = lines[lineNum+1].split(" ")
    		add_edge(points,int(args[0]),int(args[1]),int(args[2]),int(args[3]),int(args[4]),int(args[5]))
    	elif cmd == "ident":
    		add = 1
    		ident(transform)
    	elif cmd == "scale":
    		args = lines[lineNum+1].split(" ")
    		scale = make_scale(float(args[0]),float(args[1]),float(args[2]))
    		matrix_mult(scale, transform)
    	elif cmd == "move":
    		args = lines[lineNum+1].split(" ")
    		translate = make_translate(int(args[0]),int(args[1]),int(args[2]))
    		matrix_mult(translate, transform)
    	elif cmd == "rotate":
    		args = lines[lineNum+1].split(" ")
    		rotate = []
    		rad = int(args[1]) * math.pi / 180.0
    		if args[0] == "x":
    			rotate = make_rotX(rad)
    		if args[0] == "y":
    			rotate = make_rotY(rad)
    		if args[0] == "z":
    			rotate = make_rotZ(rad)
    		matrix_mult(rotate, transform)
    	elif cmd == "color":
    		args = lines[lineNum+1].split(" ")
    		print args[0]
    		if args[0] == "random":
    			color[0] = randint(0,256)
    		else:
	    		color[0] = int(args[0])
	    	if args[1] == "random":
	    		color[1] = randint(0,256)
	    	else:
    			color[1] = int(args[1])
    		if args[2] == "random\n":
	    		color[2] = randint(0,256)
	    	else:
	    		color[2] = int(args[2])
    	elif cmd == "apply":
    		add = 1
    		matrix_mult(transform, points)
    		for i in range(0,len(points)):
    			for j in range(0,len(points[0])):
    				points[i][j] = int(points[i][j])
    	elif cmd == "display":
    		add = 1
    		clear_screen(screen)
    		draw_lines( points, screen, color )
    		time.sleep(0.1)
    		display(screen)
    	elif cmd == "displaynoclr":
    		add = 1
    		draw_lines( points, screen, color )
    		time.sleep(0.1)
    		display(screen)
    	elif cmd == "save":
    		args = str(lines[lineNum+1])
    		clear_screen(screen)
    		draw_lines( points, screen, color )
    		time.sleep(0.1)
    		save_extension(screen,args)
    	elif cmd == "savenoclr":
    		args = str(lines[lineNum+1])
    		draw_lines( points, screen, color )
    		time.sleep(0.1)
    		save_extension(screen,args)
    	elif cmd == "quit":
    		break
    	lineNum += add