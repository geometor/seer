
## example 1
*input:*
```
4 5 1 1 5 4 4 5 1
5 5 5 5 5 5 5 5 5
1 5 4 4 5 1 1 5 4
```
*expected output:*
```
4 5 1
5 5 5
1 5 4
```
*transformed output:*
```
1 5 4
5 5 5
4 5 1
```
size: True
palette: True
color count: True
pixels off: 4
**FAILED!**

## example 2
*input:*
```
2 0 0 1 2 0 0 1 2 0 0 1
4 2 1 4 4 2 1 4 4 2 1 4
4 1 2 4 4 1 2 4 4 1 2 4
1 0 0 2 1 0 0 2 1 0 0 2
```
*expected output:*
```
2 0 0 1
4 2 1 4
4 1 2 4
1 0 0 2
```
*transformed output:*
```
2 1 4
1 2 4
0 0 2
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
2 1 2 1 2 1
2 3 2 3 2 3
```
*expected output:*
```
2 1
2 3
```
*transformed output:*
```
2 1 2
2 3 2
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
