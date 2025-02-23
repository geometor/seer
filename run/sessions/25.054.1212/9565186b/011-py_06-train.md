
## example 1
*input:*
```
2 2 2
2 1 8
2 8 8
```
*expected output:*
```
2 2 2
2 5 5
2 5 5
```
*transformed output:*
```
2 2 2
2 5 5
2 5 5
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
1 1 1
8 1 3
8 2 2
```
*expected output:*
```
1 1 1
5 1 5
5 5 5
```
*transformed output:*
```
5 5 5
5 5 5
5 2 2
```
size: True
palette: False
color count: False
pixels off: 6
**FAILED!**

## example 3
*input:*
```
2 2 2
8 8 2
2 2 2
```
*expected output:*
```
2 2 2
5 5 2
2 2 2
```
*transformed output:*
```
2 2 2
5 5 2
2 2 2
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 4
*input:*
```
3 3 8
4 4 4
8 1 1
```
*expected output:*
```
5 5 5
4 4 4
5 5 5
```
*transformed output:*
```
5 5 5
5 5 5
5 5 5
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**
