
## example 1
*input:*
```
0 0 0 0 0 0 0 0 0 0
0 2 2 0 0 0 0 0 0 0
0 0 2 2 2 0 0 7 7 0
0 0 0 0 0 0 7 0 7 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 6 6 6 6 0 0 0
0 0 0 0 6 6 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
6 6 6 6
0 6 6 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: transform function returned None

## example 2
*input:*
```
0 0 0 0 0 0 0 0 0 0
0 0 4 4 0 0 0 0 0 0
0 0 4 4 0 0 8 8 8 0
0 0 0 0 0 0 8 0 8 8
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 2 2 2 2 0 0 0 0
0 2 2 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
4 4
4 4
```
*transformed output:*
```
4 4
4 4
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
0 0 0 0 0 0 0 0 0 0
0 3 3 0 0 0 0 0 0 0
0 0 3 0 0 5 0 0 5 0
0 0 3 0 0 5 5 5 5 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 8 8 8 0 0 0 0
8 8 8 8 0 8 8 0 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
5 0 0 5
5 5 5 5
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: transform function returned None
