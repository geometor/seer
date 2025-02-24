
## example 1
*input:*
```
0 4 0 4 2 9 9 0 0 2 0 0 0 0
0 4 0 0 2 0 0 9 9 2 0 1 0 0
4 0 0 0 2 0 0 0 0 2 1 1 1 0
4 4 4 4 2 9 0 9 0 2 1 1 0 1
```
*expected output:*
```
9 4 0 4
0 4 9 9
4 1 1 0
4 4 4 4
```
*transformed output:*
```
4 4 9 9
4 0 0 0
0 0 0 0
4 4 9 0
```
size: True
palette: True
color count: False
pixels off: 12
**FAILED!**

## example 2
*input:*
```
4 4 4 4 2 9 0 9 0 2 0 0 0 1
4 4 0 0 2 9 9 0 0 2 1 0 0 0
4 0 4 4 2 0 0 0 9 2 0 1 0 1
0 0 0 0 2 0 0 9 0 2 1 0 1 0
```
*expected output:*
```
4 4 4 4
4 4 0 0
4 1 4 4
1 0 9 0
```
*transformed output:*
```
4 4 4 4
4 4 0 0
4 0 4 4
0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 3
*input:*
```
4 4 4 0 2 9 9 0 9 2 0 1 0 1
0 4 0 4 2 0 0 9 0 2 0 1 0 0
0 4 0 4 2 0 0 9 9 2 1 0 0 1
4 0 4 4 2 9 9 9 0 2 0 0 0 1
```
*expected output:*
```
4 4 4 9
0 4 9 4
1 4 9 4
4 9 4 4
```
*transformed output:*
```
4 4 4 9
0 4 0 0
0 4 0 0
4 0 4 9
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**

## example 4
*input:*
```
0 0 0 4 2 0 0 0 9 2 0 0 0 0
4 4 0 4 2 9 0 9 0 2 0 0 0 0
4 0 4 4 2 0 9 9 0 2 1 1 0 1
0 4 4 4 2 0 9 0 0 2 1 1 1 1
```
*expected output:*
```
0 0 0 4
4 4 9 4
4 9 4 4
1 4 4 4
```
*transformed output:*
```
4 9 0 0
4 0 4 4
4 0 4 0
4 0 0 4
```
size: True
palette: True
color count: False
pixels off: 10
**FAILED!**

## example 5
*input:*
```
4 0 4 0 2 0 0 0 0 2 0 0 0 1
4 4 4 4 2 0 0 0 9 2 1 1 0 0
0 4 4 4 2 0 9 9 0 2 1 1 0 1
0 4 4 0 2 0 0 9 0 2 0 1 0 1
```
*expected output:*
```
4 0 4 1
4 4 4 4
1 4 4 4
0 4 4 1
```
*transformed output:*
```
4 4 1 0
4 4 0 4
0 4 1 4
0 4 1 4
```
size: True
palette: True
color count: False
pixels off: 8
**FAILED!**
