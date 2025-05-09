`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/05/2025 11:37:45 PM
// Design Name: 
// Module Name: LayerNorm_top
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module LayerNorm_top (
    input wire clk,
    input wire reset,
    input wire valid_in,
    input wire [7:0] x0,
    input wire [7:0] x1,
    input wire [7:0] x2,
    input wire [7:0] x3,
    output wire valid_out,
    output wire [7:0] y0,
    output wire [7:0] y1,
    output wire [7:0] y2,
    output wire [7:0] y3
);

    LayerNorm ln_inst (
        .clk(clk),
        .rst(reset),
        .valid_in(valid_in),
        .x0(x0),
        .x1(x1),
        .x2(x2),
        .x3(x3),
        .valid_out(valid_out),
        .y0(y0),
        .y1(y1),
        .y2(y2),
        .y3(y3)
    );

endmodule
