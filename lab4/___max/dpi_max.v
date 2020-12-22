`timescale 1ns / 1ns

module top;
typedef bit[9:0]  My1DBV[2:0];
typedef bit[9:0]  My2DBV[3:0];
typedef bit[9:0]  My3DBV[4:0];
typedef bit[9:0]  My4DBV[5:0];


import "DPI-C" function void max_arr(input bit [9:0] p [], input int n, output bit [9:0] res);

My1DBV bv1d;
My2DBV bv2d;
My3DBV bv3d;
My4DBV bv4d;

bit [9:0] answer;

initial begin
bv1d[0] = 10'b0010101001;
bv1d[1] = 10'b1010000000;
bv1d[2] = 10'b0000000001;

bv2d[0] = 10'b1010101001;
bv2d[1] = 10'b1010000000;
bv2d[2] = 10'b0000001001;
bv2d[3] = 10'b0000000000;

bv3d[0] = 10'b1010101001;
bv3d[1] = 10'b1010000000;
bv3d[2] = 10'b1100000000;
bv3d[3] = 10'b0010000001;
bv3d[4] = 10'b0100000100;

bv4d[0] = 10'b1010101001;
bv4d[1] = 10'b1010000000;
bv4d[2] = 10'b1100000000;
bv4d[3] = 10'b0010000001;
bv4d[4] = 10'b0100000100;
bv4d[5] = 10'b1110000000;
max_arr(bv1d, 3, answer);
$display(" max (3 el.) = %b", answer); #10;
max_arr(bv2d, 4, answer);
$display(" max (4 el.) = %b", answer); #10;
max_arr(bv3d, 5, answer);
$display(" max (5 el.) = %b", answer); #10;
max_arr(bv4d, 6, answer);
$display(" max (6 el.) = %b", answer); #10;
$finish;
end

endmodule