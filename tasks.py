from quatro import send_email
from files import outstanding_pos_ninja, delete_pdfs
from statements import outstanding_purchase_order_purchasers, \
    outstanding_purchase_order_suppliers, get_sup_name1, outstanding_purchase_order_numbers


def outstanding_pos_task():
    for purchaser in outstanding_purchase_order_purchasers():
        for sup_id in outstanding_purchase_order_suppliers(purchaser[0]):
            sup_name = get_sup_name1(sup_id[0])
            pdfs = []
            for po_number in outstanding_purchase_order_numbers(sup_id[0]):
                pdf = outstanding_pos_ninja(po_number[0])
                pdfs.append(pdf)
            subject = f"Purchasing Followup - {purchaser[0]} - {sup_name}"
            send_email('TEST', ['jan.z@quatroair.com'], [], pdfs, subject)
    delete_pdfs()


if __name__ == "__main__":
    outstanding_pos_task()
