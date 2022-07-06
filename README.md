# Animal Crossing New Horizons Character Popularity Analysis

## Project Oversight
- Animal Crossing: New Horizons (acnh) is video game in which the player controls a character who moves to a deserted island. In this game, the player accomplishes assigned tasks, develops the island as they choose, and brings other characters to live on their island. For this project, I am using information from the Animal Crossing New Horizon character catalog csv to acquire, prepare, explore, and create models to predict whether or not a new character will be successful. 

  - A successful character is defined as falling within tier 1, 2, or 3 in the popularity poll. This accounts for about 17% of the characters.

- This information is based off of a popularity poll that is updated monthly. It is current as of June 30, 2022.


## Business Goals/ Description

- Find key drivers of success for characters in the game Animal Crossing New Horizons.
- Construct a machine learning model that can be used to predict whether or not a character is successful given the characteristics of the character. 
  - The models that will be used are decision tree models, random forest models, and k nearest neighbor models. 
  - The top performing model should be able to beat a baseline accuracy of 82%.
- This information will be used to give more insight to what characteristics should be given to characters in order to:
    - Develop characters that have a high likelihood of being successful in order to market those characters and sell them in bundles.
    - Reduce manpower hours spent developing characters that will not be successful.


## Project Goals
### Answer the questions: What features, if any, can be used to help determine whether or not a new character will be successful in the game Animal Crossing New Horizons? How can these features be combined to predict the success of a new character?

- Ask questions during the exploration phase to better understand what characteristics could be factoring into the target variable of whether or not a character is successful. 
    - Answer those questions with statistical testing and visualizations.
- These answers will be used to help predict whether or not a new character will be successful in the future. 
- Construct machine learning models to predict whether or not a new character will be successful. 
    - Run the most effective machine learning model against test.
- Make final recommendations and provide next steps.


## Executive Summary
- There are a few things that can help in determining whether or not a character will be successful in Animal Crossing New Horizons.

- Some of the things that we can use to help predict whether or not a character will be successful are (in order of importance) :
    - Species, Style_1, Gender, and Personality
    - A character's hobby can also be a slight driver in determining whether or not they will be successful, but it isn't as strong of a driver as the aforementioned categories.
- The decision tree model that I produced is able to determine whether or not a new character will be successful or not with 96% accuracy and with a 70% recall.


## Audience
- Peers 


## Deliverables
- Jupyter Notebook containing the final report.
- Python Modules that can be used to reproduce the work.
- Scratch notebook that can be referred to for my work.
- Readme file explaining the project.



## Data Dictionary 
<img src="images/acnh_data_dictionary.png" width = 750>

## Project plan 

- Acquire the animal crossing new horizons character csv file from https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset
- Clean and prepare the data for the exploration file. Create a wrangle.py file to recreate the work.
- Explore the data and ask questions to clarify what is actually happening. 
  - Ensure to properly annotate, comment, and use markdowns.
  - Write out each null and alternative hypothesis.
  - Visualize the data.
  - Run statistical test on the data.
- Create different machine learning models.
  - Decision Tree Model.
  - KNN model.
  - Random Forest model.
- Choose the model that performs the best.
  - Evaluate on test.
- Deliver final presentation to peers.

## Initial Hypotheses:
- The species, gender, hobby, and color_1 are key drivers of whether or not a character will be successful.
- While favorite_song might be a driver, I don't know that it will be significant enough to determine whether a character will be successful.
- The style of the character will also be a driver of character success as it influences the characters visual appearance. 
  - The style_1 and color_1 columns combined are generally used to determine the visual appearance of the characters in the dataset. 

## Reproduce the Project
- In order to reproduce the project, you will need:
  - A Copy of the csv from this repository.
  - Ability to clone this repository to local environment.
  - Ability to run the notebook.

- If you would like to recreate the work with up to date information, you will need to create an updated csv by doing the following:
  - copy the villagers.csv from https://www.kaggle.com/datasets/jessicali9530/animal-crossing-new-horizons-nookplaza-dataset 
  - Access https://nookipedia.com/wiki/Villagers/New_Horizons in order to get the information for the missing characters
  - Access https://www.animalcrossingportal.com/games/new-horizons/guides/villager-popularity-list.php#/ in order to get the ranking position for each of the characters.