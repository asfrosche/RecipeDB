# Data Folder

To add additional migration files for new databases, run `addRecipes.py`. Usage: `python addRecipes.py recipeCountPerKeyword recipeKeyword1 [recipeKeyword2 ...]`. Example command is `python addRecipes.py 20 pork noodles`, which creates two JSON and SQL files in `/json/` and `/migrations/recipe/`, respectively, containing information about 20 recipes based on pork and noodles. The images for these recipes are stored in `/images/`.

To run migration files, run `python applyMigrations.py`. Usage: `python applyMigrations.py [recipeKeyword1 recipeKeyword2 ...]`. Example command is `python applyMigrations pork noodles`, which adds the data that was extracted from the API as migrations from the previous command to the database.

The database credentials are stored in `scripts/connectDB.py`. Note that migration files do not include database initialization files. That is, `../queries/initDB.sql` needs to be executed on the database before `applyMigrations.py` will work.
