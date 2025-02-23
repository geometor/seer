
## example 1
*input:*
```
2 2 1
2 3 1
1 1 1
```
*expected output:*
```
1 2 3
1 2 0
1 2 0
1 0 0
1 0 0
```
*transformed output:*
```
2 2 0
0 0 0
0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 2
*input:*
```
3 1 1 4
2 2 2 4
4 4 4 4
```
*expected output:*
```
4 2 1 3
4 2 1 0
4 2 0 0
4 0 0 0
4 0 0 0
4 0 0 0
```
*transformed output:*
```
3 3 3 0
0 0 0 0
0 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
8 8 2
3 8 8
3 3 4
3 3 4
```
*expected output:*
```
3 8 4 2
3 8 4 0
3 8 0 0
3 8 0 0
3 0 0 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: index 3 is out of bounds for axis 1 with size 3

## example 4
*input:*
```
1 1 1
2 2 1
2 8 1
2 8 1
```
*expected output:*
```
1 2 8
1 2 8
1 2 0
1 2 0
1 0 0
1 0 0
```
*transformed output:*
```
1 1 0
0 0 0
0 0 0
0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
