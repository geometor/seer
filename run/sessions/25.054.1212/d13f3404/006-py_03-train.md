
## example 1
*input:*
```
6 1 0
3 0 0
0 0 0
```
*expected output:*
```
6 1 0 0 0 0
3 6 1 0 0 0
0 3 6 1 0 0
0 0 3 6 1 0
0 0 0 3 6 1
0 0 0 0 3 6
```
*transformed output:*
```
6 6 1 1 0 0
6 6 1 1 0 0
3 3 0 0 0 0
3 3 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 18
**FAILED!**

## example 2
*input:*
```
0 4 0
0 8 0
2 0 0
```
*expected output:*
```
0 4 0 0 0 0
0 8 4 0 0 0
2 0 8 4 0 0
0 2 0 8 4 0
0 0 2 0 8 4
0 0 0 2 0 8
```
*transformed output:*
```
0 0 4 4 0 0
0 0 4 4 0 0
0 0 8 8 0 0
0 0 8 8 0 0
2 2 0 0 0 0
2 2 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 19
**FAILED!**

## example 3
*input:*
```
0 0 6
1 3 0
0 0 0
```
*expected output:*
```
0 0 6 0 0 0
1 3 0 6 0 0
0 1 3 0 6 0
0 0 1 3 0 6
0 0 0 1 3 0
0 0 0 0 1 3
```
*transformed output:*
```
0 0 0 0 6 6
0 0 0 0 6 6
1 1 3 3 0 0
1 1 3 3 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 19
**FAILED!**
