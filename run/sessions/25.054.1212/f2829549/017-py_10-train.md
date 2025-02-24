
## example 1
*input:*
```
7 7 0 1 5 0 0
7 0 0 1 5 0 0
0 0 0 1 5 0 5
0 0 0 1 5 5 0
```
*expected output:*
```
0 0 3
0 3 3
0 3 0
0 0 3
```
*transformed output:*
```
3 3 0 3 3 0 0
3 0 0 3 3 0 0
0 0 0 3 3 0 3
0 0 0 3 3 3 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 2
*input:*
```
7 7 0 1 5 0 0
0 0 0 1 0 0 0
7 7 0 1 5 0 0
0 7 7 1 5 5 0
```
*expected output:*
```
0 0 3
3 3 3
0 0 3
0 0 0
```
*transformed output:*
```
3 3 0 3 3 0 0
0 0 0 3 0 0 0
3 3 0 3 3 0 0
0 3 3 3 3 3 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
0 7 7 1 5 0 0
0 0 7 1 0 5 5
0 7 0 1 5 5 0
0 0 7 1 0 0 0
```
*expected output:*
```
0 0 0
3 0 0
0 0 3
3 3 0
```
*transformed output:*
```
0 3 3 3 3 0 0
0 0 3 3 0 3 3
0 3 0 3 3 3 0
0 0 3 3 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 4
*input:*
```
7 0 7 1 5 5 0
7 7 0 1 5 5 5
0 7 0 1 0 0 0
0 0 0 1 5 0 5
```
*expected output:*
```
0 0 0
0 0 0
3 0 3
0 3 0
```
*transformed output:*
```
3 0 3 3 3 3 0
3 3 0 3 3 3 3
0 3 0 3 0 0 0
0 0 0 3 3 0 3
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 5
*input:*
```
7 0 0 1 0 5 0
0 0 7 1 5 0 0
0 0 0 1 5 5 5
7 7 7 1 5 5 5
```
*expected output:*
```
0 0 3
0 3 0
0 0 0
0 0 0
```
*transformed output:*
```
3 0 0 3 0 3 0
0 0 3 3 3 0 0
0 0 0 3 3 3 3
3 3 3 3 3 3 3
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
