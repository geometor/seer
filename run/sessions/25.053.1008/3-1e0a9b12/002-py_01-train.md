
## example 1
*input:*
```
0 4 0 9
0 0 0 0
0 4 6 0
1 0 0 0
```
*expected output:*
```
0 0 0 0
0 0 0 0
0 4 0 0
1 4 6 9
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 4 is out of bounds for axis 0 with size 4

## example 2
*input:*
```
0 0 0 0 0 9
0 0 0 8 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 0 0 0
```
*expected output:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
4 0 0 0 0 0
4 0 7 8 0 0
4 0 7 8 0 9
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 6 is out of bounds for axis 0 with size 6

## example 3
*input:*
```
0 0 0 1 0
0 3 0 0 0
0 3 0 1 2
6 0 0 0 0
0 3 0 0 0
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
0 3 0 0 0
0 3 0 1 0
6 3 0 1 2
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 5 is out of bounds for axis 0 with size 5
