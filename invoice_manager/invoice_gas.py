import pdfplumber

from utils import search_regex


def endesa_gas(pdf_path):

    invoice_data = {
        "Fecha": None,
        "€ Fijo": None,
        "€ Energía": None,
        "% Descuento": None,
        "% IVA": None,
        "€ Total": None,
        "€ Endesa X": None,
    }

    with pdfplumber.open(pdf_path) as pdf:

        first_page = pdf.pages[0]
        first_page_text = first_page.extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13)

        second_page = pdf.pages[1]
        top = second_page.search("DETALLE DE LA FACTURA", regex=True)[0]["top"]
        bottom = second_page.search("LECTURAS Y CONSUMOS", regex=True)[0]["bottom"]
        second_page_text = second_page.crop((0, top, second_page.width, bottom)) \
                            .extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13)

        invoice_data["Fecha"] = search_regex(first_page_text, r"(?<=al )\d\d/\d\d/\d\d\d\d")

        invoice_data["€ Fijo"] = search_regex(second_page_text, r"(?<=Fijo Gas .*)(\d,\d+)(?= Eur/día)")
        invoice_data["€ Energía"] = search_regex(second_page_text, r"(?<=Energía Gas .*)(\d,\d+)(?= Eur/kWh)")
        invoice_data["% Descuento"] = search_regex(second_page_text, r"(?<=Dto\. Promocional Gas -)(\d+,\d+)(?= %)")
        invoice_data["% IVA"] = search_regex(second_page_text, r"(?<=IVA .*)(\d+)(?=%)")
        invoice_data["€ Total"] = search_regex(second_page_text, r"(?<=TOTAL IMPORTE FACTURA )(\d+,\d+)(?= €)")
        invoice_data["€ Endesa X"] = search_regex(second_page_text, r"(?<=Endesa X )(\d+,\d+)(?= €)")

    return invoice_data