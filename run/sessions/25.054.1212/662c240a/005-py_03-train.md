
## example 1
*input:*
```
8 9 8
9 8 8
8 8 8
2 2 1
2 2 1
1 1 2
4 4 4
4 4 3
3 3 3
```
*expected output:*
```
4 4 4
4 4 3
3 3 3
```
*transformed output:*
```
8 9 8
9 8 8
8 8 8
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
1 5 5
5 1 1
5 1 1
3 3 3
3 6 3
3 6 6
7 7 7
7 2 2
7 2 2
```
*expected output:*
```
3 3 3
3 6 3
3 6 6
```
*transformed output:*
```
5 1 1
3 3 3
3 6 3
```
size: True
palette: False
color count: False
pixels off: 5
**FAILED!**

## example 3
*input:*
```
2 2 2
2 2 3
2 3 3
5 7 7
7 5 5
7 5 5
8 8 1
1 8 1
1 8 1
```
*expected output:*
```
8 8 1
1 8 1
1 8 1
```
*transformed output:*
```
2 2 2
2 2 3
2 3 3
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**

## example 4
*input:*
```
8 8 4
4 4 4
4 4 8
1 1 3
1 3 3
3 3 1
6 2 2
2 2 2
2 2 6
```
*expected output:*
```
8 8 4
4 4 4
4 4 8
```
*transformed output:*
```
6 2 2
2 2 2
2 2 6
```
size: True
palette: False
color count: False
pixels off: 9
**FAILED!**
