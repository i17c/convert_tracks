import curses

class Colors:
	_fg = {}
	_bg = {}
	
	def __init__(self):
		curses.setupterm()
		self._init_fg()
		self._init_bg()
	
	def _init_fg(self):
		self._fg = {
				'black': curses.tparm(curses.tigetstr('setaf'), 0),
				'red': curses.tparm(curses.tigetstr('setaf'), 1),
				'green': curses.tparm(curses.tigetstr('setaf'), 2),
				'brown': curses.tparm(curses.tigetstr('setaf'), 3),
				'blue': curses.tparm(curses.tigetstr('setaf'), 4),
				'purple': curses.tparm(curses.tigetstr('setaf'), 5),
				'cyan': curses.tparm(curses.tigetstr('setaf'), 6),
				'light-gray': curses.tparm(curses.tigetstr('setaf'), 7),
				'dark-gray': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 0),
				'light-red': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 1),
				'light-green': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 2),
				'yellow': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 3),
				'light-blue': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 4),
				'light-purple': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 5),
				'light-cyan': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 6),
				'white': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setaf'), 7)
				}
		
	def _init_bg(self):
		self._bg = {
				'black': curses.tparm(curses.tigetstr('setab'), 0),
				'red': curses.tparm(curses.tigetstr('setab'), 1),
				'green': curses.tparm(curses.tigetstr('setab'), 2),
				'brown': curses.tparm(curses.tigetstr('setab'), 3),
				'blue': curses.tparm(curses.tigetstr('setab'), 4),
				'purple': curses.tparm(curses.tigetstr('setab'), 5),
				'cyan': curses.tparm(curses.tigetstr('setab'), 6),
				'light-gray': curses.tparm(curses.tigetstr('setab'), 7),
				'dark-gray': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 0),
				'light-red': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 1),
				'light-green': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 2),
				'yellow': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 3),
				'light-blue': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 4),
				'light-purple': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 5),
				'light-cyan': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 6),
				'white': curses.tparm(curses.tigetstr('bold')) + curses.tparm(curses.tigetstr('setab'), 7)
				}
	
	def bg(self, color):
		return self._bg[color]
		
	def reset(self):
		return curses.tparm(curses.tigetstr('sgr0'))
	
	def fg(self, color):
		return self._fg[color]
