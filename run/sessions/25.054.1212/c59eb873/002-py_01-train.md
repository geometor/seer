
## example 1
*input:*
```
0 5 1
5 5 5
2 5 0
```
*expected output:*
```
0 0 5 5 1 1
0 0 5 5 1 1
5 5 5 5 5 5
5 5 5 5 5 5
2 2 5 5 0 0
2 2 5 5 0 0
```
*transformed output:*
```
0 0 5 5 1 1
0 0 5 5 1 1
5 5 5 5 5 5
5 5 5 5 5 5
2 2 5 5 0 0
2 2 5 5 0 0
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
2 1
3 1
```
*expected output:*
```
2 2 1 1
2 2 1 1
3 3 1 1
3 3 1 1
```
*transformed output:*
```
2 2 1 1
2 2 1 1
3 3 1 1
3 3 1 1
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
2 0 3 0
2 1 3 0
0 0 3 3
0 0 3 5
```
*expected output:*
```
2 2 0 0 3 3 0 0
2 2 0 0 3 3 0 0
2 2 1 1 3 3 0 0
2 2 1 1 3 3 0 0
0 0 0 0 3 3 3 3
0 0 0 0 3 3 3 3
0 0 0 0 3 3 5 5
0 0 0 0 3 3 5 5
```
*transformed output:*
```
2 2 0 0 3 3 0 0
2 2 0 0 3 3 0 0
2 2 1 1 3 3 0 0
2 2 1 1 3 3 0 0
0 0 0 0 3 3 3 3
0 0 0 0 3 3 3 3
0 0 0 0 3 3 5 5
0 0 0 0 3 3 5 5
```
size: True
palette: True
color count: True
pixels off: 0
PASSED
