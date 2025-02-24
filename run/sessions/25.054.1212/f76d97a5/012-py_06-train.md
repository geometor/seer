
## example 1
*input:*
```
4 5 4
5 5 5
4 5 4
```
*expected output:*
```
0 4 0
4 4 4
0 4 0
```
*transformed output:*
```
4 5 4
5 5 5
4 5 4
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
5 5 6 6 6
6 5 5 6 6
6 6 5 5 6
6 6 6 5 5
5 6 6 6 5
```
*expected output:*
```
6 6 0 0 0
0 6 6 0 0
0 0 6 6 0
0 0 0 6 6
6 0 0 0 6
```
*transformed output:*
```
0 0 0 6 6
0 0 0 0 6
6 0 0 0 0
0 6 0 0 0
0 0 6 0 0
```
size: True
palette: True
color count: False
pixels off: 16
**FAILED!**

## example 3
*input:*
```
9 5 9 9 9
9 9 5 5 9
9 5 9 9 9
9 9 5 9 9
9 9 9 5 5
```
*expected output:*
```
0 9 0 0 0
0 0 9 9 0
0 9 0 0 0
0 0 9 0 0
0 0 0 9 9
```
*transformed output:*
```
9 5 9 9 9
9 9 5 5 9
9 5 9 9 9
9 9 5 0 0
9 9 0 0 0
```
size: True
palette: False
color count: False
pixels off: 22
**FAILED!**
