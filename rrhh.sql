create table rrhh as
select
e.employee_id as "ID Empleado",
f.function_name as "Función",
d.department_name as "Departamento",
r.region_name as "Región",
ed.education_level as "Educación",
g.gender_name as "Género",
j.workday_type as "Jornada",
m.work_mode as "Modalidad",
e.hire_date as "Fecha Contratación",
s.status_name as "Estatus",
e.termination_date as "Fecha Baja"
from employees e
left join employee_functions f on e.function_id = f.function_id
left join departments d on e.department_id = d.department_id
left join regions r on e.region_id = r.region_id
left join education_levels ed on e.education_id = ed.education_id
left join genders g on e.gender_id = g.gender_id
left join workday_types j on e.workday_type_id = j.workday_type_id
left join work_modes m on e.work_mode_id = m.work_mode_id
left join employee_status s on e.status_id = s.status_id;
