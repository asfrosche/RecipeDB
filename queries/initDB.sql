-- Tables and Indices
CREATE TABLE Recipe(
    recipeId int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    cuisine varchar(30) NOT NULL,
    calories int NOT NULL,
    time int NOT NULL,
    instructions varchar(2000) NOT NULL, -- May need to increase size
    imageName varchar(100) NOT NULL,
    PRIMARY KEY(recipeId),
    CONSTRAINT UC_recipe_name UNIQUE(name)
);

CREATE INDEX IDX_recipe_name ON Recipe(name);

CREATE TABLE User(
    userId int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password BINARY(65) NOT NULL,
    profilePicture varchar(2500),
    PRIMARY KEY(userId),
    CONSTRAINT UC_user_email UNIQUE(email),
    CONSTRAINT UC_user_username UNIQUE(username)
);

CREATE TABLE Rating(
    userId int NOT NULL,
    recipeId int NOT NULL,
    value int NOT NULL,
    PRIMARY KEY(userId, recipeId),
    CONSTRAINT FK_rating_userId FOREIGN KEY(userId) REFERENCES User(userId),
    CONSTRAINT FK_rating_recipeId FOREIGN KEY(recipeId) REFERENCES Recipe(recipeId),
    CONSTRAINT CHK_rating_value CHECK(value >= 1 AND value <= 5)
);

CREATE TABLE Food(
    foodId varchar(255) NOT NULL,
    name varchar(255) NOT NULL,
    PRIMARY KEY(foodId),
    CONSTRAINT UC_food_name UNIQUE(name),
    FULLTEXT(name)
);

CREATE TABLE Ingredients(
    recipeId int NOT NULL,
    foodId varchar(255) NOT NULL,
    measure varchar(25),
    quantity DECIMAL(5, 2) NOT NULL,
    PRIMARY KEY(recipeId, foodId),
    CONSTRAINT FK_ingred_recipeId FOREIGN KEY(recipeId) REFERENCES Recipe(recipeId),
    CONSTRAINT FK_ingred_foodId FOREIGN KEY(foodId) REFERENCES Food(foodId)
);

CREATE TABLE DietRestrictions(
    restrictionId int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY(restrictionId),
    CONSTRAINT UC_dietres_name UNIQUE(name)
);

CREATE TABLE RecipeRestrictions(
    recipeId int NOT NULL,
    restrictionId int NOT NULL,
    PRIMARY KEY(recipeId, restrictionId),
    CONSTRAINT FK_recres_recipeId FOREIGN KEY(recipeId) REFERENCES Recipe(recipeId),
    CONSTRAINT FK_recres_restrictionId FOREIGN KEY(restrictionId) REFERENCES DietRestrictions(restrictionId)
);

-- Tables for managing database migration information
CREATE TABLE AppliedRecipeMigrations(
    migrationName VARCHAR(255) NOT NULL PRIMARY KEY
);

-- Views
CREATE VIEW AvgRating AS
	SELECT recipeId, ar FROM (
	    SELECT recipeId, AVG(value) AS ar
        FROM Rating
        GROUP BY recipeId) a
	UNION (
        SELECT recipeId, 0 AS ar
        FROM Recipe
        WHERE recipeId NOT IN (
            SELECT recipeId
            FROM Rating));

CREATE VIEW NumRatings AS
    SELECT recipeId, COUNT(*) AS nr
    FROM Rating
    GROUP BY recipeId;
