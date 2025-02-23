
## example 1
*input:*
```
0 8
0 0
0 8
```
*expected output:*
```
8 0 0 8
0 0 0 0
8 0 0 8
8 0 0 8
0 0 0 0
8 0 0 8
8 0 0 8
0 0 0 0
8 0 0 8
```
*transformed output:*
```
0 0 8 8
0 0 8 8
0 0 8 8
0 0 0 0
0 0 0 0
0 0 0 0
0 0 8 8
0 0 8 8
0 0 8 8
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**

## example 2
*input:*
```
2 0
2 2
2 0
```
*expected output:*
```
0 2 2 0
2 2 2 2
0 2 2 0
0 2 2 0
2 2 2 2
0 2 2 0
0 2 2 0
2 2 2 2
0 2 2 0
```
*transformed output:*
```
2 2 0 0
2 2 0 0
2 2 0 0
2 2 2 2
2 2 2 2
2 2 2 2
2 2 0 0
2 2 0 0
2 2 0 0
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**

## example 3
*input:*
```
0 0
0 5
5 0
```
*expected output:*
```
0 5 5 0
5 0 0 5
0 0 0 0
0 0 0 0
5 0 0 5
0 5 5 0
0 5 5 0
5 0 0 5
0 0 0 0
```
*transformed output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 5 5
0 0 5 5
0 0 5 5
5 5 0 0
5 5 0 0
5 5 0 0
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**
