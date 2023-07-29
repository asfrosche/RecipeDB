# THESE ARE THE QUERY FORMAT STRINGS WE USE
food_to_recipe_id = "SELECT recipeId FROM Ingredients as I, (SELECT foodId FROM Food WHERE name LIKE %s) as F WHERE F.foodId = I.foodId"
recipe_to_recipe_id = "SELECT * from Recipe WHERE name LIKE %s"
restrictions_from_recipe_id =  "SELECT r.name from RecipeRestrictions as R, DietRestrictions as D WHERE {} = R.recipeId AND D.restrictionId = R.restrictionId"
recipe_from_id = "SELECT DISTINCT r.recipeId, r.name, r.cuisine, r.calories, r.time, r.instructions, r.imageName from Recipe as r, (SELECT R.recipeId, COUNT(D.name) as cnt from RecipeRestrictions as R, DietRestrictions as D, {} as query WHERE query.recipeId = R.recipeId AND D.restrictionId = R.restrictionId {} GROUP BY R.recipeId) as P WHERE r.recipeId = P.recipeId"
get_top_n_recipes = "SELECT * FROM Recipe as r, NumRatings as nr WHERE r.recipeId = nr.recipeId ORDER BY nr DESC limit %s"
get_unrated_recipes = "SELECT * FROM Recipe as r WHERE r.recipeId NOT IN(SELECT recipeId FROM Rating) ORDER BY r.name LIMIT {}"
user_add_rating ="INSERT INTO Rating (userId, recipeId, value) VALUES ({}, {}, {}) ON DUPLICATE KEY UPDATE value = {};"
recipe_id_to_rating ="SELECT nr FROM NumRatings WHERE recipeId = {};"