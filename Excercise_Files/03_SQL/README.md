# CodeSpace - Induction - SQL

#### this repo is storage space for the screenshots generated while solving CodeSpace - Induction CR1CSICZ22-X1XA SQL Database Exercises

here comes the code and references to the screenshots:

### 1) - Introduction to SQL

+ execrcise 01   
```
SELECT
   *
FROM
   tblappointment;
```   
attached screenshot: 1_exercise01.png  
86 rows

+ exercise 02   
```
SELECT
   *
FROM
   module;
```   
attached screenshot: 1_exercise02.png  
2 rows  

+ exercise 03   
```
SELECT DISTINCT
   County
FROM
   tblpatient;
```   
attached screenshot: 1_exercise03.png  
2 rows

+ exercise 04   
```
SELECT DISTINCT
   title
FROM
   tblpatient;
```   
attached screenshot: 1_exercise04.png  
4 rows

### 2) - Querying Data AND Sorting Data

+ exercise 01   
```
SELECT
   locations.location_id,
   country_id,
   state_province
FROM
   locations;
```   
attached screenshot: 2_exercise01.png  
7 rows

+ exercise 02   
```
SELECT
   e.employee_id,
   last_name,
   salary AS 'Monthly Salary'
FROM
   employees e;
```   
attached screenshot: 2_exercise02.png  
40 rows

+ exercise 03   
```
SELECT
   CONCAT(first_name, ' ', last_name) AS 'Fullname'
FROM
   employees;
```   
attached screenshot: 2_exercise03.png  
40 rows

+ exercise 04   
```
SELECT
   last_name,
   email,
   salary
FROM
   employees
ORDER BY
   salary DESC,
   last_name;
```   
attached screenshot: 2_exercise04.png  
40 rows

### 3) - Filtering Data Part01

+ exercise 01   
```
SELECT
   salary
FROM
   employees
ORDER BY
   salary DESC
LIMIT 1;
```   
attached screenshot: 3_exercise01.png  
1 row

+ exercise 02   
```
SELECT
   employee_id,
   first_name,
   last_name,
   job_id
FROM
   employees
ORDER BY
   salary DESC
LIMIT 1;
```   
attached screenshot: 3_exercise02.png  
1 row

+ exercise 03   
```
SELECT
   department_name,
   department_id
FROM
   departments
ORDER BY
   department_id ASC
LIMIT 4, 6;
```   
attached screenshot: 3_exercise03.png  
6 rows

+ exercise 04   
```
SELECT DISTINCT
   location_id
FROM
   departments;
```   
attached screenshot: 3_exercise04.png  
7 rows

+ exercise 05   
```
SELECT
   first_name,
   last_name,
   salary,
   phone_number
FROM
   employees
WHERE
   salary <= 5000;
```   
attached screenshot: 3_exercise05.png  
12 rows

+ exercise 06   
```
SELECT
   employee_id,
   first_name,
   last_name,
   hire_date
FROM
   employees
WHERE
   YEAR (hire_date) >= 1999;
```   
attached screenshot: 3_exercise06.png  
5 rows

### 4) - Filtering Data Part02

+ exercise 01   
```
SELECT
   first_name,
   last_name,
   salary
FROM
   employees
WHERE
   first_name LIKE 'p%'
   AND
   salary < 8000;
```   
attached screenshot: 4_exercise01.png  
2 rows

+ exercise 02   
```
SELECT
   first_name,
   last_name,
   hire_date,
   department_id
FROM
   employees
WHERE
   YEAR(hire_date) IN (1997, 1998)
   AND department_id LIKE '5';
```   
attached screenshot: 4_exercise02.png  
4 rows

+ exercise 03   
```
SELECT
   first_name,
   last_name,
   salary,
   email,
   hire_date AS 'Year of Hire'
FROM
   employees
WHERE
   YEAR(hire_date) BETWEEN 1998 AND 2000
ORDER BY
   last_name ASC;
```   
attached screenshot: 4_exercise03.png  
11 rows

+ exercise 04   
```
SELECT
   *
FROM
   employees
WHERE
   salary >= 5000
   AND salary <= 10000;
```   
attached screenshot: 4_exercise04.png  
19 rows

+ exercise 05   
```
SELECT
   first_name,
   last_name,
   salary
FROM
   employees
WHERE
   salary BETWEEN 4000 AND 12000
ORDER BY
   first_name ASC;
```   
attached screenshot: 4_exercise05.png  
27 rows

+ exercise 06   
```
SELECT
   *
FROM
   employees
WHERE
   department_id NOT IN (1, 4, 8, 10)
ORDER BY
   salary DESC;
```   
attached screenshot: 4_exercise06.png  
26 rows

+ exercise 07   
```
SELECT
   *
FROM
   employees
WHERE
   first_name LIKE '%s'
ORDER BY
   first_name ASC;
```   
attached screenshot: 4_exercise07.png  
2 rows

+ exercise 08   
```
SELECT
   *
FROM
   employees
WHERE
   last_name LIKE '___g';
```   
attached screenshot: 4_exercise08.png  
1 row

### 5) - Joins

+ exercise 01   
```
SELECT
   first_name,
   last_name,
   manager_id,
   e.department_id,
   location_id
FROM
   employees AS e
      INNER JOIN
   departments AS d ON d.department_id = e.department_id;
```   
attached screenshot: 5_exercise01.png  
40 rows

+ exercise 02   
```
SELECT
   location_id,
   postal_code,
   l.country_id,
   country_name
FROM
   locations AS l
      INNER JOIN
   countries AS c ON c.country_id = l.country_id;
```   
attached screenshot: 5_exercise02.png  
7 rows

+ exercise 03   
```
SELECT
   e.employee_id,
   e.first_name AS 'employee fist name',
   e.last_name AS 'employee last name',
   department_id,
   d.first_name  AS 'dependent fist name',
   d.last_name AS 'dependent last name',
   relationship
FROM
   employees AS e
      INNER JOIN
   dependents AS d ON d.employee_id = e.employee_id
ORDER BY
   e.employee_id;
```   
attached screenshot: 5_exercise03.png  
30 rows

### 6) - Aggregate Functions

+ exercise 01   
```
SELECT
   COUNT(employee_id) AS 'Number of Employees In Sales'
FROM
   employees
WHERE
   department_id IN (SELECT
         department_id
      FROM
         departments
      WHERE
         department_name = 'Sales');
```   
attached screenshot: 6_exercise01.png  
6 rows

+ exercise 02   
```
SELECT
   department_name AS Department,
   COUNT(e.employee_id) AS 'Number of Employees in Department'
FROM
   departments AS d
      LEFT JOIN
   employees AS e ON e.department_id = d.department_id
GROUP BY d.department_id;
```   
attached screenshot: 6_exercise02.png  
11 rows

+ exercise 03   
```
SELECT
   e.manager_id,
   CONCAT(m.first_name, ' ', m.last_name) AS 'full name',
   COUNT(e.employee_id)
FROM
   employees AS e
      LEFT JOIN employees AS m ON m.employee_id = e.manager_id
WHERE
   e.manager_id IS NOT NULL
GROUP BY manager_id;
```   
attached screenshot: 6_exercise03.png  
11 rows

+ exercise 04   
```
SELECT
   e.employee_id,
   COUNT(d.dependent_id) AS 'dependent_no'
FROM
   employees AS e
      INNER JOIN dependents AS d ON d.employee_id = e.employee_id
GROUP BY d.employee_id
HAVING dependent_no > 1;
```   
attached screenshot: 6_exercise04.png  
Empty set

+ exercise 05   
```
SELECT
   d.department_id,
   department_name,
   SUM(salary) AS 'Salary Total in Department'
FROM
   departments AS d
      INNER JOIN employees AS e ON e.department_id = d.department_id
GROUP BY d.department_id;
```   
attached screenshot: 6_exercise05.png  
11 rows

+ exercise 06   
```
SELECT
   ROUND(AVG(max_salary),2) AS 'Avarage of Max Salaies'
FROM
   jobs;
```   
attached screenshot: 6_exercise06.png  
1 row

### 7) - Grouping

+ exercise 01   
```
SELECT
   j.job_id,
   COUNT(e.job_id) AS 'Job ID Instances'
FROM
   jobs AS j
      LEFT JOIN
   employees AS e ON e.job_id = j.job_id
GROUP BY
   j.job_id;
```   
attached screenshot: 7_exercise01.png  
19 rows

+ exercise 02   
```
SELECT
   j.job_id,
   COUNT(e.job_id) AS 'Job ID Instances'
FROM
   jobs AS j
      LEFT JOIN
   employees AS e ON e.job_id = j.job_id
WHERE
   j.job_id = 9
GROUP BY
   j.job_id;
```   
attached screenshot: 7_exercise02.png  
1 row

+ exercise 03   
```
SELECT
   j.job_id,
   j.job_title,
   COUNT(e.job_id) AS 'Job ID Instances'
FROM
   jobs AS j
      LEFT JOIN
   employees AS e ON e.job_id = j.job_id
GROUP BY
   j.job_id;
```   
attached screenshot: 7_exercise03.png  
19 rows

### 8) - Subquery PART 01

+ exercise 01   
```
SELECT
   employee_id,
   salary
FROM
   employees
WHERE
   salary = (SELECT
         MIN(salary)
      FROM
         employees);
   
```   
attached screenshot: 8_exercise01.png  
1 row

+ exercise 02   
```
SELECT
   employee_id,
   first_name,
   last_name,
   salary
FROM
   employees
WHERE
   salary > (SELECT
         ROUND(AVG(salary),0)
      FROM
         employees);
   
```   
attached screenshot: 8_exercise02.png  
17 row

+ !!!!!!!!!! exercise 03   
Determine the people earning below the average inside of department_id = 6. Then show their details
(employee_id, first_name, last_name, salary, department_id).   
Is not clear !!!!!!!!!!
```
SELECT
   employee_id,
   first_name,
   last_name,
   salary,
   department_id
FROM
   employees
WHERE
   salary < (SELECT
         ROUND(AVG(salary),0)
      FROM
         employees
      WHERE 
         department_id = 6);
   
```   
attached screenshot: 8_exercise03.png  
12 rows

+ exercise 04   
Determine the employees working in the IT department for the company.
```
SELECT
   employee_id
FROM
   employees
WHERE
   department_id IN (SELECT
         department_id
      FROM
         departments
      WHERE 
         department_name = 'IT');
   
```   
attached screenshot: 8_exercise04.png  
5 rows

+ exercise 05 - first take   
Starting with ‘Jennifer King’ determine the employees name i.e. the father to this child. Who is it?
```
SELECT
   CONCAT(d.first_name, ' ', d.last_name) dependentName,
   CONCAT(e.first_name, ' ', e.last_name) employeeNAme
FROM
   employees e
INNER JOIN
   dependents d ON d.employee_id = e.employee_id;
```   
attached screenshot: 8_exercise05_firstTake.png  
30 rows

+ exercise 05 - second take   
Starting with ‘Jennifer King’ determine the employees name i.e. the father to this child. Who is it?
```
SELECT
   CONCAT(d.first_name, ' ', d.last_name) dependentName,
   (SELECT
       CONCAT(e.first_name, ' ', e.last_name)
    FROM
       employees e
    WHERE
       e.employee_id = d.employee_id) employeeNAme
FROM
   dependents d;      
```   
attached screenshot: 8_exercise05_secondTake.png  
30 rows

### 9) - Subquery PART 02

+ exercise 01   
```
SELECT
   first_name,
   last_name,
   salary,
   department_id
FROM
   employees
WHERE
   salary < (SELECT
         ROUND(AVG(salary),0)
      FROM
         employees
      GROUP BY
         department_id
      HAVING
         department_id = (SELECT
               department_id
            FROM
               departments
            WHERE
               department_name = 'IT'));
   
```   
attached screenshot: 9_exercise01.png  
12 rows

+ exercise 02   
```
SELECT
   first_name,
   last_name,
   salary,
   department_id
FROM
   employees
WHERE
   salary < (SELECT
         MIN(salary)
      FROM
         employees
      GROUP BY
         department_id
      HAVING
         department_id = (SELECT
               department_id
            FROM
               departments
            WHERE
               department_name = 'Sales'));
   
```   
attached screenshot: 9_exercise02.png  
14 row

### 10) - Modifying Data

+ exercise 01   
```
CREATE TABLE module (
   moduleno varchar (10),
   modulename varchar (50),
   moduleunitsize int (3),
   hoursfordelivery int (3)
);
   
```   
attached screenshot: 10_exercise01.png

+ exercise 02   
```
INSERT INTO student
   (studentno, surname, firstname, email, mobileno)
VALUES 
   (7, 'Flintstone', 'Fred', 'f.flintstone@bt.com', 1234567),
   (8, 'Flintstone', 'Wilma', 'w.flintstone@bt.com', 2345678),
   (9, 'Flintstone', 'Pebbles', 'p.flintstone@bt.com', 3456789),
   (10, 'Flintstone', 'Dino', 'd.flintstone@bt.com', 4567890);
```   
attached screenshot: 10_exercise02.png

+ exercise 03   
```
INSERT INTO module
   (moduleno, modulename, moduleunitsize, hoursfordelivery, studentno)
VALUES 
   ('DH3J34', 'SQL: Introduction', '1', '32', 7);
```   
attached screenshot: 10_exercise03.png

+ exercise 04   
```
UPDATE student
SET
   firstname = 'Barney',
   surname = 'Rubble'
WHERE 
   studentno = 7;
```
```
SELECT
   *
FROM
   student
WHERE
   studentno = 7;
```
```
UPDATE student
SET
   firstname = 'Fred',
   surname = 'Flintstone'
WHERE 
   studentno = 7;
```   
attached screenshot: 10_exercise04.png

+ !!!!!!!!!! exercise 05   
do I or don't I 'put it back to Fred'??? !!!!!!!!!
```
SELECT
   surname,
   firstname,
   s.studentno,
   modulename
FROM
   student AS s
      INNER JOIN
   module AS m ON m.studentno = s.studentno;
```   
attached screenshot: 10_exercise05.png  
1 row
