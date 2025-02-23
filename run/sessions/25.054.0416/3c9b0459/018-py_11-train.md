
## example 1
*input:*
```
2 2 1
2 1 2
2 8 1
```
*expected output:*
```
1 8 2
2 1 2
1 2 2
```
*transformed output:*
```
2 1 2
2 8 1
2 2 1
```
size: True
palette: True
color count: True
pixels off: 6
**FAILED!**

## example 2
*input:*
```
9 2 4
2 4 4
2 9 2
```
*expected output:*
```
2 9 2
4 4 2
4 2 9
```
*transformed output:*
```
2 4 4
2 9 2
9 2 4
```
size: True
palette: True
color count: True
pixels off: 6
**FAILED!**

## example 3
*input:*
```
8 8 8
5 5 8
8 5 5
```
*expected output:*
```
5 5 8
8 5 5
8 8 8
```
*transformed output:*
```
5 5 8
8 5 5
8 8 8
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 4
*input:*
```
3 2 9
9 9 9
2 3 3
```
*expected output:*
```
3 3 2
9 9 9
9 2 3
```
*transformed output:*
```
9 9 9
2 3 3
3 2 9
```
size: True
palette: True
color count: True
pixels off: 8
**FAILED!**
