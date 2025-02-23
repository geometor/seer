
## example 1
*input:*
```
0 0 8 0
0 8 0 8
0 0 8 0
```
*expected output:*
```
0 0 8 0 0 8 0 0
0 8 0 8 8 0 8 0
0 0 8 0 0 8 0 0
0 0 8 0 0 8 0 0
0 8 0 8 8 0 8 0
0 0 8 0 0 8 0 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: could not broadcast input array from shape (4,) into shape (8,)

## example 2
*input:*
```
0 0 3 3
0 3 0 3
3 3 3 0
```
*expected output:*
```
0 0 3 3 3 3 0 0
0 3 0 3 3 0 3 0
3 3 3 0 0 3 3 3
3 3 3 0 0 3 3 3
0 3 0 3 3 0 3 0
0 0 3 3 3 3 0 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: could not broadcast input array from shape (4,) into shape (8,)

## example 3
*input:*
```
3 3 3 3
3 0 0 0
3 0 0 0
```
*expected output:*
```
3 3 3 3 3 3 3 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 0 0 0 0 0 0 3
3 3 3 3 3 3 3 3
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: could not broadcast input array from shape (4,) into shape (8,)
