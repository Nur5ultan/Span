CREATE DATABASE IF NOT EXISTS span;
USE span;

DROP TABLE IF EXISTS `departments`;
CREATE TABLE IF NOT EXISTS `departments` (
    `departments_id` INT(11) NOT NULL AUTO_INCREMENT,
    `departments_name` VARCHAR(250) NOT NULL DEFAULT '',
    PRIMARY KEY (`departments_id`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `employees`;
CREATE TABLE IF NOT EXISTS `employees` (
    `employee_id` INT(11) NOT NULL AUTO_INCREMENT,
    `first_name` VARCHAR(100), NOT NULL DEFAULT '',
    `middle_name` VARCHAR(100), NOT NULL DEFAULT '',
    `last_name` VARCHAR(100), NOT NULL DEFAULT '',
    `departments_id` INT(11), NOT NULL DEFAULT 0,
    PRIMARY KEY (`employee_id`)
) ENGINE=MYISAM DEFAULT CHARSET=utf8;

INSERT INTO departments (departments_id, departments_name)
VALUES (1, 'Бухгалтерия');

INSERT INTO departments (departments_id, departments_name)
VALUES (2, 'Отдел программирования');

INSERT INTO departments (departments_id, departments_name)
VALUES (3, 'Служба поддержки клиентов');


INSERT INTO employees (first_name, middle_name, last_name departments_id)
VALUES ("Артём", "Юрьевич", "Валентинов", 1);

INSERT INTO employees (first_name, middle_name, last_name departments_id)
VALUES ("Вера", "Михайловна", "Янова", 1)

INSERT INTO employees (first_name, middle_name, last_name departments_id)
VALUES ("Галина", "Руслановна", "Маргаритова", 1)

INSERT INTO employees (first_name, middle_name, last_name departments_id)
VALUES ("Артём", "Николаевич", "Григорин", 2)
