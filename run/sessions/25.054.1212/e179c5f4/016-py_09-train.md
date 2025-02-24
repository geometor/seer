
## example 1
*input:*
```
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
1 0
```
*expected output:*
```
8 1
1 8
8 1
1 8
8 1
1 8
8 1
1 8
8 1
1 8
```
*transformed output:*
```
1 8
8 8
1 8
8 8
1 8
8 8
1 8
8 8
1 8
1 8
```
size: True
palette: True
color count: False
pixels off: 14
**FAILED!**

## example 2
*input:*
```
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
1 0 0
```
*expected output:*
```
8 1 8
1 8 8
8 1 8
8 8 1
8 1 8
1 8 8
8 1 8
8 8 1
8 1 8
1 8 8
```
*transformed output:*
```
1 8 8
8 8 8
1 8 8
8 8 8
1 8 8
8 8 8
1 8 8
8 8 8
1 8 8
1 8 1
```
size: True
palette: True
color count: False
pixels off: 15
**FAILED!**

## example 3
*input:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
```
*expected output:*
```
8 8 8 1
8 8 1 8
8 1 8 8
1 8 8 8
8 1 8 8
8 8 1 8
8 8 8 1
8 8 1 8
8 1 8 8
1 8 8 8
```
*transformed output:*
```
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
1 8 1 8
```
size: True
palette: True
color count: False
pixels off: 15
**FAILED!**
