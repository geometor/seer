
## example 1
*input:*
```
1 0 0 5 0 1 0
0 1 0 5 1 1 1
1 0 0 5 0 0 0
```
*expected output:*
```
0 0 0
0 2 0
0 0 0
```
*transformed output:*
```
2 0 0
0 2 0
2 0 0
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**

## example 2
*input:*
```
1 1 0 5 0 1 0
0 0 1 5 1 1 1
1 1 0 5 0 1 0
```
*expected output:*
```
0 2 0
0 0 2
0 2 0
```
*transformed output:*
```
1 2 0
0 0 2
1 2 0
```
size: True
palette: False
color count: False
pixels off: 2
**FAILED!**

## example 3
*input:*
```
0 0 1 5 0 0 0
1 1 0 5 1 0 1
0 1 1 5 1 0 1
```
*expected output:*
```
0 0 0
2 0 0
0 0 2
```
*transformed output:*
```
0 0 2
2 2 0
0 1 1
```
size: True
palette: False
color count: False
pixels off: 4
**FAILED!**
