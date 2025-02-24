
## example 1
*input:*
```
2 0 0 0 0
0 0 0 2 0
0 0 0 0 0
0 6 0 0 0
0 0 0 0 0
```
*expected output:*
```
2 1 1 1 1
1 1 1 2 1
0 0 1 1 1
0 6 0 0 0
0 0 0 0 0
```
*transformed output:*
```
2 1 1 1 0
1 1 1 2 0
0 0 0 0 0
0 6 0 0 0
0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 3 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 8 0
0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0
```
*expected output:*
```
0 0 0 0 0 0 1 2
0 0 0 0 0 0 1 1
0 0 0 3 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 8 0
0 1 1 1 0 0 0 0
0 1 2 1 0 0 0 0
0 1 1 1 0 0 0 0
```
*transformed output:*
```
1 1 1 1 1 1 1 2
1 1 1 0 0 0 0 0
1 1 1 3 0 0 0 0
1 1 1 0 0 0 0 0
1 1 1 0 0 0 8 0
1 1 1 0 0 0 0 0
1 1 2 0 0 0 0 0
0 0 0 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 27
**FAILED!**

## example 3
*input:*
```
0 0 0 0 0
0 2 0 0 0
0 0 0 0 0
0 0 0 0 0
```
*expected output:*
```
1 1 1 0 0
1 2 1 0 0
1 1 1 0 0
0 0 0 0 0
```
*transformed output:*
```
1 1 0 0 0
1 2 0 0 0
0 0 0 0 0
0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
