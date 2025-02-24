
## example 1
*input:*
```
0 0 0 0 0 0 0
0 2 2 2 0 0 0
0 0 2 0 0 0 0
0 2 2 2 2 0 0
0 0 2 2 2 0 0
0 0 0 2 0 0 0
4 0 0 0 0 0 0
```
*expected output:*
```
0 0 0 0 0 0 0
0 4 4 4 0 0 0
0 0 4 0 0 0 0
0 4 4 4 4 0 0
0 0 4 4 4 0 0
0 0 0 4 0 0 0
0 0 0 0 0 0 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

## example 2
*input:*
```
0 0 0 0 0 0 0
0 0 0 3 0 0 0
0 0 3 3 3 0 0
0 3 3 3 3 0 0
0 3 3 0 0 0 0
0 0 3 3 0 0 0
6 0 0 0 0 0 0
```
*expected output:*
```
0 0 0 0 0 0 0
0 0 0 6 0 0 0
0 0 6 6 6 0 0
0 6 6 6 6 0 0
0 6 6 0 0 0 0
0 0 6 6 0 0 0
0 0 0 0 0 0 0
```
*transformed output:*
```
0 0 0 0 0 0 0
0 0 0 3 0 0 0
0 0 3 3 3 0 0
0 3 3 3 3 0 0
0 3 3 0 0 0 0
0 0 3 3 0 0 0
6 0 0 0 0 0 0
```
size: True
palette: False
color count: False
pixels off: 13
**FAILED!**
