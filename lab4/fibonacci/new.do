#
# Copyright 1991-2015 Mentor Graphics Corporation
#
# All Rights Reserved.
#
# THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION
# WHICH IS THE PROPERTY OF MENTOR GRAPHICS CORPORATION
# OR ITS LICENSORS AND IS SUBJECT TO LICENSE TERMS.
#
# To run this example, bring up the simulator and type the following at the prompt:
#     do run.do
# or, to run from a shell, type the following at the shell prompt:
#     vsim -c -do run.do
# (omit the "-c" to see the GUI while running from the shell)
#

onerror {resume}
# Create the library.
if [file exists work] {
    vdel -all
}
vlib work

# Compile the HDL source(s)
vlog -sv -dpiheader "D:/intelFPGA_lite/17.1/modelsim_ase/examples/systemverilog/dpi/fibonacci/fibonacci.h" "D:/intelFPGA_lite/17.1/modelsim_ase/examples/systemverilog/dpi/fibonacci/fibonacci.v" "D:/intelFPGA_lite/17.1/modelsim_ase/examples/systemverilog/dpi/fibonacci/fibonacci.c"

# Simulate the design
vsim -c top 
run -all