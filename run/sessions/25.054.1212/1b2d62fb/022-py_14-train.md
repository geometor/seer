
## example 1
*input:*
```
0 9 9 8 9 9 9
0 0 9 8 9 9 0
9 0 9 8 9 9 0
0 0 0 8 9 0 0
0 9 9 8 9 9 9
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
0 8 0
0 8 0
0 8 0
0 8 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 0 0 8 9 0 0
9 0 9 8 9 9 9
0 9 9 8 9 9 9
0 0 0 8 9 9 9
0 9 9 8 9 9 9
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
0 8 0
0 8 0
0 8 0
0 8 0
0 8 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 3
*input:*
```
9 0 0 8 9 0 9
9 0 0 8 0 9 0
9 0 0 8 9 0 0
0 9 9 8 0 9 9
0 0 9 8 0 9 0
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
0 8 0
0 8 0
0 8 0
0 8 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**

## example 4
*input:*
```
0 9 9 8 9 0 9
9 0 0 8 9 0 0
9 9 9 8 9 9 9
0 9 0 8 0 0 0
9 0 0 8 9 0 0
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
0 8 0
0 8 0
0 8 0
0 8 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**

## example 5
*input:*
```
0 9 9 8 9 0 9
9 0 9 8 9 9 9
9 9 9 8 0 0 9
9 0 0 8 9 0 0
9 9 9 8 0 0 9
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
0 8 0
0 8 0
0 8 0
0 8 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
