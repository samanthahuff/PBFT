# PBFT

To run the population model with status quo spawning schedule as well as the alternative spawning schedule :
```
python3 population_model.py > output.txt

```
To simulate different spawning schedules, create a list of probability of maturities for each age class 

```
def model(mat, year, fishing, trials, z):
    # inputs to this model include:
    # mat: (list), a list of probability of maturity for each age class
    # year: (int), the number of years to run the model
    # fishing: (age x year matrix), fishing mortality for each age class for each year 
    # trials: (int), number of trials to run the model
    # z:(boolean), only used for the 50_3_6 projection to turn this projection on/off
```


Conservation scenarios

Table 1. Different conservation scenarios projected in the model.
![image](https://user-images.githubusercontent.com/93396549/163491429-1b6c04ec-dbe2-4bf9-b12f-d6fdbdadf259.png)


pip install pyqt5
