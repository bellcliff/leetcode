# Write your MySQL query statement below
select b.Name as Department, a.Name as Employee, a.Salary as Salary 
from (
select
    DepartmentId, Salary, Name,
    @row_num := if(@row_type=DepartmentId, @row_num+1, 1) as row_num,
    @row_type := DepartmentId as dummy
from Employee, (select @row_num:=0, @row_type:=0) as b
order by DepartmentId, Salary desc
) as a, Department as b
where a.DepartmentId = b.Id and a.row_num < 4
