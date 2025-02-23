
## example 1
*input:*
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```
*expected output:*
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```
*transformed output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
4 9 4 6
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0 9
0 0 0 8 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 0 0 0
```
*expected output:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```
*transformed output:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
9 8 4 4 7 8
```
size: True
palette: True
color count: False
pixels off: 10
**FAILED!**

## example 3
*input:*
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```
*transformed output:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 3 3 1 2
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
