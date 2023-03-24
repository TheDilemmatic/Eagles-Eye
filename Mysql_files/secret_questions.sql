USE cbse_compsci_proj;
CREATE TABLE secret_questions
(
admincode INT,
userid VARCHAR(300),
password VARCHAR(300),
secret1 VARCHAR(300),
ans1 VARCHAR(300) NOT NULL,
secret2 VARCHAR(300) DEFAULT 30000,
ans2 VARCHAR(300) NOT NULL
);