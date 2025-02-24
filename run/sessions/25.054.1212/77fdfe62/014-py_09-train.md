
## example 1
*input:*
```
2 1 0 0 0 0 1 3
1 1 1 1 1 1 1 1
0 1 0 8 0 0 1 0
0 1 8 8 0 8 1 0
0 1 0 0 8 0 1 0
0 1 8 0 8 8 1 0
1 1 1 1 1 1 1 1
4 1 0 0 0 0 1 6
```
*expected output:*
```
0 2 0 0
2 2 0 3
0 0 6 0
4 0 6 6
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 8 is out of bounds for axis 0 with size 8

## example 2
*input:*
```
9 1 0 0 1 4
1 1 1 1 1 1
0 1 8 8 1 0
0 1 8 0 1 0
1 1 1 1 1 1
2 1 0 0 1 3
```
*expected output:*
```
9 4
2 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 6 is out of bounds for axis 0 with size 6

## example 3
*input:*
```
6 1 0 0 0 0 1 2
1 1 1 1 1 1 1 1
0 1 0 8 0 8 1 0
0 1 8 8 8 0 1 0
0 1 8 0 8 8 1 0
0 1 8 8 8 0 1 0
1 1 1 1 1 1 1 1
7 1 0 0 0 0 1 4
```
*expected output:*
```
0 6 0 2
6 6 2 0
7 0 4 4
7 7 4 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 8 is out of bounds for axis 0 with size 8
