def Return_index(Countries, Country):
    khali = []
    for i in range(len(Countries)):
        if Country == Countries[i]:
            khali.append(i)
    return (khali)


def Return_index1(Countrieslist, Country):
    for i in range(len(Countrieslist)):
        if Country == Countrieslist[i]:
            return (i)


def find_Avg_Without_Zero(CountryName):
    ss = 0
    suum = 0
    average = 0
    CountryData = agriDict[CountryName]
    for i in range(len(CountryData)):
        if CountryData[i] != 0:
            suum = suum + CountryData[i]
            ss += 1
            average = suum / ss
    return (average)


def Replace_zero_with_avg(AgriDict, Country):
    average = find_Avg_Without_Zero(Country)
    lst = agriDict[Country]
    for i in range(len(lst)):
        if lst[i] == 0:
            lst[i] = average
    return (lst)


def find_maximum(list):
    maximum = list[0]
    for i in range(len(list)):
        if maximum < list[i]:
            maximum = list[i]
    return (maximum)


def return_Index_max_in_list(myList):
    maximum = myList[0]
    max_Index = 0
    for i in range(len(myList)):
        if maximum < myList[i]:
            maximum = myList[i]
            max_Index = i
    return max_Index


def Sort_max_order(unSortedList):
    max_sortedList = []
    max_sortedIndices = []
    for i in range(len(unSortedList)):
        max_index = return_Index_max_in_list(unSortedList)
        max_sortedList.append(unSortedList[max_index])
        max_sortedIndices.append(max_index)
        unSortedList[max_index] = -999999999
    return max_sortedIndices, max_sortedList


def return_Index_Min_InList(myList):
    minimum = myList[0]
    minIndex = 0
    for i in range(len(myList)):
        if minimum > myList[i]:
            minimum = myList[i]
            minIndex = i
    return minIndex


def Sort_min_order(unSortedList):
    min_sorted_List = []
    min_sorted_Indices = []
    for i in range(len(unSortedList)):
        minIndex = return_Index_Min_InList(unSortedList)
        min_sorted_List.append(unSortedList[minIndex])
        min_sorted_Indices.append(minIndex)
        unSortedList[minIndex] = 10000
    return min_sorted_Indices, min_sorted_List


# print("\033[1;93m GIVE INPUT TWO TIMES ON BASIS OF PROFITABLE AND LOSSY INDICATORS. \n")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\MR\Downloads\Gapminder.csv')
myDataDict = {}
df = df.fillna(0)
columnNames = list(df.head(0))
myData = df.values
Countries = df.iloc[:, 0]
Countries = (list(Countries))
bb = set(Countries)
CountryName = sorted(list(bb))
number_of_countries = len(Countries)

agriDict = {}
Normalized_First = []
Normalized_Second = []
count = 0
New_column_Names = ['AgriculturalLand', 'DemocracyScore', 'Exports', 'GDPpercapita', 'Literacyrateyouthtotal',
                    'Taxrevenue', 'Tradebalance', 'IncomePerPerson', 'Imports', 'Inflation', 'Poverty',
                    'Populationdensity', 'Longtermunemploymentrate']
for k in range(len(New_column_Names)):
    for j in range(len(columnNames)):
        if (New_column_Names[k]) == (columnNames[j]):
            New_column_Names[k] = list(df.iloc[:, j])
            for i in range(len(CountryName)):
                data = []
                index = Return_index(Countries, CountryName[i])
                for s in range(len(index)):
                    data.append(New_column_Names[k][index[s]])
                agriDict[CountryName[i]] = data[:]
                # print(agriDict)

            new_Dict = {}
            for t in range(len(CountryName)):
                Data = (Replace_zero_with_avg(agriDict, CountryName[t]))
                new_Dict[CountryName[t]] = Data[:]
            # print(new_Dict)

            New_List = []
            for u in range(len(CountryName)):
                country_data = list(new_Dict[CountryName[u]])
                sum1 = 0
                counter = 1
                for v in range(len(country_data)):
                    sum1 = sum1 + country_data[v]
                    counter = counter + 1
                average = sum1 / counter
                # print(average)
                New_List.append(average)
            maximum = find_maximum(New_List)
            Normalized_Data = []
            for w in range(len(New_List)):
                new = New_List[w] / maximum
                Normalized_Data.append(new)
        # print(Normalized_Data)

    if count <= 7:
        Normalized_First.append(Normalized_Data)
    elif count > 7:
        Normalized_Second.append(Normalized_Data)
    count = count + 1

First_columns_sums = [sum(col) for col in zip(*Normalized_First)]
Columns_sum1 = list(First_columns_sums)
# print(Columns_sum1)
max_sorted_Indices, max_sorted_List = Sort_max_order(First_columns_sums)
# print(First_columns_sums)
Last_columns_sums = [sum(col) for col in zip(*Normalized_Second)]
Columns_sums2 = list(Last_columns_sums)
min_sorted_Indices, min_sorted_List = Sort_min_order(Last_columns_sums)

New_Names_1 = ['AgriculturalLand', 'DemocracyScore', 'Exports', 'GDPpercapita', 'Literacyrateyouthtotal', 'Taxrevenue',
               'Tradebalance', 'IncomePerPerson']
New_Names_2 = ['Imports', 'Inflation', 'Poverty', 'Populationdensity', 'Longtermunemploymentrate']
Input = int(input(
    '\033[1;93mEnter 1 to get Countries rank on the basis of" AgriculturalLand,Democracy,Exports,GDP,Literacy_rate_youth_total,Tax_Revenue,Trade_Balance,Income_per_person"'))
countries = ['India', 'Pakistan', 'Bangladesh', 'China', 'Cyprus', 'Singapore', 'Afghanistan', 'Denmark', 'Bhutan',
             'East Germany', 'Iran', 'Mexico']
Dict_1 = {}
if Input == 1:
    rank = 1
    z = 0
    for index in max_sorted_Indices[0:]:
        if max_sorted_List[z] != 0:
            print('Worlds Best Country Rank ', rank, ' goes to: ', CountryName[index], "with total Data of ",
                  max_sorted_List[z])
            rank += 1
        z += 1
    for n in range(len(New_Names_1)):
        for j in New_Names_1:
            for y in range(len(Normalized_First)):
                khali2 = []
                (Normalized_First[y])
                for i in range(len(countries)):
                    index1 = Return_index1(CountryName, countries[i])
                    khali2.append(Normalized_First[y][index1])
                Normalized_First.remove(Normalized_First[y])
                break
            Dict_1[(j)] = khali2
            New_Names_1.remove(j)
            break

    DataaFrame = pd.DataFrame(Dict_1)
    DataaFrame.insert(0, 'countries', countries)
    # print(DataaFrame)

    plt.rcParams['figure.facecolor'] = '#FFCC99'
    plt.rcParams['axes.facecolor'] = '#00FFFF'
    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["AgriculturalLand"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["AgriculturalLand"], '-o', color="#000000", linewidth=2)
    # plt.annotate("Pakistan's Agricultural Land",color="#CC0000",fontsize=22, xy=('Pakistan', 0.399), xytext=('China', 0.817),arrowprops=dict(facecolor='#CC0000', shrink=0.05))
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Agricultural Land", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["DemocracyScore"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["DemocracyScore"], '-o', color="#000000", linewidth=2)
    plt.annotate("Democracy Score Is Negative(-)", color="#CC0000", fontsize=18, xy=('Pakistan', 0.161),
                 xytext=('India', -0.878), arrowprops=dict(facecolor='#CC0000', shrink=0.05))
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Democracy Score", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["Exports"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["Exports"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Exports", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["GDPpercapita"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["GDPpercapita"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("GDP per Capita", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["Literacyrateyouthtotal"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["Literacyrateyouthtotal"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Literacy Rate Youth Total ", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["Taxrevenue"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["Taxrevenue"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Tax Revenue", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["Tradebalance"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["Tradebalance"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Trade Balance", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame["countries"], DataaFrame["IncomePerPerson"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame["countries"], DataaFrame["IncomePerPerson"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Income Per Person", fontsize=25)
    plt.show()
else:
    print('Invalid Input ')

Second_Input = int(input(
    '\033[1;96mEnter 2 to get Countries rank on the basis of " Imports, Inflation, poverty,Childern_per_Women, Population_Density,Longterm_un_employment "'))
if Second_Input == 2:
    rank = 1
    i = 0
    for index in min_sorted_Indices[0:]:
        if min_sorted_List[i] != 0:
            print('Worlds Best Country Rank ', rank, ' goes to: ', CountryName[index], "with total Data of ",
                  min_sorted_List[i])
            rank += 1
        i += 1
    Dict_2 = {}
    for n in range(len(New_Names_2)):
        for j in New_Names_2:
            for y in range(len(Normalized_Second)):
                khali2 = []
                # print(Normalized_Second[y])
                for i in range(len(countries)):
                    index1 = Return_index1(CountryName, countries[i])
                    khali2.append(Normalized_Second[y][index1])
                Normalized_Second.remove(Normalized_Second[y])
                break
            Dict_2[(j)] = khali2
            New_Names_2.remove(j)
            break

    DataaFrame2 = pd.DataFrame(Dict_2)
    DataaFrame2.insert(0, 'countries', countries)
    # print(DataaFrame2)
    plt.rcParams['figure.facecolor'] = '#FFCC99'
    plt.rcParams['axes.facecolor'] = '#00FFFF'
    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame2["countries"], DataaFrame2["Imports"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame2["countries"], DataaFrame2["Imports"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Imports", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame2["countries"], DataaFrame2["Inflation"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame2["countries"], DataaFrame2["Inflation"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Inflation", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame2["countries"], DataaFrame2["Poverty"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame2["countries"], DataaFrame2["Poverty"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Poverty", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame2["countries"], DataaFrame2["Longtermunemploymentrate"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame2["countries"], DataaFrame2["Longtermunemploymentrate"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Long-Term Unemployment Rate", fontsize=25)
    plt.show()

    plt.figure(figsize=(12, 5))
    plt.bar(DataaFrame2["countries"], DataaFrame2["Populationdensity"], color="#FF0000", width=0.1)
    plt.plot(DataaFrame2["countries"], DataaFrame2["Populationdensity"], '-o', color="#000000", linewidth=2)
    plt.xlabel("Countries", fontsize=22)
    plt.ylabel("Normalized Data", fontsize=22)
    plt.title("Population Density", fontsize=22)
    plt.show()
else:
    print('Invalid Input')