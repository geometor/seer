
## example 1
*input:*
```
0 0 0 0 0 0 0 0 0 0 0 0 0
0 2 2 0 0 3 3 0 0 0 0 0 0
0 0 2 0 0 0 3 0 0 1 0 0 0
0 0 2 2 0 0 0 0 1 1 0 0 0
0 2 2 2 0 0 0 0 1 1 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
2 2 0
0 2 0
0 2 2
2 2 2
```
*transformed output:*
```
2 2 0
0 2 0
0 2 2
2 2 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
0 0 0 0 0 0 0 6 6 0
0 3 0 0 4 4 0 0 6 0
3 3 3 0 4 4 0 0 0 0
0 3 0 0 4 4 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
4 4
4 4
4 4
```
*transformed output:*
```
4 4
4 4
4 4
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
0 0 0 0 0 0 0 0 0 0 0
0 8 8 8 0 0 0 0 7 7 0
0 0 8 0 0 0 2 0 0 7 0
0 8 8 0 0 2 2 0 0 7 0
0 8 8 0 0 0 2 0 0 7 0
0 0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
8 8 8
0 8 0
8 8 0
8 8 0
```
*transformed output:*
```
0 2
2 2
0 2
```
size: False
palette: False
color count: False
pixels off: None
**FAILED!**

## example 4
*input:*
```
0 0 0 0 0 0 0 0 0
0 0 0 7 0 0 2 2 2
0 0 0 7 7 0 0 2 0
0 0 0 0 7 0 2 2 2
8 8 8 0 0 0 0 0 0
0 8 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
```
*expected output:*
```
2 2 2
0 2 0
2 2 2
```
*transformed output:*
```
2 2 2
0 2 0
2 2 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED
