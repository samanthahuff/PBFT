# PBFT

### Running the model with status quo spawning schedule and/or the alternative spawning schedule 
![ssb_kg_conservations_scenarios](https://user-images.githubusercontent.com/93396549/163519756-cccef58e-3658-457d-b2c5-9bda5fd81b0a.png)


1. Run the population model with status quo spawning schedule for the conservation scenarios listed in Table 1:
```
python3 population_model.py > output.txt

```
Table 1. Different conservation scenarios projected in the model.
![image](https://user-images.githubusercontent.com/93396549/163491429-1b6c04ec-dbe2-4bf9-b12f-d6fdbdadf259.png)


2. To run the model with the alternative schedule, comment the status quo command and uncomment the following command from population_model.py:

```
model(matcomKOTA,30,all_fishing,name_all_fishing,1000)
```

![ssb_kg_conservations_scenarios2](https://user-images.githubusercontent.com/93396549/163520073-d8678b8c-8a6b-481e-9965-dee653fa7936.png)



### Changing model inputs

The model takes the following inputs that can be modified: 
```
def model(mat, year, all_fishing, name_all_fishing, trials):
    # inputs to this model include:
    # mat: (list), a list of probability of maturity for each age class
    # year: (int), the number of years to run the model
    # all_fishing: list of age x year matrices of fishing mortality for each age class for each year, for each scenario
    # name_all_fishing: name of fishing 
    # trials: (int), number of trials to run the model
```
To simulate different spawning schedules, create a list of probability of maturities for each age class. 
To simulate different conservation scenarios, create a nested list with age x year matrices for each age class for each year for each scenario. 




