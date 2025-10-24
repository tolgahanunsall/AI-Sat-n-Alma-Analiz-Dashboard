import pandas as pd


def process_excel(df: pd.DataFrame):
    # Normalize column names to handle potential whitespace/casing
    df = df.rename(columns={c: c.strip() for c in df.columns})

    # Expecting columns: 'Fiş Tarihi', 'Tutar', 'YIL', 'AY', 'Cari Hesap Unvanı'
    if 'Fiş Tarihi' in df.columns:
        df['Fiş Tarihi'] = pd.to_datetime(df['Fiş Tarihi'], errors='coerce')

    if 'Tutar' not in df.columns:
        raise ValueError("'Tutar' column is required")

    summary = {
        "toplam_tutar": float(df['Tutar'].sum()),
    }

    if 'YIL' in df.columns:
        yearly = df.groupby('YIL')['Tutar'].sum()
        if not yearly.empty:
            summary["yillik_ortalama"] = float(yearly.mean())
        else:
            summary["yillik_ortalama"] = 0.0
    else:
        summary["yillik_ortalama"] = 0.0

    if 'Cari Hesap Unvanı' in df.columns:
        supplier_sum = df.groupby('Cari Hesap Unvanı')['Tutar'].sum()
        if not supplier_sum.empty:
            summary["top_tedarikci"] = supplier_sum.idxmax()
        else:
            summary["top_tedarikci"] = None
    else:
        summary["top_tedarikci"] = None

    return summary
