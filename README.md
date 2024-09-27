# valuesorter
A program to sort personal values.

How to use:
1. Place your personal values, one per line, in values.txt (or use the provided examples)
2. Run **valuesorter.py** in the same directory as values.txt
3. Answer the questions to rank the values
4. When done, read the newly generated file, sorted_values.txt to see how you ranked the values

ORRRRR....if you have a lot of values (say, 50)...
The valuesorter.py script does a pairwise comparison. That's `O(n²)` comparisons for `n` values. So for `n=50` values, that'll take 1125 comparisons, and giving yourself 2 seconds each to decide between values, that's 37 minutes **minimum** to finish the ranking.

So if that's the case, you should probably try out **valuemergesorter.py** instead. That takes a merge-sort-like approach, where you only compare pairs when necessary. This approach uses a divide-and-conquer method, similar to merge sort, which cuts the number of comparisons down to `O(n log n)`. If you have 50 values, this method will reduce the number of comparisons to around 285, compared to 1,225 in a brute-force comparison. With our 2 second comparison time, that's only 9.5 minutes! 
