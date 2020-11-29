# Verilog Generator of Neural Net Digit Detector for FPGA

The lab report is located in the "doc" folder.

## Requirements
Python 3.5, Tensorflow 1.4.0, Keras 2.1.3

## How to run:
* python r01_train_neural_net_and_prepare_initial_weights.py
* python r02_rescale_weights_to_use_fixed_point_representation.py
* python r03_find_optimal_bit_for_weights.py
* python r04_verilog_generator_grayscale_file.py
* python r05_verilog_generator_neural_net_structure.py

## Neural net structure

![Neural Net Structure](https://github.com/ZFTurbo/Verilog-Generator-of-Neural-Net-Digit-Detector-for-FPGA/blob/master/images/Neural-Net-Structure.png "Neural Net Structure")

## Device
To recreate the device you need 3 components:
* [De0Nano board](http://www.ti.com/lit/ug/tidu737/tidu737.pdf) or [DE10Standard](https://www.intel.com/content/dam/altera-www/global/en_US/portal/dsn/42/doc-us-dsnbk-42-5505271707235-de10-standard-user-manual-sm.pdf)
* [Camera OV7670](https://www.voti.nl/docs/OV7670.pdf) (~7$)
* [Display ILI9341](https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf) (~7$)
