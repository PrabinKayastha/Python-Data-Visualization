query = """select procedure_code, proc_description, sum(total_admits) as admits, ccsdesc, lvl_1_label
    from  {table} where npi in %s and time_id = %s {cwhere} group by procedure_code, proc_description, ccsdesc, lvl_1_label 
    order by procedure_code ASC""".format(table='footprint_proc', cwhere='example')

query = """
    select 
        procedure_code, 
        proc_description, 
        sum(total_admits) as admits, 
        ccsdesc, 
        lvl_1_label
    from  {table} 
    where npi in %s and time_id = %s {cwhere} 
    group by procedure_code, proc_description, ccsdesc, lvl_1_label 
    order by procedure_code ASC
    """.format(table='footprint_proc', cwhere='example')

query = (
    "select "
    "procedure_code, proc_description, sum(total_admits) as admits, ccsdesc, lvl_1_label "
    "from  {table} "
    "where npi in %s and time_id = %s {cwhere} "
    "group by procedure_code, proc_description, ccsdesc, lvl_1_label "
    "order by "
    "procedure_code ASC "
).format(table='footprint_proc', cwhere='example')