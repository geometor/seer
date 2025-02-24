
## example 1
*input:*
```
6 4 0
0 3 9
1 0 0
```
*expected output:*
```
0 4 0
0 3 0
0 0 0
```
*transformed output:*
```
0 4 0
0 3 0
0 0 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
8 0 3 0 0
8 6 5 6 0
3 6 3 0 0
0 0 0 5 9
5 0 9 0 0
```
*expected output:*
```
0 0 3 0 0
0 0 5 0 0
0 0 3 0 0
0 0 0 0 0
0 0 9 0 0
```
*transformed output:*
```
0 0 3 0 0
0 0 0 0 0
3 0 3 0 0
0 0 0 0 0
0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 3
*input:*
```
3 0 4 0 0
3 0 4 7 0
0 6 0 0 7
0 0 8 0 0
0 8 0 2 2
```
*expected output:*
```
0 0 4 0 0
0 0 4 0 0
0 0 0 0 0
0 0 8 0 0
0 0 0 0 0
```
*transformed output:*
```
3 0 4 0 0
3 0 4 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
```
size: True
palette: False
color count: False
pixels off: 3
**FAILED!**
