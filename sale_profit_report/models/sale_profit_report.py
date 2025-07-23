from odoo import models, fields, api

class SaleProfitReport(models.Model):
    _name = 'sale.profit.report'
    _description = 'Sales Profit Report'
    _auto = False

    order_id = fields.Many2one('sale.order', string="Sales Order")
    date_order = fields.Datetime(related='order_id.date_order', string="Order Date")
    partner_id = fields.Many2one(related='order_id.partner_id', string="Customer")
    amount_total = fields.Monetary(string="Total Amount")
    cost_total = fields.Monetary(string="Total Cost")
    profit_total = fields.Monetary(string="Total Profit")
    currency_id = fields.Many2one('res.currency', string='Currency')

    def init(self):
        self._cr.execute("""
        CREATE OR REPLACE VIEW sale_profit_report AS (
            SELECT
                row_number() OVER() AS id,
                l.order_id AS order_id,
                o.currency_id AS currency_id,
                SUM(l.price_subtotal) AS amount_total,
                SUM(CAST(p.standard_price->>'amount' AS FLOAT) * l.product_uom_qty) AS cost_total,
                SUM(l.price_subtotal - (CAST(p.standard_price->>'amount' AS FLOAT) * l.product_uom_qty)) AS profit_total
            FROM sale_order_line l
            JOIN sale_order o ON l.order_id = o.id
            JOIN product_product p ON l.product_id = p.id
            GROUP BY l.order_id, o.currency_id
        )
    """)