
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
0 8 0 8 0 8 0 8
8 0 8 0 8 0 8 0
0 8 0 5 0 8 0 5
```
size: True
palette: True
color count: False
pixels off: 8
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
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 9 is out of bounds for axis 1 with size 8

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
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 7 is out of bounds for axis 1 with size 6

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
0 8 0 8 0 8 0 8
8 0 8 0 8 0 8 0
0 8 0 2 0 8 0 2
8 0 8 0 8 0 8 0
0 8 0 8 0 8 0 8
8 0 8 0 8 0 8 0
0 8 0 8 0 8 0 8
```
size: True
palette: True
color count: False
pixels off: 16
**FAILED!**
