## Inspiration
It can be hard to choose meals and plan given limited ingredients. We wanted to create a simple program that would plan out your meals for x-days in advance depending on what ingredients you have immediately available.

## What it does
Our program takes ingredients as input from the user. It then scans 3 opensource databases (one for breakfast, one for lunch, and one for dinner) and plans out your meals for however many days in advance you want.

## How we built it
We programmed using python and outputted information to the VS code terminal. We also built the user input functionality and since everything works through the terminal, all you need to do is open VS code, enter some information, and you will have some recipes to work with. We ran into some issues with executing some of the code but with assistance from Gemini and ChatGPT, we were able to handle the more advanced features like reading the CSV file. 

## Challenges we ran into
We tried using several different datasets for our recipes. Some were very large with 2,000,000+ entries and some were very small with 2,000 entries but in the end we decided that since we wanted to separate the meals by breakfast, lunch, and dinner we found 3 - 500 entry datasets for each. The CSV's were all formatted slightly differently which kept messing up our functions. 

## Accomplishments that we're proud of
The first time we tried implementing a function Gemini helped write to scan the 2,000,000+ CSV file it didn't work so we manually debugged it and got it working. It was not quick at all but it was very satisfying to watch it load and eventually return a massive list of all the recipes with our test case of ingredients.

## What we learned
It is important to thoroughly think about your project and your own capabilities and individual specialties within a team before you commit to an idea. The project we took on was a little bit beyond what we (a team of only beginners) could take on and learn in 24 hours. We learned how CSV files are formatted and by reading over the code we have a better understanding of how to implement these features in the future more independently.

## What's next for G-ATE-R
While we felt the pressure to have something to deliver on time, we are talking about finishing the G-ATE-R project in order to get more experience. One feature we'd especially like to experiment with is populating our ingredient list using a photo submitted by the user of their pantry or fridge using AI image recognition API built with OpenCV.
