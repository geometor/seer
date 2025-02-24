
## example 1
*input:*
```
2 1 0 0 0 0 1 3
1 1 1 1 1 1 1 1
0 1 0 8 0 0 1 0
0 1 8 8 0 8 1 0
0 1 0 0 8 0 1 0
0 1 8 0 8 8 1 0
1 1 1 1 1 1 1 1
4 1 0 0 0 0 1 6
```
*expected output:*
```
0 2 0 0
2 2 0 3
0 0 6 0
4 0 6 6
```
*transformed output:*
```
2 3
4 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 2
*input:*
```
9 1 0 0 1 4
1 1 1 1 1 1
0 1 8 8 1 0
0 1 8 0 1 0
1 1 1 1 1 1
2 1 0 0 1 3
```
*expected output:*
```
9 4
2 0
```
*transformed output:*
```
9 4
2 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
6 1 0 0 0 0 1 2
1 1 1 1 1 1 1 1
0 1 0 8 0 8 1 0
0 1 8 8 8 0 1 0
0 1 8 0 8 8 1 0
0 1 8 8 8 0 1 0
1 1 1 1 1 1 1 1
7 1 0 0 0 0 1 4
```
*expected output:*
```
0 6 0 2
6 6 2 0
7 0 4 4
7 7 4 0
```
*transformed output:*
```
6 2
7 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
