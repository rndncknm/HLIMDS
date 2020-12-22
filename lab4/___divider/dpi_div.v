`timescale 1ns / 1ns

module top;

typedef bit [9:0] bv10;

import "DPI-C" function void divider10(output bv10 quotient, input bv10 divident, divider);

bv10 x = 10'b0000010100;
bv10 y = 10'b0000000000;
bv10 answer;
initial begin
repeat (20) begin 
    #20 x=x+10'b0000000011;
    y=y+10'b0000000001;
    divider10(answer, x, y);
    $display(" %d / %d => %d", x, y, answer);
end
end

endmodule