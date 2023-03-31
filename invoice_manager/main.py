from glob import glob
import pandas as pd

from invoice_manager import get_invoice_data


def main():
    results = []

    for pdf_path in glob("../data/*/*/*.pdf"):
        print(pdf_path)

        invoice_data = get_invoice_data(pdf_path)
        
        results.append(invoice_data)


    df = pd.DataFrame(results)
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")
    df = df.sort_values(by="Fecha")

    print(df)


if __name__ == "__main__":
    main()
