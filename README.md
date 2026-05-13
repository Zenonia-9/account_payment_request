# Account Payment Request

![Odoo 19](https://img.shields.io/badge/Odoo-19.0-875A7B?style=flat-square)
![License](https://img.shields.io/badge/License-LGPL--3-blue?style=flat-square)
![Category](https://img.shields.io/badge/Category-Accounting-4ECDC4?style=flat-square)

Create and print payment request documents directly from posted vendor bills in Odoo 19.

This module adds a guided payment-request flow on `account.move` so accounting users can select one or more posted vendor bills, review request options in a wizard, and print a dedicated payment request PDF in either A4 or A5 format.

## Highlights

- Adds a **Payment Request** action on vendor bills.
- Supports **single-bill and multi-bill** request flows.
- Validates that only **posted bills** are used.
- Blocks miscellaneous journal entries from entering the request flow.
- Opens a wizard with **request date**, **group request**, and **paper size** options.
- Auto-suggests paper size based on the number of selected bills.
- Ships with dedicated **QWeb report templates**, **paper formats**, and a local report layout.

## Workflow

1. Open posted vendor bills.
2. Click the **Payment Request** action.
3. Confirm the request date and grouping options in the wizard.
4. Choose A4 or A5 output.
5. Print the payment request PDF.

## Technical Notes

- `models/account_move.py`
  Adds the entry action on `account.move` and enforces selection rules before opening the wizard.
- `wizard/payment_request_wizard.py`
  Collects request options, computes totals, and routes printing to the correct report action.
- `report/payment_request_report.py`
  Provides shared report values for the A4 and A5 payment request report models.
- `report/payment_request_layout.xml`
  Keeps the report layout local to this addon instead of altering global report templates.

## Module Layout

```text
account_payment_request/
|-- models/
|-- wizard/
|-- report/
|-- security/
|-- views/
`-- __manifest__.py
```

## Dependencies

- `account`
- `web`

## Installation

1. Place the module in your custom addons path.
2. Update the Apps list in Odoo.
3. Install **Account Payment Request**.

## License

This module is licensed under `LGPL-3`.
