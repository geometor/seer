
## example 1
*input:*
```
2 0 2
0 2 0
2 0 2
```
*expected output:*
```
1
```
*transformed output:*
```
7
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**

## example 2
*input:*
```
2 0 0
2 0 0
0 2 0
```
*expected output:*
```
7
```
*transformed output:*
```
7
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
2 0 2
2 0 2
2 0 2
```
*expected output:*
```
1
```
*transformed output:*
```
1
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 4
*input:*
```
0 0 0
2 0 2
0 0 0
```
*expected output:*
```
1
```
*transformed output:*
```
1
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 5
*input:*
```
2 2 0
0 2 2
0 0 0
```
*expected output:*
```
7
```
*transformed output:*
```
1
```
size: True
palette: False
color count: False
pixels off: 1
**FAILED!**

## example 6
*input:*
```
2 2 0
0 2 0
0 0 0
```
*expected output:*
```
7
```
*transformed output:*
```
7
```
size: True
palette: True
color count: True
pixels off: 0
PASSED
