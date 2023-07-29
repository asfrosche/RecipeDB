-- Drop view queries
DROP VIEW AvgRating;
DROP VIEW NumRatings;

-- Drop index queries (not needed if dropping tables)
-- ALTER TABLE Recipe DROP INDEX IDX_cuisine;
-- ALTER TABLE FavoriteRecipes DROP INDEX IDX_userId;
-- ALTER TABLE Rating DROP INDEX IDX_recipeId;
-- ALTER TABLE Ingredients DROP INDEX IDX_recipeId;
-- ALTER TABLE Ingredients DROP INDEX IDX_foodId;
-- ALTER TABLE RecipeRestrictions DROP INDEX IDX_recipeId;
-- ALTER TABLE RecipeRestrictions DROP INDEX IDX_restrictionId;

-- Drop table queries
DROP TABLE RecipeRestrictions;
DROP TABLE DietRestrictions;
DROP TABLE Ingredients;
DROP TABLE Food;
DROP TABLE Rating;
DROP TABLE User;
DROP TABLE Recipe;

DROP TABLE AppliedRecipeMigrations;