
## example 1
*input:*
```
0 2 2
0 2 2
2 0 0
```
*expected output:*
```
0 2 2
0 2 2
1 0 0
```
*transformed output:*
```
0 2 2
0 2 2
2 1 1
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 2
*input:*
```
2 2 2 0
0 2 0 0
0 0 0 2
0 2 0 0
```
*expected output:*
```
2 2 2 0
0 2 0 0
0 0 0 1
0 1 0 0
```
*transformed output:*
```
2 2 2 0
0 2 0 0
0 0 1 2
0 2 1 1
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 3
*input:*
```
2 2 0 0
0 2 0 0
2 2 0 2
0 0 0 0
0 2 2 2
```
*expected output:*
```
2 2 0 0
0 2 0 0
2 2 0 1
0 0 0 0
0 2 2 2
```
*transformed output:*
```
2 2 0 0
0 2 0 0
2 2 0 2
0 0 1 1
0 2 2 2
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 4
*input:*
```
2 2 0
2 0 2
0 2 0
```
*expected output:*
```
2 2 0
2 0 1
0 1 0
```
*transformed output:*
```
2 2 0
2 1 2
0 2 1
```
size: True
palette: True
color count: False
pixels off: 4
**FAILED!**
