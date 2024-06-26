# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
def conversion_damages(damages):
    conversion = {"M": 1000000, "B": 1000000000}

    updated_damages = list()
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damages.append(damage)
        if damage.find('M') != -1:
            updated_damages.append(float(damage[0:damage.find('M')]) * conversion['M'])
        if damage.find('B') != -1:
            updated_damages.append(float(damage[0:damage.find('B')]) * conversion['B'])
    return updated_damages
# test function by updating damages
updated_damages = conversion_damages(damages)
print(updated_damages)

# 2 
# Create a Table
# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 2
# Create a Table
def create_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
    hurricanes = dict()
    num_hurricanes = len(names)
    for i in range(num_hurricanes):
        hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Winds': max_sustained_winds[i], 'Areas Affected': areas_affected[i], 'Damages': damages[i], 'Deaths': deaths[i]}
    return hurricanes
# Create and view the hurricanes dictionary
hurricanes = create_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print(hurricanes)
# Create and view the hurricanes dictionary

# 3
# Organizing by Year
def sort_year(hurricanes):
    hurricanes_by_year = dict()
    for hurricane in hurricanes:
        current_year = hurricanes[hurricane]['Year']
        current_hurricane = hurricanes[hurricane]
        if current_year not in hurricanes_by_year:
            hurricanes_by_year[current_year] = [current_hurricane]
        else:
            hurricanes_by_year[current_year].append(current_hurricane)
    return hurricanes_by_year
# create a new dictionary of hurricanes with year and key
hurricanes_by_year = sort_year(hurricanes)
print(hurricanes_by_year[1932])

# 4
# Counting Damaged Areas
def count_areas(hurricanes):
    affected_areas = dict()
    for hurricane in hurricanes:
        for area in hurricanes[hurricane]['Areas Affected']:
            if area not in affected_areas:
                affected_areas[area] = 1
            else:
                affected_areas[area] += 1
    return affected_areas
# create dictionary of areas to store the number of hurricanes involved in
affected_areas = count_areas(hurricanes)
print(affected_areas)


# 5 
# Calculating Maximum Hurricane Count
def most_affected(affected_areas):
    max_area = 'Central America'
    max_area_count = 0
    for area in affected_areas:
        if affected_areas[area] > max_area_count:
            max_area = area
            max_area_count = affected_areas[area]
    return max_area, max_area_count
# find most frequently affected area and the number of hurricanes involved in
max_area, max_area_count = most_affected(affected_areas)
print(max_area, max_area_count)

# 6
# Calculating the Deadliest Hurricane
def most_deaths(hurricanes):
    max_deaths_hurricane = 'Cuba I'
    max_deaths = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Deaths'] > max_deaths:
            max_deaths_hurricane = hurricane
            max_deaths = hurricanes[hurricane]['Deaths']
    return max_deaths_hurricane, max_deaths
# find highest mortality hurricane and the number of deaths
max_deaths_hurricane, max_deaths = most_deaths(hurricanes)
print(max_deaths_hurricane, max_deaths)

# 7
# Rating Hurricanes by Mortality
def sort_deaths(hurricanes):
    death_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricanes_deaths = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricanes:
        deaths = hurricanes[hurricane]['Deaths']
        if deaths == death_scale[0]:
            hurricanes_deaths[0].append(hurricanes[hurricane])
        elif deaths > death_scale[0] and deaths <= death_scale[1]:
            hurricanes_deaths[1].append(hurricanes[hurricane])
        elif deaths > death_scale[1] and deaths <= death_scale[2]:
            hurricanes_deaths[2].append(hurricanes[hurricane])
        elif deaths > death_scale[2] and deaths <= death_scale[3]:
            hurricanes_deaths[3].append(hurricanes[hurricane])
        elif deaths > death_scale[3] and deaths <= death_scale[4]:
            hurricanes_deaths[4].append(hurricanes[hurricane])
        elif deaths > death_scale[4]:
            hurricanes_deaths[5].append(hurricanes[hurricane])
    return hurricanes_deaths   
# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_deaths = sort_deaths(hurricanes)
print(hurricanes_deaths[5])

# 8 Calculating Hurricane Maximum Damage
def max_damage(hurricanes):
    max_damage_hurricane = 'Cuba I'
    max_damage_num = 0
    for hurricane in hurricanes:
        if hurricanes[hurricane]['Damages'] == 'Damages not recorded':
            pass
        elif hurricanes[hurricane]['Damages'] > max_damage_num:
            max_damage_hurricane = hurricane
            max_damage_num = hurricanes[hurricane]['Damages']
    return max_damage_hurricane, max_damage_num
# find highest damage inducing hurricane and its total cost
max_damage_hurricane, max_damage_num = max_damage(hurricanes)
print(max_damage_hurricane, max_damage_num)   

# 9
# Rating Hurricanes by Damage
def sort_damage(hurricanes):
    damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}
    hurricanes_damage = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
    for hurricane in hurricanes:
        cost = hurricanes[hurricane]['Damages']
        if cost == 'Damages not recorded':
            hurricanes_damage[0].append(hurricanes[hurricane])
        elif cost == damage_scale[0]:
            hurricanes_damage[0].append(hurricanes[hurricane])
        elif cost > damage_scale[0] and cost <= damage_scale[1]:
            hurricanes_damage[1].append(hurricanes[hurricane])
        elif cost > damage_scale[1] and cost <= damage_scale[2]:
            hurricanes_damage[2].append(hurricanes[hurricane])
        elif cost > damage_scale[2] and cost <= damage_scale[3]:
            hurricanes_damage[3].append(hurricanes[hurricane])
        elif cost > damage_scale[3] and cost <= damage_scale[4]:
            hurricanes_damage[4].append(hurricanes[hurricane])
        elif cost > damage_scale[4]:
            hurricanes_damage[5].append(hurricanes[hurricane])
    return hurricanes_damage   
# categorize hurricanes in new dictionary with damage severity as key
hurricanes_damage = sort_damage(hurricanes)
print(hurricanes_damage[5])
