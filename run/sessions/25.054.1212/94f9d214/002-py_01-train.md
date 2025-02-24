
## example 1
*input:*
```
0 0 0 0
0 3 3 0
0 0 0 0
3 0 0 3
0 0 0 1
1 0 1 1
1 1 1 1
0 1 0 1
```
*expected output:*
```
2 2 2 0
0 0 0 0
0 0 0 0
0 0 2 0
```
*transformed output:*
```
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 2
```
size: True
palette: True
color count: False
pixels off: 5
**FAILED!**

## example 2
*input:*
```
3 3 3 3
0 3 3 0
0 0 3 3
3 0 0 0
0 0 0 1
0 0 0 1
0 1 0 0
1 0 0 1
```
*expected output:*
```
0 0 0 0
2 0 0 0
2 0 0 0
0 2 2 0
```
*transformed output:*
```
0
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 3
*input:*
```
0 3 3 0
0 3 0 3
0 0 3 0
3 3 3 3
1 1 1 1
1 1 0 0
1 1 0 0
0 1 1 0
```
*expected output:*
```
0 0 0 0
0 0 2 0
0 0 0 2
0 0 0 0
```
*transformed output:*
```
0 0 0
0 0 0
0 0 2
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**

## example 4
*input:*
```
3 3 3 3
3 0 0 0
3 0 3 3
3 3 0 3
1 1 1 0
0 1 1 1
1 0 1 1
0 1 1 1
```
*expected output:*
```
0 0 0 0
0 0 0 0
0 2 0 0
0 0 0 0
```
*transformed output:*
```
2
```
size: False
palette: True
color count: False
pixels off: None
**FAILED!**
