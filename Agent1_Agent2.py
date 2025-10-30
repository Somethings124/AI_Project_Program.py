import pandas as pd

#365 days = 365 trials
#Agent 1 probabilities will be hardcoded
#After everyday Agent 2 will update their history for Agent 1
    #Agent 2 at the end of the year will have a total of 365 data points
#Agent 2 will use that "history" set to improve their calculations as days progress


#Use season for probability.
#For example, if fall may have higher chance of getting a pumpkin spice
#If winter maybe a higher chance of hot beverage rather than cold
#If summer/spring higher chance of cold beverage
season = ["Summer", "Spring", "Winter", "Fall"]

#Colder weather = higher chance of choosing hot beverage
#Hotter weather = higher chance of choosing cold beverage
weather = ["Sunny", "Cloudy", "Rainy", "Snowy", "Windy"]

#Certain days agent may have preference
#Hardcode whatever probability we make up
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Menu for the solids
menu_solids = ["hashbrowns", "pancakes", "eggs", "oatmeal", "soup", "bagel", "toast", "burrito"  ]

#Menu for the liquids
menu_liquids = ["coffee", "milk", "water", "soda", "iced tea", "chai", "pumpkin spice", "latte", "hot chocolate"]

