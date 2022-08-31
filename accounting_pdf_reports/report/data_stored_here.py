from odoo import fields, models, api


class ModelName(models.AbstractModel):
    _name = 'report.accounting_pdf_reports.report_template_here'
    _description = 'Description'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['account.financial.print.report'].search([])
        return {
            'docs': docs

        }
