PRAGMA foreign_keys=ON;



CREATE TABLE IF NOT EXISTS user(
    userID INTEGER NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,

    PRIMARY KEY(userID)
);

CREATE TABLE IF NOT EXISTS followers(
    id INTEGER,
    userID INTEGER NOT NULL,
    followingID INTEGER NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(userID) REFERENCES user(userID),
    FOREIGN KEY(followingID) REFERENCES user(userID)
);

INSERT INTO user VALUES(1, "Ryan", "ryan@gmail.com", "395i9g");
INSERT INTO user VALUES(2, "Pure", "pure@gmail.com", "395i9g");
INSERT INTO user VALUES(3, "Alfonso", "alfonso@gmail.com", "395i9g");
INSERT INTO user VALUES(4, "Yash", "yash@gmail.com", "395i9g");
INSERT INTO user VALUES(5, "Rosendo", "rosendo@gmail.com", "395i9g");
INSERT INTO user VALUES(6, "Valerie", "valerie@gmail.com", "395i9g");
INSERT INTO user VALUES(7, "Caitlyn", "Caitlyn@gmail.com", "395i9g");
INSERT INTO user VALUES(8, "Morgana", "rosendo@gmail.com", "395i9g");

INSERT INTO followers(userID, followingID) VALUES(1, 2);
INSERT INTO followers(userID, followingID) VALUES(2, 5);
INSERT INTO followers(userID, followingID) VALUES(3, 1);
INSERT INTO followers(userID, followingID) VALUES(4, 2);
INSERT INTO followers(userID, followingID) VALUES(5, 4);
INSERT INTO followers(userID, followingID) VALUES(1, 2);
INSERT INTO followers(userID, followingID) VALUES(1, 3);
INSERT INTO followers(userID, followingID) VALUES(3, 7);
INSERT INTO followers(userID, followingID) VALUES(7, 2);
INSERT INTO followers(userID, followingID) VALUES(8, 1);


