
SELECT id AS 'identifier', first_name AS 'First Name', last_name AS 'Last Name'
FROM users;

SELECT id AS 'Identifier', CONCAT( first_name, ' ', last_name ) AS 'Full Name' 
FROM users;

SELECT *
FROM users;

INSERT INTO users( first_name, last_name )
VALUES( 'Michael', 'Winston' );

INSERT INTO users( first_name, last_name )
VALUES( 'Martha', 'Smith' ),
	  ( 'Roger', 'Anderson' ),
      ( 'Julie', 'Venegas' );
      
SELECT *
FROM users
WHERE first_name = 'Alex' AND last_name = 'Miller';

SELECT *
FROM users
WHERE id > 2;

SELECT *
FROM users
WHERE created_at > '2023-03-14 10:20:03';

UPDATE users
SET last_name = 'Anderson', first_name = 'Juliet'
WHERE id = 4;

DELETE FROM users
WHERE id = 5;

SELECT *
FROM users;



      
      