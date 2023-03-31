import pdfplumber

from utils import search_regex


def iberdrola_light(pdf_path):

    invoice_data = {
        "Fecha": None,
        "Potencia facturada": None,
        "€ Potencia punta": None,
        "€ Potencia valle": None,
        "Energía facturada": None,
        "€ Energía facturada": None,
        "€ Bono social": None,
        "€ Tope precio del gas": None,
        "€ Mecanismo ajuste": None,
        "€ Alquiler equipos medida": None,
        "TOTAL IMPORTE FACTURA": None,
    }

    with pdfplumber.open(pdf_path) as pdf:

        first_page = pdf.pages[0]
        first_page_text = first_page.extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13)
        
        second_page = pdf.pages[1]
        x0 = second_page.search("Potencia facturada", regex=True)[0]["x0"]
        top = second_page.search("Potencia facturada", regex=True)[0]["top"]
        bottom = second_page.search("TOTAL IMPORTE FACTURA", regex=True)[0]["bottom"]
        second_page_text = second_page.crop((x0, top, second_page.width, bottom)) \
                            .extract_text(x_tolerance=3, y_tolerance=3, layout=False, x_density=7.25, y_density=13)

        invoice_data["Fecha"] = search_regex(first_page_text, r"\d\d/\d\d/\d\d\d\d")

        invoice_data["Potencia facturada"] = search_regex(second_page_text, r"(?<=Potencia facturada.*)(\d,\d+)(?= kW)")
        invoice_data["€ Potencia punta"] = search_regex(second_page_text, r"(?<=Punta.*x )(-?0,\d+)(?=\s./kW)")
        invoice_data["€ Potencia valle"] = search_regex(second_page_text, r"(?<=Valle.*x )(-?0,\d+)(?=\s./kW)")
        invoice_data["kW Energía facturada"] = search_regex(second_page_text, r"(?<=Energía facturada.*)(-?\d+)(?= kW)")
        invoice_data["€ Energía facturada"] = search_regex(second_page_text, r"(?<=Energía facturada.*x )(-?0,\d+)(?= ./kW)")
        invoice_data["€ Bono social"] = search_regex(second_page_text, r"(?<=bono social.*x )(-?0,\d+)(?= ./día)")
        invoice_data["€ Tope precio del gas"] = search_regex(second_page_text, r"(?<=Tope precio del gas.*x )(-?0,\d+)(?= ./kW)")
        invoice_data["€ Mecanismo ajuste"] = search_regex(second_page_text, r"(?<=Mecanismo ajuste.*x )(-?0,\d+)(?= ./kW)")
        invoice_data["€ Alquiler equipos medida"] = search_regex(second_page_text, r"(?<=Alquiler equipos medida.*x )(-?0,\d+)(?= ./día)")
        invoice_data["TOTAL IMPORTE FACTURA"] = search_regex(second_page_text, r"(?<=TOTAL IMPORTE FACTURA )(-?\d+,\d+)")

        # print(invoice_data)

    return invoice_data
    