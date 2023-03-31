from invoice_light import iberdrola_light
from invoice_gas import endesa_gas


def get_invoice_data(pdf_path):

    invoice_type = pdf_path.split("/")[-3]
    invoice_company = pdf_path.split("/")[-2]

    if invoice_type == "light":
        if invoice_company == "iberdrola":
            return iberdrola_light(pdf_path)
    elif invoice_type == "gas":
        if invoice_company == "endesa":
            return endesa_gas(pdf_path)

    return None