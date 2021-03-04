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
INSERT INTO post(postUserID, author, postText) VALUES(5, "Rosendo", "Hi! Im Rosendo!");
INSERT INTO post(postUserID, author, postText) VALUES (3, "Alfonso", "Bye Alfonso");
INSERT INTO post(postUserID, author, postText) VALUES (2, "Pure", "Bye Pure");















