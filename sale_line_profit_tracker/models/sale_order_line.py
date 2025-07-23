from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    cost_price_total = fields.Monetary(
        string="Cost Subtotal", compute="_compute_profitability", store=True
    )
    profit = fields.Monetary(
        string="Profit", compute="_compute_profitability", store=True
    )
    margin_percent = fields.Float(
        string="Margin %", compute="_compute_profitability", store=True
    )

    @api.depends('product_id', 'product_uom_qty', 'price_subtotal')
    def _compute_profitability(self):
        for line in self:
            cost = line.product_id.standard_price * line.product_uom_qty
            line.cost_price_total = cost
            line.profit = line.price_subtotal - cost
            line.margin_percent = (line.profit / cost * 100) if cost else 0.0

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    locked = fields.Boolean(
        help="Locked orders cannot be modified.",
        default=False,
        copy=False,
        tracking=True)

