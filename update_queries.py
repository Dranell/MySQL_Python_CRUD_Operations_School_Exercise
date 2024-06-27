#create a query to update the last name of Stefanie from teacher table to have the last name of green

update_teacher_table = """
update teacher
set last_name = "Green"
where first_name = "Stefanie";
"""