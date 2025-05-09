`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 04/05/2025 11:36:05 PM
// Design Name: 
// Module Name: LayerNorm
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


module LayerNorm (
    input wire clk,
    input wire rst,
    input wire valid_in,
    input wire [7:0] x0,
    input wire [7:0] x1,
    input wire [7:0] x2,
    input wire [7:0] x3,
    output reg valid_out,
    output reg [7:0] y0,
    output reg [7:0] y1,
    output reg [7:0] y2,
    output reg [7:0] y3
);

    integer i;
    reg [9:0] sum;
    reg [9:0] mean;
    reg [15:0] variance;
    reg [7:0] x[0:3];
    reg [7:0] norm[0:3];

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            valid_out <= 0;
            y0 <= 0;
            y1 <= 0;
            y2 <= 0;
            y3 <= 0;
        end
        else if (valid_in) begin
            // Prepare inputs
            x[0] = x0;
            x[1] = x1;
            x[2] = x2;
            x[3] = x3;

            // Compute mean
            sum = x[0] + x[1] + x[2] + x[3];
            mean = sum >> 2;

            // Compute variance (not used for normalization here)
            variance = 0;
            for (i = 0; i < 4; i = i + 1)
                variance = variance + (x[i] - mean) * (x[i] - mean);
            variance = variance >> 2;

            // Normalize (center only)
            for (i = 0; i < 4; i = i + 1)
                norm[i] = x[i] - mean;

            // Assign outputs
            y0 <= norm[0];
            y1 <= norm[1];
            y2 <= norm[2];
            y3 <= norm[3];

            valid_out <= 1;
        end else begin
            valid_out <= 0;
        end
    end
endmodule
