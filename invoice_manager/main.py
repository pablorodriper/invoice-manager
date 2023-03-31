from glob import glob
import pandas as pd

from invoice_manager import get_invoice_data


def main():
    for invoice_type in glob("../data/*"):
        results = []
        for pdf_path in glob(f"../data/{invoice_type}/*/*.pdf"):
            print(pdf_path)

            invoice_data = get_invoice_data(pdf_path)
            if invoice_data:
                results.append(invoice_data)
            else:
                print(f"WARNING: No se ha podido leer la factura {pdf_path}")
        
        if results:
            df = pd.DataFrame(results)
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")
            df = df.sort_values(by="Fecha")
            print(df)




if __name__ == "__main__":
    main()
