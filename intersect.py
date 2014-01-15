#Hadar Cohen
#CS102E
#Professor Cusack
#12/7/2011

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
	try:
		ua = ((x4-x3)*(y1-y3)-(y4-y3)*(x1-x3))/((y4-y3)*(x2-x1)-(x4-x3)*(y2-y1))
		x = x1 + ua*(x2-x1)
		y = y1 + ua*(y2-y1)
		if between( x, x1, x2) and between(x, x3, x4) and between(y, y1, y2) and between(y, y3, y4):
			return (x, y)
	except:
		return None
		
def between( n, first, second ):
	if first <= n <= second:
		return True
	if second <= n <= first:
		return True
	return False

def edges( sx, sy, ex, ey ):
	return ( (sx,sy,ex,sy), (ex, sy, ex, ey), (ex, ey, sx, ey), (sx, ey, sx, sy) )
	
def intersectOne( coords1, coords2 ):
		if intersect(*(coords1 + coords2)):
			return True
		return False
		
def intersectAny( coords1, many ):
		for coord in many:
			if intersectOne(coords1, coord ):
				return True
		return False
			
def hits(sx1,sy1,ex1,ey1,sx2,sy2,ex2,ey2):
	i_was_hit_on = []
	box2 = edges( sx1, sy1, ex1, ey1)
	box1 = edges( sx2, sy2, ex2, ey2)
	if intersectAny( box2[0], box1 ):
		i_was_hit_on.append( "N")
	if intersectAny( box2[1], box1 ):
		i_was_hit_on.append( "E")
	if intersectAny( box2[2], box1 ):
		i_was_hit_on.append( "S")
	if intersectAny( box2[3], box1 ):
		i_was_hit_on.append( "W")
	return i_was_hit_on

if __name__ == '__main__':
	print( intersect( -1.0, 2.0, 1.0, -1.0, 1.0, 1.0, -2.0, -1.0 ) )
	print( intersect( -1.0, 2.0, 1.0, -1.0, 1.0, 1.0, 3.0, 4.0 ) )
	print( intersect( 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 2.0, 2.0 ) )
	print( intersect( 1.0, 1.0, 2.0, 2.0, 2.0, 1.0, 3.0, 2.0 ) )
	box1 = ( 1, 1, 10, 10 )
	print( edges( *box1 ) )
	coords1 = (-1.0, 2.0 ,1.0, -1.0)
	coords2 = (1.0, 1.0, -2.0, -1.0)
	coords3 = (1.0, 1.0, 3.0, 4.0)
	many1 = ( coords2, coords3 )
	many2 = ( coords3, coords3 )
	print( intersectOne( coords1, coords2 ))
	print( intersectAny( coords1, many1))
	print( intersectAny( coords1, many2))
	box1 = ( 1.0, 1.0, 10.0, 10.0 )
	box2 = ( 0.0, 0.0, .5, .5 )
	box3 = ( 0.0, 0.0, 5.0, 5.0 )
	box4 = ( 0.0, 0.0, 11.0, 2.0 )
	box5 = ( 0.0, 0.0, 11.0, 11.0 )
	box6 = ( 3.0, 3.0, 4.0, 4.0 )
	box7 = ( 4.0, 0.0, 5.0, 5.0 )
	print( hits( *(box1+box2) ) )
	print( hits( *(box1+box3) ) )
	print( hits( *(box1+box4) ) )
	print( hits( *(box1+box5) ) )
	print( hits( *(box1+box6) ) )
	print( hits( *(box1+box7) ) )
