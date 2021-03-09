PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS posts(
    postID INTEGER NOT NULL,
    author VARCHAR(255) NOT NULL,
    text VARCHAR(255) NOT NULL,
    userID  INTEGER NOT NULL,
    timestamp INTEGER DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(postID)
);

INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "Hi im Ryan");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "Hi Im Pure");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "Hi! Im Alfonso");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "Hi! Im Yash");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "Hi! Im Valerie!");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "Hi! Im Caitlyn!");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "Hi! Im Morgana!");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "C++ is fun");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "I like football");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "I like running");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "I like games");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "I like Soccer");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "sandwhiches is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "pasta is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "soup is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "Cant wait to go back to work");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "I like Tennis");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "I like Swimming");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "pizza is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "hamburgers is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "cheeseburgers is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "Is disneyland open yet?");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "Soaking up the sun today");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "Going to san diego this week!");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "Watching Netflix!");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "salmon is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "I like stuns");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "Its finally raining!");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "Monday sucks");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "Tuesday kinda sucks");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "Wednesday is kinda even");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "Almost Friday!");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "Today is Friday!");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "Today is Saturday!");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "It's Sunday!");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "Python is fun");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "I like to hate on stuff");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "I like hiking");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "I like root");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "I hate waking up");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "Duo is my favorite thing");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "seafood is my not favorite food");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "chicken is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "Don't let me go back to work");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "I like watching badminton");
INSERT INTO posts(userID, author, text) VALUES(4, "Yash", "I like staying at home");
INSERT INTO posts(userID, author, text) VALUES(1, "Ryan", "pho is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "bun bo hue is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "poko is my favorite food");
INSERT INTO posts(userID, author, text) VALUES(5, "Valerie", "When will Disneyland open up?");
INSERT INTO posts(userID, author, text) VALUES(2, "Pure", "Can't soak up because of raining days");
INSERT INTO posts(userID, author, text) VALUES(3, "Alfonso", "Returning home today!");
INSERT INTO posts(userID, author, text) VALUES(6, "Caitlyn", "Watching my matches!");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "stun is my favorite effect");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "I like roots");
INSERT INTO posts(userID, author, text) VALUES(7, "Morgana", "It's finally sunny!");










