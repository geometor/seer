
## example 1
*input:*
```
0 8 0 0 0 8 0
8 8 0 0 0 8 8
0 0 0 0 0 0 0
8 8 0 0 0 8 8
0 8 0 0 0 8 0
```
*expected output:*
```
0 8 0
8 8 8
0 8 0
```
*transformed output:*
```
8 8 8
8 8 8
8 8 0
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 2
*input:*
```
2 2 0 0 0 2 2
0 0 0 0 0 0 2
0 0 0 0 0 0 0
0 2 0 0 0 2 0
2 0 0 0 0 0 2
```
*expected output:*
```
2 2 2
0 2 2
2 0 2
```
*transformed output:*
```
2 2 2
2 2 0
2 0 2
```
size: True
palette: True
color count: True
pixels off: 2
**FAILED!**

## example 3
*input:*
```
4 4 0 0 0 4 0
0 0 0 0 0 4 4
0 0 0 0 0 0 0
0 0 0 0 0 0 0
4 0 0 0 0 0 4
```
*expected output:*
```
4 4 0
0 4 4
4 0 4
```
*transformed output:*
```
4 4 4
0 0 0
4 0 4
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 4
*input:*
```
4 0 0 0 0 0 4
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
4 0 0 0 0 4 4
```
*expected output:*
```
4 0 4
0 0 0
4 4 4
```
*transformed output:*
```
4 0 4
0 0 0
4 4 4
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 5
*input:*
```
0 3 0 0 0 3 0
3 0 0 0 0 0 3
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 3
```
*expected output:*
```
0 3 0
3 0 3
0 0 3
```
*transformed output:*
```
3 3 3
0 0 0
0 0 3
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**
