import sys
import json
import pynq

def writeSetting(setting):
    ol.reg_bank_0.write(value=setting["value"], offset=setting["offset"])
def getReading(reading):
    value = ol.reg_bank_0.read(offset=reading["offset"])
    readingString = '{"command":"reading","offset":'+ str(reading["offset"]) + ',"value":' + str(value) + '}'
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
        

