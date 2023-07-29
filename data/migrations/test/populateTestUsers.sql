-- Adding 5 Users
INSERT INTO User (username, email, password) VALUES ("User1", "user1@fakeemail.com", "User1");
INSERT INTO User (username, email, password) VALUES ("User2", "user2@fakeemail.com", "User2");
INSERT INTO User (username, email, password) VALUES ("User3", "user3@fakeemail.com", "User3");
INSERT INTO User (username, email, password) VALUES ("User4", "user4@fakeemail.com", "User4");
INSERT INTO User (username, email, password) VALUES ("User5", "user5@fakeemail.com", "User5");

-- Adding User Ratings
INSERT INTO Rating (userId, recipeId, value) VALUES (1, 3, 3);
INSERT INTO Rating (userId, recipeId, value) VALUES (1, 4, 4);
INSERT INTO Rating (userId, recipeId, value) VALUES (1, 5, 5);
INSERT INTO Rating (userId, recipeId, value) VALUES (2, 3, 5);
INSERT INTO Rating (userId, recipeId, value) VALUES (2, 5, 5);
INSERT INTO Rating (userId, recipeId, value) VALUES (3, 5, 3);

-- Adding User Favorites
INSERT INTO FavoriteRecipes (userId, recipeId) VALUES (1, 4);
INSERT INTO FavoriteRecipes (userId, recipeId) VALUES (1, 5);
INSERT INTO FavoriteRecipes (userId, recipeId) VALUES (2, 5);
INSERT INTO FavoriteRecipes (userId, recipeId) VALUES (3, 5);