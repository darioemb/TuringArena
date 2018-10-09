# TuringArena
## Description:
Implementation of different kind of algorithm problems using TuringArena.
Each problems has different folders, one is called solutions containing the correct algorithm in c++, and another folder containing the text (testo.pdf) of the problems. 
Furthermore a file call **interface.txt** which refer to the function of the algorithm. The **the evaluator.py** written in python  controls the execution of the algorithm and if it is correct or not and give the time spent for its execution.

## List of problems:
The marked problems are the one with mutiple solutions.The others problem has one correct optimal solution and one wrong solution.
- [x] Poldo
- [x] Padella
- [ ] Luci
- [ ] Distributori
- [ ] Kfree
- [ ] Interrogazione

### How it works:
Enter the following command from terminal:
```bash
sudo turingarenad
```
Open another teriminal and enter the following command for the optimal solution:
```bash
turingarena evaluate solutions/correct.cpp
```
If someone wants to try a quadratic one:
```bash
turingarena evaluate solutions/correctquadratic.cpp
```
For a wrong solution:
```bash
turingarena evaluate solutions/wrong.cpp
```



