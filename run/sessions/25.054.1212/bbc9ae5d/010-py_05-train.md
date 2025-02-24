
## example 1
*input:*
```
1 1 0 0 0 0
```
*expected output:*
```
1 1 0 0 0 0
1 1 1 0 0 0
1 1 1 1 0 0
```
*transformed output:*
```
1 0 0 0 0 0
1 1 0 0 0 0
1 1 1 0 0 0
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**

## example 2
*input:*
```
2 0 0 0 0 0 0 0
```
*expected output:*
```
2 0 0 0 0 0 0 0
2 2 0 0 0 0 0 0
2 2 2 0 0 0 0 0
2 2 2 2 0 0 0 0
```
*transformed output:*
```
2 0 0 0 0 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
5 5 5 0 0 0 0 0 0 0
```
*expected output:*
```
5 5 5 0 0 0 0 0 0 0
5 5 5 5 0 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
5 5 5 5 5 5 0 0 0 0
5 5 5 5 5 5 5 0 0 0
```
*transformed output:*
```
5 0 0 0 0 0 0 0 0 0
5 5 0 0 0 0 0 0 0 0
5 5 5 0 0 0 0 0 0 0
5 5 5 5 0 0 0 0 0 0
5 5 5 5 5 0 0 0 0 0
```
size: True
palette: True
color count: False
pixels off: 10
**FAILED!**

## example 4
*input:*
```
8 8 8 8 0 0
```
*expected output:*
```
8 8 8 8 0 0
8 8 8 8 8 0
8 8 8 8 8 8
```
*transformed output:*
```
8 0 0 0 0 0
8 8 0 0 0 0
8 8 8 0 0 0
8 8 8 8 0 0
8 8 8 8 8 0
8 8 8 8 8 8
8 8 8 8 8 8
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 5
*input:*
```
7 0 0 0 0 0
```
*expected output:*
```
7 0 0 0 0 0
7 7 0 0 0 0
7 7 7 0 0 0
```
*transformed output:*
```
7 0 0 0 0 0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
