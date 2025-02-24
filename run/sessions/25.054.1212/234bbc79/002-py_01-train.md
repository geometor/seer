
## example 1
*input:*
```
0 5 0 0 0 0 0 0 0
2 2 0 5 1 0 5 2 2
0 0 0 0 5 0 0 0 0
```
*expected output:*
```
0 2 1 1 0 0 0
2 2 0 1 2 2 2
0 0 0 0 0 0 0
```
*transformed output:*
```
0 0 0 0 0 0 0
2 2 0 1 0 2 2
0 0 0 1 0 0 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 0 0 5 1 5 0 0 0 0 0
2 2 0 0 0 0 0 0 3 3 3
0 5 0 0 0 0 0 5 3 0 0
```
*expected output:*
```
0 0 0 0 0 0 0 0 0
2 2 0 0 0 0 3 3 3
0 2 1 1 1 3 3 0 0
```
*transformed output:*
```
0 0 0 1 1 0 0 0 0
2 2 0 0 0 0 3 3 3
0 0 0 0 0 0 3 0 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**

## example 3
*input:*
```
0 0 0 0 0 0 5 0 0 0 0
2 2 2 0 5 8 8 0 0 0 0
0 0 5 0 0 0 0 0 5 6 6
```
*expected output:*
```
0 0 0 0 0 0 0 0 0
2 2 2 0 0 8 6 6 6
0 0 2 8 8 8 0 0 0
```
*transformed output:*
```
0 0 0 0 0 0 0 0 0
2 2 2 0 8 0 0 0 0
0 0 0 0 0 0 0 6 6
```
size: True
palette: True
color count: False
pixels off: 11
**FAILED!**

## example 4
*input:*
```
0 1 5 0 0 0 0 0 2 2 0
1 1 0 0 5 2 0 5 2 0 0
0 0 0 0 0 5 0 0 0 0 0
```
*expected output:*
```
0 1 1 2 2 0 2 2
1 1 0 0 2 2 2 0
0 0 0 0 0 0 0 0
```
*transformed output:*
```
0 1 1 0 0 0 2 2 0
1 1 0 0 2 0 2 0 0
0 0 0 0 0 0 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
