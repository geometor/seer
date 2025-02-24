
## example 1
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 0 5 5 0
5 5 5 5 0 5 0 0 5 0 0 5 5 0
5 5 5 5 0 5 5 5 5 0 5 5 5 5
```
*expected output:*
```
2 2 2
8 8 8
3 3 3
```
*transformed output:*
```
4 4 4
8 8 8
8 8 8
```
size: True
palette: False
color count: False
pixels off: 6
**FAILED!**

## example 2
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
0 5 5 0 0 5 5 5 5 0 5 5 5 5
0 5 5 0 0 5 0 0 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
```
*expected output:*
```
3 3 3
4 4 4
2 2 2
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 2 is out of bounds for axis 0 with size 2

## example 3
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 0 0 5 0 5 5 5 5 0 5 5 5 5
5 0 0 5 0 5 5 5 5 0 5 0 0 5
5 5 5 5 0 5 5 5 5 0 5 0 0 5
```
*expected output:*
```
8 8 8
2 2 2
4 4 4
```
*transformed output:*
```
0 0 0
8 8 8
2 2 2
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 4
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
```
*expected output:*
```
2 2 2
4 4 4
2 2 2
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 2 is out of bounds for axis 0 with size 2
