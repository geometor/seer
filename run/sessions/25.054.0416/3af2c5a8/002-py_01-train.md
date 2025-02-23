
## example 1
*input:*
```
0 0 8 0
0 8 0 8
0 0 8 0
```
*expected output:*
```
0 0 8 0 0 8 0 0
0 8 0 8 8 0 8 0
0 0 8 0 0 8 0 0
0 0 8 0 0 8 0 0
0 8 0 8 8 0 8 0
0 0 8 0 0 8 0 0
```
*transformed output:*
```
0 0 8 0 0 0 8 0
0 8 0 8 0 8 0 8
0 0 8 0 0 0 8 0
0 0 8 0 0 0 8 0
0 8 0 8 0 8 0 8
0 0 8 0 0 0 8 0
```
size: True
palette: True
color count: True
pixels off: 16
**FAILED!**

## example 2
*input:*
```
0 0 3 3
0 3 0 3
3 3 3 0
```
*expected output:*
```
0 0 3 3 3 3 0 0
0 3 0 3 3 0 3 0
3 3 3 0 0 3 3 3
3 3 3 0 0 3 3 3
0 3 0 3 3 0 3 0
0 0 3 3 3 3 0 0
```
*transformed output:*
```
0 0 3 3 0 0 3 3
0 3 0 3 0 3 0 3
3 3 3 0 3 3 3 0
0 0 3 3 0 0 3 3
0 3 0 3 0 3 0 3
3 3 3 0 3 3 3 0
```
size: True
palette: True
color count: True
pixels off: 22
**FAILED!**

## example 3
*input:*
```
3 3 3 3
3 0 0 0
3 0 0 0
```
*expected output:*
```
3 3 3 3 3 3 3 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 3 3 3 3 3 3 3
```
*transformed output:*
```
3 3 3 3 3 3 3 3
3 0 0 0 3 0 0 0
3 0 0 0 3 0 0 0
3 3 3 3 3 3 3 3
3 0 0 0 3 0 0 0
3 0 0 0 3 0 0 0
```
size: True
palette: True
color count: True
pixels off: 18
**FAILED!**
