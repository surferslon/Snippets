delete
from gateways_externallink out
where (
    select count(*)
    from gateways_externallink inr
    where inr.object_id = out.object_id
    and inr.content_type_id=out.content_type_id ) > 1 ;
