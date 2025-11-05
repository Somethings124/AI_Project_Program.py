import random
import numpy as np


#365 days = 365 trials
#Agent 1 probabilities will be hardcoded
#After everyday Agent 2 will update their history for Agent 1
    #Agent 2 at the end of the year will have a total of 365 data points
#Agent 2 will use that "history" set to improve their calculations as days progress


#Use season for probabilit y.
#For example, if fall may have higher chance of getting a pumpkin spice
#If winter maybe a higher chance of hot beverage rather than cold
#If summer/spring higher chance of cold beverage
seasons = ["summer", "spring", "winter", "fall"]

#Colder weather = higher chance of choosing hot beverage
#Hotter weather = higher chance of choosing cold beverage
weather = ["sunny", "cloudy", "rainy", "snowy", "windy"]

#Certain days agent may have preference
#Hardcode whatever probability we make up

num_days = 365

count = 0

days = {"Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"}

#Menu for the solids
menu_solids = ["hashbrowns" , "pancakes", "eggs", "oatmeal" , "soup" , "bagel" , "toast" , "burrito"]

#Menu for the liquids
menu_liquids = ["coffee", "water" , "soda" , "iced tea", "chai", "pumpkin spice", "latte",  "hot chocolate"]


#Menu for Agent2 #Agent2 knows nothing of agent1 so each food has equal probability
agent2_menu_solids = {"sunny": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.1 , "soup": 0.1, "bagel": 0.1, "toast": 0.1 , "burrito": 0.1 },
                             "cloudy": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.1 , "soup": 0.1, "bagel": 0.1, "toast": 0.1 , "burrito": 0.1},
                             "rainy": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.1 , "soup": 0.1, "bagel": 0.1, "toast": 0.1 , "burrito": 0.1 },
                             "snowy": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.1 , "soup": 0.1, "bagel": 0.1, "toast": 0.1 , "burrito": 0.1 },
                             "windy": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.1 , "soup": 0.1, "bagel": 0.1, "toast": 0.1 , "burrito": 0.1 }
                             }

agent2_menu_liquids = {"sunny": {"coffee": 0.1, "water": 0.1, "soda": 0.1, "iced_tea": 0.1, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1},
                              "cloudy": {"coffee": 0.1, "water": 0.1, "soda": 0.1, "iced_tea": 0.1, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1},
                              "rainy": {"coffee": 0.1, "water": 0.1, "soda": 0.1, "iced_tea": 0.1, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1},
                              "snowy": {"coffee": 0.1, "water": 0.1, "soda": 0.1, "iced_tea": 0.1, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1},
                              "windy": {"coffee": 0.1, "water": 0.1, "soda": 0.1, "iced_tea": 0.1, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1}

}




agent2_stored_agent1 = {"sunny": {"right": 0, "wrong": 0},
                        "cloudy": {"right": 0, "wrong": 0},
                        "rainy": {"right": 0, "wrong": 0},
                        "snowy": {"right": 0, "wrong": 0},
                        "windy": {"right": 0, "wrong": 0}}


#Given the season, the temperature will either be hot or cold
agent1_season ={
    "spring": {"hot": 0.7, "cold": 0.3},
    "summer": {"hot": 0.9, "cold":0.1},
    "fall": {"hot": 0.4, "cold": 0.6},
    "winter": {"hot": 0.1, "cold": 0.9}
}

#Given hot or cold, the weather will vary based on probability/weights
agent1_weather = {
    "hot": {"sunny": 0.6, "cloudy": 0.2, "rainy": 0.1, "snowy": 0.0, "windy": 0.1},
    "cold": {"sunny": 0.2, "cloudy": 0.2, "rainy": 0.1, "snowy": 0.3, "windy": 0.2}

}

agent1_food_choice_solids = {"sunny": {"hashbrowns": 0.3 , "pancakes":0.1, "eggs": 0.3, "oatmeal": 0.0 , "soup": 0.0, "bagel": 0.3, "toast": 0.1 , "burrito": 0 },
                             "cloudy": {"hashbrowns": 0.1 , "pancakes":0.3, "eggs": 0.1, "oatmeal": 0.2 , "soup": 0.2, "bagel": 0.0, "toast": 0.1 , "burrito": 0 },
                             "rainy": {"hashbrowns": 0.1 , "pancakes":0.1, "eggs": 0.1, "oatmeal": 0.2 , "soup": 0.3, "bagel": 0.0, "toast": 0.1 , "burrito": 0.1 },
                             "snowy": {"hashbrowns": 0 , "pancakes":0, "eggs": 0, "oatmeal": 0.3 , "soup": 0.4, "bagel": 0, "toast": 0.1 , "burrito": 0.2 },
                             "windy": {"hashbrowns": 0.1 , "pancakes":0.3, "eggs": 0.2, "oatmeal": 0.0 , "soup": 0.2, "bagel": 0.1, "toast": 0 , "burrito": 0.1 }
                             }

agent1_food_choice_liquids = {"sunny": {"coffee": 0.5, "water": 0.1, "soda": 0.2, "iced_tea": 0.2, "chai": 0.0, "pumpkin_spice": 0.0, "latte": 0.0, "hot_chocolate": 0.0},
                              "cloudy": {"coffee": 0.2, "water": 0, "soda": 0.1, "iced_tea": 0, "chai": 0.2, "pumpkin_spice": 0.1, "latte": 0.2, "hot_chocolate": 0.2},
                              "rainy": {"coffee": 0.5, "water": 0, "soda": 0.1, "iced_tea": 0, "chai": 0.1, "pumpkin_spice": 0.1, "latte": 0.1, "hot_chocolate": 0.1},
                              "snowy": {"coffee": 0.1,"water": 0, "soda": 0, "iced_tea": 0, "chai": 0.4, "pumpkin_spice": 0.2, "latte": 0.2, "hot_chocolate": 0.2},
                              "windy": {"coffee": 0.2, "water": 0.1, "soda": 0.2, "iced_tea": 0, "chai": 0.0, "pumpkin_spice": 0.0, "latte": 0.3, "hot_chocolate": 0.2}

}





#Begin the trial
year = 0


for i in range(1, 20):
    year+= 1
    correct_predictions_solids = 0
    correct_predictions_liquids = 0
    for days in range(1, num_days+1):
        # Days are separated by their corresponding season based around the year
        current_day = days
        if current_day < 90:
            season = "spring"
        elif current_day < 180:
            season = "summer"
        elif current_day < 270:
            season = "fall"
        else:
            season = "winter"

        # Choose the dictionary for the corresponding temperature
        # Example: if season = "spring" then season_weather_choices = {"hot": 0.7, "cold": 0.3}
        season_temperature_choices = agent1_season[season]

        # Chooses either "hot" or "cold" based on the probability given for these two words
        chosen_season_temperature = \
            random.choices(list(season_temperature_choices.keys()), weights=list(season_temperature_choices.values()))[0]

        # Choose the dictionary for the corresponding weather
        # Example: if chosen_season_temperature = hot, then {"sunny": 0.6, "cloudy": 0.2, "rainy": 0.1, "snowy": 0.0, "windy": 0.1}
        choose_weather = agent1_weather[chosen_season_temperature]

        # Choose the weather based on the probability for hot or cold
        chosen_temperature = random.choices(list(choose_weather.keys()), weights=list(choose_weather.values()))[0]

        # Choose the dictionary for the corresponding food based on the weather
        choose_solid_food = agent1_food_choice_solids[chosen_temperature]


        #--------------------------------------------------
        # Pick the food from the solids list
        agent1_solid_food_choice = \
            random.choices(list(choose_solid_food.keys()), weights=list(choose_solid_food.values()))[0]

        # Choose the dictionary for the corresponding liquid based on the weather
        choose_liquid_food = agent1_food_choice_liquids[chosen_temperature]

        # Pick the liquid from the liquid list
        agent1_liquid_food_choice = \
            random.choices(list(choose_liquid_food.keys()), weights=list(choose_liquid_food.values()))[0]

        #-------------------------------------------------------



        # Agent2 guessing
        #-----------------------------------------------------


        # Agent2 will use what the current weather is (sunny, windy, etc) and guess from that list
        agent2_guess_solids = random.choices(list(agent2_menu_solids[chosen_temperature].keys()), weights = list(agent2_menu_solids[chosen_temperature].values()))[0]
        agent2_guess_liquids = random.choices(list(agent2_menu_liquids[chosen_temperature].keys()), weights = list(agent2_menu_liquids[chosen_temperature].values()))[0]


        #If correct then reward Agent2 and increase that items probability for sunny, windy, etc
        #If not correct then decrease the probability of that food item being chosen for sunny, windy, etc
        if agent2_guess_solids == agent1_solid_food_choice:
            correct_predictions_solids += 1
            increased_probability_solid = 0.12
        else:
            increased_probability_solid = -0.005

        if agent2_guess_liquids == agent1_liquid_food_choice:
            correct_predictions_liquids += 1
            increased_probability_liquid = 0.12
        else:
            increased_probability_liquid = -0.005

        #Update the probability in the set and prevent negative probabilities
        agent2_menu_solids[chosen_temperature][agent1_solid_food_choice] += increased_probability_solid
        agent2_menu_solids[chosen_temperature][agent1_solid_food_choice] = max(
            agent2_menu_solids[chosen_temperature][agent1_solid_food_choice], 0.005)

        agent2_menu_liquids[chosen_temperature][agent1_liquid_food_choice] += increased_probability_liquid
        agent2_menu_liquids[chosen_temperature][agent1_liquid_food_choice] = max(
            agent2_menu_liquids[chosen_temperature][agent1_liquid_food_choice], 0.005)

        #Keep the probability even and equal
        total_solids = sum(agent2_menu_solids[chosen_temperature].values())
        total_liquids = sum(agent2_menu_liquids[chosen_temperature].values())

        for num_solids in agent2_menu_solids[chosen_temperature]:
            agent2_menu_solids[chosen_temperature][num_solids] /= total_solids


        for num_liquids in agent2_menu_liquids[chosen_temperature]:
            agent2_menu_liquids[chosen_temperature][num_liquids] /= total_liquids

    print(f"Year {year}: Total probability for solids is: {(correct_predictions_solids/365 * 100):.2f}% " )
    print(f"Year {year}: Total probability for liquids is: {(correct_predictions_liquids/365 * 100):.2f}% " )







