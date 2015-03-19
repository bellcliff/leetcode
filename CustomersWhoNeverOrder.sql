select Name from (
select a.Name, b.Id from Customers a left join Orders b on b.CustomerId =a.Id
) as a where Id is null
