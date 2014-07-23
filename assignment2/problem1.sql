select count(*) from frequency where docid='10398_txt_earn';

select count(distinct term) from frequency where docid='10398_txt_earn' and count=1;

select count(distinct term) from (
select term from frequency where docid='10398_txt_earn' and count=1
union
select term from frequency where docid='925_txt_trade' and count=1
);

select count(distinct docid) 
from frequency where term='parliament';

select count(*) from
(select docid, sum(count)
from frequency
group by docid
having sum(count) > 300
);

select count(*) 
from frequency f1
join frequency f2 on f1.docid=f2.docid and f1.term='transactions' and f2.term='world';

