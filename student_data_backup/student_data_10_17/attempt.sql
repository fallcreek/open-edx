/* to generate raw_attempt.tsv*/
select ch.id, ch.state, c.id as studentmodule_id, c.student_id, a.username
from edxapp_csmh.coursewarehistoryextended_studentmodulehistoryextended ch, edxapp.courseware_studentmodule c,edxapp.auth_user a 
where ch.student_module_id = c.id and a.id = c.student_id and c.module_id like "%problem%"
order by c.student_id;
