
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
VALUES (0, 'bar of choclate', 5, 1),
		(0, 'ice-cream', 0.1, 0.33),
        (0, 'food', 0.4, 0.14),
        (0, 'weed', 0.2, 0.1),
        (1, '50 mins focused', 6, 12);
INSERT INTO habit (nature, name, current_frecuency, goal_frecuency)
VALUES (0, 'weed', 0.2, 0.1);


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

SELECT * FROM historial;

USE habits;


