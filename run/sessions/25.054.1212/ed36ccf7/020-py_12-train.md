
## example 1
*input:*
```
9 0 0
9 9 9
9 9 9
```
*expected output:*
```
0 9 9
0 9 9
9 9 9
```
*transformed output:*
```
2 2 2
2 2 0
2 2 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
0 6 6
6 0 0
6 6 0
```
*expected output:*
```
6 0 0
6 0 6
6 0 6
```
*transformed output:*
```
2 2 0
2 0 2
0 0 2
```
size: True
palette: False
color count: False
pixels off: 6
**FAILED!**

## example 3
*input:*
```
0 0 9
0 0 9
9 9 9
```
*expected output:*
```
9 9 9
0 0 9
0 0 9
```
*transformed output:*
```
2 0 0
2 0 0
2 2 2
```
size: True
palette: False
color count: False
pixels off: 8
**FAILED!**

## example 4
*input:*
```
2 0 2
0 0 2
0 2 2
```
*expected output:*
```
2 2 2
0 0 2
2 0 0
```
*transformed output:*
```
0 0 0
0 0 0
0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
