
# IMPLEMENT DATABASE

CREATE DATABASE IF NOT EXISTS habits;
CREATE DATABASE habits;
USE habits;


# HABITS TABLE IMPLEMENTATION

DROP TABLE IF EXISTS habit;
CREATE TABLE habit (
	habit_id INT NOT NULL AUTO_INCREMENT,
    nature boolean,
    name VARCHAR(50),
    current_frecuency DECIMAL(6,3),
    goal_frecuency DECIMAL(6,3),
    PRIMARY KEY (habit_id)
    );
INSERT INTO habit (nature, name, current_frecuency, goal_frecuency)
VALUES (0, 'Bar of choclate', 5, 1),
		(0, 'Ice-cream', 0.1, 0.33),
        (0, 'Food', 0.4, 0.14),
        (0, 'Weed', 0.2, 0.1),
        (1, '50 mins focused', 6, 12);
INSERT INTO habit (nature, name, current_frecuency, goal_frecuency)
VALUES (0, 'weed', 0.2, 0.1);

SELECT * FROM habit;

UPDATE habit
SET name = 'Weed'
WHERE habit_id = 5;

# IMPLEMENT HISTORIAL

DROP TABLE IF EXISTS historial;
CREATE TABLE historial(
	id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    time TIME NOT NULL,
    habit_id INT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (habit_id) REFERENCES habit(habit_id)
    );
SELECT * FROM historial;



# ADD HABIT TO HISTORIAL

DROP PROCEDURE IF EXISTS add_habit_to_historial;
DELIMITER //
CREATE PROCEDURE add_habit_to_historial(IN id INT)
BEGIN
    INSERT INTO historial (date, time, habit_id)
	VALUES (DATE(NOW()), TIME(NOW()), id);
END //
DELIMITER ;
CALL add_habit_to_historial(1);


# IMPLEMENT rewards storage

CREATE TABLE acumulated_rewards (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO acumulated_rewards (name, quantity)
VALUES ('Bar of choclate', 0),
		('Food', 0),
        ('Weed', 0);
        
DROP PROCEDURE IF EXISTS get_acumulated_rewards;
DELIMITER //
CREATE PROCEDURE get_acumulated_rewards()
BEGIN
	SELECT * FROM acumulated_rewards;
END //
DELIMITER ;
        
CALL get_acumulated_rewards;

SELECT * FROM historial;