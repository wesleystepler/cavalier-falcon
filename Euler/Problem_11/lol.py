# Problem in 2a used 4 instructions

# gull
total_instr = 4444321834
disp_instr = (427841147 + 326186380 + 101654767 + 2414641 + 328601021)
updated_instr_count = (total_instr - disp_instr) + (disp_instr*4)

print("Gull:")
print(updated_instr_count/total_instr)
print()

# queens
total_instr = 713017270
disp_instr = (132112301 + 118158999 + 13953302 + 59815403 + 177974402)
updated_instr_count = (total_instr - disp_instr) + (disp_instr*4)
print("Queens:")
print(updated_instr_count/total_instr)
print()

# gcc-queens
total_instr = 242758909
disp_instr = (10566416 + 5457678 + 5108738 + 1746053 + 7203731)
updated_instr_count = (total_instr - disp_instr) + (disp_instr*4)
print("Gcc-Queens:")
print(updated_instr_count/total_instr)
print()



# blocked-matmul
total_instr = 399411
instr_32 = 144297 - 128025
instr_48 = 147388 - 144297
instr_64 = total_instr - 147388
updated_instr_count = (total_instr - instr_32 - instr_48 - instr_64) + (instr_32*2 + instr_48*4 + instr_64 * 5)
print("Blocked-Matmul")
print(updated_instr_count/total_instr)
print()

# gull
total_instr = 637591
instr_32 = 217186 - 177898
instr_48 = 221586 - 217186
instr_64 = total_instr - 221586
updated_instr_count = (total_instr - instr_32 - instr_48 - instr_64) + (instr_32*2 + instr_48*4 + instr_64 * 5)
print("Gull")
print(updated_instr_count/total_instr)
print()

#gcc-queens
total_instr = 4968570
instr_32 = 1791300 - 1536716
instr_48 = 1812536 - 1791300
instr_64 = total_instr - 1812536
updated_instr_count = (total_instr - instr_32 - instr_48 - instr_64) + (instr_32*2 + instr_48*4 + instr_64 * 5)
print("Gcc-Queens")
print(updated_instr_count/total_instr)
print()


    
