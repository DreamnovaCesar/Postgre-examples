Sure, here's an example of how to create a view using Postgres:

Let's say we have two tables named "employees" and "departments" in our database, and we want to create a view that displays the names and salaries of all employees along with their department names.

First, we'll need to join the two tables using a common column, which in this case is the "department_id" column. We can do this using the following query:

```SQL
SELECT employees.name, employees.salary, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;
```

This query will return a result set that includes the names and salaries of all employees, along with their corresponding department names.

Now, to create a view using this query, we can use the CREATE VIEW statement in Postgres. Here's an example:

```SQL
CREATE VIEW employee_salary_dept AS
SELECT employees.name, employees.salary, departments.name AS department_name
FROM employees
JOIN departments ON employees.department_id = departments.id;
```

This will create a new view called "employee_salary_dept" that contains the same result set as the query we just ran. We can now use this view in other queries just like we would use a table.

To query the view, we can simply use a SELECT statement like this:

```SQL
SELECT * FROM employee_salary_dept;
```

This will return the same result set as our original query, but we can now refer to the view by name instead of having to write out the entire query every time we need to access the data.