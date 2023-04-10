Sure, here's an example of an inner join in SQL with some sample data:

Let's say we have the following data in our "employees" table:

id	name	department_id	salary
1	Alice	1	50000
2	Bob	2	60000
3	Charlie	1	55000
4	Dave	3	70000
And we have the following data in our "departments" table:

id	name
1	Sales
2	Marketing
3	Engineering
To join these two tables using an inner join, we can use the following query:

```SQL
SELECT employees.name, employees.salary, departments.name AS department_name
FROM employees
INNER JOIN departments ON employees.department_id = departments.id;
This query will return the following result set:
```

name	salary	department_name
Alice	50000	Sales
Bob	60000	Marketing
Charlie	55000	Sales
Dave	70000	Engineering
As you can see, the inner join has combined the "employees" and "departments" tables based on the matching "department_id" and "id" columns, and returned the name, salary, and department name for each employee. The rows where there is no matching department ID in the "departments" table (in this case, there are none) are not included in the result set.