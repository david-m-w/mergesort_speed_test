import numpy as np
import time as t
import platform
import cpuinfo

def print_system_info():
    print(f"system: {platform.system()}")
    # save info here, cuz getting is slow af (like 2 seconds) for some reason, and i want two items from it, so this way i avoid waiting an eternity twice
    cpu_info = cpuinfo.get_cpu_info()
    print(f"processor: {cpu_info["brand_raw"]}")
    print(f"python version: {cpu_info["python_version"]}")


def mergesort(input_):
    if len(input_) == 1:
        return input_

    def merge(list_a, list_b):
        output_ = []
        index_a = 0
        index_b = 0
        while len(list_a)>index_a and len(list_b)>index_b:
            if list_a[index_a] < list_b[index_b]:
                output_.append(list_a[index_a])
                index_a += 1
            else:
                output_.append(list_b[index_b])
                index_b += 1
        #output_ += list_a[index_a:]
        #output_ += list_b[index_b:]
        #return output_

        return output_ + list_a[index_a:] + list_b[index_b:]

    middle = len(input_)//2
    return merge(mergesort(input_[:middle]), mergesort(input_[middle:]))


def main(repetitions, list_length, include_system_info):
    #repetitions = 10
    #list_length = 1000000
    lists = []
    t_start = t.time()
    for _ in range(repetitions):
        lists.append(list(map(float,list(np.random.random(list_length)))))
    t_end = t.time()
    print(f"list generation time (s): {t_end-t_start}")

    t_start = t.time()
    for i in range(repetitions):
        mergesort(lists[i])
    t_end = t.time()

    print(f"liste length: {list_length}")
    print(f"repetitions: {repetitions}")
    print(f"average time (s): {(t_end-t_start)/repetitions}")
    print(f"totatl time (s): {(t_end-t_start)}")
    
    if include_system_info:
        print_system_info()
    print()

if __name__ == "__main__":
    main(10, 1000, True)
    print(mergesort([1,3,6,8,2,4,5,4,7,9,0]))