
## example 1
*input:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 9 3 0 0
0 0 7 8 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
*expected output:*
```
8 8 0 0 7 7
8 8 0 0 7 7
0 0 9 3 0 0
0 0 7 8 0 0
3 3 0 0 9 9
3 3 0 0 9 9
```
*transformed output:*
```
9 9 0 0 3 3
9 9 0 0 3 3
0 0 9 3 0 0
0 0 7 8 0 0
7 7 0 0 8 8
7 7 0 0 8 8
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0 0
0 4 6 0 0 0
0 2 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
*expected output:*
```
1 0 0 2 2 0
0 4 6 0 0 0
0 2 1 0 0 0
6 0 0 4 4 0
6 0 0 4 4 0
0 0 0 0 0 0
```
*transformed output:*
```
4 4 0 0 6 6
4 4 6 0 6 6
0 2 1 0 0 0
0 0 0 0 0 0
2 2 0 0 1 1
2 2 0 0 1 1
```
size: True
palette: True
color count: False
pixels off: 20
**FAILED!**

## example 3
*input:*
```
0 0 0 0 0 0
0 0 0 0 0 0
0 0 3 6 0 0
0 0 5 2 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
*expected output:*
```
2 2 0 0 5 5
2 2 0 0 5 5
0 0 3 6 0 0
0 0 5 2 0 0
6 6 0 0 3 3
6 6 0 0 3 3
```
*transformed output:*
```
3 3 0 0 6 6
3 3 0 0 6 6
0 0 3 6 0 0
0 0 5 2 0 0
5 5 0 0 2 2
5 5 0 0 2 2
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**
