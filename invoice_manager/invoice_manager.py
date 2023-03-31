from light_invoice import iberdrola_light


def get_invoice_data(pdf_path):

    invoice_type = pdf_path.split("/")[-3]
    invoice_company = pdf_path.split("/")[-2]

    if invoice_type == "light":
        if invoice_company == "iberdrola":
            return iberdrola_light(pdf_path)

    return None