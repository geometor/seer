
## example 1
*input:*
```
0 0 0
0 2 0
2 4 2
```
*expected output:*
```
4 0 4
0 2 0
2 4 2
```
*transformed output:*
```
4 0 4
0 2 0
2 4 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 8 0 0
8 8 3 8 8
```
*expected output:*
```
0 0 0 0 0
3 0 0 0 3
0 3 0 3 0
0 0 8 0 0
8 8 3 8 8
```
*transformed output:*
```
4 0 0 0 4
3 0 0 0 3
1 0 0 0 1
0 0 8 0 0
8 8 3 8 8
```
size: True
palette: False
color count: False
pixels off: 6
**FAILED!**

## example 3
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 6 6 6 0
6 1 1 1 6
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
1 0 0 0 1
0 6 6 6 0
6 1 1 1 6
```
*transformed output:*
```
4 0 0 0 4
3 0 0 0 3
1 0 0 0 1
0 6 6 6 0
6 1 1 1 6
```
size: True
palette: False
color count: False
pixels off: 4
**FAILED!**

## example 4
*input:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
*expected output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
4 0 0 0 0 0 4
0 4 0 0 0 4 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
*transformed output:*
```
4 0 0 0 0 0 4
3 0 0 0 0 0 3
1 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
size: True
palette: False
color count: False
pixels off: 10
**FAILED!**
