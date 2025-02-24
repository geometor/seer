
## example 1
*input:*
```
3 8 7
9 3 8
7 9 3
```
*expected output:*
```
3 8 7 0 0 0 0 0 0
9 3 8 0 0 0 0 0 0
7 9 3 0 0 0 0 0 0
0 0 0 3 8 7 0 0 0
0 0 0 9 3 8 0 0 0
0 0 0 7 9 3 0 0 0
0 0 0 0 0 0 3 8 7
0 0 0 0 0 0 9 3 8
0 0 0 0 0 0 7 9 3
```
*transformed output:*
```
0 0 0 0 0 0 0 0 0
0 3 8 9 3 8 9 3 0
0 9 3 7 9 3 7 9 0
0 8 7 3 8 7 3 8 0
0 3 8 9 3 8 9 3 0
0 9 3 7 9 3 7 9 0
0 8 7 3 8 7 3 8 0
0 3 8 9 3 8 9 3 0
0 0 0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 42
**FAILED!**

## example 2
*input:*
```
8 6 8
3 3 8
8 8 8
```
*expected output:*
```
8 6 8 0 0 0 8 6 8
3 3 8 0 0 0 3 3 8
8 8 8 0 0 0 8 8 8
0 0 0 0 0 0 8 6 8
0 0 0 0 0 0 3 3 8
0 0 0 0 0 0 8 8 8
8 6 8 8 6 8 8 6 8
3 3 8 3 3 8 3 3 8
8 8 8 8 8 8 8 8 8
```
*transformed output:*
```
0 0 0 0 0 0 0 0 0
0 3 8 3 3 8 3 3 0
0 8 8 8 8 8 8 8 0
0 6 8 8 6 8 8 6 0
0 3 8 3 3 8 3 3 0
0 8 8 8 8 8 8 8 0
0 6 8 8 6 8 8 6 0
0 3 8 3 3 8 3 3 0
0 0 0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 47
**FAILED!**

## example 3
*input:*
```
6 9 9
4 6 8
9 9 8
```
*expected output:*
```
0 0 0 6 9 9 6 9 9
0 0 0 4 6 8 4 6 8
0 0 0 9 9 8 9 9 8
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
6 9 9 6 9 9 0 0 0
4 6 8 4 6 8 0 0 0
9 9 8 9 9 8 0 0 0
```
*transformed output:*
```
0 0 0 0 0 0 0 0 0
0 6 0 0 6 0 0 6 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 6 0 0 6 0 0 6 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 6 0 0 6 0 0 6 0
0 0 0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 37
**FAILED!**
