
## example 1
*input:*
```
8 6
6 8
```
*expected output:*
```
8 6 6 8
6 8 8 6
6 8 8 6
8 6 6 8
```
*transformed output:*
```
8 8 0 0
6 6 6 6
8 8 6 6
8 8 0 0
```
size: True
palette: False
color count: False
pixels off: 10
**FAILED!**

## example 2
*input:*
```
7 7 8
7 7 8
8 8 8
```
*expected output:*
```
7 7 8 8 7 7
7 7 8 8 7 7
8 8 8 8 8 8
8 8 8 8 8 8
7 7 8 8 7 7
7 7 8 8 7 7
```
*transformed output:*
```
7 7 0 0 0 0
7 7 7 0 0 7
7 7 8 8 8 8
8 8 8 8 8 8
8 8 8 0 0 8
8 8 0 0 0 0
```
size: True
palette: False
color count: False
pixels off: 20
**FAILED!**

## example 3
*input:*
```
6 9 9
6 4 4
6 4 4
```
*expected output:*
```
6 9 9 6 6 6
6 4 4 4 4 9
6 4 4 4 4 9
9 4 4 4 4 6
9 4 4 4 4 6
6 6 6 9 9 6
```
*transformed output:*
```
6 6 0 0 0 0
9 6 6 0 0 9
4 4 6 6 9 9
4 4 4 6 9 4
4 4 4 0 0 4
4 4 0 0 0 0
```
size: True
palette: False
color count: False
pixels off: 28
**FAILED!**
