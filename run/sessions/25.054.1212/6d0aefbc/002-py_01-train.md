
## example 1
*input:*
```
6 6 6
1 6 1
8 8 6
```
*expected output:*
```
6 6 6 6 6 6
1 6 1 1 6 1
8 8 6 6 8 8
```
*transformed output:*
```
6 6 6 6 6 6
1 1 6 6 1 1
8 8 8 8 6 6
```
size: True
palette: True
color count: True
pixels off: 8
**FAILED!**

## example 2
*input:*
```
6 8 1
6 1 1
1 1 6
```
*expected output:*
```
6 8 1 1 8 6
6 1 1 1 1 6
1 1 6 6 1 1
```
*transformed output:*
```
6 6 8 8 1 1
6 6 1 1 1 1
1 1 1 1 6 6
```
size: True
palette: True
color count: True
pixels off: 11
**FAILED!**

## example 3
*input:*
```
1 1 1
8 1 6
6 8 8
```
*expected output:*
```
1 1 1 1 1 1
8 1 6 6 1 8
6 8 8 8 8 6
```
*transformed output:*
```
1 1 1 1 1 1
8 8 1 1 6 6
6 6 8 8 8 8
```
size: True
palette: True
color count: True
pixels off: 7
**FAILED!**

## example 4
*input:*
```
1 1 1
1 6 6
6 6 6
```
*expected output:*
```
1 1 1 1 1 1
1 6 6 6 6 1
6 6 6 6 6 6
```
*transformed output:*
```
1 1 1 1 1 1
1 1 6 6 6 6
6 6 6 6 6 6
```
size: True
palette: True
color count: True
pixels off: 2
**FAILED!**
