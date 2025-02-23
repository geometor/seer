
## example 1
*input:*
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 2 2 2 0 0 0 0 0
0 0 0 0 0 2 0 0 0 0 0 0
0 0 0 2 2 2 0 0 0 0 0 0
0 0 0 2 0 2 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
0 2 2 2
0 0 2 0
2 2 2 0
2 0 2 0
```
*transformed output:*
```
2 2 0 0
0 2 0 2
2 2 2 2
0 0 0 2
```
size: True
palette: True
color count: True
pixels off: 10
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0
0 0 1 1 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0 0 0
0 0 1 1 1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
1 0 0
1 1 0
0 1 0
1 1 1
0 0 1
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: unsupported operand type(s) for +: 'NoneType' and 'int'

## example 3
*input:*
```
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 8 0 8 0 0 0 0 0
0 0 0 8 8 8 8 0 0 0 0 0
0 0 0 0 0 0 8 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
0 8 0 8 0
8 8 8 8 0
0 0 0 8 8
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: unsupported operand type(s) for +: 'NoneType' and 'int'
