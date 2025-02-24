
## example 1
*input:*
```
2 1 4
5 5 5
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
0 0 0
```
*expected output:*
```
2 1 4
5 5 5
2 2 2
1 1 1
4 4 4
2 2 2
1 1 1
4 4 4
```
*transformed output:*
```
2 1 4
5 5 5
2 1 4
5 5 5
2 1 4
5 5 5
2 1 4
5 5 5
```
size: True
palette: True
color count: False
pixels off: 15
**FAILED!**

## example 2
*input:*
```
3 2 1 4
5 5 5 5
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
```
*expected output:*
```
3 2 1 4
5 5 5 5
3 3 3 3
2 2 2 2
1 1 1 1
4 4 4 4
3 3 3 3
2 2 2 2
1 1 1 1
4 4 4 4
```
*transformed output:*
```
3 2 1 4
5 5 5 5
3 2 1 4
5 5 5 5
3 2 1 4
5 5 5 5
3 2 1 4
5 5 5 5
3 2 1 4
5 5 5 5
```
size: True
palette: True
color count: False
pixels off: 28
**FAILED!**

## example 3
*input:*
```
8 3
5 5
0 0
0 0
0 0
0 0
```
*expected output:*
```
8 3
5 5
8 8
3 3
8 8
3 3
```
*transformed output:*
```
8 3
5 5
8 3
5 5
8 3
5 5
```
size: True
palette: True
color count: False
pixels off: 6
**FAILED!**
