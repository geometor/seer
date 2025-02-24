
## example 1
*input:*
```
0 7 7 7 7 0 0 0 0 0
0 7 0 0 7 0 0 0 0 0
0 7 0 0 7 0 0 0 0 0
0 7 7 7 7 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 8 8 8 8 8 0 0
0 0 0 8 0 0 0 8 0 0
0 0 0 8 0 0 0 8 0 0
0 0 0 8 8 8 8 8 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
8 8
8 8
```
*transformed output:*
```
8 8 8 8 8
8 0 0 0 8
8 0 0 0 8
8 8 8 8 8
```
size: False
palette: False
color count: False
pixels off: None
**FAILED!**

## example 2
*input:*
```
6 6 6 6 6 0 0 0 0 0
6 0 0 0 6 0 0 0 0 0
6 0 0 0 6 0 0 0 0 0
6 6 6 6 6 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 7 7 7 7 7 7 0 0
0 0 7 0 0 0 0 7 0 0
0 0 7 0 0 0 0 7 0 0
0 0 7 7 7 7 7 7 0 0
0 0 0 0 0 0 0 0 0 0
```
*expected output:*
```
7 7
7 7
```
*transformed output:*
```

```
**ERROR**: Could not save image: 'NoneType' object has no attribute 'to_image'

## example 3
*input:*
```
0 4 4 4 4 4 4 0 0 0
0 4 0 0 0 0 4 0 0 0
0 4 0 0 0 0 4 0 0 0
0 4 0 0 0 0 4 0 0 0
0 4 0 0 0 0 4 0 0 0
0 4 0 0 0 0 4 0 0 0
0 4 4 4 4 4 4 0 0 0
0 0 0 0 0 0 0 2 2 2
0 0 0 0 0 0 0 2 0 2
0 0 0 0 0 0 0 2 2 2
```
*expected output:*
```
4 4
4 4
```
*transformed output:*
```

```
**ERROR**: Could not save image: 'NoneType' object has no attribute 'to_image'
