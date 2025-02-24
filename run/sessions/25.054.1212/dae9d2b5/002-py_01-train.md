
## example 1
*input:*
```
4 4 0 3 3 0
4 0 0 3 0 0
0 0 0 0 0 3
```
*expected output:*
```
6 6 0
6 0 0
0 0 6
```
*transformed output:*
```
6 6 0 6 6 0
6 0 0 6 0 0
0 0 0 0 0 6
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 2
*input:*
```
4 0 4 3 3 0
4 0 0 3 0 0
0 0 4 3 0 0
```
*expected output:*
```
6 6 6
6 0 0
6 0 6
```
*transformed output:*
```
6 0 6 6 6 0
6 0 0 6 0 0
0 0 6 6 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
0 0 4 0 3 0
0 4 4 3 0 3
4 4 0 0 0 3
```
*expected output:*
```
0 6 6
6 6 6
6 6 6
```
*transformed output:*
```
0 0 6 0 6 0
0 6 6 6 0 6
6 6 0 0 0 6
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 4
*input:*
```
4 4 0 3 0 0
0 0 0 0 0 3
4 0 0 0 0 0
```
*expected output:*
```
6 6 0
0 0 6
6 0 0
```
*transformed output:*
```
6 6 0 6 0 0
0 0 0 0 0 6
6 0 0 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 5
*input:*
```
0 0 0 0 3 0
4 0 0 0 0 0
0 0 4 3 3 0
```
*expected output:*
```
0 6 0
6 0 0
6 6 6
```
*transformed output:*
```
0 0 0 0 6 0
6 0 0 0 0 0
0 0 6 6 6 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
