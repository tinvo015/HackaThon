
from appJar import gui
from shutil import copyfile

app = gui('ID_entifer', '600x500')

blankImage = 'blank.gif'
mainPersonImage = 'mainImage.gif'
newPersonImage = 'newPersonImage.gif'
fingerPrintFile = 'blank.gif'

# When 'new person' button is pressed.
# reset and open popup
def newPerson():
	copyfile(blankImage, newPersonImage)
	app.reloadImage('new image', newPersonImage)
	app.showSubWindow('identify new person')

def exitButton():
	app.stop()

def openPic():
	fileTypes = [('images', '*.jpeg'), ('images', '*.png'), ('images', '*.gif')]
	image = app.openBox(title='select image', fileTypes=fileTypes, parent='identify new person')
	if image:
		copyfile(image, newPersonImage)
		print('newPersonImage is '+str(image))
		app.reloadImage('new image', newPersonImage)
		app.zoomImage('new image', -10)
	
def openPrintfile():
	fileTypes = [('images', '*.jpg')] # What filetypes for fingerpring???
	image = app.openBox(title='select image', fileTypes=fileTypes, parent='identify new person')
	if image:
		copyfile(image, fingerPrintFile)

def reloadMainPic(fileName):
	copyfile(image, mainPersonImage)
	app.reloadImage('identifying image', mainPersonImage)
	app.zoomImage('identifying image', -10)

def addPoint():
	# show popup
	app.showSubWindow('add data to person')

def doneAddData():
	app.hideSubWindow('add data to person')
	# Save the data
	
# Clears all the fields and loads new data
def reloadAll():
	app.hideSubWindow('identify new person', useStopFunction=False)
	
	
def setupGui():
	copyfile(blankImage, mainPersonImage)
	
	app.setSticky('w')
	app.addButton('new person', newPerson, 0, 0)
	app.setSticky('')
	app.addImage('identifying image', mainPersonImage, 1,0,0,2)
	app.setImageSize('identifying image', 200, 300)
	
	app.setSticky('e')
	app.addButton('logout', exitButton, 0, 1)
	app.setSticky('ew')
	
	app.startLabelFrame("Photo match confidence",3,0)
	app.setSticky('ew')
	app.addMeter('photo confidance')
	app.setMeterFill('photo confidance', "blue")
	app.setMeter('photo confidance', 0)
	app.stopLabelFrame()
	
	app.startLabelFrame("Fingerprint match confidence",4,0)
	app.setSticky('ew')
	app.addMeter('Fingerprint confidance')
	app.setMeterFill('Fingerprint confidance', "blue")
	app.setMeter('Fingerprint confidance', 0)
	app.stopLabelFrame()
	
	app.startLabelFrame('Identification Code', 1,1)
	app.setSticky('')
	app.addLabel('id_code','DEADBEEF1234')
	app.stopLabelFrame()
	
	app.setSticky('new')
	app.startLabelFrame('Other data',2,1,0,2)
	app.setSticky('nsew')
	app.addMessage('other data message', 'NO ADDITIONAL DATA')
	app.setMessageWidth('other data message', 200)
	app.stopLabelFrame()
	
	app.startLabelFrame('Total Confidance in identification',5,0,2)
	app.setSticky('ew')
	app.addMeter('total confidance')
	app.setMeterFill('total confidance', "red")
	app.setMeter('total confidance', 0)
	app.stopLabelFrame()
	
	app.addButton('Add data to person',addPoint,4,1)

def setupSubwindows():
	# New person window
	app.startSubWindow("identify new person")
	copyfile(blankImage, newPersonImage)
	app.addButton('Add Picture', openPic)
	app.addImage('new image', newPersonImage)
	app.startLabelFrame('Preview')
	app.setImageSize('new image', 200, 300)
	app.stopLabelFrame()
	app.addButton('Add Fingerprint file', openPrintfile)
	app.addButton('Done', reloadAll)
	app.stopSubWindow()
	
	# Add data window
	app.startSubWindow('add data to person')
	app.startLabelFrame('Key:')
	app.addEntry('key field')
	app.stopLabelFrame()
	app.startLabelFrame('Value:')
	app.addEntry('value field')
	app.stopLabelFrame()
	app.addButton('Add data', doneAddData)
	app.stopSubWindow()
	
def main():
	print('GUI starting...')
	setupGui()
	setupSubwindows()
	app.go()
	

if __name__ == '__main__':
	main()
