select sum(d1.count * d2.count)
from frequency d1
join frequency d2 on d1.docid='10080_txt_crude' and d2.docid='17035_txt_earn' and d1.term=d2.term;


select d1.docid, sum(d1.count * d2.count)
from frequency d1,
(SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
) d2
where d1.term=d2.term
group by d1.docid
order by 2 asc;
