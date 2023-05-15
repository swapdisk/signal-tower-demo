# Signal Tower Demo

I was given this signal tower and asked to interface it to Raspberry Pi GPIO outputs. The only problem is the lights are powered by 120/240 VAC, so obviously, the Pi can't drive it directly. I made this custom 4-channel driver board to get it going. The python scripts in this repo demonstrate how to interface to the lights using my driver board.

Here's the driver board schematic. This circuit is repeated for each channel:

![Schematic diagram](images/driver-sch.png)

Here are some photos from my weekend spent making the driver board:

![Schematic diagram](images/PXL_20230512_212219251.jpg)<br>Prototyping the circuit.

![Schematic diagram](images/PXL_20230512_212808728.jpg)<br>Getting the parts together.

![Schematic diagram](images/PXL_20230513_203036608.jpg)<br>The finished board ready to plug in and test.

![Schematic diagram](images/PXL_20230513_203401300.TS.jpg)<br>Oh wow, it works!

![Schematic diagram](images/PXL_20230515_114307146.jpg)<br>Safely packaged so nobody gets shocked.

Enjoy with beverage of choice!