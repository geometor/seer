
## example 1
*input:*
```
0 0 0 0 0 0 0 0
0 8 8 0 0 0 0 0
0 0 8 0 0 0 0 0
0 8 8 8 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```
*expected output:*
```
8 8 0 8 8 0
0 8 0 0 8 0
8 8 8 8 8 8
```
*transformed output:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 12
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 2 0 0 0 0
0 0 2 2 2 0 0 0
0 0 2 2 0 0 0 0
```
*expected output:*
```
0 2 0 0 2 0
2 2 2 2 2 2
2 2 0 2 2 0
```
*transformed output:*
```
0 2 0 0 2 0
2 2 2 2 2 2
2 2 0 2 2 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
0 0 0 0 0 0 0 0
0 0 0 0 0 1 1 0
0 0 0 0 1 0 0 0
0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```
*expected output:*
```
0 1 1 0 1 1
1 0 0 1 0 0
0 1 0 0 1 0
```
*transformed output:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 8
**FAILED!**
