
## example 1
*input:*
```
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
0 0
1 0
```
*expected output:*
```
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
```
*transformed output:*
```
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
1 0 0
```
*expected output:*
```
0 1 0
1 0 0
0 1 0
0 0 1
0 1 0
1 0 0
0 1 0
0 0 1
0 1 0
1 0 0
```
*transformed output:*
```
0 1 0
1 0 0
0 1 0
1 0 0
0 1 0
1 0 0
0 1 0
1 0 0
0 1 0
1 0 0
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**

## example 3
*input:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
1 0 0 0
```
*expected output:*
```
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
0 0 1 0
0 1 0 0
1 0 0 0
```
*transformed output:*
```
0 1 0 0
1 0 0 0
0 1 0 0
1 0 0 0
0 1 0 0
1 0 0 0
0 1 0 0
1 0 0 0
0 1 0 0
1 0 0 0
```
size: True
palette: True
color count: True
pixels off: 10
**FAILED!**
