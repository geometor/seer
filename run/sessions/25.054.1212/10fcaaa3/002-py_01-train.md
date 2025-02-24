
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
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 4 is out of bounds for axis 0 with size 4

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
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 28
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
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 32
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
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
8 0 8 0 8 0 8 0
```
size: True
palette: True
color count: False
pixels off: 20
**FAILED!**
