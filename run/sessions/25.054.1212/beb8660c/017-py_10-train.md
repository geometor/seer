
## example 1
*input:*
```
0 2 2 0 0 0 0
0 0 0 0 3 0 0
1 1 1 0 0 0 0
0 0 0 0 0 0 0
0 5 5 5 5 5 5
0 0 0 0 0 0 0
6 6 6 6 6 0 0
0 0 0 4 4 4 4
0 0 0 0 0 0 0
8 8 8 8 8 8 8
```
*expected output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 3
0 0 0 0 0 2 2
0 0 0 0 1 1 1
0 0 0 4 4 4 4
0 0 6 6 6 6 6
0 5 5 5 5 5 5
8 8 8 8 8 8 8
```
*transformed output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
8 8 8 8 8 8 8
6 6 6 6 6 0 0
0 5 5 5 5 5 5
1 1 1 4 4 4 4
0 2 2 0 3 0 0
```
size: True
palette: True
color count: True
pixels off: 37
**FAILED!**

## example 2
*input:*
```
0 0 0 1
0 0 0 0
2 2 2 0
0 0 0 0
0 3 3 0
0 0 0 0
8 8 8 8
```
*expected output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
0 0 3 3
0 2 2 2
8 8 8 8
```
*transformed output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
8 8 8 8
0 3 3 0
2 2 2 1
```
size: True
palette: True
color count: True
pixels off: 12
**FAILED!**

## example 3
*input:*
```
2 2 0
0 4 0
8 8 8
```
*expected output:*
```
0 0 4
0 2 2
8 8 8
```
*transformed output:*
```
8 8 8
0 4 0
2 2 0
```
size: True
palette: True
color count: True
pixels off: 8
**FAILED!**
