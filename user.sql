PRAGMA foreign_keys=ON;



CREATE TABLE IF NOT EXISTS users(
    userID INTEGER NOT NULL,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,

    PRIMARY KEY(userID)
);

CREATE TABLE IF NOT EXISTS followers(
    id INTEGER,
    userID INTEGER NOT NULL,
    followerID INTEGER NOT NULL,

    PRIMARY KEY(id),
    FOREIGN KEY(userID) REFERENCES users(userID),
    FOREIGN KEY(followerID) REFERENCES users(userID)
);

INSERT INTO users VALUES(1, "Ryan", "ryan@gmail.com", "39Afwe9g");
INSERT INTO users VALUES(2, "Pure", "pure@gmail.com", "VEINVI232");
INSERT INTO users VALUES(3, "Alfonso", "alfonso@gmail.com", "adwO12312");
INSERT INTO users VALUES(4, "Yash", "yash@gmail.com", "3popoWer");
INSERT INTO users VALUES(5, "Rosendo", "rosendo@gmail.com", "opoQPfr1");
INSERT INTO users VALUES(6, "Valerie", "valerie@gmail.com", "Meok23451");
INSERT INTO users VALUES(7, "Caitlyn", "Caitlyn@gmail.com", "oojgoejgQ13e");
INSERT INTO users VALUES(8, "Morgana", "rosendo@gmail.com", "395i9g");

INSERT INTO followers(userID, followerID) VALUES(1, 2);
INSERT INTO followers(userID, followerID) VALUES(2, 5);
INSERT INTO followers(userID, followerID) VALUES(3, 1);
INSERT INTO followers(userID, followerID) VALUES(4, 2);
INSERT INTO followers(userID, followerID) VALUES(5, 4);
INSERT INTO followers(userID, followerID) VALUES(1, 3);
INSERT INTO followers(userID, followerID) VALUES(3, 7);
INSERT INTO followers(userID, followerID) VALUES(7, 2);
INSERT INTO followers(userID, followerID) VALUES(8, 1);


