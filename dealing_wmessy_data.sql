-- https://www.codewars.com/kata/5821ee33ec380124f1000013/train/sql

with consultants as (
select 
  case
    when full_name like '%.%'
    -- firstname will be in the middle if name has suffix
    then split_part(full_name, ' ', 2)
    when full_name like '%, %'
    then split_part(full_name, ', ', 2)
    else split_part(full_name, ' ', 1)
  end first_name
  , case
    when full_name like '%, %'
    then split_part(full_name, ', ', 1)
    when full_name like '%.%'
    then split_part(full_name, ' ', 3)
    else split_part(full_name, ' ', 2)
  end last_name
, credit_limit consultant_limit
from prospects
)

select 
  customers.first_name
  , customers.last_name
  , credit_limit old_limit
  , max(consultant_limit) new_limit
from customers
inner join consultants
  on lower(concat(customers.first_name,customers.last_name)) 
    = lower(concat(consultants.first_name,consultants.last_name))
  and consultant_limit > credit_limit
group by 1,2,3 
order by 1,2