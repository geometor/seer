
## example 1
*input:*
```
2 0 0 0 0
0 2 0 0 2
2 0 0 2 0
0 0 0 2 2
0 0 2 2 0
```
*expected output:*
```
5 5 5
0 5 0
0 5 0
```
*transformed output:*
```
5 0 0
0 5 0
5 0 0
```
size: True
palette: True
color count: False
pixels off: 4
**FAILED!**

## example 2
*input:*
```
0 0 0 0 0
0 0 1 1 1
0 1 0 1 1
0 1 0 1 0
0 0 0 0 1
```
*expected output:*
```
0 5 0
5 5 5
0 5 0
```
*transformed output:*
```
0 5 5
5 0 5
5 0 5
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 3
*input:*
```
3 0 0 0 0
0 0 0 3 3
0 3 3 0 0
0 3 0 3 0
3 0 3 3 0
```
*expected output:*
```
0 0 5
0 0 5
5 5 5
```
*transformed output:*
```
5 0 0
0 0 0
0 5 5
```
size: True
palette: True
color count: False
pixels off: 4
**FAILED!**

## example 4
*input:*
```
1 0 1 0 0
1 0 0 1 1
1 1 0 1 0
0 1 0 1 0
1 0 0 0 1
```
*expected output:*
```
0 5 0
5 5 5
0 5 0
```
*transformed output:*
```
5 0 5
5 0 0
5 5 0
```
size: True
palette: True
color count: True
pixels off: 6
**FAILED!**

## example 5
*input:*
```
2 0 2 0 2
2 0 0 0 2
2 2 0 0 0
2 0 0 2 2
2 2 2 0 2
```
*expected output:*
```
5 5 5
0 5 0
0 5 0
```
*transformed output:*
```
5 0 5
5 0 0
5 5 0
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**

## example 6
*input:*
```
0 2 0 2 0
0 2 2 2 0
0 2 2 0 2
2 2 2 0 0
0 0 2 0 2
```
*expected output:*
```
5 5 5
0 5 0
0 5 0
```
*transformed output:*
```
0 5 0
0 5 5
0 5 5
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**

## example 7
*input:*
```
0 3 0 3 0
3 3 0 0 0
0 3 0 0 0
0 0 3 0 0
3 3 3 0 0
```
*expected output:*
```
0 0 5
0 0 5
5 5 5
```
*transformed output:*
```
0 5 0
5 5 0
0 5 0
```
size: True
palette: True
color count: False
pixels off: 7
**FAILED!**
