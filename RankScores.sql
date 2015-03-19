# Write your MySQL query statement below
select a.score, b.rank
from Scores as a, (
    select score, @rank:=@rank+1 as rank 
    from
        (select distinct score from Scores order by score desc) as a,
        (select @rank:=0) as b
) as b
where a.score = b.score
order by b.rank
