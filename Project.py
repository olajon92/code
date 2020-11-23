import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

# Reads in csv file and splits data into separate series
Data = pd.read_csv('District presidential election data.csv')
Dem = Data.clinton
Rep = Data.trump
Ind = Data.johnson + Data.stein + Data.other
State = Data.state
District = Data.jurisdiction

# Creates a dataframe only including the series that we need. We started by only including then state columns then
# inserting the other part affiliation columns
Df = pd.DataFrame(State)
Df.columns = ['State']
Df.insert(1, 'Democrat', Dem)
Df.insert(2, 'Republican', Rep)
Df.insert(3, 'Independent', Ind)
del Df['State']


# print(Df[0:5])

# This function is for adding up the columns for each state's dataframe. Since the data is split by district we added
# all the columns in order to get the total state votes for each party. We then calculate the percentage by adding
# all the party votes together and dividing each party total by that state total in order to get a percentage.
def sum(state):
    State_sum = state.sum(axis=0)
    Dem_per = round(((state['Democrat'] / State_sum) * 100), 2)
    Rep_per = round(((state['Republican'] / State_sum) * 100), 2)
    Ind_per = round(((state['Independent'] / State_sum) * 100), 2)
    print('% of voting population that voted Democrats:', Dem_per, '%')
    print('% of voting population that voted Republican:', Rep_per, '%')
    print('% of voting population that voted Independent:', Ind_per, '%')


# This function tallies up the district votes in each state
def count(state):
    Dem_count_state = np.where(state['Democrat'] > state['Republican'])
    Dem_count_state = np.count_nonzero(Dem_count_state)
    Rep_count_state = np.where(state['Democrat'] < state['Republican'])
    Rep_count_state = np.count_nonzero(Rep_count_state)
    print('Democrats', Dem_count_state, 'districts\nRepublicans', Rep_count_state, 'districts')
    state_sum = state.sum(axis=0)
    sum(state_sum)
    if Dem_count_state > Rep_count_state:
        print('Democrats won\n')
    else:
        print('Republicans won\n')


# This function sums up the total votes in each states and compares that to the population of thus state, showing the
# percentage of voters in each state.
def voting_pop(state, pop):
    state = state.sum(axis=0)
    state_sum = state.sum(axis=0)
    percentage = round(((state_sum / pop) * 100), 2)
    print(percentage, '% of the population voted')


# In thi section we split the dataframe by state and then applied each function above.
AK = Df.iloc[:41]
print('ALASKA:')
voting_pop(AK, 741894)
count(AK)
AL = Df.iloc[42:109]
print('ALABAMA:')
voting_pop(AL, 4863300)
count(AL)
AR = Df.iloc[109:184]
print('ARKANSAS:')
voting_pop(AR, 6931071)
count(AR)
AZ = Df.iloc[184:199]
print('ARIZONA:')
voting_pop(AZ, 6931071)
count(AZ)
CA = Df.iloc[199:257]
print('CALIFORNIA:')
voting_pop(CA, 39250017)
count(CA)
CO = Df.iloc[257:321]
print('COLORADO:')
voting_pop(CO, 5540545)
count(CO)
CT = Df.iloc[321:490]
print('CONNECTICUT:')
voting_pop(CT, 3576452)
count(CT)
DC = Df.iloc[490:498]
print('WASHINGTON D.C:')
voting_pop(DC, 659009)
count(DC)
DE = Df.iloc[498:501]
print('DELAWARE:')
voting_pop(DE, 952065)
count(DE)
FL = Df.iloc[501:568]
print('FLORIDA:')
voting_pop(FL, 20612439)
count(FL)
GA = Df.iloc[568:727]
print('GEORGIA:')
voting_pop(GA, 10310371)
count(GA)
HI = Df.iloc[727:731]
print('HAWAII:')
voting_pop(HI, 1428557)
count(HI)
IA = Df.iloc[731:830]
print('IOWA:')
voting_pop(IA, 3134693)
count(IA)
ID = Df.iloc[830:874]
print('IDAHO:')
voting_pop(ID, 1683140)
count(ID)
IL = Df.iloc[874:976]
print('ILLINOIS:')
voting_pop(IL, 12801539)
count(IL)
IN = Df.iloc[976:1068]
print('INDIANA:')
voting_pop(IN, 6633053)
count(ID)
KS = Df.iloc[1067]
print('KANSAS:')
KS_sum = KS.sum(axis=0)
KS_percentage = round(((KS_sum / 2907289) * 100), 2)
print(KS_percentage, '% of the population voted')
KS_dem_per = round(((KS['Democrat'] / KS_sum) * 100), 2)
KS_rep_per = round(((KS['Republican'] / KS_sum) * 100), 2)
KS_Ind_per = round(((KS['Independent'] / KS_sum) * 100), 2)
print('% of voting population that voted Democrats:', KS_dem_per, '%')
print('% of voting population that voted Republican:', KS_rep_per, '%')
print('% of voting population that voted Independent:', KS_Ind_per, '%\n')
KY = Df.iloc[1068:1189]
print('KENTUCKY:')
voting_pop(KY, 4436974)
count(KY)
LA = Df.iloc[1189:1253]
print('LOUISIANA:')
voting_pop(LA, 4681666)
count(LA)
MA = Df.iloc[1253:1604]
print('MASSACHUSETTS:')
voting_pop(MA, 6811779)
count(MA)
MD = Df.iloc[1604:1628]
print('MARYLAND:')
voting_pop(MD, 6016447)
count(MD)
ME = Df.iloc[1628:2161]
print('MAINE:')
voting_pop(ME, 1331479)
count(ME)
MI = Df.iloc[2161:2244]
print('MICHIGAN:')
voting_pop(MI, 9928300)
count(MI)
MN = Df.iloc[2244:2331]
print('MINNESOTA:')
voting_pop(MN, 5519952)
count(MN)
MO = Df.iloc[2331:2447]
print('MISSOURI:')
voting_pop(MO, 6093000)
count(MO)
MS = Df.iloc[2446]
print('MISSISSIPPI:')
MS_sum = MS.sum(axis=0)
MS_percentage = round(((MS_sum / 2988726) * 100), 2)
print(MS_percentage, '% of the population voted')
MS_dem_per = round(((KS['Democrat'] / MS_sum) * 100), 2)
MS_rep_per = round(((KS['Republican'] / MS_sum) * 100), 2)
MS_Ind_per = round(((KS['Independent'] / MS_sum) * 100), 2)
print('% of voting population that voted Democrats:', MS_dem_per, '%')
print('% of voting population that voted Republican:', MS_rep_per, '%')
print('% of voting population that voted Independent:', MS_Ind_per, '%\n')
MT = Df.iloc[2447:2504]
print('MONTANA:')
voting_pop(MT, 1042520)
count(MT)
NC = Df.iloc[2504:2604]
print('NORTH CAROLINA:')
voting_pop(NC, 10146788)
count(NC)
ND = Df.iloc[2604:2657]
print('NORTH DAKOTA:')
voting_pop(ND, 757952)
count(ND)
NE = Df.iloc[2657:2750]
print('NEBRASKA:')
voting_pop(NE, 1907116)
count(NE)
NH = Df.iloc[2750:3052]
print('NEW HAMPSHIRE:')
voting_pop(NH, 1334795)
count(NH)
NJ = Df.iloc[3052:3073]
print('NEW JERSEY:')
voting_pop(NJ, 8944469)
count(NJ)
NM = Df.iloc[3073:3106]
print('NEW MEXICO:')
voting_pop(NM, 2081015)
count(NM)
NV = Df.iloc[3106:3123]
print('NEVADA:')
voting_pop(NV, 2940058)
count(NV)
NY = Df.iloc[3123:3185]
print('NEW YORK:')
voting_pop(NY, 19745289)
count(NY)
OH = Df.iloc[3185:3273]
print('OHIO:')
voting_pop(OH, 11614373)
count(OH)
OK = Df.iloc[3273:3350]
print('OKLAHOMA:')
voting_pop(OK, 3923561)
count(OK)
OR = Df.iloc[3350:3386]
print('OREGON:')
voting_pop(OR, 4093465)
count(OR)
PA = Df.iloc[3386:3453]
print('PENNSYLVANIA:')
voting_pop(PA, 12784227)
count(PA)
RI = Df.iloc[3453:3492]
print('RHODE ISLAND:')
voting_pop(RI, 1056426)
count(RI)
SC = Df.iloc[3492:3538]
print('South Carolina:')
voting_pop(SC, 4961119)
count(SC)
SD = Df.iloc[3538:3604]
print('SOUTH DAKOTA:')
voting_pop(SD, 865454)
count(SD)
TN = Df.iloc[3604:3699]
print('TENNESSEE:')
voting_pop(TN, 6651194)
count(TN)
TX = Df.iloc[3699:3953]
print('TEXAS:')
voting_pop(TX, 27862596)
count(TX)
UT = Df.iloc[3953:3982]
print('UTAH:')
voting_pop(UT, 3051217)
count(UT)
VA = Df.iloc[3982:4115]
print('VIRGINIA:')
voting_pop(VA, 8411808)
count(VA)
VT = Df.iloc[4115:4361]
print('VERMONT:')
voting_pop(VT, 624594)
count(VT)
WA = Df.iloc[4361:4400]
print('WASHINGTON:')
voting_pop(WA, 7288000)
count(WA)
WI = Df.iloc[4400:4472]
print('WISCONSIN:')
voting_pop(WI, 5778708)
count(WI)
WV = Df.iloc[4472:4527]
print('WEST VIRGINIA:')
voting_pop(WV, 1831102)
count(WV)
WY = Df.iloc[4527:4550]
print('WYOMING:')
voting_pop(WY, 585501)
count(WY)

# In this section, we summed up the votes from each state and used that to calculate the national election results.
print('UNITED STATES:')
Df_sum = Df.sum(axis=0)
Df_sum2 = Df_sum.sum(axis=0)
Df_percentage = round(((Df_sum2 / 323127513) * 100), 2)
Df_novote = 100 - Df_percentage
print(Df_percentage, '% of the U.S. population voted')
Df_dem_per = round(((Df_sum['Democrat'] / Df_sum2) * 100), 2)
Df_rep_per = round(((Df_sum['Republican'] / Df_sum2) * 100), 2)
Df_Ind_per = round(((Df_sum['Independent'] / Df_sum2) * 100), 2)
print('% of voting U.S. population that voted Democrats:', Df_dem_per, '%')
print('% of voting U.S. population that voted Republican:', Df_rep_per, '%')
print('% of voting U.S. population that voted Independent:', Df_Ind_per, '%\n')

# In this section we plotted the 2016 election result showing the percentage of votes each party accumulation nationally
fig = plt.figure()
ax = fig.add_axes([0, 0, 1, 1])
Parties = ['Democrats', 'Republicans', 'Independents']
Per = [Df_dem_per, Df_rep_per, Df_Ind_per]
colors = ['blue', 'red', 'yellow']
ax.pie(Per, labels=Parties, autopct='%1.2f%%', colors=colors)
ax.set_title('2016 election results by Popular Vote')
plt.show()
