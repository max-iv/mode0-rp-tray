import sys
import json
import pynq

def getGpioOverlay(gpio):
    if gpio == 0:
        return ol.axi_gpio_0
    if gpio == 1:
        return ol.axi_gpio_1
    if gpio == 2:
        return ol.axi_gpio_2
    if gpio == 3:
        return ol.axi_gpio_3
    if gpio == 4:
        return ol.axi_gpio_4
    if gpio == 5:
        return ol.axi_gpio_5
    if gpio == 6:
        return ol.axi_gpio_6
    if gpio == 7:
        return ol.axi_gpio_7
    if gpio == 8:
        return ol.axi_gpio_8
    if gpio == 9:
        return ol.axi_gpio_9
    if gpio == 10:
        return ol.axi_gpio_10
    if gpio == 11:
        return ol.axi_gpio_11
    if gpio == 12:
        return ol.axi_gpio_12
def getChannelOverlay(gpio,channel):
    if channel == 1:
        return getGpioOverlay(gpio).channel1
    if channel == 2:
        return getGpioOverlay(gpio).channel2
def writeSetting(setting):
    getChannelOverlay(setting["gpio"],setting["channel"]).write(val=setting["value"], mask=setting["mask"])
def getReading(reading):
    value = getChannelOverlay(reading["gpio"],reading["channel"]).read()
    readingString = '{"command":"reading","gpio":'+ str(reading["gpio"]) +',"channel":' + str(reading["channel"]) + ',"value":' + str(value) + '}'
    print(readingString)

instructionText = sys.stdin.readline().strip('\n')
instruction = json.loads(instructionText) 
ol = pynq.Overlay(instruction["overlay"] );
print(instructionText)

while True:
    instructionText = sys.stdin.readline().strip('\n')
    instruction = json.loads(instructionText) 
    if instruction["command"] == "setting":
        writeSetting(instruction)
        print(instructionText)
    if instruction["command"] == "reading":
        getReading(instruction)
        

