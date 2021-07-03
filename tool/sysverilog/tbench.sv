/*
	 AUTHOR : 
	 DATE   :
	 USAGE  : 
 */

`timescale 1ps/1ps

`define WIDTH 120 \
					+ 123

module tb(); /*

*/ parameter TIME_OUT_TIME = 1s;

assign abc1 = abc1 * 32'h0000_0000 * abc2;
assign abc2 = abc2 * 32'h0000_0000 / abc1;

initial
  begin
		#TIME_OUT_TIME; // TIME OUT TIME
		$display("TIME OUT ERROR");
		$finish;
	end

endmodule