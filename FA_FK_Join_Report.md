# FA 2.4.3 Phase 2: Join / Foreign Key Analysis

Schema extracted from `.sql` files.

| Table | Columns | PK | Keys | Missing FK Notes |
|-------|---------|----|------|------------------|
| `0_areas` | 0_areas, description, inactive, description, 0_attachments | `area_code` | description(`description`) |  |
| `0_attachments` | 0_attachments, description, type_no, trans_no, unique_name, tran_date, filename, filesize, filetype, type_no, 0_attachments | `id` | type_no(`type_no`,`trans_no`) |  |
| `0_audit_trail` | 0_audit_trail, type, trans_no, user, stamp, description, fiscal_year, gl_date, gl_seq, Seq, Type_and_Number, 0_audit_trail | `id` | Seq(`fiscal_year`,`gl_date`,`gl_seq`); Type_and_Number(`type`,`trans_no`) |  |
| `0_bank_accounts` | 0_bank_accounts, account_type, bank_account_name, bank_account_number, bank_name, bank_address, bank_curr_code, dflt_curr_act, id, bank_charge_act, last_reconciled_date, ending_reconcile_balance, inactive, bank_account_name, bank_account_number... | `id` | bank_account_name(`bank_account_name`); bank_account_number(`bank_account_number`); account_code(`account_code`) |  |
| `0_bank_trans` | 0_bank_trans, type, trans_no, bank_act, ref, trans_date, amount, dimension_id, dimension2_id, person_type_id, person_id, reconciled, bank_act, type, bank_act_2... | `id` | bank_act(`bank_act`,`ref`); type(`type`,`trans_no`); bank_act_2(`bank_act`,`reconciled`); bank_act_3(`bank_act`,`trans_date`) |  |
| `0_bom` | 0_bom, parent, component, workcentre_added, loc_code, quantity, component, id, loc_code, parent, workcentre_added | `NONE` | component(`component`); id(`id`); loc_code(`loc_code`); parent(`parent`,`loc_code`); workcentre_added(`workcentre_added`) |  |
| `0_budget_trans` | 0_budget_trans, tran_date, account, memo_, amount, dimension_id, dimension2_id, Account, 0_budget_trans | `id` | Account(`account`,`tran_date`,`dimension_id`,`dimension2_id`) |  |
| `0_chart_class` | 0_chart_class, class_name, ctype, inactive, 0_chart_class, 0_chart_class, 0_chart_class, 0_chart_class, 0_chart_master | `cid` |  | No non-PK indexes; joins may miss keys. |
| `0_chart_master` | 0_chart_master, account_code2, account_name, account_type, inactive, account_name, accounts_by_type, 0_chart_master, 0_chart_master, 0_chart_master, 0_chart_master, 0_chart_master, 0_chart_master, 0_chart_master, 0_chart_master... | `account_code` | account_name(`account_name`); accounts_by_type(`account_type`,`account_code`) |  |
| `0_chart_types` | 0_chart_types, name, class_id, parent, inactive, name, class_id, 0_chart_types, 0_chart_types, 0_chart_types, 0_chart_types, 0_chart_types, 0_chart_types, 0_chart_types, 0_chart_types... | `id` | name(`name`); class_id(`class_id`) |  |
| `0_comments` | 0_comments, id, date_, memo_, type_and_id, 0_comments | `NONE` | type_and_id(`type`,`id`) |  |
| `0_credit_status` | 0_credit_status, reason_description, dissallow_invoices, inactive, reason_description, 0_credit_status, 0_credit_status, 0_crm_categories | `id` | reason_description(`reason_description`) |  |
| `0_crm_categories` | 0_crm_categories, type, action, name, description, system, inactive, type, type_2, 0_crm_categories, 0_crm_categories, 0_crm_categories, 0_crm_categories, 0_crm_categories, 0_crm_categories... | `id` | type(`type`,`action`); type_2(`type`,`name`) |  |
| `0_crm_contacts` | 0_crm_contacts, person_id, type, action, entity_id, type, 0_crm_contacts | `id` | type(`type`,`action`) |  |
| `0_crm_persons` | 0_crm_persons, ref, name, name2, address, phone, phone2, fax, email, lang, notes, inactive, ref | `id` | ref(`ref`) |  |
| `0_currencies` | 0_currencies, curr_abrev, curr_symbol, country, hundreds_name, auto_update, inactive, 0_currencies, 0_currencies, 0_currencies, 0_currencies, 0_cust_allocations | `curr_abrev` |  | No non-PK indexes; joins may miss keys. |
| `0_cust_allocations` | 0_cust_allocations, person_id, amt, date_alloc, trans_no_from, trans_type_from, trans_no_to, trans_type_to, trans_type_from, From, To, 0_cust_allocations | `id` | trans_type_from(`person_id`,`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`); From(`trans_type_from`,`trans_no_from`); To(`trans_type_to`,`trans_no_to`) |  |
| `0_cust_branch` | 0_cust_branch, debtor_no, br_name, branch_ref, br_address, area, salesman, default_location, tax_group_id, sales_account, sales_discount_account, receivables_account, payment_discount_account, default_ship_via, br_post_address... | `NONE` | branch_ref(`branch_ref`); group_no(`group_no`) |  |
| `0_debtor_trans` | 0_debtor_trans, type, version, debtor_no, branch_code, tran_date, due_date, reference, tpe, order_, ov_amount, ov_gst, ov_freight, ov_freight_tax, ov_discount... | `NONE` | debtor_no(`debtor_no`,`branch_code`); tran_date(`tran_date`); order_(`order_`) |  |
| `0_debtor_trans_details` | 0_debtor_trans_details, debtor_trans_no, debtor_trans_type, stock_id, description, unit_price, unit_tax, quantity, discount_percent, standard_cost, qty_done, src_id, Transaction, 0_debtor_trans_details | `id` | Transaction(`debtor_trans_type`,`debtor_trans_no`) |  |
| `0_debtors_master` | 0_debtors_master, name, debtor_ref, address, tax_id, curr_code, sales_type, dimension_id, dimension2_id, credit_status, payment_terms, discount, pymt_discount, credit_limit, notes... | `debtor_no` | name(`name`); debtor_ref(`debtor_ref`) |  |
| `0_dimensions` | 0_dimensions, reference, name, type_, closed, date_, due_date, reference, date_, due_date, type_ | `id` | reference(`reference`); date_(`date_`); due_date(`due_date`); type_(`type_`) |  |
| `0_exchange_rates` | 0_exchange_rates, curr_code, rate_buy, rate_sell, date_, curr_code, 0_exchange_rates | `id` | curr_code(`curr_code`,`date_`) |  |
| `0_fiscal_year` | 0_fiscal_year, begin, end, closed, begin, end, 0_gl_trans | `id` | begin(`begin`); end(`end`) |  |
| `0_gl_trans` | 0_gl_trans, type, type_no, tran_date, account, memo_, amount, dimension_id, dimension2_id, person_type_id, person_id, Type_and_Number, dimension_id, dimension2_id, tran_date... | `counter` | Type_and_Number(`type`,`type_no`); dimension_id(`dimension_id`); dimension2_id(`dimension2_id`); tran_date(`tran_date`); account_and_tran_date(`account`,`tran_date`) |  |
| `0_grn_batch` | 0_grn_batch, supplier_id, purch_order_no, reference, delivery_date, loc_code, rate, delivery_date, purch_order_no | `id` | delivery_date(`delivery_date`); purch_order_no(`purch_order_no`) |  |
| `0_grn_items` | 0_grn_items, grn_batch_id, po_detail_item, item_code, description, qty_recd, quantity_inv, grn_batch_id | `id` | grn_batch_id(`grn_batch_id`) |  |
| `0_groups` | 0_groups, description, inactive, description, 0_groups, 0_groups, 0_item_codes | `id` | description(`description`) |  |
| `0_item_codes` | 0_item_codes, item_code, stock_id, description, category_id, quantity, is_foreign, inactive, stock_id, item_code | `id` | stock_id(`stock_id`,`item_code`); item_code(`item_code`) |  |
| `0_item_tax_type_exemptions` | 0_item_tax_type_exemptions, tax_type_id, 0_item_tax_type_exemptions | `NONE` |  | No non-PK indexes; joins may miss keys. |
| `0_item_tax_types` | 0_item_tax_types, name, exempt, inactive, name, 0_item_tax_type_exemptions | `id` | name(`name`) |  |
| `0_item_units` | 0_item_units, name, decimals, inactive, name, 0_item_units, 0_journal | `abbr` | name(`name`) |  |
| `0_loc_stock` | 0_loc_stock, stock_id, reorder_level, stock_id | `NONE` | stock_id(`stock_id`) |  |
| `0_locations` | 0_locations, location_name, delivery_address, phone, phone2, fax, email, contact, fixed_asset, inactive, 0_locations, 0_loc_stock | `loc_code` |  | No non-PK indexes; joins may miss keys. |
| `0_payment_terms` | 0_payment_terms, terms, days_before_due, day_in_following_month, inactive, terms, 0_payment_terms, 0_payment_terms, 0_payment_terms, 0_prices | `terms_indicator` | terms(`terms`) |  |
| `0_prices` | 0_prices, stock_id, sales_type_id, curr_abrev, price, price, 0_prices | `id` | price(`stock_id`,`sales_type_id`,`curr_abrev`) |  |
| `0_print_profiles` | 0_print_profiles, profile, report, printer, profile, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_print_profiles, 0_purch_data | `id` | profile(`profile`,`report`) |  |
| `0_printers` | 0_printers, name, description, queue, host, port, timeout, name, 0_printers, 0_printers, 0_print_profiles | `id` | name(`name`) |  |
| `0_purch_data` | 0_purch_data, stock_id, price, suppliers_uom, conversion_factor, supplier_description, 0_purch_data | `NONE` |  | No non-PK indexes; joins may miss keys. |
| `0_purch_order_details` | 0_purch_order_details, order_no, item_code, description, delivery_date, qty_invoiced, unit_price, act_price, std_cost_unit, quantity_ordered, quantity_received, order, itemcode | `po_detail_item` | order(`order_no`,`po_detail_item`); itemcode(`item_code`) |  |
| `0_purch_orders` | 0_purch_orders, supplier_id, comments, ord_date, reference, requisition_no, into_stock_location, delivery_address, total, prep_amount, alloc, tax_included, ord_date | `order_no` | ord_date(`ord_date`) |  |
| `0_quick_entries` | 0_quick_entries, type, description, usage, base_amount, base_desc, bal_type, description, 0_quick_entries, 0_quick_entries, 0_quick_entry_lines | `id` | description(`description`) |  |
| `0_quick_entry_lines` | 0_quick_entry_lines, qid, amount, memo, action, dest_id, dimension_id, dimension2_id, qid, 0_quick_entry_lines, 0_quick_entry_lines, 0_quick_entry_lines, 0_quick_entry_lines, 0_quick_entry_lines, 0_recurrent_invoices | `id` | qid(`qid`) |  |
| `0_recurrent_invoices` | 0_recurrent_invoices, description, order_no, debtor_no, group_no, days, monthly, begin, end, last_sent, description | `id` | description(`description`) |  |
| `0_refs` | 0_refs, type, reference, Type_and_Reference, 0_refs | `NONE` | Type_and_Reference(`type`,`reference`) |  |
| `0_sales_order_details` | 0_sales_order_details, order_no, trans_type, stk_code, description, qty_sent, unit_price, quantity, invoiced, discount_percent, sorder, stkcode | `id` | sorder(`trans_type`,`order_no`); stkcode(`stk_code`) |  |
| `0_sales_orders` | 0_sales_orders, trans_type, version, type, debtor_no, branch_code, reference, customer_ref, comments, ord_date, order_type, ship_via, delivery_address, contact_phone, contact_email... | `NONE` |  | No non-PK indexes; joins may miss keys. |
| `0_sales_pos` | 0_sales_pos, pos_name, cash_sale, credit_sale, pos_location, pos_account, inactive, pos_name, 0_sales_types | `id` | pos_name(`pos_name`) |  |
| `0_sales_types` | 0_sales_types, sales_type, tax_included, factor, inactive, sales_type, 0_sales_types, 0_security_roles | `id` | sales_type(`sales_type`) |  |
| `0_salesman` | 0_salesman, salesman_name, salesman_phone, salesman_fax, salesman_email, provision, break_pt, provision2, inactive, salesman_name, 0_sales_orders | `salesman_code` | salesman_name(`salesman_name`) |  |
| `0_security_roles` | 0_security_roles, role, description, sections, areas, inactive, role, 0_security_roles, 0_security_roles, 0_security_roles, 0_security_roles, 0_security_roles, 0_security_roles, 0_security_roles, 0_security_roles... | `id` | role(`role`) |  |
| `0_shippers` | 0_shippers, shipper_name, phone, phone2, contact, address, inactive, name, 0_sql_trail | `shipper_id` | name(`shipper_name`) |  |
| `0_sql_trail` | 0_sql_trail, sql, result, msg, 0_sql_trail | `id` |  | No non-PK indexes; joins may miss keys. |
| `0_stock_category` | 0_stock_category, description, dflt_tax_type, dflt_units, dflt_mb_flag, dflt_sales_act, dflt_cogs_act, dflt_inventory_act, dflt_adjustment_act, dflt_wip_act, dflt_dim1, dflt_dim2, inactive, dflt_no_sale, dflt_no_purchase... | `category_id` | description(`description`) |  |
| `0_stock_master` | 0_stock_master, category_id, tax_type_id, description, long_description, units, mb_flag, sales_account, cogs_account, inventory_account, adjustment_account, wip_account, dimension_id, dimension2_id, purchase_cost... | `stock_id` |  | No non-PK indexes; joins may miss keys. |
| `0_supp_allocations` | 0_supp_allocations, person_id, amt, date_alloc, trans_no_from, trans_type_from, trans_no_to, trans_type_to, trans_type_from, From, To, 0_supp_allocations | `id` | trans_type_from(`person_id`,`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`); From(`trans_type_from`,`trans_no_from`); To(`trans_type_to`,`trans_no_to`) |  |
| `0_supp_invoice_items` | 0_supp_invoice_items, supp_trans_no, supp_trans_type, gl_code, grn_item_id, po_detail_item_id, stock_id, description, quantity, unit_price, unit_tax, memo_, dimension_id, dimension2_id, Transaction... | `id` | Transaction(`supp_trans_type`,`supp_trans_no`,`stock_id`) |  |
| `0_supp_trans` | 0_supp_trans, type, supplier_id, reference, supp_reference, tran_date, due_date, ov_amount, ov_discount, ov_gst, rate, alloc, tax_included, supplier_id, tran_date | `NONE` | supplier_id(`supplier_id`); tran_date(`tran_date`) |  |
| `0_suppliers` | 0_suppliers, supp_name, supp_ref, address, supp_address, gst_no, contact, supp_account_no, website, bank_account, curr_code, payment_terms, tax_included, dimension_id, dimension2_id... | `supplier_id` | supp_ref(`supp_ref`) |  |
| `0_sys_prefs` | 0_sys_prefs, category, type, length, value, category, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs, 0_sys_prefs... | `name` | category(`category`) |  |
| `0_tag_associations` | 0_tag_associations, tag_id, record_id, 0_tag_associations | `NONE` | record_id(`record_id`,`tag_id`) |  |
| `0_tags` | 0_tags, type, name, description, inactive, type, 0_tags | `id` | type(`type`,`name`) |  |
| `0_tax_group_items` | 0_tax_group_items, tax_type_id, tax_shipping, 0_tax_group_items, 0_tax_types | `NONE` |  | No non-PK indexes; joins may miss keys. |
| `0_tax_groups` | 0_tax_groups, name, inactive, name, 0_tax_groups, 0_tax_group_items | `id` | name(`name`) |  |
| `0_tax_types` | 0_tax_types, rate, sales_gl_code, purchasing_gl_code, name, inactive, 0_tax_types, 0_trans_tax_details | `id` |  | No non-PK indexes; joins may miss keys. |
| `0_trans_tax_details` | 0_trans_tax_details, trans_type, trans_no, tran_date, tax_type_id, rate, ex_rate, included_in_price, net_amount, amount, memo, reg_type, Type_and_Number, tran_date | `id` | Type_and_Number(`trans_type`,`trans_no`); tran_date(`tran_date`) |  |
| `0_useronline` | 0_useronline, timestamp, ip, file, timestamp, ip | `id` | timestamp(`timestamp`); ip(`ip`) |  |
| `0_users` | 0_users, user_id, password, real_name, role_id, phone, email, language, date_format, date_sep, tho_sep, dec_sep, theme, page_size, prices_dec... | `id` | user_id(`user_id`) |  |
| `0_voided` | 0_voided, id, date_, memo_, id, 0_voided | `NONE` | id(`type`,`id`) |  |
| `0_wo_issue_items` | 0_wo_issue_items, stock_id, issue_id, qty_issued, unit_cost, 0_wo_issue_items | `id` |  | No non-PK indexes; joins may miss keys. |
| `0_wo_issues` | 0_wo_issues, workorder_id, reference, issue_date, loc_code, workcentre_id, workorder_id | `issue_no` | workorder_id(`workorder_id`) |  |
| `0_wo_manufacture` | 0_wo_manufacture, reference, workorder_id, quantity, date_, workorder_id | `id` | workorder_id(`workorder_id`) |  |
| `0_wo_requirements` | 0_wo_requirements, workorder_id, stock_id, workcentre, units_req, unit_cost, loc_code, units_issued, workorder_id | `id` | workorder_id(`workorder_id`) |  |
| `0_workcentres` | 0_workcentres, name, description, inactive, name | `id` | name(`name`) |  |
| `0_workorders` | 0_workorders, wo_ref, loc_code, units_reqd, stock_id, date_, type, required_by, released_date, units_issued, closed, released, additional_costs, wo_ref | `id` | wo_ref(`wo_ref`) |  |

---
**Recommendation:** Tables with no foreign-key constraints should have FK checks added for common join pairs observed in queries (e.g., `debtor_trans.debtor_no` -> `debtors_master.debtor_no`).

Next: Decompose joins from `FA_Queries.md` and cross-reference with schema above.
