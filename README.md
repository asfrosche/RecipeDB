# Personal Recipe Database

This is a personal project to create a recipe database that can be accessed online. The database is hosted on a MySQL server and can be accessed using the command line.

## Creating and Loading the Database

To create and load a copy of the sample database, follow these steps:

1. Modify the database information in `/data/scripts/connectDB.py`.
2. Run the queries in `/queries/initDB.sql`.
3. Change directories to the `/data` directory and run `python applyMigrations.py`, passing in any number of additional command line arguments corresponding to keywords that correspond to files in `/data/json`.

## Accessing and Deploying the Application

To access and deploy the application, follow these steps:

1. From the repository directory, navigate to `streamlit_app` using the terminal.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Once the dependencies are installed, run the following command on the terminal:

4. Access the URL `http://localhost:8501` or the URL provided after the `streamlit run` command to access the deployed app.

## Features Supported

Core Features:

- Get all user information.
- Add a new user.
- Get all favorite recipes of a user.
- Add a recipe to a user's favorites.
- Remove a recipe from a user's favorites.
- Get a user's current rating for a recipe.
- Add or update a user's rating for a recipe.
- Get all recipe information.
- Get all details of a recipe with a given name.
- Get all recipes with a specific ingredient.
- Get the number of ratings for a recipe.
- Get the average rating for a recipe.
- Select the top X recipes by rating.
- Get all dietary restrictions associated with a recipe.


## Relevant SQL Files/Scripts

The relevant SQL files/scripts are as follows:

- `/queries/initDB.sql`: Contains all the queries for creating tables, indexes, and views.
- `/queries/clearDB.sql`: Drops all of the tables and views.
- `/data/migrations/base/populateDietRestrictions.sql`: Populates the `DietRestrictions` table.
- `/data/migrations/recipe`: Contains all the relevant SQL statements for populating the database with the recipes.
- `/data/migrations/test/populateTestUsers.sql`: Populates the database with test users.

## Queries

The SQL statements listed in the `report.pdf` document can be found in `/queries/test-sample/test-sample.sql`, and the output of these queries can be found in `/queries/test-sample/test-sample.out`.

Other queries that can be used to query the database (beyond those presented in the `report.pdf` document) are in `/queries/recipeQueries.sql` and `/queries/userQueries.sql`.

## Code for Downloading/Transforming Data

Scripts corresponding to the database migration pipeline can be found in the `/data` folder. These scripts include queries to the API for recipes, data transformation into JSON files, and populating the database with the extracted recipe data.

Feel free to explore the application and the database to manage and access your personal recipe collection. If you encounter any issues or have suggestions, please don't hesitate to contribute or reach out to the project maintainers.

Happy cooking! 🍳🥗🍰
