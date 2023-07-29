import json
import base64

def createMigrationFromJSON(jsonFile, migrationFileName):
    """Must be checked that migration has not yet been applied."""
    data = {}
    with open(f"json/{jsonFile}") as f:
        data = json.load(f)
    
    with open(f"migrations/recipe/{migrationFileName}.sql", "w") as f:
        # Adding migration to list of applied migrations
        sql = f"INSERT INTO AppliedRecipeMigrations (migrationName) VALUES ('RECIPE-{migrationFileName}');"
        f.write(f"{sql}\n")

        for _, recipes in data.items():
            for recipeName, recipeFields in recipes.items():
                # Adding new recipe
                sql = "INSERT IGNORE INTO Recipe (name, cuisine, calories, time, instructions, imageName) VALUES ('{}', '{}', '{}', {}, '{}', '{}');".format(
                    recipeName,
                    recipeFields['cuisineType'],
                    recipeFields['calories'],
                    int(recipeFields['totalTime']),
                    recipeFields['url'],
                    recipeFields['imageName']
                )
                f.write(f"{sql}\n")

                recipeIdNestedQuery = "(SELECT recipeId FROM Recipe WHERE name = '{}')".format(
                    recipeName
                )

                # Adding food items and ingredients
                ingredients = recipeFields['ingredients']
                for ingredient in ingredients:
                    sql = "INSERT IGNORE INTO Food (foodId, name) VALUES ('{}', '{}');".format(
                        ingredient["foodId"],
                        ingredient["food"]
                    )

                    f.write(f"{sql}\n")

                    measure = ingredient["measure"]
                    sql = "INSERT IGNORE INTO Ingredients (recipeId, foodId, measure, quantity) VALUES ({}, '{}', {}, {});".format(
                        recipeIdNestedQuery,
                        ingredient["foodId"],
                        "null" if not measure or measure == "<unit>" else f"'{measure}'",
                        ingredient["quantity"]
                    )
                    f.write(f"{sql}\n")
                
                # Adding food restrictions
                for healthLabel in recipeFields['healthLabels']:
                    sql = "INSERT IGNORE INTO RecipeRestrictions (recipeId, restrictionId) VALUES ({}, (SELECT restrictionId FROM DietRestrictions WHERE name = '{}'));".format(
                        recipeIdNestedQuery,
                        healthLabel
                    )
                    f.write(f"{sql}\n")