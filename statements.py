from quatro import log, sql_query, scalar_data, tabular_data, configuration as c


def outstanding_purchase_order_purchasers():
    sql_exp = f"""
    SELECT DISTINCT usr_name
    
    FROM purchase_order_line
    JOIN purchase_order_header USING(puh_id)
    
    WHERE pul_prch_qty > pul_rcvd_qty
    AND pul_req_dt IS NOT NULL
    AND pul_req_dt = now()::DATE + '2 days'::INTERVAL
    """
    log(sql_exp)
    result_set = sql_query(sql_exp, c.config.sigm_db_cursor)
    return tabular_data(result_set)


def outstanding_purchase_order_suppliers(usr_name):
    sql_exp = f"""
    SELECT DISTINCT sup_id

    FROM purchase_order_line
    JOIN purchase_order_header USING(puh_id)

    WHERE pul_prch_qty > pul_rcvd_qty
    AND pul_req_dt IS NOT NULL
    AND pul_req_dt = now()::DATE + '2 days'::INTERVAL
    AND usr_name = '{usr_name}'
    """
    log(sql_exp)
    result_set = sql_query(sql_exp, c.config.sigm_db_cursor)
    return tabular_data(result_set)


def outstanding_purchase_order_numbers(sup_id):
    sql_exp = f"""
    SELECT DISTINCT puh_no

    FROM purchase_order_line
    JOIN purchase_order_header USING(puh_id)

    WHERE pul_prch_qty > pul_rcvd_qty
    AND pul_req_dt IS NOT NULL
    AND pul_req_dt = now()::DATE + '2 days'::INTERVAL
    AND sup_id = {sup_id}
    """
    log(sql_exp)
    result_set = sql_query(sql_exp, c.config.sigm_db_cursor)
    return tabular_data(result_set)


def get_sup_name1(sup_id):
    sql_exp = f"SELECT sup_name1 FROM supplier WHERE sup_id = {sup_id}"
    log(sql_exp)
    result_set = sql_query(sql_exp, c.config.sigm_db_cursor)
    return scalar_data(result_set)


if __name__ == "__main__":
    outstanding_purchase_order_purchasers()
