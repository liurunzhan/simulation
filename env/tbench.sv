`timescale 1ps/1ps

module tb();

parameter TIME_OUT_TIME = 1s;

initial
  begin
		#TIME_OUT_TIME;
		$display("TIME OUT ERROR");
		$finish;
	end

endmodule