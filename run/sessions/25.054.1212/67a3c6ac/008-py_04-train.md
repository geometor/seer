
## example 1
*input:*
```
6 6 6 2
6 1 6 2
7 2 7 2
1 7 2 2
```
*expected output:*
```
2 6 6 6
2 6 1 6
2 7 2 7
2 2 7 1
```
*transformed output:*
```
6 6 7 1
6 1 2 7
6 6 7 2
2 2 2 2
```
size: True
palette: True
color count: True
pixels off: 13
**FAILED!**

## example 2
*input:*
```
7 7 7 6 6 6 2
6 7 1 1 7 7 1
7 7 2 1 2 6 6
2 2 7 7 7 2 2
7 2 7 1 2 7 2
6 6 6 2 2 1 1
6 2 6 6 6 6 6
```
*expected output:*
```
2 6 6 6 7 7 7
1 7 7 1 1 7 6
6 6 2 1 2 7 7
2 2 7 7 7 2 2
2 7 2 1 7 2 7
1 1 2 2 6 6 6
6 6 6 6 6 2 6
```
*transformed output:*
```
7 6 7 2 7 6 6
7 7 7 2 2 6 2
7 1 2 7 7 6 6
6 1 1 7 1 2 6
6 7 2 7 2 2 6
6 7 6 2 7 1 6
2 1 6 2 2 1 6
```
size: True
palette: True
color count: True
pixels off: 35
**FAILED!**

## example 3
*input:*
```
1 2 7 1 1 1
2 1 7 7 2 6
2 1 2 6 2 1
1 2 1 7 6 2
2 7 1 2 7 1
2 1 6 2 7 7
```
*expected output:*
```
1 1 1 7 2 1
6 2 7 7 1 2
1 2 6 2 1 2
2 6 7 1 2 1
1 7 2 1 7 2
7 7 2 6 1 2
```
*transformed output:*
```
1 2 2 1 2 2
2 1 1 2 7 1
7 7 2 1 1 6
1 7 6 7 2 2
1 2 2 6 7 7
1 6 1 2 1 7
```
size: True
palette: True
color count: True
pixels off: 28
**FAILED!**
