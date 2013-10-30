running = True          # Trying to set a variable that will switch the program off

class State(object):
	menu = 'menu'
	play = 'play'
	quit = 'quit'

class Main:

	def __init__(self, state):
		self.state = state

	def displayState(self):
		print self.state

	def getState(self):
		return self.state

	def changeState(self, state):
		self.state = state

	def getInput(self):
		uIn = raw_input('Gimme a state: ')
		if uIn == 'Menu':
			print 'OK menu'
			self.state = State.menu
		elif uIn == 'Quit':
			print 'OK quit'
			self.state = State.quit
		elif uIn == 'Play':
			print 'OK play'
			self.state = State.play
		else:
			print 'Whatever'
		return uIn

	def update(self):
		self.getInput()

	def prog_loop(self):
		running = True
		self.state = State.menu

		while running:
			if self.state is State.menu:
				# Do something a menu might do
				print "I'm doing menu-y things!"
				self.update()

			elif self.state is State.play:
				# Throw a ball or something!
				print "I'm throwing a penguin!"
				self.update()
			else:
				# Make like a tree
				running = False


prog = Main(State.menu) # Create a main loop object that starts with the 'menu state'

prog.prog_loop()


