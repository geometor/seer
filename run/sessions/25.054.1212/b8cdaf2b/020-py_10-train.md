
## example 1
*input:*
```
0 0 0
0 2 0
2 4 2
```
*expected output:*
```
4 0 4
0 2 0
2 4 2
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 3 is out of bounds for axis 0 with size 3

## example 2
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 8 0 0
8 8 3 8 8
```
*expected output:*
```
0 0 0 0 0
3 0 0 0 3
0 3 0 3 0
0 0 8 0 0
8 8 3 8 8
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 6 is out of bounds for axis 1 with size 5

## example 3
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 6 6 6 0
6 1 1 1 6
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
1 0 0 0 1
0 6 6 6 0
6 1 1 1 6
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 6 is out of bounds for axis 1 with size 5

## example 4
*input:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
*expected output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
4 0 0 0 0 0 4
0 4 0 0 0 4 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
*transformed output:*
```
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
4 0 0 0 0 0 4
0 4 0 0 0 4 0
0 0 2 2 2 0 0
2 2 4 4 4 2 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED
