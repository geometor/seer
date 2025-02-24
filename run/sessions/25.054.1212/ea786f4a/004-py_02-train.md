
## example 1
*input:*
```
1 1 1
1 0 1
1 1 1
```
*expected output:*
```
0 1 0
1 0 1
0 1 0
```
*transformed output:*
```
1 0 1
0 1 0
1 0 1
```
size: True
palette: True
color count: False
pixels off: 9
**FAILED!**

## example 2
*input:*
```
2 2 2 2 2
2 2 2 2 2
2 2 0 2 2
2 2 2 2 2
2 2 2 2 2
```
*expected output:*
```
0 2 2 2 0
2 0 2 0 2
2 2 0 2 2
2 0 2 0 2
0 2 2 2 0
```
*transformed output:*
```
2 2 0 2 2
2 2 0 2 2
0 0 2 0 0
2 2 0 2 2
2 2 0 2 2
```
size: True
palette: True
color count: False
pixels off: 17
**FAILED!**

## example 3
*input:*
```
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 0 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
3 3 3 3 3 3 3
```
*expected output:*
```
0 3 3 3 3 3 0
3 0 3 3 3 0 3
3 3 0 3 0 3 3
3 3 3 0 3 3 3
3 3 0 3 0 3 3
3 0 3 3 3 0 3
0 3 3 3 3 3 0
```
*transformed output:*
```
3 3 3 0 3 3 3
3 3 3 0 3 3 3
3 3 3 0 3 3 3
0 0 0 3 0 0 0
3 3 3 0 3 3 3
3 3 3 0 3 3 3
3 3 3 0 3 3 3
```
size: True
palette: True
color count: False
pixels off: 25
**FAILED!**
