
## example 1
*input:*
```
2 0 0 0 2 0 0 0 2 0
0 2 0 2 0 2 0 2 0 2
0 0 2 0 0 0 2 0 0 0
```
*expected output:*
```
2 0 0 0 2 4 4 4 2 0
4 2 0 2 0 2 4 2 0 2
4 4 2 0 0 0 2 0 0 0
```
*transformed output:*
```
4 0 0 0 4 0 0 0 2 0
0 4 0 2 0 4 0 2 0 2
0 0 4 0 0 0 4 0 0 0
```
size: True
palette: True
color count: False
pixels off: 13
**FAILED!**

## example 2
*input:*
```
2 0 0 0 2 0 0 0 2 0 0 0 2 0 0
0 2 0 2 0 2 0 2 0 2 0 2 0 2 0
0 0 2 0 0 0 2 0 0 0 2 0 0 0 2
```
*expected output:*
```
2 0 0 0 2 4 4 4 2 0 0 0 2 0 0
4 2 0 2 0 2 4 2 0 2 0 2 4 2 0
4 4 2 0 0 0 2 0 0 0 2 4 4 4 2
```
*transformed output:*
```
4 0 0 0 4 0 0 0 4 0 0 0 4 0 0
0 4 0 2 0 4 0 2 0 4 0 2 0 4 0
0 0 4 0 0 0 4 0 0 0 4 0 0 0 4
```
size: True
palette: True
color count: False
pixels off: 23
**FAILED!**

## example 3
*input:*
```
2 0 0 0 2 0 0 0 2 0 0 0 2 0 0 0 2 0
0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2 0 2
0 0 2 0 0 0 2 0 0 0 2 0 0 0 2 0 0 0
```
*expected output:*
```
2 0 0 0 2 4 4 4 2 0 0 0 2 0 0 0 2 4
4 2 0 2 0 2 4 2 0 2 0 2 4 2 0 2 0 2
4 4 2 0 0 0 2 0 0 0 2 4 4 4 2 0 0 0
```
*transformed output:*
```
4 0 0 0 4 0 0 0 4 0 0 0 4 0 0 0 2 0
0 4 0 2 0 4 0 2 0 4 0 2 0 4 0 2 0 2
0 0 4 0 0 0 4 0 0 0 4 0 0 0 4 0 0 0
```
size: True
palette: True
color count: False
pixels off: 24
**FAILED!**
