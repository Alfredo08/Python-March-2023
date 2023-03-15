
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

INSERT INTO todos( name, status, user_id )
VALUES ( 'Learning Flask', 'complete', 1 ),
	   ( 'Learning Routes', 'complete', 1 ),
       ( 'Learning Sessions', 'complete', 2 ),
       ( 'Learning POST', 'complete', 3 ),
       ( 'Learning SQL', 'in_progress', 1 ),
       ( 'Learning ERD', 'in_progress', 2 );
       
INSERT INTO todos( name, status, user_id )
VALUES ( 12, 20, 1 ) ;   

DELETE FROM todos
WHERE id = 8; 

SELECT u.first_name, u.last_name, t.name, t.status
FROM todos t 
	JOIN users u ON t.user_id = u.id
WHERE u.id = 1;

SELECT *
FROM todos t, users u
WHERE t.user_id = u.id AND u.id = 1;

SELECT u.first_name, u.last_name, t.name, t.status
FROM users u
	LEFT JOIN todos t ON u.id = t.user_id;


SELECT u.first_name, COUNT( t.user_id ) AS 'Num of todos'
FROM users u
	JOIN todos t ON u.id = t.user_id
GROUP BY ( u.first_name )
ORDER BY DESC( u.first_name );


      
      