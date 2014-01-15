#Hadar Cohen
#CS102E
#Professor Cusack
#12/7/2011
#Project 13

from Tkinter import *
root= Tk()
from intersect import *

class MyCanvas (Canvas):
	def __init__( this, *args, **kwargs ):
		Canvas.__init__( this, *args, **kwargs )
		this.ball = this.makeBall(400, 100)
		this.ball2 = this.makeBall2(1, 100)
		this.paddle = this.makeRectangle(225, 475)
		for x in range (0,500, 50):
			for y in range (0, 50, 20):
				this.makeBlock(x,y)
		for x in range (0,500, 50):
			for y in range (50, 100, 20):
				this.makeStrongBlock(x,y)
		#this.bind("<KeyPress>", this.keyWasPressed ) 
		this.bind("<Motion>", this.mouseHasMoved )
		this.focus_set()
		this.ball_velocity_x = 3
		this.ball_velocity_y = 2
		this.ball2_velocity_x = 4
		this.ball2_velocity_y = -2.5
	def makeRectangle( this, x, y, color="black" ):
		return this.create_rectangle( x, y, x+50, y+10, fill=color )
	def makeBlock (this, x, y, color="red"):
		return this.create_rectangle( x, y, x+50, y+10, fill=color, tags=("block",))
	def makeStrongBlock (this, x, y, color="orange"):
		return this.create_rectangle( x, y, x+50, y+10, fill=color, tags=("block", "strong"))
	def makeBall (this, x, y, color="yellow"):
		return this.create_oval( x, y, x+5, y+5, fill=color )
	def makeBall2 (this, x, y, color="yellow"):
		return this.create_oval( x, y, x+5, y+5, fill=color )
	def moveStuff( this ): 
		sx, sy, ex, ey = this.coords( this.ball )
		rx, ry, dx, dy = this.coords( this.paddle )
		if sy <=0:
			this.ball_velocity_y = -this.ball_velocity_y
		if sx <=0:
			this.ball_velocity_x = -this.ball_velocity_x
		if ex >=500:
			this.ball_velocity_x = -this.ball_velocity_x
		if ey >=500:
			raise("Game Over")
		if ey >= 475 and rx <= sx <=dx and rx <= ex <=dx: 
			if (sx+ex)/2 <= (rx+dx)/2:
				this.ball_velocity_y = -this.ball_velocity_y
				this.ball_velocity_x = (this.ball_velocity_x) -  1
			if (sx+ex)/2 >= (rx+dx)/2:
				this.ball_velocity_y = -this.ball_velocity_y
				this.ball_velocity_x = (this.ball_velocity_x) + 1
		this.move( this.ball, this.ball_velocity_x, this.ball_velocity_y )
		sx, sy, ex, ey = this.coords( this.ball2 )
		if sy <=0:
			this.ball2_velocity_y = -this.ball2_velocity_y
		if sx <=0:
			this.ball2_velocity_x = -this.ball2_velocity_x
		if ex >=500:
			this.ball2_velocity_x = -this.ball2_velocity_x
		if ey >=500:
			raise("Game Over")
		if ey >= 475 and rx <= sx <=dx and rx <= ex <=dx:
			if (sx+ex)/2 <= (rx+dx)/2:
				this.ball2_velocity_y = -this.ball2_velocity_y
				this.ball2_velocity_x = (this.ball2_velocity_x) - 1
			if (sx+ex)/2 >= (rx+dx)/2:
				this.ball2_velocity_y = -this.ball2_velocity_y
				this.ball2_velocity_x = (this.ball2_velocity_x) + 1
		this.move( this.ball2, this.ball2_velocity_x, this.ball2_velocity_y )
		allblocks = this.find_withtag( "block" )
		for block in allblocks:
			rx, ry, dx, dy = this.coords( block )
			sx, sy, ex, ey = this.coords( this.ball )
			qx, qy, wx, wy = this.coords( this.ball2 )
			a = hits(rx, ry, dx, dy, sx, sy, ex, ey)
			b = hits(rx, ry, dx, dy, qx, qy, wx, wy)
			tags = this.gettags( block )
			if 'N' in a:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball_velocity_y = -abs(this.ball_velocity_y)
				print(a)
			if 'S' in a:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball_velocity_y = abs(this.ball_velocity_y)
				print(a)
			if 'E' in a:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball_velocity_x = abs(this.ball_velocity_x)
				print(a)
			if 'W' in a:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball_velocity_x = -abs(this.ball_velocity_x)
				print(a)
			if 'N' in b:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball2_velocity_y = -abs(this.ball2_velocity_y)
				print(b)
			if 'S' in b:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball2_velocity_y = abs(this.ball2_velocity_y)
				print(b)
			if 'E' in b:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball2_velocity_x = abs(this.ball2_velocity_x)
				print(b)
			if 'W' in b:
				if 'strong' in tags:
					this.delete( block )
					this.makeBlock (rx, ry)
				else:
					this.delete( block )
				this.ball2_velocity_x = -abs(this.ball2_velocity_x)
				print(b)
		if len(allblocks) == 0:
			raise( "You Win!")
	def keyWasPressed( this, event=None ):
		sx, sy, ex, ey = this.coords( this.paddle )
		key = event.keysym 
		if key == "Left":
			if sx >0:
				this.move( this.paddle, -25, 0)
		if key == "Right":
			if ex <500:
				this.move( this.paddle, 25, 0)
		if sx<0:
			this.move( this.paddle, -sx, 0)
		if ex>500:
			this.move (this.paddle, 500-ex, 0)
	def mouseHasMoved( this, event ):
		rx, ry, dx, dy = this.coords( this.paddle )
		this.move( this.paddle, event.x - (rx+dx)/2, 0)
		rx, ry, dx, dy = this.coords( this.paddle )
		if rx<=0:
			this.move( this.paddle, -rx, 0)
		if dx>=500:
			this.move (this.paddle, 500-dx, 0)
		#print( event.x, event.y )
canvas = MyCanvas( root, width=500, height=500 ) 
canvas.pack()
while( True ): 
	canvas.moveStuff()
	root.update()
