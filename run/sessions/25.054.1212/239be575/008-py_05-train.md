
## example 1
*input:*
```
0 0 8 0 8
2 2 8 0 0
2 2 0 0 8
0 0 0 2 2
8 8 0 2 2
```
*expected output:*
```
0
```
*transformed output:*
```
2
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**

## example 2
*input:*
```
0 8 0 0 0 0 0
2 2 0 8 8 8 0
2 2 8 8 0 2 2
0 0 8 0 0 2 2
0 8 0 0 8 0 0
```
*expected output:*
```
8
```
*transformed output:*
```
8
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
8 2 2 8 8 0 0
0 2 2 0 0 0 8
0 8 8 0 0 8 0
0 0 8 0 0 0 8
8 0 8 8 8 2 2
8 0 0 0 0 2 2
```
*expected output:*
```
8
```
*transformed output:*
```
8
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 4
*input:*
```
8 8 0 0 2 2 0
0 8 8 0 2 2 8
0 0 0 8 0 8 0
8 0 0 0 0 0 0
0 2 2 0 8 0 8
0 2 2 8 8 0 8
```
*expected output:*
```
0
```
*transformed output:*
```
2
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**

## example 5
*input:*
```
8 0 0 0 0 8 0
0 0 2 2 0 8 0
8 0 2 2 0 0 0
0 0 8 0 0 8 0
0 0 8 2 2 0 8
8 0 0 2 2 8 0
```
*expected output:*
```
8
```
*transformed output:*
```
2
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**

## example 6
*input:*
```
8 0 0 2 2 8
8 0 8 2 2 0
0 0 0 0 8 0
2 2 8 0 8 0
2 2 0 0 0 8
0 8 8 0 8 0
```
*expected output:*
```
0
```
*transformed output:*
```
2
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**
