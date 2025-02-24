
## example 1
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 5 0 0
5 5 5 5 5
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 5 0 0
5 5 1 5 5
```
*transformed output:*
```
0 0 0 0 0
0 0 0 0 0
0 0 5 0 0
0 0 1 0 0
5 5 5 5 5
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 1 0 1 0
0 5 0 5 0
5 5 5 5 5
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 5 0 5 0
5 1 5 1 5
```
*transformed output:*
```
0 0 0 0 0
0 0 0 0 0
0 5 0 1 0
0 1 0 5 0
5 5 5 5 5
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 3
*input:*
```
0 0 0 0 0
0 0 0 0 0
0 1 0 0 1
0 5 0 0 5
5 5 5 5 5
```
*expected output:*
```
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 5 0 0 5
5 1 5 5 1
```
*transformed output:*
```
0 0 0 0 0
0 0 0 0 0
0 5 0 0 1
0 1 0 0 5
5 5 5 5 5
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**
