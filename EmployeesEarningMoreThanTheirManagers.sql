# Write your MySQL query statement below

select a.Name from (
select a.Name, a.Salary, b.Salary as s1 from Employee a left join Employee b on a.ManagerId = b.Id
) a where a.Salary > s1
