class Main:								# Creating a basic Main class
	def __init__(self, state):
		self.state = state

	def displayState(self):
		print self.state

	def getState(self):
		return self.state

	def changeState(self, state):
		self.state = state

mainLoop = Main('menu') # Create a main loop object that starts with the 'menu state'
mainLoop.displayState() # Test a function of the mainLoop object

running = True          # Trying to set a variable that will switch the program off
state = mainLoop.state
print state             # For testing

while running:
	if state == 'menu':
		print state
		mainLoop.changeState('travel')
	elif state == 'travel':
		print state
		mainLoop.changeState('quit')
		running = False						# Infinite loop for some reason.