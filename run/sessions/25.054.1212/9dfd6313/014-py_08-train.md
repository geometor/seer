
## example 1
*input:*
```
5 0 0
3 5 0
0 0 5
```
*expected output:*
```
5 3 0
0 5 0
0 0 5
```
*transformed output:*
```
5 0 0
3 5 0
0 0 5
```
size: True
palette: True
color count: True
pixels off: 2
**FAILED!**

## example 2
*input:*
```
5 0 0 0
0 5 0 0
6 0 5 0
6 0 4 5
```
*expected output:*
```
5 0 6 6
0 5 0 0
0 0 5 4
0 0 0 5
```
*transformed output:*
```
5 0 0 0
0 5 0 0
6 0 5 0
6 0 4 5
```
size: True
palette: True
color count: True
pixels off: 6
**FAILED!**

## example 3
*input:*
```
5 0 0 0 0
0 5 0 0 0
8 8 5 0 0
0 2 0 5 0
0 2 0 1 5
```
*expected output:*
```
5 0 8 0 0
0 5 8 2 2
0 0 5 0 0
0 0 0 5 1
0 0 0 0 5
```
*transformed output:*
```
5 0 8 2 2
0 5 0 0 0
0 0 5 0 0
0 0 0 5 0
0 0 0 1 5
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**
