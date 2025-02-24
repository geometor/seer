
## example 1
*input:*
```
8 5 0
8 5 3
0 3 2
```
*expected output:*
```
8 5 0 0 8 8
8 5 3 3 5 5
0 3 2 2 3 0
0 3 2 2 3 0
5 5 3 3 5 8
8 8 0 0 5 8
```
*transformed output:*
```
8 5 5 0 0 0
8 5 5 3 3 3
8 5 5 3 3 0
0 3 3 2 2 2
0 3 3 2 2 0
0 3 0 2 0 2
```
size: True
palette: True
color count: False
pixels off: 23
**FAILED!**

## example 2
*input:*
```
3 8 2
3 2 2
8 5 2
```
*expected output:*
```
3 8 2 8 3 3
3 2 2 5 2 8
8 5 2 2 2 2
2 2 2 2 5 8
8 2 5 2 2 3
3 3 8 2 8 3
```
*transformed output:*
```
3 8 8 2 2 0
3 2 2 2 2 2
3 2 2 2 2 0
8 5 5 2 2 2
8 5 5 2 2 0
0 5 0 2 0 2
```
size: True
palette: False
color count: False
pixels off: 21
**FAILED!**

## example 3
*input:*
```
0 3 0
6 6 6
0 3 0
```
*expected output:*
```
0 3 0 0 6 0
6 6 6 3 6 3
0 3 0 0 6 0
0 6 0 0 3 0
3 6 3 6 6 6
0 6 0 0 3 0
```
*transformed output:*
```
0 3 3 0 0 0
6 6 6 6 6 6
6 6 6 6 6 0
0 3 3 0 0 0
0 3 3 0 0 0
0 3 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 18
**FAILED!**
