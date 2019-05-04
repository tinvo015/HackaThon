
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
	app.showSubWindow('identify new person')
	pass

def exitButton():
	app.stop()

def openPic():
	fileTypes = [('images', '*.jpeg'), ('images', '*.png'), ('images', '*.gif')]
	image = app.openBox(title='select image', fileTypes=fileTypes, parent='identify new person')
	if image:
		copyfile(image, newPersonImage)
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
	app.startLabelFrame('Other data',2,1,0,3)
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

def setupSubwindows():
	# Sub-windows...
	app.startSubWindow("identify new person")
	copyfile(blankImage, newPersonImage)
	app.addButton('Add Picture', openPic)
	app.addImage('new image', newPersonImage)
	app.startLabelFrame('Preview')
	app.setImageSize('new image', 200, 300)
	app.stopLabelFrame()
	app.addButton('Add Fingerprint file', openPrintfile)
	
	app.stopSubWindow()
	
def main():
	print('GUI starting...')
	setupGui()
	setupSubwindows()
	app.go()
	

if __name__ == '__main__':
	main()
