# Goals
This proyect researches how a modification to the mergesort algorithm affects its preformance.

# Result
It does improve runtime on mot test i ran, especially on longer runs. I havent plotted the data yet, to know if its a linear or nlogn imporvement (or something else).
## Further interpretation
Maybe in languages/implementations that use real arrays (hardware adyacent, here i used python lists, numpy is only used to generate the data, that i then convert to python), the speed of the cached values makes the normal merge function faster (since the data beeing acsessed is from contiguous arrays and in order). This eimay be enough speedup to make the if statement to check for the modification not worth it. But I havent checkd this myself, it is just speculation. 

# Credit
Credit for the idea to  Sofia (https://github.com/BuckbeakS007).

# Modification
In the merge step, before we check if all items of one list are smaller than the other, to just concatenate the lists O(1) instead of merging like usual, that would be O(n).

