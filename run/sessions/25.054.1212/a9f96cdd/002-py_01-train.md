
## example 1
*input:*
```
0 0 0 0 0
0 2 0 0 0
0 0 0 0 0
```
*expected output:*
```
3 0 6 0 0
0 0 0 0 0
8 0 7 0 0
```
*transformed output:*
```
0 4 6 7 0
0 5 1 0 8
0 0 9 0 3
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 2
```
*expected output:*
```
0 0 0 0 0
0 0 0 3 0
0 0 0 0 0
```
*transformed output:*
```
3 0 0 9 0
5 0 1 0 7
0 4 6 8 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 3
*input:*
```
0 0 2 0 0
0 0 0 0 0
0 0 0 0 0
```
*expected output:*
```
0 0 0 0 0
0 8 0 7 0
0 0 0 0 0
```
*transformed output:*
```
5 0 4 0 0
0 7 9 6 0
0 8 1 0 3
```
size: True
palette: False
color count: False
pixels off: 8
**FAILED!**

## example 4
*input:*
```
0 0 0 0 0
0 0 0 2 0
0 0 0 0 0
```
*expected output:*
```
0 0 3 0 6
0 0 0 0 0
0 0 8 0 7
```
*transformed output:*
```
0 5 4 0 0
1 6 0 7 9
0 0 8 0 3
```
size: True
palette: False
color count: False
pixels off: 8
**FAILED!**
