
## example 1
*input:*
```
3 1 2
3 1 2
3 1 2
```
*expected output:*
```
4 5 6
4 5 6
4 5 6
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: 4

## example 2
*input:*
```
2 3 8
2 3 8
2 3 8
```
*expected output:*
```
6 4 9
6 4 9
6 4 9
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: 4

## example 3
*input:*
```
5 8 6
5 8 6
5 8 6
```
*expected output:*
```
1 9 2
1 9 2
1 9 2
```
*transformed output:*
```
2 8 0
2 8 0
2 8 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 4
*input:*
```
9 4 2
9 4 2
9 4 2
```
*expected output:*
```
8 3 6
8 3 6
8 3 6
```
*transformed output:*
```
8 1 4
8 1 4
8 1 4
```
size: True
palette: False
color count: False
pixels off: 6
**FAILED!**
