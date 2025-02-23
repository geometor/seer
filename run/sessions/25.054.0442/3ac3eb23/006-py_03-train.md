
## example 1
*input:*
```
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
0 2 0 0 0 8 0 0 0 0
2 0 2 0 8 0 8 0 0 0
```
*transformed output:*
```
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 2 0 0 0 8 0 0 0 0
0 0 0 0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 12
**FAILED!**

## example 2
*input:*
```
0 4 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
```
*expected output:*
```
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
0 4 0 0 0 0 0
4 0 4 0 0 0 0
```
*transformed output:*
```
0 4 0 0 0 0 0
0 0 0 0 0 0 0
0 4 0 0 0 0 0
0 0 0 0 0 0 0
0 4 0 0 0 0 0
0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 6
**FAILED!**
