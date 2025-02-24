
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
2 8 0 8 0 8
8 8 8 8 8 8
0 8 0 8 0 8
8 8 8 8 8 8
0 8 0 8 2 8
8 8 8 8 8 8
```
size: True
palette: True
color count: False
pixels off: 21
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
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 6 is out of bounds for axis 1 with size 6

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
0 8 4 8 8 8
8 8 8 8 8 8
0 8 0 8 8 8
8 8 8 8 8 8
8 8 8 8 8 8
8 8 8 8 8 8
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
