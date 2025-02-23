
## example 1
*input:*
```
1 1 3 2 1 1 3 2
1 1 3 3 1 1 3 3
3 3 1 1 3 3 1 1
2 3 1 1 2 3 1 1
```
*expected output:*
```
1 1 3 2
1 1 3 3
3 3 1 1
2 3 1 1
```
*transformed output:*
```
1 1 3 2
1 1 3 3
3 3 1 1
2 3 1 1
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 2
*input:*
```
4 4 4 4 4 4
6 4 8 6 4 8
6 6 8 6 6 8
```
*expected output:*
```
4 4 4
6 4 8
6 6 8
```
*transformed output:*
```
4 4 4
6 4 8
6 6 8
```
size: True
palette: True
color count: True
pixels off: 0
PASSED

## example 3
*input:*
```
2 3
3 2
4 4
2 3
3 2
4 4
```
*expected output:*
```
2 3
3 2
4 4
```
*transformed output:*
```
2
3
4
2
3
4
```
size: False
palette: True
color count: True
pixels off: None
**FAILED!**
