import sys
import json
import pynq
import struct
import numpy as np

def writeSetting(setting):
    ol.reg_bank_0.write(value=setting["value"], offset=setting["offset"])
def getReading(reading):
    value = ol.reg_bank_0.read(offset=reading["offset"])
    readingString = '{"command":"reading","offset":'+ str(reading["offset"]) + ',"value":' + str(value) + '}'
    print(readingString)
def getTrace(trace):
    samples = trace["samples"]
    fftDisplayPts = trace["fftDisplayPts"]
    input_buffer_1 = pynq.allocate(shape=(samples,), dtype=np.int16)

    ol.axi_gpio_0.channel1.write(val=0, mask=0x1) #Trig low
    ol.axi_gpio_0.channel2.write(val=samples, mask=0xffffffff) #Set samples
    ol.axi_dma_0.recvchannel.transfer(input_buffer_1)
    ol.axi_gpio_0.channel1.write(val=1, mask=0x1) #Trig high
    ol.axi_dma_0.recvchannel.wait()
    fft = np.fft.fft(input_buffer_1) / samples
    fftrim1 = 2000 * np.log10(abs(fft[0:fftDisplayPts]))
    fftrim2 = np.zeros(shape=(fftDisplayPts,), dtype=np.int16)
    for ii in range(fftDisplayPts):
        fftrim2[ii] = int(fftrim1[ii])

#    bufI = []
#    for ii in range(0,samples):
#        bufI.append(struct.pack("h", input_buffer_1[ii]))
#    bufTotal = b''.join(bufI)
#    print('trace',end='\n')
#    sys.stdout.buffer.write(bufTotal)
#    print('',end='\n')

    print('{"command":"trace","value":',end='[')
    for ii in range(0,fftDisplayPts - 1):
        print(fftrim2[ii],end=",")
    print(fftrim2[fftDisplayPts - 1],end="]}\n")
    
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
    if instruction["command"] == "trace":
        getTrace(instruction)
        

