import pandas as pd

class Analytics:
    @staticmethod
    def calculate_summary(df):
        return {
            "total_spending": df["amount"].sum(),
            "avg_order_value": df["amount"].mean(),
            "total_orders": len(df),
            "top_suppliers": df.groupby("supplier")["amount"].sum().nlargest(5).to_dict()
        }
