
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
8 8
1 8
8 8
1 8
8 8
1 8
8 8
1 8
8 8
1 8
```
size: True
palette: True
color count: False
pixels off: 5
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
8 8 8
1 8 8
8 8 8
1 8 8
8 8 8
1 8 8
8 8 8
1 8 8
8 8 8
1 8 1
```
size: True
palette: True
color count: False
pixels off: 10
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
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 8 8
8 8 8 8
1 8 1 8
```
size: True
palette: True
color count: False
pixels off: 12
**FAILED!**
