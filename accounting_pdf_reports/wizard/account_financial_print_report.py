from odoo import fields, models, api


class AccountFinancialReport(models.TransientModel):
    _name = 'account.financial.print.report'
    _inherit = 'account.common.partner.report'
    _description = ''

    name = fields.Char()
    age = fields.Integer()

    # journal_ids = fields.Many2many('account.journal', string='Journals', required=True)
    def print_here(self):
        data = {
            # 'model': 'account.financial.print.report',
            'form_data': self.read()[0]
        }
        return self.env.ref('accounting_pdf_reports.account_financial_print_report_rec').report_action(self,data=data)
