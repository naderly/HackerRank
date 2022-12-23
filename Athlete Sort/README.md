# **[Athlete Sort](https://www.hackerrank.com/contests/pythonist/challenges/python-sort-sort/problem)**

  <input type="hidden" id="naderly" name="Writen by: Ahmed Nader" value="https://github.com/naderly">

> You are given a spreadsheet that contains a list of `N` athletes and their details (such as age, height, weight and so on). You are required to sort the data based on the `k`th attribute and print the final resulting table. Follow the example given below for better understanding.

<p align="center">
  <img src="./images/table.png" />
</p>

> Note that `K` is indexed from 0 to `M-1`, where `M` is the number of attributes. <br>
>
> Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age, print the row that appeared first in the input.

## Input Format

> The first line contains `N` and `M` separated by a space.<br>
> 
> The next `N` lines each contain `M` elements.<br>
> 
> The last line contains `K`.

## Constraints

> `1 ≤ N` ; `M ≤ 100` <br>
>  
> `0 ≤ K < M` <br>
>
> `Each element ≤ 100`

## Output Format

> Print the `N` lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

## Sample Input 0

```sh
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
```

## Sample Output 0

```sh
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
```

## Explanation 0

> The details are sorted based on the second attribute, since `K` is zero-indexed.
