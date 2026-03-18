import mergesort_normal 
import mergesort_modified 
import platform
import cpuinfo

iterations = [
    # [repetitions, list length]  
    [50000, 100],
    [10000, 1000],
    [1000,  10000],
    [100,   100000],
    [60,    1000000],
    [10,    10000000],
    [5,     100000000]
]


mergesort_normal.print_system_info()
print()

print("#############################################################")
print("# Normal version:")
print()
for pair in iterations:
    mergesort_normal.main(pair[0], pair[1], False)
print("#############################################################")
print()
print("#############################################################")
print("# Modified version:")
print()
for pair in iterations:
    mergesort_modified.main(pair[0], pair[1], False)
print("#############################################################")