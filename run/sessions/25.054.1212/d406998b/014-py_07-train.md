
## example 1
*input:*
```
5 0 5 0 0 5 0 0 0 5
0 5 0 0 5 0 0 5 0 0
0 0 0 5 0 0 5 0 5 0
```
*expected output:*
```
5 0 5 0 0 3 0 0 0 3
0 3 0 0 5 0 0 3 0 0
0 0 0 3 0 0 5 0 5 0
```
*transformed output:*
```
3 0 5 0 0 5 0 0 0 5
0 3 0 0 5 0 0 5 0 0
0 0 0 5 0 0 5 0 5 0
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
0 5 0 5 0 0 5 0 5 0 0 0
5 0 0 0 5 0 0 5 0 0 5 0
0 0 5 0 0 5 0 0 0 5 0 5
```
*expected output:*
```
0 3 0 3 0 0 5 0 5 0 0 0
5 0 0 0 5 0 0 3 0 0 5 0
0 0 5 0 0 3 0 0 0 3 0 3
```
*transformed output:*
```
0 3 0 5 0 0 5 0 5 0 0 0
3 0 0 0 5 0 0 5 0 0 5 0
0 0 5 0 0 5 0 0 0 5 0 5
```
size: True
palette: True
color count: False
pixels off: 6
**FAILED!**

## example 3
*input:*
```
0 0 5 0 0 5 0 5 0 0 0 5 0
5 0 0 0 5 0 5 0 0 5 0 0 5
0 5 0 5 0 0 0 0 5 0 5 0 0
```
*expected output:*
```
0 0 3 0 0 5 0 5 0 0 0 5 0
3 0 0 0 3 0 3 0 0 5 0 0 3
0 5 0 5 0 0 0 0 3 0 3 0 0
```
*transformed output:*
```
0 0 5 0 0 5 0 5 0 0 0 5 0
3 0 0 0 5 0 5 0 0 5 0 0 5
0 3 0 5 0 0 0 0 5 0 5 0 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**

## example 4
*input:*
```
0 0 5 0 0 5 0 5 0 5 0 5 0 0
5 0 0 0 5 0 0 0 5 0 5 0 0 5
0 5 0 5 0 0 5 0 0 0 0 0 5 0
```
*expected output:*
```
0 0 5 0 0 3 0 3 0 3 0 3 0 0
5 0 0 0 5 0 0 0 5 0 5 0 0 3
0 3 0 3 0 0 5 0 0 0 0 0 5 0
```
*transformed output:*
```
0 0 5 0 0 5 0 5 0 5 0 5 0 0
3 0 0 0 5 0 0 0 5 0 5 0 0 5
0 3 0 5 0 0 5 0 0 0 0 0 5 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**
