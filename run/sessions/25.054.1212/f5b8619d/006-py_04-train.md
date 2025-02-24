
## example 1
*input:*
```
2 0 0
0 0 0
0 0 2
```
*expected output:*
```
2 0 8 2 0 8
8 0 8 8 0 8
8 0 2 8 0 2
2 0 8 2 0 8
8 0 8 8 0 8
8 0 2 8 0 2
```
*transformed output:*
```
2 0 0 8 8 8
0 0 0 8 8 8
0 0 2 8 8 8
8 8 8 8 8 8
8 8 8 8 8 8
8 8 8 8 8 8
```
size: True
palette: True
color count: False
pixels off: 19
**FAILED!**

## example 2
*input:*
```
0 5 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
5 0 0 0 0 5
0 0 0 0 0 0
```
*expected output:*
```
8 5 0 0 0 8 8 5 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
5 8 0 0 0 5 5 8 0 0 0 5
8 8 0 0 0 8 8 8 0 0 0 8
8 5 0 0 0 8 8 5 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
8 8 0 0 0 8 8 8 0 0 0 8
5 8 0 0 0 5 5 8 0 0 0 5
8 8 0 0 0 8 8 8 0 0 0 8
```
*transformed output:*
```
0 5 0 0 0 0 8 8 8 8 8 8
0 0 0 0 0 0 8 8 8 8 8 8
0 0 0 0 0 0 8 8 8 8 8 8
0 0 0 0 0 0 8 8 8 8 8 8
5 0 0 0 0 5 8 8 8 8 8 8
0 0 0 0 0 0 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8
```
size: True
palette: True
color count: False
pixels off: 78
**FAILED!**

## example 3
*input:*
```
0 4
0 0
```
*expected output:*
```
0 4 0 4
0 8 0 8
0 4 0 4
0 8 0 8
```
*transformed output:*
```
0 4 8 8
0 0 8 8
8 8 8 8
8 8 8 8
```
size: True
palette: True
color count: False
pixels off: 10
**FAILED!**
