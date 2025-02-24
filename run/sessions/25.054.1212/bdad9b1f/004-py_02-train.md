
## example 1
*input:*
```
0 0 0 0 8 0
0 0 0 0 8 0
2 2 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
*expected output:*
```
0 0 0 0 8 0
0 0 0 0 8 0
2 2 2 2 4 2
0 0 0 0 8 0
0 0 0 0 8 0
0 0 0 0 8 0
```
*transformed output:*
```
0 0 0 0 8 0
0 0 0 0 8 0
2 2 2 2 2 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 8 0 0 0 0
0 8 0 0 0 0
0 0 0 0 0 0
0 0 0 0 2 2
0 0 0 0 0 0
0 0 0 0 0 0
```
*expected output:*
```
0 8 0 0 0 0
0 8 0 0 0 0
0 8 0 0 0 0
2 4 2 2 2 2
0 8 0 0 0 0
0 8 0 0 0 0
```
*transformed output:*
```
0 8 0 0 0 0
0 8 0 0 0 0
0 8 0 0 0 0
2 2 0 0 2 2
0 0 0 0 0 0
0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
