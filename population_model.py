'''
Created on Oct 22, 2016

@author: samanthahuff
'''
import math
import numpy

#DEFINE INPUTS TO MODEL

#age by year matrix of fishing mortalities for different projection scenarios
    #status quo, no reduction in fishing mortality after year 10
fishing_sq = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] for i in range(30)]
    #sq for 10 years, than 50% reduction in fishing mortality for every age class
fishing_50 = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] if i <= 10 else [0.251923077, 0.4275, 0.251538462, 0.120961538, 0.074615385, 0.061538462, 0.055769231, 0.052307692, 0.050961538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538, 0.053461538] for i in range(30)]
    #sq for 10 years, than 50% reduction in fishing mortality only for fish <= age 3
fishing_50_3 = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] if i <= 10 else [0.251923077, 0.4275, 0.251538462, 0.120961538, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] for i in range(30)]
    #sq for 10 years, than 50% reduction in fishing mortality only for fish <= age 6
fishing_50_6 = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] if i <= 10 else [0.251923077, 0.4275, 0.251538462, 0.120961538, 0.074615385, 0.061538462, 0.055769231, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] for i in range(30)]
    #sq for 10 years, than 70% reduction in fm of fish <=3, but with a concurrent increase in catch of fish >3 equal to the tonnage of 20% of the "savings" in fish <=3
fishing_50_3_6 = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] if i <= 10 else [0.151153846, 0.2565, 0.150923077, 0.072576923, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] for i in range(30)]
    #sq for 10 years, than 90% reduction in fishing mortality for every age class
fishing_90 = [[0.503846154, 0.855, 0.503076923, 0.241923077, 0.149230769, 0.123076923, 0.111538462, 0.104615385, 0.101923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077, 0.106923077] if i <= 10 else [0.050384615, 0.0855, 0.050307692, 0.024192308, 0.014923077, 0.012307692, 0.011153846, 0.010461538, 0.010192308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308, 0.010692308] for i in range(30)]

#probabilities of maturity at age for different spawning schedules
matcomKOTA=[0.02315826,0.031950026,0.043929385,0.060121342,0.081771051,0.110301897,0.14719174,0.193732656,0.25066405,0.317732624,0.393326909,0.47440076,0.556847102,0.636276271,0.708910949,0.772232992,0.825177236,0.867919562,0.901459754,0.927197261,0.946610579]
matsq = [0, 0, 0.2, 0.5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#DEFINE POPULATION MODEL
def model(mat, year, fishing, trials, z):
    # inputs to this model include:
    # mat: (list), a list of probability of maturity for each age class
    # year: (int), the number of years to run the model
    # fishing: (age x year matrix), fishing mortality for each age class for each year 
    # trials: (int), number of trials to run the model
    # z:(boolean), only used for the 50_3_6 projection to turn this projection on/off
    
    # set variables
    Linf = 254.41  # Linf=theoretical maximum age, obtained from stock assessment
    k = 0.1575  # growth coefficent, obtained from stock assessment 
    t0 = 0.5607  # theoretical age when length is equal to 0, stock assessment 
    a = 0.000017117  # used in age to weight eqn, stock assessment
    b = 3.0382  # used in age to weight eqn, stock assessment 
    h = 0.95  # steepness
    R0 = 18225  # unfished equilibrium recruitment (Table 1 Atika 2016);
    B0 = 767853  # unfished equilibrium spawning biomass (Table 1 Atika 2016);
    sig = 0.6  # standard deviation, stock assessment
    # Natual mortality used in stock assessment
    M = [1.6, 0.386, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
    
    # create empty lists to store length at age, weight at age, and fecundity at age
    lengths = []
    weights = []
    fecundities = []
    
    # SSB table keeps track of total SSB for each year each time the model is run, 
    # for example, there will be 1000 lists with 30 elements in each list, when the model
    # is run with 1000 trials and 30 years. Each element will be the total SSB for that year
    SSBtable = [[0 for j in range(year)] for n in range(trials)]
    
    # Btable is a year by age matrix that records number of fish for each trial for each year for each age
    # for example, there will be 30 rows with 20 columns, for 30 years and 20 age classes
    # the table will have 1000 copies, one for each trial
    Btable = [[[0 for j in range(21)] for i in range(year)] for n in range(trials)]


    for n in range(trials):
        for i in range(21):
            # calculate lengths at age, weights at age, fecundities at age
            lengths.append(Linf * (1 - math.exp(-k * (i + t0))))
            weights.append(a * (lengths[i]) ** b)
            fecundities.append(mat[i] * weights[i])
        
        # put unfished equilibrium as the starting age 0 population
        Btable[n][0][0] = R0
        
        # The SB table keeps track for one year, the spawning biomass for each age class 
        # The table will have 20 columns, one for each age class, and one row. 
        # The sum of SB for each year gets put into the SSB table
        SBtable = []
        
        # the first element in SBtable will be the number of age0 fish multipled by
        # the fecundity of age0 fish (i.e. 0)
        SBtable.append(Btable[n][0][0] * fecundities[0])
        
        # Rt is the expected recruitment in year t
        Rt = []
        
        # the following code initializes the first year in the model with no fishing mortality
        for i in range(1, 21):
            # calculate number at age from the previous age in the previous year, using natural mortality
            Btable[n][0][i] = Btable[n][0][i - 1] * math.exp(-M[i - 1])
            SBtable.append(Btable[n][0][i] * fecundities[i])
            # the last year is an accumulator year, and so it has special equations
            if i == 20:
                Btable[n][0][i] = (Btable[n][0][i - 1] * math.exp(-M[i - 1])) / (1 - math.exp(-M[i]))
                SBtable.append(Btable[n][0][i] * fecundities[i])
                
        # calculate spawning stock biomass for the first year
        SSBtable[n][0] = sum(SBtable)
        # expected recruitment calculated using beverton holt equations
        Rt.append((4 * h * R0 * SSBtable[n][0]) / (B0 * (1 - h) + SSBtable[n][0] * (5 * h - 1)))
        
        # for years after the first year...
        for x in range(1, year):  
            SBtable = []  # reset the SB table 
            for i in range(21):
                rollOver = 0  # this is only used for the 50_3_6 projection
                if i == 0:  # for age0 calculate realized recruitment from expected 
                    Btable[n][x][i] = Rt[x - 1] * math.exp((-(sig ** 2) / 2) + numpy.random.normal(0, 0.6))  # put realized recruitment as population of age 0 fish
                    SBtable.append(Btable[n][x][i] * fecundities[i]) 
                if z == True and i <= 3 and i >= 0:  # this is only used for the 50_3_6 projection
                    reduction = Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - fishing[x - 1][i - 1])
                    reduction = reduction * weights[i]
                    normal = Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - (fishing[x - 1][i - 1]) * (.5 / .3))
                    normal = normal * weights[i]
                    rollOver += reduction - normal
                if i >= 1and i < 20:  # for age classes greater than 0
                    if z == True and i > 3:  # this is only used for the 50_3_6 projection
                        Btable[n][x][i] = Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - fishing[x - 1][i - 1]) - (rollOver / (17 * weights[i]))
                        SBtable.append(Btable[n][x][i] * fecundities[i])
                    else:  # calculate numbers at age based on the previous age in the previous year
                        # using natural and fishing mortality 
                        Btable[n][x][i] = Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - fishing[x - 1][i - 1])
                        SBtable.append(Btable[n][x][i] * fecundities[i])
                elif i == 20:  # different equations for age 20, accumulator age
                    if z == True:  # this is only used for the 50_3_6 projection
                        Btable[n][x][20] = (Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - fishing[x - 1][i - 1]) + Btable[n][x - 1][i] * math.exp(-M[i] - fishing[x - 1][i])) - (rollOver / (17 * weights[i]))
                        SBtable.append(Btable[n][x][20] * fecundities[20])
                    else:
                        Btable[n][x][20] = Btable[n][x - 1][i - 1] * math.exp(-M[i - 1] - fishing[x - 1][i - 1]) + Btable[n][x - 1][i] * math.exp(-M[i] - fishing[x - 1][i])
                        SBtable.append(Btable[n][x][20] * fecundities[20])
            SSBtable[n][x] = sum(SBtable)  # enter the total SSB for this year into the SSBtable 
            Rt.append((4 * h * R0 * SSBtable[n][x]) / (B0 * (1 - h) + SSBtable[n][x] * (5 * h - 1)))  # calculate expected recruitment for the next year from the SSB 
    
    
    # VISUALIZING OUTPUTS
    
    #Graphing SSB over time...
    # SSB_kg stores the sum for all trials the total SSB (in kg) for that age class and the standard deviation    
    SSB_kg = []
    for y in range(year):
        # for each age class, go through each trial and add SSB to Blist
        Blist = []
        for n in range(trials):
            Blist.append(SSBtable[n][y])
            # calculate the mean SSB and std for all trials and add that to SSB_kg
            if n == (trials - 1):
                SSB_kg.append((numpy.mean(Blist), numpy.std(Blist)))
    
    # print SSB_kg
    # print the mean SSB for that age class, and the std
    print ('mean SSB and std SSB (kg)')
    for i in range(0, len(SSB_kg)):
        print (SSB_kg[i][0], SSB_kg[i][1])
    
    
    #Graphing %SSB by age...
    # SSB_age is similar to the Btable in that it is an age by year matrix for each trial
    # however each cell is equal to the SSB (instead of # of fish) of that age class in that year in that trial 

    SSB_age = [[[0 for j in range(21)]for i in range(year)] for n in range(trials)]
    # populate table by multiplying the Btable in every cell by fecundity 
    for n in range(trials):
        for y in range(year):
            for i in range(21):
                SSB_age[n][y][i] = (Btable[n][y][i] * fecundities[i])

    # for each age class, for every year in every trial calculate the % SSB of that age class by dividing by the total SSB for that year 
    # for the last year in the model (ie. 29) calculate the %SSB by age class

    for i in range(21):
        ageList = []  # stores SSB for a specific age class for all the trials
        for n in range(trials):
            ageList.append(SSB_age[n][29][i] / sum(SSB_age[n][29])) 
        # print mean and std SSB for specific age class
        print ("% SSB for age" + str(i), numpy.mean(ageList), numpy.std(ageList)) 
    
    
    #Graphing % of fish that make it to maturity...
    # to calculate the number of fish reaching maturity, for each row in the Btable, calculate the number of mature fish
    # divide this by total number of fish

    for y in range(1,year):
        Ylist = []
        for n in range(trials):
            mature = []
            for i in range(21):
                mature.append(Btable[n][y][i] * mat[i])
            Ylist.append((sum(mature) / sum(Btable[n][y-1])))
        print ("% that make it to maturity in year", y, numpy.mean(Ylist), numpy.std(Ylist))
    

if __name__ == "__main__":
#RUN model with status quo spawning schedule
     print('status quo spawning schedule/', 'fishing mortality: sq')
     model(matsq,30,fishing_sq,1000,False)
     print("\n",'status quo spawning schedule/', 'fishing mortality: 50')
     model(matsq,30,fishing_50,1000,False)
     print("\n",'status quo spawning schedule/', 'fishing mortality: 50_3')
     model(matsq,30,fishing_50_3,1000,False)
     print("\n",'status quo spawning schedule/', 'fishing mortality: 50_6')
     model(matsq,30,fishing_50_6,1000,False)
     print("\n",'status quo spawning schedule/', 'fishing mortality: 90')
     model(matsq,30,fishing_90,1000,False)
     print("\n",'status quo spawning schedule/', 'fishing mortality: 50_3_6')
     model(matsq,30,fishing_50_3_6,1000,True)
      
#RUN model with alternative spawning schedule
print ("\n",'alternative spawning schedule/', 'fishing mortality: sq')
model(matcomKOTA,30,fishing_sq,1000,False)
print ("\n",'alternative spawning schedule/','fishing mortality: 50')
model(matcomKOTA,30,fishing_50,1000,False)
print ("\n",'alternative spawning schedule/','fishing mortality: 50_3')
model(matcomKOTA,30,fishing_50_3,1000,False)
print ("\n",'alternative spawning schedule/','fishing mortality: 50_6')
model(matcomKOTA,30,fishing_50_6,1000,False)
print ("\n",'alternative spawning schedule/', 'fishing mortality: 90')
model(matcomKOTA,30,fishing_90,1000,False)
print ("\n",'alternative spawning schedule/','fishing mortality: 50_3_6')
model(matcomKOTA,30,fishing_50_3_6,1000,True)
