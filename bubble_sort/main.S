        .text

init:       move    $t0, $0             
            
           # li      $v0, 78             
            li      $t8, 0x10           # размер массива
            li      $t9, 0x40           # размер массива*4

            ###########################################            
            #для симуляции смотрим $v0 (массив до сортировки)                      
read:      
            lw      $v0, 0x0 ($t0)#0x10010000 ($t0)      
            addiu   $t0, $t0, 4         
            bne     $t0, $t9, read

            move    $v0, $0

bubble_sort:           
            move $t1, $0 #counter1( i )=0

loop1:
            move $t0, $0
            addiu $t1, $t1, 1 #i++
            #bgt $t1, $t8, endloop1 #if i < 16 break;##################
            sltu $t5, $t1, $t8
            beqz $t5, endloop1

            move $t2, $t8 #counter2(j) = size = 16

loop2: 
            #bge $t1, $t2, loop1 # i>= j###########################
            beq $t1, $t2, loop1
            sltu $t5, $t1, $t2
            beqz $t5,  loop1

            subiu $t2, $t2, 1 #j--
 
            #читаем 2 элемента из памяти для сравнения
            lw      $t3, 0x0 ($t0)#0x10010000 ($t0)
            addiu   $t0, $t0, 4
            lw      $t4, 0x0 ($t0)#0x10010000 ($t0)
            
            
            #bgt $t4, $t3, loop2####################
            sltu $t5, $t4, $t3
            beqz $t5,  loop2

            
            sw $t3, 0x0 ($t0)#0x10010000 ($t0)
            subiu   $t0, $t0, 4
            sw $t4, 0x0 ($t0)#0x10010000 ($t0)
            addiu   $t0, $t0, 4

            beqz    $0,  loop2 #j loop2

endloop1:
            #для симуляции смотрим $v0 (массив после сортировки)
            move    $t0, $0             
read1:      
            lw      $v0, 0x0 ($t0)#0x10010000 ($t0)     
            addiu   $t0, $t0, 4         
            bne     $t0, $t9, read1      
           
            
end:        beqz    $0,  end 
            
            
            
            
            
            
