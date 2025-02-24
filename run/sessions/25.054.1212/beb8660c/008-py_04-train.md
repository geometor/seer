
## example 1
*input:*
```
0 2 2 0 0 0 0
0 0 0 0 3 0 0
1 1 1 0 0 0 0
0 0 0 0 0 0 0
0 5 5 5 5 5 5
0 0 0 0 0 0 0
6 6 6 6 6 0 0
0 0 0 4 4 4 4
0 0 0 0 0 0 0
8 8 8 8 8 8 8
```
*expected output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 3
0 0 0 0 0 2 2
0 0 0 0 1 1 1
0 0 0 4 4 4 4
0 0 6 6 6 6 6
0 5 5 5 5 5 5
8 8 8 8 8 8 8
```
*transformed output:*
```
0 0 0 0 0 0 0
0 2 2 0 0 0 0
0 0 0 0 0 0 0
1 1 1 0 3 0 0
0 0 0 0 0 0 0
0 5 5 5 5 5 5
0 0 0 0 0 0 0
0 0 0 0 0 0 0
6 6 6 4 4 4 4
8 8 8 8 8 8 8
```
size: True
palette: True
color count: False
pixels off: 31
**FAILED!**

## example 2
*input:*
```
0 0 0 1
0 0 0 0
2 2 2 0
0 0 0 0
0 3 3 0
0 0 0 0
8 8 8 8
```
*expected output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
0 0 3 3
0 2 2 2
8 8 8 8
```
*transformed output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
2 2 2 0
0 0 0 0
0 3 3 1
8 8 8 8
```
size: True
palette: True
color count: True
pixels off: 9
**FAILED!**

## example 3
*input:*
```
2 2 0
0 4 0
8 8 8
```
*expected output:*
```
0 0 4
0 2 2
8 8 8
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 3 is out of bounds for axis 0 with size 3
