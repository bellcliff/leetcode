# Write your MySQL query statement below
select distinct Num ConsecutiveNums from (
select Num, @num:=if(@type=Num, @num+1, 1) num1, @type:=Num dummy
from Logs, (select @num:=0, @type:=0) a
) as a
where a.num1 >2
