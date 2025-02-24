
## example 1
*input:*
```
4 5 1 1 5 4 4 5 1
5 5 5 5 5 5 5 5 5
1 5 4 4 5 1 1 5 4
```
*expected output:*
```
4 5 1
5 5 5
1 5 4
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 3 is out of bounds for axis 0 with size 3

## example 2
*input:*
```
2 0 0 1 2 0 0 1 2 0 0 1
4 2 1 4 4 2 1 4 4 2 1 4
4 1 2 4 4 1 2 4 4 1 2 4
1 0 0 2 1 0 0 2 1 0 0 2
```
*expected output:*
```
2 0 0 1
4 2 1 4
4 1 2 4
1 0 0 2
```
*transformed output:*
```
2 0 0 1
4 2 1 4
4 1 2 4
1 0 0 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
2 1 2 1 2 1
2 3 2 3 2 3
```
*expected output:*
```
2 1
2 3
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 2 is out of bounds for axis 0 with size 2
