
## example 1
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 0 5 5 0
5 5 5 5 0 5 0 0 5 0 0 5 5 0
5 5 5 5 0 5 5 5 5 0 5 5 5 5
```
*expected output:*
```
2 2 2
8 8 8
3 3 3
```
*transformed output:*
```
0 0 0
0 0 0
0 0 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
0 5 5 0 0 5 5 5 5 0 5 5 5 5
0 5 5 0 0 5 0 0 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
```
*expected output:*
```
3 3 3
4 4 4
2 2 2
```
*transformed output:*
```
8 0 0
8 0 0
8 0 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 3
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 0 0 5 0 5 5 5 5 0 5 5 5 5
5 0 0 5 0 5 5 5 5 0 5 0 0 5
5 5 5 5 0 5 5 5 5 0 5 0 0 5
```
*expected output:*
```
8 8 8
2 2 2
4 4 4
```
*transformed output:*
```
0 8 8
0 8 8
0 8 8
```
size: True
palette: False
color count: False
pixels off: 7
**FAILED!**

## example 4
*input:*
```
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 5 5 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
5 5 5 5 0 5 0 0 5 0 5 5 5 5
```
*expected output:*
```
2 2 2
4 4 4
2 2 2
```
*transformed output:*
```
0 0 0
0 0 0
0 0 0
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**
