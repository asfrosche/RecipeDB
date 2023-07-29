-- Query for all user information
SELECT * FROM User WHERE userId = <USER_ID>;

-- Query for adding a new user
INSERT INTO User (userId, username, email)
VALUES (<USER_ID>, <USERNAME>, <EMAIL>);

-- Query for all of a user's favorite recipes
SELECT recipeId
FROM FavoriteRecipes
WHERE userId = <USER_ID>;

-- Query for a user adding a recipe to their favorites
INSERT INTO FavoriteRecipes (userId, recipeId)
VALUES (<USER_ID>, <RECIPE_ID>);

-- Query for a user removing a recipe from their favorites
DELETE FROM FavoriteRecipes
WHERE userId = <USER_ID> AND recipeId = <RECIPE_ID>;

-- Query for a user's current rating for a recipe
SELECT value
FROM Rating
WHERE userId = <USER_ID> AND recipeId = <RECIPE_ID>;

-- Query for adding a user's rating
INSERT INTO Rating (userId, recipeId, value)
VALUES (<USER_ID>, <RECIPE_ID>, <RATING_VALUE>)
ON DUPLICATE KEY UPDATE value = <RATING_VALUE>;
