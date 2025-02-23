
## example 1
*input:*
```
0 9 9 1 9 9 9
0 0 9 1 9 9 0
9 0 9 1 9 9 0
0 0 0 1 9 0 0
0 9 9 1 9 9 9
```
*expected output:*
```
0 0 0
0 0 0
0 0 0
0 8 8
0 0 0
```
*transformed output:*
```
0 0 0
0 0 8
0 0 8
0 8 8
0 0 0
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**

## example 2
*input:*
```
0 0 0 1 9 0 0
9 0 9 1 9 9 9
0 9 9 1 9 9 9
0 0 0 1 9 9 9
0 9 9 1 9 9 9
```
*expected output:*
```
0 8 8
0 0 0
0 0 0
0 0 0
0 0 0
```
*transformed output:*
```
0 8 8
0 0 0
0 0 0
0 0 0
0 0 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
9 0 0 1 9 0 9
9 0 0 1 0 9 0
9 0 0 1 9 0 0
0 9 9 1 0 9 9
0 0 9 1 0 9 0
```
*expected output:*
```
0 8 0
0 0 8
0 8 8
8 0 0
8 0 0
```
*transformed output:*
```
0 8 0
8 0 8
0 8 8
8 0 0
8 0 8
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**

## example 4
*input:*
```
0 9 9 1 9 0 9
9 0 0 1 9 0 0
9 9 9 1 9 9 9
0 9 0 1 0 0 0
9 0 0 1 9 0 0
```
*expected output:*
```
0 0 0
0 8 8
0 0 0
8 0 8
0 8 8
```
*transformed output:*
```
0 8 0
0 8 8
0 0 0
8 8 8
0 8 8
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**

## example 5
*input:*
```
0 9 9 1 9 0 9
9 0 9 1 9 9 9
9 9 9 1 0 0 9
9 0 0 1 9 0 0
9 9 9 1 0 0 9
```
*expected output:*
```
0 0 0
0 0 0
0 0 0
0 8 8
0 0 0
```
*transformed output:*
```
0 8 0
0 0 0
8 8 0
0 8 8
8 8 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
