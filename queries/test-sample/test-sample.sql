-- R6
SELECT *
FROM Recipe
WHERE recipeId IN (
	SELECT recipeId
	FROM Ingredients
	WHERE foodId = (
		SELECT foodId
		FROM Food
		WHERE name = "Chicken"));

-- R7
SELECT *
FROM Recipe
WHERE name = 'Chicken Vesuvio';

-- R8
SELECT *
FROM Recipe
WHERE recipeId IN (
	SELECT recipeId
    FROM RecipeRestrictions
    WHERE restrictionId IN (
		SELECT restrictionId
        FROM DietRestrictions
        WHERE name = 'Peanut-Free'))
LIMIT 10;

-- R9
SELECT *
FROM Recipe AS r, AvgRating AS ar 
WHERE r.recipeId = ar.recipeId
ORDER BY ar DESC
LIMIT 3;

-- R10
INSERT INTO User (username, email, password, profilePicture)
VALUES ('User6', 'user6@fakeemail.com', 'User6', 'pic');

-- R11
INSERT INTO Rating (userId, recipeId, value)
VALUES (1, 7, 4);

SELECT value
FROM Rating
WHERE userId = 1 AND recipeId = 7;