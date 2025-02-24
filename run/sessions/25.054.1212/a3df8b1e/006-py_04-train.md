
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
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
1 0
0 1
```
size: True
palette: True
color count: True
pixels off: 20
**FAILED!**

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
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
1 0 1
0 1 0
```
size: True
palette: True
color count: False
pixels off: 25
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
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
0 1 0 1
```
size: True
palette: True
color count: False
pixels off: 30
**FAILED!**
