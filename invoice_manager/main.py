from glob import glob

import pandas as pd
from loguru import logger
from utils import set_logger

from invoice_manager import get_invoice_data


def main():
    set_logger()

    for invoice_type in glob("../data/*"):
        results = []
        for pdf_path in glob(f"{invoice_type}/*/*.pdf"):
            logger.info(pdf_path)

            invoice_data = get_invoice_data(pdf_path)
            if invoice_data:
                results.append(invoice_data)
            else:
                logger.warning(f"WARNING: No se ha podido leer la factura {pdf_path}")
        
        if results:
            df = pd.DataFrame(results)
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")
            df = df.sort_values(by="Fecha")
            print(df)


if __name__ == "__main__":
    main()
