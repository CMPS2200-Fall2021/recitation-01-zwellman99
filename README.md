# CMPS 2200  Recitation 01

**Name (Team Member 1):**_________________________  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Login to Github.
- Click on the assignment link sent through canvas and accept the assignment.
- Click on your personal github repository for the assignment (e.g., https://github.com/tulane-cmps2200/recitation-01-your_username).
- [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) the repository to your local device
- Complete the lab task
- [Add, commit, and push](https://docs.github.com/en/github/managing-files-in-a-repository/managing-files-using-the-command-line/adding-a-file-to-a-repository-using-the-command-line) your completed lab back up to GitHub.
  - You will need to issue `git add` for all files that you have modified, e.g., `main.py`, `README.md`, and any others that you modify as well.
  - For example, on the command line, in the same directory as your cloned lab:
```
$ git add main.py
$ git commit -m "Implement Required Functions"
$ git push origin main
```

You'll work with a partner to complete this recitation. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.

## Turning in your work
- Only one team member needs to push your completed lab to github.
- In the README.md file, include the name of the team members.


## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`.

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`?


**TODO: The worst case input value would be if the value doesn't exist in the**
**array or list. This is because the search would go through the entire list**
**before returning -1.**

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`?

**TODO: The best case input value for the linear search would be if the key is**
**in the first index in the list or array (mylist[0]). In binary search the**
**best case would be if the key is in the middle index value because the search**
**first splits the array in half and looks at the center index value.**

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

**TODO: add your timing results here**
|        n |   linear |   binary |
|----------|----------|----------|
|       10 |    0.003 |    0.004 |
|      100 |    0.006 |    0.006 |
|     1000 |    0.062 |    0.005 |
|    10000 |    0.626 |    0.013 |
|   100000 |   10.924 |    0.021 |
|  1000000 |   79.074 |    0.042 |
| 10000000 | 1266.221 |    0.052 |


- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

**TODO: They do match the run times because for linear search the run times increase in a linear fashion. O(n) is supposed**
**to increase in a linear fashion as the function continues to run. Binary search also matches because O(log_2(n)) would be**
**an only slight increase in run times as the size of the list increases.**

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times.
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search?
  **TODO: For linear search, worst case is go through whole thing and not find it**
  **so it would be O(n)*k.**

  + For binary search? **TODO: For binary search, it's theta(n^2)+[k*O(log_2(n))]**
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? **TODO: k < -n^2 / (log_2(n) - n)**
