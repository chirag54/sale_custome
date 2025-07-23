{
    "name": "Sale Profit Report",
    "version": "18.0.1.0.0",
    "author": "Chirag Chauhan",
    "license": "AGPL-3",
    "category": "Sales",
    "summary": "Report for Sales Profitability",
    "depends": ["sale", "stock", "account"],
    "data": [
        "views/sale_profit_report_view.xml",
        "security/ir.model.access.csv"
    ],
    "installable": True,
    "application": False,
    "development_status": "Alpha",
    "maintainers": ["chirag"],
    'price': 8.00,
    'currency': 'EUR',
}