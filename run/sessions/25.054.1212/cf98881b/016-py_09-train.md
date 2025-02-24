
## example 1
*input:*
```
0 4 0 4 2 9 9 0 0 2 0 0 0 0
0 4 0 0 2 0 0 9 9 2 0 1 0 0
4 0 0 0 2 0 0 0 0 2 1 1 1 0
4 4 4 4 2 9 0 9 0 2 1 1 0 1
```
*expected output:*
```
9 4 0 4
0 4 9 9
4 1 1 0
4 4 4 4
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

## example 2
*input:*
```
4 4 4 4 2 9 0 9 0 2 0 0 0 1
4 4 0 0 2 9 9 0 0 2 1 0 0 0
4 0 4 4 2 0 0 0 9 2 0 1 0 1
0 0 0 0 2 0 0 9 0 2 1 0 1 0
```
*expected output:*
```
4 4 4 4
4 4 0 0
4 1 4 4
1 0 9 0
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

## example 3
*input:*
```
4 4 4 0 2 9 9 0 9 2 0 1 0 1
0 4 0 4 2 0 0 9 0 2 0 1 0 0
0 4 0 4 2 0 0 9 9 2 1 0 0 1
4 0 4 4 2 9 9 9 0 2 0 0 0 1
```
*expected output:*
```
4 4 4 9
0 4 9 4
1 4 9 4
4 9 4 4
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

## example 4
*input:*
```
0 0 0 4 2 0 0 0 9 2 0 0 0 0
4 4 0 4 2 9 0 9 0 2 0 0 0 0
4 0 4 4 2 0 9 9 0 2 1 1 0 1
0 4 4 4 2 0 9 0 0 2 1 1 1 1
```
*expected output:*
```
0 0 0 4
4 4 9 4
4 9 4 4
1 4 4 4
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()

## example 5
*input:*
```
4 0 4 0 2 0 0 0 0 2 0 0 0 1
4 4 4 4 2 0 0 0 9 2 1 1 0 0
0 4 4 4 2 0 9 9 0 2 1 1 0 1
0 4 4 0 2 0 0 9 0 2 0 1 0 1
```
*expected output:*
```
4 0 4 1
4 4 4 4
1 4 4 4
0 4 4 1
```
size: None
palette: None
color count: None
pixels off: None
**ERROR**: ERROR: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
