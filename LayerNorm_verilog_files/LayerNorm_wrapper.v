//Copyright 1986-2022 Xilinx, Inc. All Rights Reserved.
//--------------------------------------------------------------------------------
//Tool Version: Vivado v.2022.2 (lin64) Build 3671981 Fri Oct 14 04:59:54 MDT 2022
//Date        : Sun Apr  6 00:00:31 2025
//Host        : lifam-OptiPlex-7060 running 64-bit Ubuntu 20.04.6 LTS
//Command     : generate_target design_1_wrapper.bd
//Design      : design_1_wrapper
//Purpose     : IP block netlist
//--------------------------------------------------------------------------------
`timescale 1 ps / 1 ps

module design_1_wrapper
   (DDR_addr,
    DDR_ba,
    DDR_cas_n,
    DDR_ck_n,
    DDR_ck_p,
    DDR_cke,
    DDR_cs_n,
    DDR_dm,
    DDR_dq,
    DDR_dqs_n,
    DDR_dqs_p,
    DDR_odt,
    DDR_ras_n,
    DDR_reset_n,
    DDR_we_n,
    FIXED_IO_ddr_vrn,
    FIXED_IO_ddr_vrp,
    FIXED_IO_mio,
    FIXED_IO_ps_clk,
    FIXED_IO_ps_porb,
    FIXED_IO_ps_srstb,
    M_AXI_GP0_0_araddr,
    M_AXI_GP0_0_arburst,
    M_AXI_GP0_0_arcache,
    M_AXI_GP0_0_arid,
    M_AXI_GP0_0_arlen,
    M_AXI_GP0_0_arlock,
    M_AXI_GP0_0_arprot,
    M_AXI_GP0_0_arqos,
    M_AXI_GP0_0_arready,
    M_AXI_GP0_0_arsize,
    M_AXI_GP0_0_arvalid,
    M_AXI_GP0_0_awaddr,
    M_AXI_GP0_0_awburst,
    M_AXI_GP0_0_awcache,
    M_AXI_GP0_0_awid,
    M_AXI_GP0_0_awlen,
    M_AXI_GP0_0_awlock,
    M_AXI_GP0_0_awprot,
    M_AXI_GP0_0_awqos,
    M_AXI_GP0_0_awready,
    M_AXI_GP0_0_awsize,
    M_AXI_GP0_0_awvalid,
    M_AXI_GP0_0_bid,
    M_AXI_GP0_0_bready,
    M_AXI_GP0_0_bresp,
    M_AXI_GP0_0_bvalid,
    M_AXI_GP0_0_rdata,
    M_AXI_GP0_0_rid,
    M_AXI_GP0_0_rlast,
    M_AXI_GP0_0_rready,
    M_AXI_GP0_0_rresp,
    M_AXI_GP0_0_rvalid,
    M_AXI_GP0_0_wdata,
    M_AXI_GP0_0_wid,
    M_AXI_GP0_0_wlast,
    M_AXI_GP0_0_wready,
    M_AXI_GP0_0_wstrb,
    M_AXI_GP0_0_wvalid,
    M_AXI_GP0_ACLK_0,
    valid_in_0,
    valid_out_0,
    x0_0,
    x1_0,
    x2_0,
    x3_0,
    y0_0,
    y1_0,
    y2_0,
    y3_0);
  inout [14:0]DDR_addr;
  inout [2:0]DDR_ba;
  inout DDR_cas_n;
  inout DDR_ck_n;
  inout DDR_ck_p;
  inout DDR_cke;
  inout DDR_cs_n;
  inout [3:0]DDR_dm;
  inout [31:0]DDR_dq;
  inout [3:0]DDR_dqs_n;
  inout [3:0]DDR_dqs_p;
  inout DDR_odt;
  inout DDR_ras_n;
  inout DDR_reset_n;
  inout DDR_we_n;
  inout FIXED_IO_ddr_vrn;
  inout FIXED_IO_ddr_vrp;
  inout [53:0]FIXED_IO_mio;
  inout FIXED_IO_ps_clk;
  inout FIXED_IO_ps_porb;
  inout FIXED_IO_ps_srstb;
  output [31:0]M_AXI_GP0_0_araddr;
  output [1:0]M_AXI_GP0_0_arburst;
  output [3:0]M_AXI_GP0_0_arcache;
  output [11:0]M_AXI_GP0_0_arid;
  output [3:0]M_AXI_GP0_0_arlen;
  output [1:0]M_AXI_GP0_0_arlock;
  output [2:0]M_AXI_GP0_0_arprot;
  output [3:0]M_AXI_GP0_0_arqos;
  input M_AXI_GP0_0_arready;
  output [2:0]M_AXI_GP0_0_arsize;
  output M_AXI_GP0_0_arvalid;
  output [31:0]M_AXI_GP0_0_awaddr;
  output [1:0]M_AXI_GP0_0_awburst;
  output [3:0]M_AXI_GP0_0_awcache;
  output [11:0]M_AXI_GP0_0_awid;
  output [3:0]M_AXI_GP0_0_awlen;
  output [1:0]M_AXI_GP0_0_awlock;
  output [2:0]M_AXI_GP0_0_awprot;
  output [3:0]M_AXI_GP0_0_awqos;
  input M_AXI_GP0_0_awready;
  output [2:0]M_AXI_GP0_0_awsize;
  output M_AXI_GP0_0_awvalid;
  input [11:0]M_AXI_GP0_0_bid;
  output M_AXI_GP0_0_bready;
  input [1:0]M_AXI_GP0_0_bresp;
  input M_AXI_GP0_0_bvalid;
  input [31:0]M_AXI_GP0_0_rdata;
  input [11:0]M_AXI_GP0_0_rid;
  input M_AXI_GP0_0_rlast;
  output M_AXI_GP0_0_rready;
  input [1:0]M_AXI_GP0_0_rresp;
  input M_AXI_GP0_0_rvalid;
  output [31:0]M_AXI_GP0_0_wdata;
  output [11:0]M_AXI_GP0_0_wid;
  output M_AXI_GP0_0_wlast;
  input M_AXI_GP0_0_wready;
  output [3:0]M_AXI_GP0_0_wstrb;
  output M_AXI_GP0_0_wvalid;
  input M_AXI_GP0_ACLK_0;
  input valid_in_0;
  output valid_out_0;
  input [7:0]x0_0;
  input [7:0]x1_0;
  input [7:0]x2_0;
  input [7:0]x3_0;
  output [7:0]y0_0;
  output [7:0]y1_0;
  output [7:0]y2_0;
  output [7:0]y3_0;

  wire [14:0]DDR_addr;
  wire [2:0]DDR_ba;
  wire DDR_cas_n;
  wire DDR_ck_n;
  wire DDR_ck_p;
  wire DDR_cke;
  wire DDR_cs_n;
  wire [3:0]DDR_dm;
  wire [31:0]DDR_dq;
  wire [3:0]DDR_dqs_n;
  wire [3:0]DDR_dqs_p;
  wire DDR_odt;
  wire DDR_ras_n;
  wire DDR_reset_n;
  wire DDR_we_n;
  wire FIXED_IO_ddr_vrn;
  wire FIXED_IO_ddr_vrp;
  wire [53:0]FIXED_IO_mio;
  wire FIXED_IO_ps_clk;
  wire FIXED_IO_ps_porb;
  wire FIXED_IO_ps_srstb;
  wire [31:0]M_AXI_GP0_0_araddr;
  wire [1:0]M_AXI_GP0_0_arburst;
  wire [3:0]M_AXI_GP0_0_arcache;
  wire [11:0]M_AXI_GP0_0_arid;
  wire [3:0]M_AXI_GP0_0_arlen;
  wire [1:0]M_AXI_GP0_0_arlock;
  wire [2:0]M_AXI_GP0_0_arprot;
  wire [3:0]M_AXI_GP0_0_arqos;
  wire M_AXI_GP0_0_arready;
  wire [2:0]M_AXI_GP0_0_arsize;
  wire M_AXI_GP0_0_arvalid;
  wire [31:0]M_AXI_GP0_0_awaddr;
  wire [1:0]M_AXI_GP0_0_awburst;
  wire [3:0]M_AXI_GP0_0_awcache;
  wire [11:0]M_AXI_GP0_0_awid;
  wire [3:0]M_AXI_GP0_0_awlen;
  wire [1:0]M_AXI_GP0_0_awlock;
  wire [2:0]M_AXI_GP0_0_awprot;
  wire [3:0]M_AXI_GP0_0_awqos;
  wire M_AXI_GP0_0_awready;
  wire [2:0]M_AXI_GP0_0_awsize;
  wire M_AXI_GP0_0_awvalid;
  wire [11:0]M_AXI_GP0_0_bid;
  wire M_AXI_GP0_0_bready;
  wire [1:0]M_AXI_GP0_0_bresp;
  wire M_AXI_GP0_0_bvalid;
  wire [31:0]M_AXI_GP0_0_rdata;
  wire [11:0]M_AXI_GP0_0_rid;
  wire M_AXI_GP0_0_rlast;
  wire M_AXI_GP0_0_rready;
  wire [1:0]M_AXI_GP0_0_rresp;
  wire M_AXI_GP0_0_rvalid;
  wire [31:0]M_AXI_GP0_0_wdata;
  wire [11:0]M_AXI_GP0_0_wid;
  wire M_AXI_GP0_0_wlast;
  wire M_AXI_GP0_0_wready;
  wire [3:0]M_AXI_GP0_0_wstrb;
  wire M_AXI_GP0_0_wvalid;
  wire M_AXI_GP0_ACLK_0;
  wire valid_in_0;
  wire valid_out_0;
  wire [7:0]x0_0;
  wire [7:0]x1_0;
  wire [7:0]x2_0;
  wire [7:0]x3_0;
  wire [7:0]y0_0;
  wire [7:0]y1_0;
  wire [7:0]y2_0;
  wire [7:0]y3_0;

  design_1 design_1_i
       (.DDR_addr(DDR_addr),
        .DDR_ba(DDR_ba),
        .DDR_cas_n(DDR_cas_n),
        .DDR_ck_n(DDR_ck_n),
        .DDR_ck_p(DDR_ck_p),
        .DDR_cke(DDR_cke),
        .DDR_cs_n(DDR_cs_n),
        .DDR_dm(DDR_dm),
        .DDR_dq(DDR_dq),
        .DDR_dqs_n(DDR_dqs_n),
        .DDR_dqs_p(DDR_dqs_p),
        .DDR_odt(DDR_odt),
        .DDR_ras_n(DDR_ras_n),
        .DDR_reset_n(DDR_reset_n),
        .DDR_we_n(DDR_we_n),
        .FIXED_IO_ddr_vrn(FIXED_IO_ddr_vrn),
        .FIXED_IO_ddr_vrp(FIXED_IO_ddr_vrp),
        .FIXED_IO_mio(FIXED_IO_mio),
        .FIXED_IO_ps_clk(FIXED_IO_ps_clk),
        .FIXED_IO_ps_porb(FIXED_IO_ps_porb),
        .FIXED_IO_ps_srstb(FIXED_IO_ps_srstb),
        .M_AXI_GP0_0_araddr(M_AXI_GP0_0_araddr),
        .M_AXI_GP0_0_arburst(M_AXI_GP0_0_arburst),
        .M_AXI_GP0_0_arcache(M_AXI_GP0_0_arcache),
        .M_AXI_GP0_0_arid(M_AXI_GP0_0_arid),
        .M_AXI_GP0_0_arlen(M_AXI_GP0_0_arlen),
        .M_AXI_GP0_0_arlock(M_AXI_GP0_0_arlock),
        .M_AXI_GP0_0_arprot(M_AXI_GP0_0_arprot),
        .M_AXI_GP0_0_arqos(M_AXI_GP0_0_arqos),
        .M_AXI_GP0_0_arready(M_AXI_GP0_0_arready),
        .M_AXI_GP0_0_arsize(M_AXI_GP0_0_arsize),
        .M_AXI_GP0_0_arvalid(M_AXI_GP0_0_arvalid),
        .M_AXI_GP0_0_awaddr(M_AXI_GP0_0_awaddr),
        .M_AXI_GP0_0_awburst(M_AXI_GP0_0_awburst),
        .M_AXI_GP0_0_awcache(M_AXI_GP0_0_awcache),
        .M_AXI_GP0_0_awid(M_AXI_GP0_0_awid),
        .M_AXI_GP0_0_awlen(M_AXI_GP0_0_awlen),
        .M_AXI_GP0_0_awlock(M_AXI_GP0_0_awlock),
        .M_AXI_GP0_0_awprot(M_AXI_GP0_0_awprot),
        .M_AXI_GP0_0_awqos(M_AXI_GP0_0_awqos),
        .M_AXI_GP0_0_awready(M_AXI_GP0_0_awready),
        .M_AXI_GP0_0_awsize(M_AXI_GP0_0_awsize),
        .M_AXI_GP0_0_awvalid(M_AXI_GP0_0_awvalid),
        .M_AXI_GP0_0_bid(M_AXI_GP0_0_bid),
        .M_AXI_GP0_0_bready(M_AXI_GP0_0_bready),
        .M_AXI_GP0_0_bresp(M_AXI_GP0_0_bresp),
        .M_AXI_GP0_0_bvalid(M_AXI_GP0_0_bvalid),
        .M_AXI_GP0_0_rdata(M_AXI_GP0_0_rdata),
        .M_AXI_GP0_0_rid(M_AXI_GP0_0_rid),
        .M_AXI_GP0_0_rlast(M_AXI_GP0_0_rlast),
        .M_AXI_GP0_0_rready(M_AXI_GP0_0_rready),
        .M_AXI_GP0_0_rresp(M_AXI_GP0_0_rresp),
        .M_AXI_GP0_0_rvalid(M_AXI_GP0_0_rvalid),
        .M_AXI_GP0_0_wdata(M_AXI_GP0_0_wdata),
        .M_AXI_GP0_0_wid(M_AXI_GP0_0_wid),
        .M_AXI_GP0_0_wlast(M_AXI_GP0_0_wlast),
        .M_AXI_GP0_0_wready(M_AXI_GP0_0_wready),
        .M_AXI_GP0_0_wstrb(M_AXI_GP0_0_wstrb),
        .M_AXI_GP0_0_wvalid(M_AXI_GP0_0_wvalid),
        .M_AXI_GP0_ACLK_0(M_AXI_GP0_ACLK_0),
        .valid_in_0(valid_in_0),
        .valid_out_0(valid_out_0),
        .x0_0(x0_0),
        .x1_0(x1_0),
        .x2_0(x2_0),
        .x3_0(x3_0),
        .y0_0(y0_0),
        .y1_0(y1_0),
        .y2_0(y2_0),
        .y3_0(y3_0));
endmodule
