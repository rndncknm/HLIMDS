/*
 * Copyright 1991-2015 Mentor Graphics Corporation
 *
 * All Rights Reserved.
 *
 * THIS WORK CONTAINS TRADE SECRET AND PROPRIETARY INFORMATION WHICH IS THE
 * PROPERTY OF MENTOR GRAPHICS CORPORATION OR ITS LICENSORS AND IS SUBJECT TO
 * LICENSE TERMS.
 *
 * Simple SystemVerilog DPI Example - C function to compute fibonacci seq.
 */
#include "fibonacci.h"

unsigned int fibonacci_rec(unsigned int N) {
   if(N == 0){
      return 0;
   } else if(N == 1) {
      return 1;
   } else {
      return (fibonacci_rec(N-1) + fibonacci_rec(N-2));
   }
}