
## example 1
*input:*
```
2 1 2 1 2
1 1 1 1 1
2 1 2 1 2
0 0 1 1 1
0 0 2 1 2
```
*expected output:*
```
1 1
2 1
```
*transformed output:*
```
2 1
1 1
```
size: True
palette: True
color count: True
pixels off: 2
**FAILED!**

## example 2
*input:*
```
8 6 0 6
6 8 6 8
8 6 8 6
6 8 6 8
```
*expected output:*
```
8
```
*transformed output:*
```
8 6
6 8
```
size: False
palette: False
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
2 2 5 2 2 5 2
2 2 5 2 2 5 2
5 5 5 5 5 5 5
2 2 5 2 2 5 2
2 2 5 2 2 5 2
5 5 5 5 5 0 0
2 2 5 2 2 0 0
```
*expected output:*
```
5 5
5 2
```
*transformed output:*
```
2 2
2 2
```
size: True
palette: True
color count: False
pixels off: 3
**FAILED!**
