-- Query for all recipe information
SELECT * FROM Recipe WHERE recipeId = <RECIPE_ID>;


-- Given recipe name return all details of recipe
SELECT * from Recipe, <OTHER> as query WHERE name = <Recipe_name>;


-- Query for all recipes with particular ingredient (searching by food name)
SELECT recipeId
FROM Ingredients
WHERE foodId = (SELECT foodId
                FROM Food
                WHERE name = <FOOD_NAME>);

-- Query for number of ratings a particular recipe has
SELECT nr FROM NumRatings WHERE recipeId = <RECIPE_ID>;

-- Query for average rating a recipe has
SELECT ar FROM AvgRating WHERE recipeId = <RECIPE_ID>;

-- Query to select the top X recipes by Rating
SELECT recipeId FROM AvgRating ORDER BY ar DESC LIMIT <X>;

-- Query for all dietary restrictions a recipe has (returns dietary restriction names)
SELECT name
FROM DietRestrictions
WHERE restrictionId IN (SELECT restrictionId
                        FROM RecipeRestrictions
                        WHERE recipeId = <RECIPE_ID>);
