
## example 1
*input:*
```
0 0 5
0 5 0
5 0 0
```
*expected output:*
```
3 3 3
4 4 4
2 2 2
```
*transformed output:*
```
2 2 3
2 4 2
2 2 2
```
size: True
palette: True
color count: False
pixels off: 4
**FAILED!**

## example 2
*input:*
```
0 0 5
0 0 5
0 0 5
```
*expected output:*
```
3 3 3
3 3 3
3 3 3
```
*transformed output:*
```
3 3 3
3 3 3
3 3 3
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
5 0 0
0 5 0
5 0 0
```
*expected output:*
```
2 2 2
4 4 4
2 2 2
```
*transformed output:*
```
2 2 2
2 4 2
2 2 2
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**

## example 4
*input:*
```
0 5 0
0 0 5
0 5 0
```
*expected output:*
```
4 4 4
3 3 3
4 4 4
```
*transformed output:*
```
4 4 4
4 4 3
4 4 4
```
size: True
palette: True
color count: False
pixels off: 2
**FAILED!**
