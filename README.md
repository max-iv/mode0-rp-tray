# Timing Gate Generator
* gateGen125-tray <a href="https://github.com/bl-mirrotron/gateGen125-tray" target="_blank">source code</a>
* [Timing System Overview](https://bl-mirrotron.github.io/#timing-system)

The Timing Gate Generator uses a <a href="https://redpitaya.com/product-category/stemlab-125-14/" target="_blank">Red Pitaya Stemlab 125-14</a> to generate 8 timing channels system based on a 32 bit counter clocked at 125 MHz. The resolution of the timing system is 8nS and can have intervals as long as 17 seconds. The output of the gate generator uses the <a href="https://bl-mirrotron.github.io/mirrotron-rfq-llrf-timer-cube" target="_blank">RFQ LLRF Timer Cube</a> circuit as shown in Figure 1.

The FPGA code for the Gate Generator was developed with the <a href="https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html" target="_blank">Vivado 2020.2 HLS</a> design edition following the  <a href="https://github.com/dspsandbox/FPGA-Notes-for-Scientists" target="_blank">FPGA Notes for Scientists</a> tutorials.

<p></p><p style="text-align:center;font-size: large;"><span style="font-weight: bold;color: green;">Figure 1. </span> <span style="font-style: italic;">Gate Generator Implementation</span></p>
<div style="width:100%;text-align:center;"><img width="100%" style="border-style:solid;border-color:#1c6e97;" src="doc/GateGenImpl.jpg"/></div><br>



 <a href="" target="_blank"></a>
