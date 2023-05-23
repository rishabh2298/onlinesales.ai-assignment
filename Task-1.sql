
-- Fetch top 3 departments along with their name and average monthly salary.

select
d.name as DEPT_NAME, avg(s.amt) as AVG_MONTHLY_SALARY
from
Departments as d inner join Employees as e inner join Salaries as s
ON
d.id = e.dept_id AND e.id = s.emp_id
group by d.id
order by AVG_MONTHLY_SALARY desc limit 3;


-- at line 5 department name and average salary get print by applying aggrigate function

-- at line 7 Iam using inner join to connect departments,employees and salaries table
-- so that it will do correct calculation for aggrigate funtion without any error.

-- at line 9 inner join is joining by linking to same value as between departments
-- and employees table on basis of department id (common in both) and in case of 
-- employees table and salaries employee id (common in both)

-- at line 10 by using (group by) it will confirm that final output will be come
-- only in unique values of department Id

-- at line 11 by using (order by) clauss in descending formate Iam sorting the final
-- table in reverse order on basis of (average salary)
-- and by applying limit-3 it will bound to show only top 3 departments with their
-- average salaries (which are highest as compare to other department employees)