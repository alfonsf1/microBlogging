PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS post(
    postID INTEGER NOT NULL,
    author VARCHAR(255) NOT NULL,
    postText VARCHAR(255) NOT NULL,
    postUserID  INTEGER NOT NULL,
    timestamp INTEGER DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(postID)
);

INSERT INTO post(postUserID, author, postText) VALUES(1, "Ryan", "Hi im Ryan");
INSERT INTO post(postUserID, author, postText) VALUES(2, "Pure", "Hi Im Pure");
INSERT INTO post(postUserID, author, postText) VALUES(3, "Alfonso", "Hi! Im Alfonso");
INSERT INTO post(postUserID, author, postText) VALUES(4, "Yash", "Hi! Im Yash");
INSERT INTO post(postUserID, author, postText) VALUES(5, "Valerie", "Hi! Im Rosendo!");
INSERT INTO post(postUserID, author, postText) VALUES(6, "Caitlyn", "Hi! Im Rosendo!");
INSERT INTO post(postUserID, author, postText) VALUES(7, "Morgana", "Hi! Im Rosendo!");

INSERT INTO post(postUserID, author, postText) VALUES(1, "Ryan", "C++ is fun");
INSERT INTO post(postUserID, author, postText) VALUES(2, "Pure", "I like football");
INSERT INTO post(postUserID, author, postText) VALUES(5, "Valerie", "I like running");
INSERT INTO post(postUserID, author, postText) VALUES(6, "Caitlyn", "I like games");
INSERT INTO post(postUserID, author, postText) VALUES(1, "Ryan", "I like Soccer");
INSERT INTO post(postUserID, author, postText) VALUES(6, "Caitlyn", "sandwhiches is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(4, "Yash", "pasta is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(5, "Valerie", "soup is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(4, "Yash", "Cant wait to go back to work");
INSERT INTO post(postUserID, author, postText) VALUES(3, "Alfonso", "I like Tennis");
INSERT INTO post(postUserID, author, postText) VALUES(4, "Yash", "I like Swimming");
INSERT INTO post(postUserID, author, postText) VALUES(1, "Ryan", "pizza is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(2, "Pure", "hamburgers is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(3, "Alfonso", "cheeseburgers is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(5, "Valerie", "Is disneyland open yet?");
INSERT INTO post(postUserID, author, postText) VALUES(2, "Pure", "Soaking up the sun today");
INSERT INTO post(postUserID, author, postText) VALUES(3, "Alfonso", "Going to san diego this week!");
INSERT INTO post(postUserID, author, postText) VALUES(6, "Caitlyn", "Watching Netflix!");
INSERT INTO post(postUserID, author, postText) VALUES(7, "Morgana", "salmon is my favorite food");
INSERT INTO post(postUserID, author, postText) VALUES(7, "Morgana", "I like stuns");
INSERT INTO post(postUserID, author, postText) VALUES(7, "Morgana", "Its finally raining!");












