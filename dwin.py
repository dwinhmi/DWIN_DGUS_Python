import serial
​
print("## ~~ DWIN Functions Init ~~ ")
print("Initializing Serial Port TTYS0")
​
dwinSerial = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)
​
​
def pageSwitch(pageNO):
	data = [0x5A, 0xA5, 0x07, 0x82, 0x00, 0x84, 0x5A, 0x01, 0x00, pageNO]
	dwinSerial.write(bytes(data))
​
def hmiBrightness(pBrightness):
	data = [0x5A, 0xA5, 0x04, 0x82, 0x00, 0x82, pBrightness]
	dwinSerial.write(bytes(data))
​
def setDatatoVP(pData):
	strLen = len(pData)
	strList = list(pData)
	data = [0x5A, 0xA5, strLen+3, 0x82, 0x20 , 0x10]
    # Here 2010 is the VP address
	for xValue in strList:
	 data.append(ord(xValue))
	dwinSerial.write(bytes(data))
​

def dwinListen():
	data = dwinSerial.read()
	return data.hex()