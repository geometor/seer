
## example 1
*input:*
```
0 0 0 0
0 5 0 0
```
*expected output:*
```
8 0 8 0 8 0 8 0
0 5 0 0 0 5 0 0
8 0 8 0 8 0 8 0
0 5 0 0 0 5 0 0
```
*transformed output:*
```
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 5 0 8 5 8 0
8 0 8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 14
**FAILED!**

## example 2
*input:*
```
0 0 6 0
0 0 0 0
0 6 0 0
```
*expected output:*
```
0 0 6 0 0 0 6 0
8 8 8 8 8 8 8 8
0 6 0 8 0 6 0 8
8 0 6 0 8 0 6 0
8 8 8 8 8 8 8 8
0 6 0 0 0 6 0 0
```
*transformed output:*
```
8 0 8 0 6 0 8 0
8 0 8 0 8 0 8 0
8 0 6 0 8 6 8 0
8 0 8 0 8 0 8 0
8 0 8 6 8 0 8 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
0 0 0
0 4 0
0 0 0
0 0 0
4 0 0
```
*expected output:*
```
8 0 8 8 0 8
0 4 0 0 4 0
8 0 8 8 0 8
0 8 8 0 8 0
4 0 0 4 0 0
8 8 8 8 8 8
0 4 0 0 4 0
8 0 8 8 0 8
0 8 8 0 8 0
4 0 0 4 0 0
```
*transformed output:*
```
8 0 8 0 8 0
8 0 8 0 8 0
8 0 4 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 4 8 0
4 0 8 0 8 4
8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 34
**FAILED!**

## example 4
*input:*
```
0 0 0 0
0 2 0 0
0 0 0 0
0 0 0 0
```
*expected output:*
```
8 0 8 0 8 0 8 0
0 2 0 0 0 2 0 0
8 0 8 0 8 0 8 0
0 0 0 0 0 0 0 0
8 0 8 0 8 0 8 0
0 2 0 0 0 2 0 0
8 0 8 0 8 0 8 0
0 0 0 0 0 0 0 0
```
*transformed output:*
```
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 2 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 2 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 20
**FAILED!**
