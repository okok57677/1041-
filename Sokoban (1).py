import curses
stdscr = curses.initscr()
curses.start_color()

curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK) # 'H'
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK) # 'W'
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK) # 'B'
curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_CYAN) # 'D'
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_CYAN) # 'C'

def readMap(n):
	mapn = "{0:03}".format(n)
	map = "map"+mapn+".txt"
	inmap = open(map,"r")
	mapdata = inmap.read()
	return mapdata

def showMap(m):
	maplen = len(m)
	stdscr.move(0,0)
	for i in range(maplen):
		if m[i] == "H":
			stdscr.addstr(m[i],curses.color_pair(1))
		elif m[i] == "W":
			stdscr.addstr(m[i],curses.color_pair(2))
		elif m[i] == "B":
			stdscr.addstr(m[i],curses.color_pair(3))
		elif m[i] == "D":
			stdscr.addstr(" ",curses.color_pair(4))
		elif m[i] == "C":
			stdscr.addstr("B",curses.color_pair(5))
		else:
			stdscr.addstr(m[i])

	stdscr.refresh()

def main():
	myMap = readMap(0)
	showMap(myMap)

curses.endwin()

if __name__ == "__main__":
	main()
