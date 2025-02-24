
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
2 2 2
2 2 2
1 1 1
1 1 1
4 4 4
4 4 4
```
size: True
palette: True
color count: True
pixels off: 12
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
3 3 3 3
3 3 3 3
2 2 2 2
2 2 2 2
1 1 1 1
1 1 1 1
4 4 4 4
4 4 4 4
```
size: True
palette: True
color count: True
pixels off: 24
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
8 8
8 8
3 3
3 3
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**
