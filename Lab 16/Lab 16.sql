
CREATE TABLE IF NOT EXISTS emp (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    hire_date DATE
);

INSERT INTO emp (first_name, last_name, department, salary, hire_date)
VALUES
('Amit', 'Sharma', 'HR', 45000.00, '2020-05-23'),
('Priya', 'Patel', 'Finance', 60000.00, '2021-01-20'),
('John', 'Kumar', 'IT', 50000.00, '2020-08-15'),
('Neha', 'Singh', 'Marketing', 55000.00, '2022-03-10'),
('Arjun', 'Singh', 'IT', 62000.00, '2021-06-30');

SELECT * FROM emp;

SELECT first_name, last_name, department FROM emp;

SELECT DISTINCT department FROM emp;

SELECT first_name, last_name, department
FROM emp
WHERE salary > 50000;

SELECT first_name, last_name, salary
FROM emp
WHERE department = 'IT';

SELECT first_name, last_name, hire_date
FROM emp
WHERE hire_date > '2020-12-31';

SELECT first_name, last_name, salary
FROM emp
ORDER BY salary ASC;

SELECT first_name, last_name, salary
FROM emp
ORDER BY salary DESC
LIMIT 3;

SELECT COUNT(*) AS total_employees FROM emp;

SELECT AVG(salary) AS average_salary FROM emp;

SELECT 
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM emp;

SELECT department, SUM(salary) AS total_expenditure
FROM emp
GROUP BY department

SELECT department, COUNT(*) AS employee_count
FROM emp
GROUP BY department
HAVING COUNT(*) > 1;

SELECT department, AVG(salary) AS average_salary
FROM emp
GROUP BY department;
CREATE TABLE IF NOT EXISTS dept (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    location VARCHAR(100) NOT NULL
);
INSERT INTO dept (dept_id, dept_name, location)
VALUES
(1, 'HR', 'Hyderabad'),
(2, 'Finance', 'Mumbai'),
(3, 'IT', 'Bangalore'),
(4, 'Marketing', 'Chennai'),
(5, 'Operations', 'Delhi');
SELECT * FROM dept;

SELECT YEAR(hire_date) AS hire_year, COUNT(*) AS employee_count
FROM emp
GROUP BY YEAR(hire_date)
ORDER BY hire_year;

SELECT 
    e.first_name,
    e.last_name,
    e.department,
    d.location AS department_location
FROM emp e
JOIN dept d ON e.department = d.dept_name;

SELECT 
    e.first_name,
    e.last_name,
    e.department,
    d.location
FROM emp e
JOIN dept d ON e.department = d.dept_name
WHERE d.location = 'Bangalore';

SELECT 
    e.first_name,
    e.last_name,
    e.department,
    d.location AS department_location
FROM emp e
LEFT JOIN dept d ON e.department = d.dept_name;

SELECT d.dept_name, d.location
FROM dept d
LEFT JOIN emp e ON d.dept_name = e.department
WHERE e.emp_id IS NULL;

SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM dept d
LEFT JOIN emp e ON d.dept_name = e.department
GROUP BY d.dept_name;

SELECT first_name, last_name, salary
FROM emp
WHERE salary > (
    SELECT AVG(salary) FROM emp
);

SELECT department, AVG(salary) AS avg_salary
FROM emp
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 1;

SELECT *
FROM emp
ORDER BY hire_date DESC
LIMIT 5;

SELECT *
FROM emp
WHERE salary = (
    SELECT MAX(salary)
    FROM emp
    WHERE salary < (
        SELECT MAX(salary) FROM emp
    )
);

SELECT *
FROM emp
WHERE department = (
    SELECT department
    FROM emp
    WHERE first_name = 'Amit' AND last_name = 'Sharma'
)
AND NOT (first_name = 'Amit' AND last_name = 'Sharma');

UPDATE emp
SET salary = salary * 1.10
WHERE department = 'IT';

UPDATE emp
SET department = 'Marketing'
WHERE first_name = 'Ravi';

SELECT * FROM emp
WHERE salary < 40000;

ALTER TABLE emp
ADD COLUMN email VARCHAR(100);

SHOW COLUMNS FROM emp;
UPDATE emp
SET email = CONCAT(LOWER(first_name), '.', LOWER(last_name), '@company.com');

SELECT department, AVG(salary) AS avg_salary
FROM emp
GROUP BY department
ORDER BY avg_salary DESC
LIMIT 2;

SELECT d.location AS city, COUNT(e.emp_id) AS employee_count
FROM emp e
JOIN dept d ON e.department = d.dept_name
GROUP BY d.location;

SELECT department, COUNT(*) AS employee_count, SUM(salary) AS total_salary
FROM emp
GROUP BY department;

SELECT *
FROM emp
WHERE first_name LIKE 'A%';

SELECT *
FROM emp
WHERE last_name LIKE '%a';

SELECT *
FROM emp
WHERE YEAR(hire_date) = 2020;

SELECT 
    emp_id,
    first_name,
    last_name,
    hire_date,
    DATEDIFF(CURDATE(), hire_date) AS days_since_hired
FROM emp;

SELECT 
    UPPER(first_name) AS first_name_upper,
    UPPER(last_name) AS last_name_upper
FROM emp;

SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name
FROM emp;

SELECT *
FROM emp
WHERE salary BETWEEN 45000 AND 60000;

CREATE VIEW high_salary_employees AS
SELECT *
FROM emp
WHERE salary > 55000;

SELECT *
FROM high_salary_employees;

ALTER TABLE emp
MODIFY department VARCHAR(50) NOT NULL;

DROP VIEW high_salary_employees;

RENAME TABLE emp TO staff;

CREATE TABLE emp_backup AS
SELECT *
FROM emp;

DELETE FROM emp;

DROP TABLE emp_backup;

CREATE INDEX idx_last_name
ON emp(last_name);

DROP INDEX idx_last_name ON emp;