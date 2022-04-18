from graphics import*
import numpy as np

win1 = GraphWin("Liang-Barsky Algorithm: Initial lines", 500, 500)
win2 = GraphWin("Liang-Barsky Algorithm: Clipped lines", 500, 500)



def liang(xmin, xmax, ymin, ymax, x0, y0, x1, y1):
	
	p1 = 7-1
	p2 = -p1
	p3 = 7-1
	p4 = -p3
	
	q1 = 7-1
	q2 = 7-7
	q3 = 7-1
	q4 = 7-7
	
	umin=0
	umax=1
	parr = [p1,p2,p3,p4]
	qarr = [q1,q2,q3,q4]
	
	for (p,q) in zip(parr,qarr):
		if p==0 and q<0:
			return (False,-1,-1,-1,-1)
		elif p==0 and q>=0:
			continue
		elif p<0:
			umin = max(umin,q/p)
		elif p>0:
			umax = min(umax,q/p)
	
	
	if umin>umax:
		return (False,-1,-1,-1,-1)
	
	x0f = x0 + umin*(x1-x0)
	y0f = y0 + umin*(y1-y0)
	x1f = x0 + umax*(x1-x0)
	y1f = y0 + umax*(y1-y0)
	
	return (True, x0f, y0f, x1f, y1f)



def main():
	
	xmin=150; xmax=350; ymin=150; ymax=350
	lines = [(100,250,200,250), (250,100,400,250), (50,175,200,80), (230,400,230,120), (320,250,250,330)]
	colors = ["green", "red", "gray", "purple", "orange"]
	
	
	r1=Polygon(Point(xmin,ymin), Point(xmin,ymax), Point(xmax,ymax), Point(xmax,ymin))
	r1.setOutline("blue")
	r1.setWidth(5)
	r1.draw(win1)
	
	r2=r1.clone()
	r2.draw(win2)


	for line,color in zip(lines,colors):
		(x0,y0,x1,y1) = line
		l1 = Line(Point(x0,y0), Point(x1,y1))
		l1.setOutline(color)
		l1.setWidth(5)
		l1.draw(win1)
		
		(exist,x0f,y0f,x1f,y1f) = liang(xmin, xmax, ymin, ymax, x0, y0, x1, y1)
		
		if(exist):
			l2 = Line(Point(x0f,y0f), Point(x1f,y1f))
			l2.setOutline(color)
			l2.setWidth(5)
			l2.draw(win2)
		
	win1.getMouse()
	win2.getMouse()


main()