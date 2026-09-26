# FA 2.4.3 Functional Query Inventory (CRUD / Forms / Displays)

Excludes: SQL install/update scripts, reporting queries, docs.
Includes: access, admin, applications, company, dimensions, fixed_assets, gl, inventory, manufacturing, modules, purchasing, sales, taxes, includes/db.

| File | Line | SQL Snippet / Context |
|------|------|-----------------------|
| `admin/db/attachments_db.inc` | 19 | `$sql = "INSERT INTO ".TB_PREF."attachments (type_no, trans_no, description, filename, unique_name,` |
| `admin/db/attachments_db.inc` | 32 | `$sql = "UPDATE ".TB_PREF."attachments SET` |
| `admin/db/attachments_db.inc` | 51 | `$sql = "DELETE FROM ".TB_PREF."attachments WHERE id = ".db_escape($id);` |
| `admin/db/attachments_db.inc` | 52 | `db_query($sql, "Could not delete attachment");` |
| `admin/db/attachments_db.inc` | 61 | `$sql = "SELECT * FROM ".TB_PREF."attachments WHERE type_no=".db_escape($type)." AND trans_no=".db_escape($id)." ORDER BY trans_no";` |
| `admin/db/attachments_db.inc` | 77 | `$sql = "SELECT * FROM ".TB_PREF."attachments WHERE type_no=".db_escape($type)` |
| `admin/db/attachments_db.inc` | 84 | `$sql = "SELECT * FROM ".TB_PREF."attachments WHERE id=".db_escape($id);` |
| `admin/db/attachments_db.inc` | 91 | `$sql = "SELECT DISTINCT * FROM ".TB_PREF."attachments WHERE type_no=".db_escape($type)." AND trans_no=".db_escape($id);` |
| `admin/db/attachments_db.inc` | 102 | `return "SELECT trans_no, description, filename, filesize, filetype, tran_date, id, type_no FROM ".TB_PREF."attachments WHERE type_no=".db_escape($type)` |
| `admin/db/attachments_db.inc` | 108 | `$sql = "UPDATE ".TB_PREF."attachments SET trans_no=".db_escape($trans_to)` |
| `admin/db/company_db.inc` | 17 | `$sql = "UPDATE ".TB_PREF."sys_prefs SET value = ";` |
| `admin/db/company_db.inc` | 83 | `$sql = "INSERT INTO ".TB_PREF."payment_terms (terms,` |
| `admin/db/company_db.inc` | 90 | `$sql = "INSERT INTO ".TB_PREF."payment_terms (terms,` |
| `admin/db/company_db.inc` | 102 | `$sql = "UPDATE ".TB_PREF."payment_terms SET terms=" . db_escape($terms) . ",` |
| `admin/db/company_db.inc` | 109 | `$sql = "UPDATE ".TB_PREF."payment_terms SET terms=" . db_escape($terms) . ",` |
| `admin/db/company_db.inc` | 119 | `$sql="DELETE FROM ".TB_PREF."payment_terms WHERE terms_indicator=".db_escape($selected_id);` |
| `admin/db/company_db.inc` | 120 | `db_query($sql,"could not delete a payment terms");` |
| `admin/db/company_db.inc` | 125 | `$sql = "SELECT *, (t.days_before_due=0) AND (t.day_in_following_month=0) as cash_sale` |
| `admin/db/company_db.inc` | 135 | `$sql = "SELECT * FROM ".TB_PREF."payment_terms";` |
| `admin/db/company_db.inc` | 158 | `$sqls[] = "(SELECT COUNT(*) as cnt FROM `".TB_PREF."$tbl` WHERE `$key`=".db_escape($id).")\n";` |
| `admin/db/company_db.inc` | 161 | `$sql = "SELECT sum(cnt) FROM (". implode(' UNION ', $sqls).") as counts";` |
| `admin/db/company_db.inc` | 182 | `$sql = "UPDATE {$conn['tbpref']}users SET theme='default' WHERE theme='$theme'";` |
| `admin/db/company_db.inc` | 183 | `if (!db_query($sql, 'Cannot update user theme settings'))` |
| `admin/db/fiscalyears_db.inc` | 20 | `$sql = "INSERT INTO ".TB_PREF."fiscal_year (begin, end, closed)` |
| `admin/db/fiscalyears_db.inc` | 28 | `$sql = "UPDATE ".TB_PREF."fiscal_year SET closed=".db_escape($closed)."` |
| `admin/db/fiscalyears_db.inc` | 31 | `db_query($sql, "could not update fiscal year");` |
| `admin/db/fiscalyears_db.inc` | 36 | `$sql = "SELECT * FROM ".TB_PREF."fiscal_year ORDER BY begin";` |
| `admin/db/fiscalyears_db.inc` | 43 | `$sql = "SELECT * FROM ".TB_PREF."fiscal_year WHERE id=".db_escape($id);` |
| `admin/db/fiscalyears_db.inc` | 54 | `$sql = "SELECT * FROM ".TB_PREF."fiscal_year WHERE id=".db_escape($year);` |
| `admin/db/fiscalyears_db.inc` | 66 | `$sql="DELETE FROM ".TB_PREF."fiscal_year WHERE id=".db_escape($id);` |
| `admin/db/fiscalyears_db.inc` | 68 | `db_query($sql, "could not delete fiscal year");` |
| `admin/db/fiscalyears_db.inc` | 76 | `$sql = "SELECT * FROM ".TB_PREF."fiscal_year WHERE '$date' >= begin AND '$date' <= end";` |
| `admin/db/fiscalyears_db.inc` | 86 | `$sql = "SELECT begin FROM ".TB_PREF."fiscal_year WHERE '$date' >= begin AND '$date' <= end";` |
| `admin/db/fiscalyears_db.inc` | 97 | `$sql = "SELECT MAX(end), MIN(begin) FROM ".TB_PREF."fiscal_year";` |
| `admin/db/fiscalyears_db.inc` | 109 | `$sql = "SELECT MAX(end) FROM ".TB_PREF."fiscal_year";` |
| `admin/db/fiscalyears_db.inc` | 120 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."fiscal_year WHERE begin < '$date'";` |
| `admin/db/fiscalyears_db.inc` | 151 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."gl_trans INNER JOIN ".TB_PREF."chart_master ON account=account_code` |
| `admin/db/fiscalyears_db.inc` | 192 | `$sql = "SELECT * FROM ".TB_PREF."attachments WHERE type_no = $type_no AND trans_no = $trans_no";` |
| `admin/db/fiscalyears_db.inc` | 204 | `$sql = "DELETE FROM ".TB_PREF."attachments WHERE  type_no = $type_no AND trans_no = $trans_no";` |
| `admin/db/fiscalyears_db.inc` | 205 | `db_query($sql, "Could not delete attachment");` |
| `admin/db/fiscalyears_db.inc` | 207 | `$sql = "DELETE FROM ".TB_PREF."comments WHERE  type = $type_no AND id = $trans_no";` |
| `admin/db/fiscalyears_db.inc` | 208 | `db_query($sql, "Could not delete comments");` |
| `admin/db/fiscalyears_db.inc` | 209 | `$sql = "DELETE FROM ".TB_PREF."refs WHERE  type = $type_no AND id = $trans_no";` |
| `admin/db/fiscalyears_db.inc` | 210 | `db_query($sql, "Could not delete refs");` |
| `admin/db/fiscalyears_db.inc` | 223 | `$sql = "SELECT order_no, trans_type FROM ".TB_PREF."sales_orders WHERE ord_date <= '$to' AND type <> 1"; // don't take the templates` |
| `admin/db/fiscalyears_db.inc` | 227 | `$sql = "SELECT SUM(qty_sent), SUM(quantity) FROM ".TB_PREF."sales_order_details WHERE order_no = {$row['order_no']} AND trans_type = {$row['trans_type']}";` |
| `admin/db/fiscalyears_db.inc` | 232 | `$sql = "DELETE FROM ".TB_PREF."sales_order_details WHERE order_no = {$row['order_no']} AND trans_type = {$row['trans_type']}";` |
| `admin/db/fiscalyears_db.inc` | 233 | `db_query($sql, "Could not delete sales order details");` |
| `admin/db/fiscalyears_db.inc` | 234 | `$sql = "DELETE FROM ".TB_PREF."sales_orders WHERE order_no = {$row['order_no']} AND trans_type = {$row['trans_type']}";` |
| `admin/db/fiscalyears_db.inc` | 235 | `db_query($sql, "Could not delete sales order");` |
| `admin/db/fiscalyears_db.inc` | 239 | `$sql = "SELECT order_no FROM ".TB_PREF."purch_orders WHERE ord_date <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 243 | `$sql = "SELECT SUM(quantity_ordered), SUM(quantity_received) FROM ".TB_PREF."purch_order_details WHERE order_no = {$row['order_no']}";` |
| `admin/db/fiscalyears_db.inc` | 248 | `$sql = "DELETE FROM ".TB_PREF."purch_order_details WHERE order_no = {$row['order_no']}";` |
| `admin/db/fiscalyears_db.inc` | 249 | `db_query($sql, "Could not delete purchase order details");` |
| `admin/db/fiscalyears_db.inc` | 250 | `$sql = "DELETE FROM ".TB_PREF."purch_orders WHERE order_no = {$row['order_no']}";` |
| `admin/db/fiscalyears_db.inc` | 251 | `db_query($sql, "Could not delete purchase order");` |
| `admin/db/fiscalyears_db.inc` | 255 | `$sql = "SELECT id FROM ".TB_PREF."grn_batch WHERE delivery_date <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 259 | `$sql = "DELETE FROM ".TB_PREF."grn_items WHERE grn_batch_id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 260 | `db_query($sql, "Could not delete grn items");` |
| `admin/db/fiscalyears_db.inc` | 261 | `$sql = "DELETE FROM ".TB_PREF."grn_batch WHERE id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 262 | `db_query($sql, "Could not delete grn batch");` |
| `admin/db/fiscalyears_db.inc` | 265 | `$sql = "SELECT trans_no, type FROM ".TB_PREF."debtor_trans WHERE tran_date <= '$to' AND` |
| `admin/db/fiscalyears_db.inc` | 275 | `$sql = "DELETE FROM ".TB_PREF."debtor_trans_details WHERE debtor_trans_no = $delivery AND debtor_trans_type = ".ST_CUSTDELIVERY;` |
| `admin/db/fiscalyears_db.inc` | 276 | `db_query($sql, "Could not delete debtor trans details");` |
| `admin/db/fiscalyears_db.inc` | 277 | `$sql = "DELETE FROM ".TB_PREF."debtor_trans WHERE trans_no = $delivery AND type = ".ST_CUSTDELIVERY;` |
| `admin/db/fiscalyears_db.inc` | 278 | `db_query($sql, "Could not delete debtor trans");` |
| `admin/db/fiscalyears_db.inc` | 282 | `$sql = "DELETE FROM ".TB_PREF."cust_allocations WHERE trans_no_from = {$row['trans_no']} AND trans_type_from = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 283 | `db_query($sql, "Could not delete cust allocations");` |
| `admin/db/fiscalyears_db.inc` | 284 | `$sql = "DELETE FROM ".TB_PREF."debtor_trans_details WHERE debtor_trans_no = {$row['trans_no']} AND debtor_trans_type = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 285 | `db_query($sql, "Could not delete debtor trans details");` |
| `admin/db/fiscalyears_db.inc` | 286 | `$sql = "DELETE FROM ".TB_PREF."debtor_trans WHERE trans_no = {$row['trans_no']} AND type = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 287 | `db_query($sql, "Could not delete debtor trans");` |
| `admin/db/fiscalyears_db.inc` | 290 | `$sql = "SELECT trans_no, type FROM ".TB_PREF."supp_trans WHERE tran_date <= '$to' AND` |
| `admin/db/fiscalyears_db.inc` | 295 | `$sql = "DELETE FROM ".TB_PREF."supp_allocations WHERE trans_no_from = {$row['trans_no']} AND trans_type_from = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 296 | `db_query($sql, "Could not delete supp allocations");` |
| `admin/db/fiscalyears_db.inc` | 297 | `$sql = "DELETE FROM ".TB_PREF."supp_invoice_items WHERE supp_trans_no = {$row['trans_no']} AND supp_trans_type = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 298 | `db_query($sql, "Could not delete supp invoice items");` |
| `admin/db/fiscalyears_db.inc` | 299 | `$sql = "DELETE FROM ".TB_PREF."supp_trans WHERE trans_no = {$row['trans_no']} AND type = {$row['type']}";` |
| `admin/db/fiscalyears_db.inc` | 300 | `db_query($sql, "Could not delete supp trans");` |
| `admin/db/fiscalyears_db.inc` | 303 | `$sql = "SELECT id FROM ".TB_PREF."workorders WHERE released_date <= '$to' AND closed=1";` |
| `admin/db/fiscalyears_db.inc` | 307 | `$sql = "SELECT issue_no FROM ".TB_PREF."wo_issues WHERE workorder_id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 311 | `$sql = "DELETE FROM ".TB_PREF."wo_issue_items WHERE issue_id = {$row2[0]}";` |
| `admin/db/fiscalyears_db.inc` | 312 | `db_query($sql, "Could not delete wo issue items");` |
| `admin/db/fiscalyears_db.inc` | 313 | `$sql = "DELETE FROM ".TB_PREF."wo_issues WHERE workorder_id = {$row2[0]}";` |
| `admin/db/fiscalyears_db.inc` | 314 | `db_query($sql, "Could not delete wo issues");` |
| `admin/db/fiscalyears_db.inc` | 317 | `$sql = "DELETE FROM ".TB_PREF."wo_manufacture WHERE workorder_id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 318 | `db_query($sql, "Could not delete wo manufacture");` |
| `admin/db/fiscalyears_db.inc` | 319 | `$sql = "DELETE FROM ".TB_PREF."wo_requirements WHERE workorder_id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 320 | `db_query($sql, "Could not delete wo requirements");` |
| `admin/db/fiscalyears_db.inc` | 321 | `$sql = "DELETE FROM ".TB_PREF."workorders WHERE id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 322 | `db_query($sql, "Could not delete workorders");` |
| `admin/db/fiscalyears_db.inc` | 325 | `$sql = "SELECT loc_code, stock_id, SUM(qty) AS qty, SUM(qty*standard_cost) AS std_cost FROM ".TB_PREF."stock_moves WHERE tran_date <= '$to' GROUP by` |
| `admin/db/fiscalyears_db.inc` | 330 | `$sql = "DELETE FROM ".TB_PREF."stock_moves WHERE tran_date <= '$to' AND loc_code = '{$row['loc_code']}' AND stock_id = '{$row['stock_id']}'";` |
| `admin/db/fiscalyears_db.inc` | 331 | `db_query($sql, "Could not delete stock moves");` |
| `admin/db/fiscalyears_db.inc` | 334 | `$sql = "INSERT INTO ".TB_PREF."stock_moves (stock_id, loc_code, tran_date, reference, qty, standard_cost) VALUES` |
| `admin/db/fiscalyears_db.inc` | 336 | `db_query($sql, "Could not insert stock move");` |
| `admin/db/fiscalyears_db.inc` | 338 | `$sql = "DELETE FROM ".TB_PREF."voided WHERE date_ <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 339 | `db_query($sql, "Could not delete voided items");` |
| `admin/db/fiscalyears_db.inc` | 340 | `$sql = "DELETE FROM ".TB_PREF."trans_tax_details WHERE tran_date <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 341 | `db_query($sql, "Could not delete trans tax details");` |
| `admin/db/fiscalyears_db.inc` | 342 | `$sql = "DELETE FROM ".TB_PREF."exchange_rates WHERE date_ <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 343 | `db_query($sql, "Could not delete exchange rates");` |
| `admin/db/fiscalyears_db.inc` | 344 | `$sql = "DELETE FROM ".TB_PREF."budget_trans WHERE tran_date <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 345 | `db_query($sql, "Could not delete budget trans");` |
| `admin/db/fiscalyears_db.inc` | 346 | `$sql = "SELECT account, SUM(amount) AS amount, person_type_id, person_id FROM "` |
| `admin/db/fiscalyears_db.inc` | 357 | `$sql = "DELETE FROM ".TB_PREF."gl_trans WHERE tran_date <= '$to' AND account = '{$row['account']}'";` |
| `admin/db/fiscalyears_db.inc` | 358 | `db_query($sql, "Could not delete gl trans");` |
| `admin/db/fiscalyears_db.inc` | 363 | `$sql = "INSERT INTO ".TB_PREF."gl_trans (type, type_no, tran_date, account, memo_, amount, person_type_id, person_id) VALUES` |
| `admin/db/fiscalyears_db.inc` | 366 | `db_query($sql, "Could not insert gl trans");` |
| `admin/db/fiscalyears_db.inc` | 381 | `$sql = "SELECT bank_act, SUM(amount) AS amount FROM ".TB_PREF."bank_trans WHERE trans_date <= '$to' GROUP BY bank_act";` |
| `admin/db/fiscalyears_db.inc` | 385 | `$sql = "DELETE FROM ".TB_PREF."bank_trans WHERE trans_date <= '$to' AND bank_act = '{$row['bank_act']}'";` |
| `admin/db/fiscalyears_db.inc` | 386 | `db_query($sql, "Could not delete bank trans");` |
| `admin/db/fiscalyears_db.inc` | 387 | `$sql = "INSERT INTO ".TB_PREF."bank_trans (type, trans_no, trans_date, bank_act, ref, amount) VALUES` |
| `admin/db/fiscalyears_db.inc` | 389 | `db_query($sql, "Could not insert bank trans");` |
| `admin/db/fiscalyears_db.inc` | 392 | `$sql = "DELETE FROM ".TB_PREF."audit_trail WHERE gl_date <= '$to'";` |
| `admin/db/fiscalyears_db.inc` | 393 | `db_query($sql, "Could not delete audit trail");` |
| `admin/db/fiscalyears_db.inc` | 395 | `$sql = "SELECT type, id FROM ".TB_PREF."comments WHERE type != ".ST_SALESQUOTE." AND type != ".ST_SALESORDER." AND type != ".ST_PURCHORDER;` |
| `admin/db/fiscalyears_db.inc` | 399 | `$sql = "SELECT count(*) FROM ".TB_PREF."gl_trans WHERE type = {$row['type']} AND type_no = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 404 | `$sql = "DELETE FROM ".TB_PREF."comments WHERE type = {$row['type']} AND id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 405 | `db_query($sql, "Could not delete comments");` |
| `admin/db/fiscalyears_db.inc` | 408 | `$sql = "SELECT type, id FROM ".TB_PREF."refs WHERE type != ".ST_SALESQUOTE." AND type != ".ST_SALESORDER." AND type != ".ST_PURCHORDER;` |
| `admin/db/fiscalyears_db.inc` | 412 | `$sql = "SELECT count(*) FROM ".TB_PREF."gl_trans WHERE type = {$row['type']} AND type_no = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 417 | `$sql = "DELETE FROM ".TB_PREF."refs WHERE type = {$row['type']} AND id = {$row['id']}";` |
| `admin/db/fiscalyears_db.inc` | 418 | `db_query($sql, "Could not delete refs");` |
| `admin/db/maintenance_db.inc` | 63 | `$sql = "UPDATE ".$conn['tbpref']."users SET password=".db_escape($password) . "` |
| `admin/db/maintenance_db.inc` | 65 | `db_query($sql, "could not update user password for 'admin'");` |
| `admin/db/maintenance_db.inc` | 618 | `$res1 = db_query("SHOW CREATE TABLE `" . $table['Name'] . "`");` |
| `admin/db/maintenance_db.inc` | 675 | `$res2 = db_query("SELECT * FROM `" . $tablename . "`");` |
| `admin/db/printers_db.inc` | 16 | `$sql = "UPDATE ".TB_PREF."printers SET description=".db_escape($descr)` |
| `admin/db/printers_db.inc` | 21 | `$sql = "INSERT INTO ".TB_PREF."printers ("` |
| `admin/db/printers_db.inc` | 31 | `$sql = "SELECT * FROM ".TB_PREF."printers";` |
| `admin/db/printers_db.inc` | 37 | `$sql = "SELECT * FROM ".TB_PREF."printers` |
| `admin/db/printers_db.inc` | 46 | `$sql="DELETE FROM ".TB_PREF."printers WHERE id=".db_escape($id);` |
| `admin/db/printers_db.inc` | 47 | `db_query($sql,"could not delete printer definition");` |
| `admin/db/printers_db.inc` | 62 | `$sql = "DELETE FROM ".TB_PREF."print_profiles WHERE ("` |
| `admin/db/printers_db.inc` | 66 | `$result = db_query($sql,"could not update printing profile");` |
| `admin/db/printers_db.inc` | 78 | `$sql = "SELECT printer FROM ".TB_PREF."print_profiles WHERE "` |
| `admin/db/printers_db.inc` | 97 | `$sql="DELETE FROM ".TB_PREF."print_profiles WHERE profile=".db_escape($name);` |
| `admin/db/printers_db.inc` | 98 | `return db_query($sql,"could not delete printing profile");` |
| `admin/db/printers_db.inc` | 105 | `$sql = "SELECT	* FROM ".TB_PREF."print_profiles WHERE profile=".db_escape($name);` |
| `admin/db/security_db.inc` | 16 | `$sql = "SELECT * FROM ".TB_PREF."security_roles WHERE id=".(int)$id;` |
| `admin/db/security_db.inc` | 30 | `$sql = "INSERT INTO ".TB_PREF."security_roles (role, description, sections, areas)` |
| `admin/db/security_db.inc` | 44 | `$sql = "UPDATE ".TB_PREF."security_roles SET role=".db_escape($name)` |
| `admin/db/security_db.inc` | 49 | `db_query($sql, "could not update role");` |
| `admin/db/security_db.inc` | 55 | `$sql = "DELETE FROM ".TB_PREF."security_roles WHERE id=".(int)$id;` |
| `admin/db/security_db.inc` | 57 | `db_query($sql, "could not delete role");` |
| `admin/db/security_db.inc` | 62 | `$sql = "SELECT count(*) FROM ".TB_PREF."users WHERE role_id=".(int)$id;` |
| `admin/db/shipping_db.inc` | 17 | `$sql = "INSERT INTO ".TB_PREF."shippers (shipper_name, contact, phone, phone2, address)` |
| `admin/db/shipping_db.inc` | 31 | `$sql = "UPDATE ".TB_PREF."shippers SET shipper_name=" . db_escape($shipper_name). " ,` |
| `admin/db/shipping_db.inc` | 45 | `$sql="DELETE FROM ".TB_PREF."shippers WHERE shipper_id=".db_escape($selected_id);` |
| `admin/db/shipping_db.inc` | 47 | `db_query($sql,"could not delete shipper");` |
| `admin/db/shipping_db.inc` | 54 | `$sql = "SELECT * FROM ".TB_PREF."shippers";` |
| `admin/db/shipping_db.inc` | 65 | `$sql = "SELECT * FROM ".TB_PREF."shippers WHERE shipper_id=".db_escape($selected_id);` |
| `admin/db/tags_db.inc` | 15 | `$sql = "INSERT INTO ".TB_PREF."tags (type, name, description)` |
| `admin/db/tags_db.inc` | 25 | `$sql = "UPDATE ".TB_PREF."tags SET name=".db_escape($name).",` |
| `admin/db/tags_db.inc` | 39 | `$sql = "SELECT * FROM ".TB_PREF."tags WHERE type=".db_escape($type);` |
| `admin/db/tags_db.inc` | 52 | `$sql = "SELECT * FROM ".TB_PREF."tags WHERE id = ".db_escape($id);` |
| `admin/db/tags_db.inc` | 63 | `$sql = "SELECT type FROM ".TB_PREF."tags WHERE id = ".db_escape($id);` |
| `admin/db/tags_db.inc` | 75 | `$sql = "SELECT name FROM ".TB_PREF."tags WHERE id = ".db_escape($id);` |
| `admin/db/tags_db.inc` | 103 | `$sql = "SELECT description FROM ".TB_PREF."tags WHERE id = ".db_escape($id);` |
| `admin/db/tags_db.inc` | 115 | `$sql = "DELETE FROM ".TB_PREF."tags WHERE id = ".db_escape($id);` |
| `admin/db/tags_db.inc` | 117 | `db_query($sql, "could not delete tag");` |
| `admin/db/tags_db.inc` | 126 | `$sql = "INSERT INTO ".TB_PREF."tag_associations (record_id, tag_id)` |
| `admin/db/tags_db.inc` | 150 | `$sql = "DELETE ta FROM ".TB_PREF."tag_associations ta` |
| `admin/db/tags_db.inc` | 155 | `$sql = "SELECT * FROM ".TB_PREF."tag_associations ta` |
| `admin/db/tags_db.inc` | 160 | `$result = db_query($sql, "could not select tag associations");` |
| `admin/db/tags_db.inc` | 163 | `$sql2 = "DELETE FROM ".TB_PREF."tag_associations WHERE` |
| `admin/db/tags_db.inc` | 165 | `db_query($sql2, "could not delete tag associations");` |
| `admin/db/tags_db.inc` | 188 | `$sql = "SELECT $table.* FROM $table` |
| `admin/db/tags_db.inc` | 200 | `$sql = "SELECT tags.* FROM ".TB_PREF."tag_associations AS ta` |
| `admin/db/tags_db.inc` | 213 | `$sql = "SELECT ta.record_id FROM ".TB_PREF."tag_associations AS ta` |
| `admin/db/transactions_db.inc` | 28 | `$sql = "SELECT t.$trans_no_name as trans_no";` |
| `admin/db/transactions_db.inc` | 75 | `$sql = "SELECT order.customer_id as person_id, debtor.name as name` |
| `admin/db/transactions_db.inc` | 85 | `$sql = "SELECT trans.debtor_no as person_id, debtor.name as name` |
| `admin/db/transactions_db.inc` | 92 | `$sql = "SELECT order.supplier_id as person_id, supp.supp_name as name` |
| `admin/db/transactions_db.inc` | 101 | `$sql = "SELECT trans.supplier_id as person_id, supp.supp_name as name` |
| `admin/db/transactions_db.inc` | 108 | `$sql = "SELECT trans.supplier_id as person_id, supp.supp_name as name` |
| `admin/db/transactions_db.inc` | 116 | `$sql = "SELECT trans.debtor_no as person_id, debtor.name as name` |
| `admin/db/transactions_db.inc` | 167 | `$sql1 = "SELECT MAX(`$st[2]`) as last_no FROM $st[0]";` |
| `admin/db/transactions_db.inc` | 172 | `$sql2 = "SELECT MAX(`id`) as last_no FROM ".TB_PREF."voided WHERE `type`=".db_escape($trans_type);` |
| `admin/db/transactions_db.inc` | 174 | `$sql = "SELECT max(last_no) last_no FROM ($sql1 UNION $sql2) a";` |
| `admin/db/users_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."users (user_id, real_name, password"` |
| `admin/db/users_db.inc` | 31 | `$sql = "UPDATE ".TB_PREF."users SET password=".db_escape($password) . ",` |
| `admin/db/users_db.inc` | 34 | `return db_query($sql, "could not update user password for $user_id");` |
| `admin/db/users_db.inc` | 42 | `$sql = "UPDATE ".TB_PREF."users SET real_name=".db_escape($real_name).` |
| `admin/db/users_db.inc` | 52 | `return db_query($sql, "could not update user for $user_id");` |
| `admin/db/users_db.inc` | 59 | `$sql = "UPDATE ".TB_PREF."users SET ";` |
| `admin/db/users_db.inc` | 65 | `return db_query($sql, "could not update user display prefs for $id");` |
| `admin/db/users_db.inc` | 73 | `$sql = "SELECT u.*, r.role FROM ".TB_PREF."users u, ".TB_PREF."security_roles r` |
| `admin/db/users_db.inc` | 84 | `$sql = "SELECT * FROM ".TB_PREF."users WHERE id=".db_escape($id);` |
| `admin/db/users_db.inc` | 95 | `$sql = "SELECT * FROM ".TB_PREF."users WHERE user_id=".db_escape($user_id);` |
| `admin/db/users_db.inc` | 106 | `$sql = "SELECT * FROM ".TB_PREF."users WHERE email=".db_escape($email);` |
| `admin/db/users_db.inc` | 120 | `$sql="DELETE FROM ".TB_PREF."users WHERE id=".db_escape($id);` |
| `admin/db/users_db.inc` | 122 | `db_query($sql, "could not delete user $id");` |
| `admin/db/users_db.inc` | 130 | `$sql = "SELECT * FROM ".TB_PREF."users WHERE user_id = ".db_escape($user_id)." AND"` |
| `admin/db/users_db.inc` | 140 | `$sql = "UPDATE ".TB_PREF."users SET last_visit_date='". date("Y-m-d H:i:s") ."'` |
| `admin/db/users_db.inc` | 143 | `db_query($sql, "could not update last visit date for user $user_id");` |
| `admin/db/users_db.inc` | 149 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."audit_trail WHERE audit_trail.user="` |
| `admin/db/users_db.inc` | 197 | `db_query("INSERT INTO ".TB_PREF."useronline (timestamp, ip, file) VALUES ('". $timestamp ."',". db_escape($ip) .",". db_escape($_SERVER['PHP_SELF']) .")");` |
| `admin/db/users_db.inc` | 199 | `db_query("DELETE FROM ".TB_PREF."useronline WHERE timestamp<". $timeout);` |
| `admin/db/users_db.inc` | 202 | `$result = db_query("SELECT DISTINCT ip FROM ".TB_PREF."useronline");` |
| `admin/db/voiding_db.inc` | 137 | `$sql = "SELECT * FROM ".TB_PREF."voided WHERE type=".db_escape($type)` |
| `admin/db/voiding_db.inc` | 150 | `$sql = "INSERT INTO ".TB_PREF."voided (type, id, date_, memo_)` |
| `admin/includes/fa_patch.class.inc` | 58 | `$roles = db_query("SELECT * FROM ".TB_PREF."security_roles");` |
| `dimensions/includes/dimensions_db.inc` | 21 | `$sql = "INSERT INTO ".TB_PREF."dimensions (reference, name, type_, date_, due_date)` |
| `dimensions/includes/dimensions_db.inc` | 43 | `$sql = "UPDATE ".TB_PREF."dimensions SET name=".db_escape($name).",` |
| `dimensions/includes/dimensions_db.inc` | 49 | `db_query($sql, "could not update dimension");` |
| `dimensions/includes/dimensions_db.inc` | 63 | `$sql="DELETE FROM ".TB_PREF."dimensions WHERE id=".db_escape($id);` |
| `dimensions/includes/dimensions_db.inc` | 75 | `$sql = "SELECT * FROM ".TB_PREF."dimensions	WHERE id=".db_escape($id);` |
| `dimensions/includes/dimensions_db.inc` | 109 | `$sql = "SELECT * FROM ".TB_PREF."dimensions ORDER BY date_";` |
| `dimensions/includes/dimensions_db.inc` | 125 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."gl_trans WHERE dimension_id = ".db_escape($id)` |
| `dimensions/includes/dimensions_db.inc` | 142 | `$sql = "UPDATE ".TB_PREF."dimensions SET closed='1' WHERE id = ".db_escape($id);` |
| `dimensions/includes/dimensions_db.inc` | 150 | `$sql = "UPDATE ".TB_PREF."dimensions SET closed='0' WHERE id = ".db_escape($id);` |
| `dimensions/includes/dimensions_db.inc` | 160 | `$sql = "SELECT account, coa.account_name, sum(amount) AS amt` |
| `dimensions/includes/dimensions_db.inc` | 176 | `$sql = "SELECT SUM(amount)` |
| `dimensions/includes/dimensions_db.inc` | 192 | `$sql = "SELECT dim.id,` |
| `fixed_assets/includes/fa_classes_db.inc` | 15 | `$sql="SELECT * FROM ".TB_PREF."stock_fa_class";` |
| `fixed_assets/includes/fa_classes_db.inc` | 24 | `$sql="SELECT description FROM ".TB_PREF."stock_fa_class WHERE fa_class_id = ".db_escape($class);;` |
| `fixed_assets/includes/fa_classes_db.inc` | 35 | `$sql = "UPDATE ".TB_PREF."stock_fa_class SET` |
| `fixed_assets/includes/fa_classes_db.inc` | 47 | `$sql = "INSERT INTO ".TB_PREF."stock_fa_class (fa_class_id, parent_id, description, long_description,` |
| `fixed_assets/includes/fa_classes_db.inc` | 58 | `$sql = "DELETE FROM ".TB_PREF."stock_fa_class WHERE fa_class_id=".db_escape($fa_class_id);` |
| `fixed_assets/includes/fixed_assets_db.inc` | 54 | `$sql = "UPDATE ".TB_PREF."stock_master SET` |
| `fixed_assets/includes/fixed_assets_db.inc` | 71 | `$sql = "SELECT * FROM ".TB_PREF."stock_moves` |
| `fixed_assets/includes/fixed_assets_db.inc` | 86 | `$sql = "SELECT * FROM ".TB_PREF."stock_moves` |
| `fixed_assets/includes/fixed_assets_db.inc` | 103 | `$sql = "SELECT *` |
| `fixed_assets/includes/fixed_assets_db.inc` | 126 | `$sql="SELECT * FROM ".TB_PREF."stock_fa_class WHERE fa_class_id=".db_escape($id);` |
| `fixed_assets/includes/fixed_assets_db.inc` | 137 | `$sql = "SELECT s.stock_id, c.description, s.units, s.description as name,` |
| `fixed_assets/includes/fixed_assets_db.inc` | 157 | `//	$sql = "SELECT	IF(ISNULL(a.gl_seq),0,a.gl_seq) as gl_seq,` |
| `gl/includes/db/gl_db_account_types.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."chart_types (id, name, class_id, parent)` |
| `gl/includes/db/gl_db_account_types.inc` | 25 | `$sql = "SELECT id` |
| `gl/includes/db/gl_db_account_types.inc` | 33 | `$sql = "UPDATE ".TB_PREF."chart_types SET parent=".db_escape($id)` |
| `gl/includes/db/gl_db_account_types.inc` | 35 | `db_query($sql, "could not update account type");` |
| `gl/includes/db/gl_db_account_types.inc` | 37 | `$sql = "SELECT account_code` |
| `gl/includes/db/gl_db_account_types.inc` | 45 | `$sql = "UPDATE ".TB_PREF."chart_master` |
| `gl/includes/db/gl_db_account_types.inc` | 48 | `db_query($sql, "could not update account");` |
| `gl/includes/db/gl_db_account_types.inc` | 51 | `$sql = "UPDATE ".TB_PREF."chart_types` |
| `gl/includes/db/gl_db_account_types.inc` | 56 | `$ret = db_query($sql, "could not update account type");` |
| `gl/includes/db/gl_db_account_types.inc` | 63 | `$sql = "SELECT * FROM ".TB_PREF."chart_types";` |
| `gl/includes/db/gl_db_account_types.inc` | 87 | `$sql = "SELECT * FROM ".TB_PREF."chart_types WHERE id = ".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 96 | `$sql = "SELECT name FROM ".TB_PREF."chart_types WHERE id = ".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 106 | `$sql = "DELETE FROM ".TB_PREF."chart_types WHERE id = ".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 108 | `db_query($sql, "could not delete account type");` |
| `gl/includes/db/gl_db_account_types.inc` | 113 | `$sql = "INSERT INTO ".TB_PREF."chart_class (cid, class_name, ctype)` |
| `gl/includes/db/gl_db_account_types.inc` | 121 | `$sql = "UPDATE ".TB_PREF."chart_class SET class_name=".db_escape($name).",` |
| `gl/includes/db/gl_db_account_types.inc` | 129 | `$sql = "SELECT * FROM ".TB_PREF."chart_class";` |
| `gl/includes/db/gl_db_account_types.inc` | 144 | `$sql = "SELECT * FROM ".TB_PREF."chart_class WHERE cid = ".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 153 | `$sql = "SELECT class_name FROM ".TB_PREF."chart_class WHERE cid =".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 163 | `$sql = "DELETE FROM ".TB_PREF."chart_class WHERE cid = ".db_escape($id);` |
| `gl/includes/db/gl_db_account_types.inc` | 165 | `db_query($sql, "could not delete account type");` |
| `gl/includes/db/gl_db_accounts.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."chart_master (account_code, account_code2, account_name, account_type)` |
| `gl/includes/db/gl_db_accounts.inc` | 23 | `$sql = "UPDATE ".TB_PREF."chart_master SET account_name=".db_escape($account_name)` |
| `gl/includes/db/gl_db_accounts.inc` | 32 | `$sql = "DELETE FROM ".TB_PREF."chart_master WHERE account_code=".db_escape($code);` |
| `gl/includes/db/gl_db_accounts.inc` | 34 | `db_query($sql, "could not delete gl account");` |
| `gl/includes/db/gl_db_accounts.inc` | 39 | `$sql = "SELECT coa.*, act_type.name AS AccountTypeName` |
| `gl/includes/db/gl_db_accounts.inc` | 57 | `$sql = "SELECT * FROM ".TB_PREF."chart_master WHERE account_code=".db_escape($code);` |
| `gl/includes/db/gl_db_accounts.inc` | 65 | `$sql = "SELECT act_class.ctype` |
| `gl/includes/db/gl_db_accounts.inc` | 81 | `$sql = "SELECT account_name from ".TB_PREF."chart_master WHERE account_code=".db_escape($code);` |
| `gl/includes/db/gl_db_accounts.inc` | 96 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 125 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 141 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 157 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 171 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 187 | `$sql= "SELECT COUNT(*)` |
| `gl/includes/db/gl_db_accounts.inc` | 217 | `$sql = "SELECT 1` |
| `gl/includes/db/gl_db_accounts.inc` | 232 | `$sql = "SELECT debtor_ref as name, branch_code as id` |
| `gl/includes/db/gl_db_accounts.inc` | 248 | `$sql = "SELECT debtor_ref as ref` |
| `gl/includes/db/gl_db_accounts.inc` | 265 | `$sql= "SELECT COUNT(*) FROM ".TB_PREF."bank_accounts WHERE` |
| `gl/includes/db/gl_db_accounts.inc` | 283 | `$sql= "SELECT id FROM ".TB_PREF."bank_accounts WHERE account_code=".db_escape($account_code);` |
| `gl/includes/db/gl_db_accounts.inc` | 302 | `$sql = "SELECT chart.account_code, chart.account_name, type.name` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 14 | `$sql = "UPDATE ".TB_PREF."bank_accounts SET dflt_curr_act=0 WHERE bank_curr_code="` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 16 | `db_query($sql, "could not update default currency account");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 26 | `$sql = "INSERT INTO ".TB_PREF."bank_accounts (account_code, account_type,` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 45 | `$sql = "UPDATE ".TB_PREF."bank_accounts	SET account_type = ".db_escape($account_type).",` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 53 | `db_query($sql, "could not update bank account for $account_code");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 60 | `$sql = "DELETE FROM ".TB_PREF."bank_accounts WHERE id=".db_escape($id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 62 | `db_query($sql,"could not delete bank account for $id");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 70 | `$sql = "SELECT * FROM ".TB_PREF."bank_accounts WHERE id=".db_escape($id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 81 | `$sql = "SELECT account.*, gl_account.account_name` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 94 | `$sql = "SELECT account_code FROM ".TB_PREF."bank_accounts WHERE id=".db_escape($id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 107 | `$sql = "SELECT bank_charge_act FROM ".TB_PREF."bank_accounts WHERE id=".db_escape($id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 120 | `$sql = "INSERT INTO ".TB_PREF."quick_entries (description, type, base_amount, base_desc, bal_type, `usage`)` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 124 | `db_query($sql, "could not insert quick entry for $description");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 131 | `$sql = "UPDATE ".TB_PREF."quick_entries	SET description = ".db_escape($description).",` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 136 | `db_query($sql, "could not update quick entry for $selected_id");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 143 | `$sql = "DELETE FROM ".TB_PREF."quick_entries WHERE id=".db_escape($selected_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 145 | `db_query($sql,"could not delete quick entry $selected_id");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 152 | `$sql = "INSERT INTO ".TB_PREF."quick_entry_lines` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 158 | `db_query($sql, "could not insert quick entry line for $qid");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 165 | `$sql = "UPDATE ".TB_PREF."quick_entry_lines SET qid = ".db_escape($qid)` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 171 | `db_query($sql, "could not update quick entry line for $selected_id");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 178 | `$sql = "DELETE FROM ".TB_PREF."quick_entry_lines WHERE id=".db_escape($selected_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 180 | `db_query($sql,"could not delete quick entry line $selected_id");` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 187 | `$sql = "SELECT id FROM ".TB_PREF."quick_entries";` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 197 | `$sql = "SELECT * FROM ".TB_PREF."quick_entries";` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 207 | `$sql = "SELECT * FROM ".TB_PREF."quick_entries WHERE id=".db_escape($selected_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 216 | `$sql = "SELECT line.*, coa.account_name, taxtype.name as tax_name` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 228 | `$sql = "SELECT id FROM ".TB_PREF."quick_entry_lines WHERE qid=".db_escape($qid);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 238 | `$sql = "SELECT * FROM ".TB_PREF."quick_entry_lines WHERE id=".db_escape($selected_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 253 | `$sql = "SELECT MAX(reconciled) as last_date,` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 269 | `$sql = "SELECT ending_reconcile_balance` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 280 | `$sql = "SELECT	type, trans_no, ref, trans_date,` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 294 | `$sql = "UPDATE ".TB_PREF."bank_trans SET reconciled=$reconcile_value"` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 299 | `$sql2 = "UPDATE ".TB_PREF."bank_accounts SET last_reconciled_date='"` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 320 | `$sql = "SELECT b.*, b.bank_curr_code='$home_curr' as fall_back FROM "` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 333 | `$sql = "SELECT curr_code FROM ".TB_PREF."debtors_master WHERE debtor_no=".db_escape($cust_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 342 | `$sql = "SELECT curr_code FROM ".TB_PREF."suppliers WHERE supplier_id=".db_escape($supplier_id);` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 366 | `$sql = "(SELECT id AS id, ".BO_COMPANY." AS type FROM ".TB_PREF."bank_accounts WHERE REPLACE(bank_account_number,' ', '')=$number)";` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 367 | `$sql .= " UNION (SELECT supplier_id AS id, ".BO_SUPPLIER." AS type FROM ".TB_PREF."suppliers WHERE REPLACE(bank_account,' ', '')=$number)";` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 368 | `$sql .= " UNION (SELECT branch_code AS id, ".BO_CUSTBRANCH." AS type FROM ".TB_PREF."cust_branch WHERE REPLACE(bank_account,' ', '')=$number)";` |
| `gl/includes/db/gl_db_bank_accounts.inc` | 382 | `$sql= "SELECT bank_curr_code FROM ".TB_PREF."bank_accounts WHERE id=".db_escape($id);` |
| `gl/includes/db/gl_db_bank_trans.inc` | 37 | `$sql = "INSERT INTO ".TB_PREF."bank_trans (type, trans_no, bank_act, ref,` |
| `gl/includes/db/gl_db_bank_trans.inc` | 54 | `$sql = "SELECT trans_no` |
| `gl/includes/db/gl_db_bank_trans.inc` | 67 | `$sql = "SELECT bt.*, act.*,` |
| `gl/includes/db/gl_db_bank_trans.inc` | 98 | `$sql = "SELECT t.*` |
| `gl/includes/db/gl_db_bank_trans.inc` | 116 | `$sql = "SELECT SUM(amount)` |
| `gl/includes/db/gl_db_bank_trans.inc` | 128 | `$sql = "SELECT SUM(amount)` |
| `gl/includes/db/gl_db_bank_trans.inc` | 148 | `$sql = "UPDATE ".TB_PREF."bank_trans` |
| `gl/includes/db/gl_db_bank_trans.inc` | 191 | `$sql = "SELECT sum(amount) as amount, trans_date` |
| `gl/includes/db/gl_db_banking.inc` | 23 | `$sql = "SELECT SUM(bt.amount) AS for_amount, ba.bank_curr_code` |
| `gl/includes/db/gl_db_banking.inc` | 89 | `$sql = "SELECT SUM(IF(t.type IN(". implode(',', array(ST_CUSTCREDIT, ST_CUSTPAYMENT, ST_BANKDEPOSIT, ST_JOURNAL))."),` |
| `gl/includes/db/gl_db_banking.inc` | 109 | `$sql = "SELECT SUM(-(t.ov_amount + t.ov_gst + t.ov_discount)) AS amount,` |
| `gl/includes/db/gl_db_banking.inc` | 126 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."gl_trans` |
| `gl/includes/db/gl_db_banking.inc` | 141 | `$sql = "SELECT * FROM ".TB_PREF."bank_accounts";` |
| `gl/includes/db/gl_db_currencies.inc` | 17 | `$sql = "UPDATE ".TB_PREF."currencies SET currency=".db_escape($currency)` |
| `gl/includes/db/gl_db_currencies.inc` | 23 | `db_query($sql, "could not update currency for $curr_abrev");` |
| `gl/includes/db/gl_db_currencies.inc` | 31 | `$sql = "INSERT INTO ".TB_PREF."currencies (curr_abrev, curr_symbol, currency,` |
| `gl/includes/db/gl_db_currencies.inc` | 44 | `$sql="DELETE FROM ".TB_PREF."currencies WHERE curr_abrev=".db_escape($curr_code);` |
| `gl/includes/db/gl_db_currencies.inc` | 45 | `db_query($sql, "could not delete currency	$curr_code");` |
| `gl/includes/db/gl_db_currencies.inc` | 47 | `$sql="DELETE FROM ".TB_PREF."exchange_rates WHERE curr_code='$curr_code'";` |
| `gl/includes/db/gl_db_currencies.inc` | 48 | `db_query($sql, "could not delete exchange rates for currency $curr_code");` |
| `gl/includes/db/gl_db_currencies.inc` | 55 | `$sql = "SELECT * FROM ".TB_PREF."currencies WHERE curr_abrev=".db_escape($curr_code);` |
| `gl/includes/db/gl_db_currencies.inc` | 66 | `$sql = "SELECT * FROM ".TB_PREF."currencies";` |
| `gl/includes/db/gl_db_rates.inc` | 16 | `$sql = "SELECT * FROM ".TB_PREF."exchange_rates WHERE id=".db_escape($rate_id);` |
| `gl/includes/db/gl_db_rates.inc` | 26 | `$sql = "SELECT rate_buy` |
| `gl/includes/db/gl_db_rates.inc` | 45 | `$sql = "SELECT rate_buy, max(date_) as date_` |
| `gl/includes/db/gl_db_rates.inc` | 68 | `$sql = "UPDATE ".TB_PREF."exchange_rates SET rate_buy=$buy_rate, rate_sell=".db_escape($sell_rate)` |
| `gl/includes/db/gl_db_rates.inc` | 83 | `$sql = "INSERT INTO ".TB_PREF."exchange_rates (curr_code, date_, rate_buy, rate_sell)` |
| `gl/includes/db/gl_db_rates.inc` | 104 | `$sql = "DELETE FROM ".TB_PREF."exchange_rates WHERE id=".db_escape($rate_id);` |
| `gl/includes/db/gl_db_rates.inc` | 105 | `db_query($sql, "could not delete exchange rate $rate_id");` |
| `gl/includes/db/gl_db_rates.inc` | 244 | `$sql = "SELECT date_, rate_buy, id` |
| `gl/includes/db/gl_db_trans.inc` | 48 | `$sql = "INSERT INTO ".TB_PREF."gl_trans ( type, type_no, tran_date,` |
| `gl/includes/db/gl_db_trans.inc` | 115 | `$sql = "SELECT gl.*, j.event_date, j.doc_date, a.gl_seq, u.user_id, st.supp_reference, gl.person_id subcode,` |
| `gl/includes/db/gl_db_trans.inc` | 181 | `$sql = "SELECT gl.*, cm.account_name, IFNULL(refs.reference, '') AS reference, user.real_name,` |
| `gl/includes/db/gl_db_trans.inc` | 209 | `$sql = "SELECT costing.*, gl.*, chart.account_name, com.memo_` |
| `gl/includes/db/gl_db_trans.inc` | 228 | `$sql = "SELECT issue.*, gl.*, chart.account_name, com.memo_` |
| `gl/includes/db/gl_db_trans.inc` | 246 | `$sql = "SELECT rcv.*, gl.*, chart.account_name, com.memo_` |
| `gl/includes/db/gl_db_trans.inc` | 268 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."gl_trans` |
| `gl/includes/db/gl_db_trans.inc` | 292 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."gl_trans` |
| `gl/includes/db/gl_db_trans.inc` | 315 | `$sql = "SELECT	SUM(IF(amount >= 0, amount, 0)) as debit,` |
| `gl/includes/db/gl_db_trans.inc` | 344 | `$sql = "SELECT SUM(amount)` |
| `gl/includes/db/gl_db_trans.inc` | 364 | `$sql = "SELECT account FROM ".TB_PREF."budget_trans WHERE account=".db_escape($account)` |
| `gl/includes/db/gl_db_trans.inc` | 377 | `$sql = "UPDATE ".TB_PREF."budget_trans SET amount=".db_escape($amount)` |
| `gl/includes/db/gl_db_trans.inc` | 383 | `$sql = "INSERT INTO ".TB_PREF."budget_trans (tran_date,` |
| `gl/includes/db/gl_db_trans.inc` | 395 | `$sql = "DELETE FROM ".TB_PREF."budget_trans WHERE account=".db_escape($account)` |
| `gl/includes/db/gl_db_trans.inc` | 408 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."budget_trans` |
| `gl/includes/db/gl_db_trans.inc` | 457 | `$sql = "INSERT INTO ".TB_PREF."trans_tax_details` |
| `gl/includes/db/gl_db_trans.inc` | 473 | `$sql = "SELECT tax_details.*,` |
| `gl/includes/db/gl_db_trans.inc` | 492 | `$sql = "UPDATE ".TB_PREF."trans_tax_details SET amount=0, net_amount=0` |
| `gl/includes/db/gl_db_trans.inc` | 503 | `$sql = "DELETE FROM ".TB_PREF."trans_tax_details` |
| `gl/includes/db/gl_db_trans.inc` | 515 | `$sql = "SELECT` |
| `gl/includes/db/gl_db_trans.inc` | 554 | `$sql = "SELECT type_no FROM ".TB_PREF."gl_trans WHERE type=".db_escape($type)` |
| `gl/includes/db/gl_db_trans.inc` | 568 | `$sql = "UPDATE ".TB_PREF."gl_trans SET amount=0 WHERE type=".db_escape($type)` |
| `gl/includes/db/gl_db_trans.inc` | 584 | `$sql = "DELETE FROM ".TB_PREF."gl_trans WHERE type=".db_escape($type)` |
| `gl/includes/db/gl_db_trans.inc` | 597 | `$sql = "SELECT	IFNULL(a.gl_seq,0) as gl_seq,` |
| `gl/includes/db/gl_db_trans.inc` | 626 | `" LEFT JOIN (SELECT type, type_no, MAX(IFNULL(dimension_id, dimension2_id)) dimension FROM ".TB_PREF."gl_trans GROUP BY type, type_no) dim` |
| `gl/includes/db/gl_journal.inc` | 15 | `$sql = "INSERT INTO ".TB_PREF."journal(` |
| `gl/includes/db/gl_journal.inc` | 36 | `$sql = "UPDATE ".TB_PREF."journal SET "` |
| `gl/includes/db/gl_journal.inc` | 47 | `return db_query($sql, 'cannot update journal entry');` |
| `gl/includes/db/gl_journal.inc` | 52 | `$sql = "DELETE FROM ".TB_PREF."journal` |
| `gl/includes/db/gl_journal.inc` | 55 | `return db_query($sql, 'cannot delete journal entry');` |
| `gl/includes/db/gl_journal.inc` | 60 | `$sql = "SELECT * FROM ".TB_PREF."journal` |
| `gl/includes/db/gl_journal.inc` | 74 | `$sql = "INSERT INTO ".TB_PREF."debtor_trans (trans_no, type, debtor_no, branch_code, tran_date, reference, ov_amount, rate)` |
| `gl/includes/db/gl_journal.inc` | 90 | `$sql = "INSERT INTO ".TB_PREF."supp_trans (trans_no, type, supplier_id, tran_date, reference, ov_amount, rate, supp_reference)` |
| `gl/includes/db/gl_journal.inc` | 151 | `$sql = "UPDATE ".TB_PREF."journal SET amount=0` |
| `inventory/includes/inventory_db.inc` | 37 | `$sql = "SELECT move.*, IF(ISNULL(supplier.supplier_id), debtor.name, supplier.supp_name) name";` |
| `inventory/includes/inventory_db.inc` | 63 | `$sql = "SELECT stock.*, loc.location_name, loc.email` |
| `inventory/includes/db/items_adjust_db.inc` | 98 | `$sql = "UPDATE ".TB_PREF."stock_master SET inactive=1` |
| `inventory/includes/db/items_category_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."stock_category (description, dflt_tax_type,` |
| `inventory/includes/db/items_category_db.inc` | 43 | `$sql = "UPDATE ".TB_PREF."stock_category SET "` |
| `inventory/includes/db/items_category_db.inc` | 64 | `$sql="DELETE FROM ".TB_PREF."stock_category WHERE category_id=".db_escape($id);` |
| `inventory/includes/db/items_category_db.inc` | 71 | `$sql = "SELECT c.*, t.name as tax_name FROM ".TB_PREF."stock_category c, "` |
| `inventory/includes/db/items_category_db.inc` | 87 | `$sql="SELECT * FROM ".TB_PREF."stock_category WHERE category_id=".db_escape($id);` |
| `inventory/includes/db/items_category_db.inc` | 96 | `$sql = "SELECT description FROM ".TB_PREF."stock_category WHERE category_id=".db_escape($id);` |
| `inventory/includes/db/items_codes_db.inc` | 18 | `$sql = "UPDATE ".TB_PREF."item_codes SET` |
| `inventory/includes/db/items_codes_db.inc` | 38 | `$sql = "INSERT INTO ".TB_PREF."item_codes` |
| `inventory/includes/db/items_codes_db.inc` | 49 | `$sql="DELETE FROM ".TB_PREF."item_codes WHERE id=".db_escape($id);` |
| `inventory/includes/db/items_codes_db.inc` | 55 | `$sql="SELECT * FROM ".TB_PREF."item_codes WHERE id=".db_escape($id);` |
| `inventory/includes/db/items_codes_db.inc` | 64 | `$sql="SELECT i.*, c.description as cat_name FROM "` |
| `inventory/includes/db/items_codes_db.inc` | 78 | `$sql="DELETE FROM ".TB_PREF."item_codes WHERE item_code=".db_escape($item_code);` |
| `inventory/includes/db/items_codes_db.inc` | 84 | `$sql="SELECT DISTINCT kit.*, item.units, comp.description as comp_name` |
| `inventory/includes/db/items_codes_db.inc` | 103 | `$sql = "SELECT units, decimals, description, category_id` |
| `inventory/includes/db/items_codes_db.inc` | 140 | `$sql = "SELECT description, category_id FROM ".TB_PREF."item_codes "` |
| `inventory/includes/db/items_codes_db.inc` | 148 | `$sql = "UPDATE ".TB_PREF."item_codes SET description="` |
| `inventory/includes/db/items_codes_db.inc` | 151 | `db_query($sql, "kit name update failed");` |
| `inventory/includes/db/items_codes_db.inc` | 156 | `$sql = "SELECT item_code, description FROM "` |
| `inventory/includes/db/items_db.inc` | 19 | `$sql = "UPDATE ".TB_PREF."stock_master SET long_description=".db_escape($long_description).",` |
| `inventory/includes/db/items_db.inc` | 63 | `$sql = "INSERT INTO ".TB_PREF."stock_master (stock_id, description, long_description, category_id,` |
| `inventory/includes/db/items_db.inc` | 83 | `$sql = "INSERT INTO ".TB_PREF."loc_stock (loc_code, stock_id)` |
| `inventory/includes/db/items_db.inc` | 94 | `$sql="DELETE FROM ".TB_PREF."stock_master WHERE stock_id=".db_escape($stock_id);` |
| `inventory/includes/db/items_db.inc` | 95 | `db_query($sql, "could not delete stock item");` |
| `inventory/includes/db/items_db.inc` | 98 | `$sql ="DELETE FROM ".TB_PREF."loc_stock WHERE stock_id=".db_escape($stock_id);` |
| `inventory/includes/db/items_db.inc` | 99 | `db_query($sql, "could not delete stock item loc stock");` |
| `inventory/includes/db/items_db.inc` | 102 | `$sql ="DELETE FROM ".TB_PREF."purch_data WHERE stock_id=".db_escape($stock_id);` |
| `inventory/includes/db/items_db.inc` | 103 | `db_query($sql, "could not delete stock item purch data");` |
| `inventory/includes/db/items_db.inc` | 106 | `$sql ="DELETE FROM ".TB_PREF."prices WHERE stock_id=".db_escape($stock_id);` |
| `inventory/includes/db/items_db.inc` | 107 | `db_query($sql, "could not delete stock item prices");` |
| `inventory/includes/db/items_db.inc` | 110 | `$sql = "DELETE FROM ".TB_PREF."bom WHERE parent=".db_escape($stock_id);` |
| `inventory/includes/db/items_db.inc` | 111 | `db_query($sql, "could not delete stock item bom");` |
| `inventory/includes/db/items_db.inc` | 118 | `$sql = "SELECT item.*, taxtype.name AS tax_type_name` |
| `inventory/includes/db/items_db.inc` | 130 | `$sql = "SELECT * FROM ".TB_PREF."stock_master WHERE fixed_asset=".db_escape($fixed_asset);` |
| `inventory/includes/db/items_db.inc` | 186 | `$sql = "SELECT COUNT(i.item_code) AS kit, i.item_code, i.description, c.description category` |
| `inventory/includes/db/items_locations_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."locations (loc_code, location_name, delivery_address, phone, phone2, fax, email, contact, fixed_asset)` |
| `inventory/includes/db/items_locations_db.inc` | 22 | `$sql = "INSERT INTO ".TB_PREF."loc_stock (loc_code, stock_id, reorder_level)` |
| `inventory/includes/db/items_locations_db.inc` | 23 | `SELECT ".db_escape($loc_code).", ".TB_PREF."stock_master.stock_id, 0 FROM ".TB_PREF."stock_master";` |
| `inventory/includes/db/items_locations_db.inc` | 33 | `$sql = "UPDATE ".TB_PREF."locations SET location_name=".db_escape($location_name).",` |
| `inventory/includes/db/items_locations_db.inc` | 47 | `$sql="DELETE FROM ".TB_PREF."locations WHERE loc_code=".db_escape($item_location);` |
| `inventory/includes/db/items_locations_db.inc` | 50 | `$sql = "DELETE FROM ".TB_PREF."loc_stock WHERE loc_code =".db_escape($item_location);` |
| `inventory/includes/db/items_locations_db.inc` | 58 | `$sql="SELECT * FROM ".TB_PREF."locations WHERE loc_code=".db_escape($item_location);` |
| `inventory/includes/db/items_locations_db.inc` | 69 | `$sql = "SELECT * FROM ".TB_PREF."locations WHERE fixed_asset = ".db_escape($fixed_asset);` |
| `inventory/includes/db/items_locations_db.inc` | 78 | `$sql = "UPDATE ".TB_PREF."loc_stock SET reorder_level = $reorder_level` |
| `inventory/includes/db/items_locations_db.inc` | 88 | `$sql = "SELECT stock.loc_code, stock.location_name, "` |
| `inventory/includes/db/items_prices_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."prices (stock_id, sales_type_id, curr_abrev, price)` |
| `inventory/includes/db/items_prices_db.inc` | 23 | `$sql = "UPDATE ".TB_PREF."prices SET sales_type_id=".db_escape($sales_type_id).",` |
| `inventory/includes/db/items_prices_db.inc` | 32 | `$sql="DELETE FROM ".TB_PREF."prices WHERE id= ".db_escape($price_id);` |
| `inventory/includes/db/items_prices_db.inc` | 38 | `$sql = "SELECT pricelist.sales_type, price.*` |
| `inventory/includes/db/items_prices_db.inc` | 50 | `$sql = "SELECT * FROM ".TB_PREF."prices WHERE id=".db_escape($price_id);` |
| `inventory/includes/db/items_prices_db.inc` | 59 | `$sql = "SELECT * FROM ".TB_PREF."prices WHERE stock_id=".db_escape($stock_id)."` |
| `inventory/includes/db/items_purchases_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."purch_data (supplier_id, stock_id, price, suppliers_uom,` |
| `inventory/includes/db/items_purchases_db.inc` | 29 | `$sql = "UPDATE ".TB_PREF."purch_data SET price=" . $price . ",` |
| `inventory/includes/db/items_purchases_db.inc` | 40 | `$sql = "DELETE FROM ".TB_PREF."purch_data WHERE supplier_id=".db_escape($selected_id)."` |
| `inventory/includes/db/items_purchases_db.inc` | 42 | `db_query($sql,"could not delete purchasing data");` |
| `inventory/includes/db/items_purchases_db.inc` | 47 | `$sql = "SELECT pdata.*, supplier.supp_name,	supplier.curr_code` |
| `inventory/includes/db/items_purchases_db.inc` | 57 | `$sql = "SELECT pdata.*, supplier.supp_name` |
| `inventory/includes/db/items_trans_db.inc` | 23 | `$sql = "UPDATE ".TB_PREF."stock_master SET material_cost=".db_escape($material_cost)."` |
| `inventory/includes/db/items_trans_db.inc` | 33 | `$sql = "UPDATE ".TB_PREF."stock_master SET material_cost=".db_escape($material_cost).",` |
| `inventory/includes/db/items_trans_db.inc` | 89 | `$sql = "UPDATE ".TB_PREF."stock_moves SET standard_cost = standard_cost + ".db_escape($diff_cost). " WHERE stock_id = "` |
| `inventory/includes/db/items_transfer_db.inc` | 84 | `$sql = "SELECT loc_from.*, loc_to.*` |
| `inventory/includes/db/items_units_db.inc` | 15 | `$sql = "UPDATE ".TB_PREF."item_units SET` |
| `inventory/includes/db/items_units_db.inc` | 21 | `$sql = "INSERT INTO ".TB_PREF."item_units` |
| `inventory/includes/db/items_units_db.inc` | 30 | `$sql="DELETE FROM ".TB_PREF."item_units WHERE abbr=".db_escape($unit);` |
| `inventory/includes/db/items_units_db.inc` | 37 | `$sql="SELECT * FROM ".TB_PREF."item_units WHERE abbr=".db_escape($unit);` |
| `inventory/includes/db/items_units_db.inc` | 46 | `$sql = "SELECT description FROM ".TB_PREF."item_units WHERE abbr=".db_escape($unit);` |
| `inventory/includes/db/items_units_db.inc` | 55 | `$sql= "SELECT COUNT(*) FROM ".TB_PREF."stock_master WHERE units=".db_escape($unit);` |
| `inventory/includes/db/items_units_db.inc` | 62 | `$sql = "SELECT * FROM ".TB_PREF."item_units";` |
| `inventory/includes/db/items_units_db.inc` | 70 | `$sql = "SELECT decimals FROM ".TB_PREF."item_units,	".TB_PREF."stock_master` |
| `manufacturing/includes/db/work_centres_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."workcentres (name, description)` |
| `manufacturing/includes/db/work_centres_db.inc` | 22 | `$sql = "UPDATE ".TB_PREF."workcentres SET name=".db_escape($name).", description=".db_escape($description)."` |
| `manufacturing/includes/db/work_centres_db.inc` | 25 | `db_query($sql, "could not update work centre");` |
| `manufacturing/includes/db/work_centres_db.inc` | 30 | `$sql = "SELECT * FROM ".TB_PREF."workcentres";` |
| `manufacturing/includes/db/work_centres_db.inc` | 38 | `$sql = "SELECT * FROM ".TB_PREF."workcentres WHERE id=".db_escape($type_id);` |
| `manufacturing/includes/db/work_centres_db.inc` | 47 | `$sql="DELETE FROM ".TB_PREF."workcentres WHERE id=".db_escape($type_id);` |
| `manufacturing/includes/db/work_centres_db.inc` | 49 | `db_query($sql, "could not delete work centre");` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 15 | `$sql = "INSERT INTO ".TB_PREF."wo_costing (workorder_id, cost_type, trans_type, trans_no, factor)` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 26 | `$sql="SELECT *` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 38 | `$sql="DELETE FROM ".TB_PREF."wo_costing WHERE trans_type=".db_escape($trans_type)` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 41 | `db_query($sql, "could not delete work order costing");` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 109 | `$sql = "UPDATE ".TB_PREF."stock_master SET material_cost=".db_escape($avg_cost)."` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 213 | `$sql = "SELECT workorder_id FROM ".TB_PREF."wo_costing WHERE trans_type= ".db_escape($type)." AND trans_no=".db_escape($trans_no);` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 242 | `$sql = "DELETE FROM ".TB_PREF."wo_costing WHERE workorder_id=".db_escape($wo_id);` |
| `manufacturing/includes/db/work_order_costing_db.inc` | 243 | `db_query($sql, "could not delete work order costing");` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 26 | `$sql = "INSERT INTO ".TB_PREF."wo_issues (workorder_id, reference, issue_date, loc_code, workcentre_id)` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 47 | `$sql = "INSERT INTO ".TB_PREF."wo_issue_items (issue_id, stock_id, qty_issued, unit_cost)` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 92 | `$sql = "SELECT * FROM ".TB_PREF."wo_issues WHERE workorder_id=".db_escape($woid)` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 99 | `$sql = "SELECT issue.*, item.*, stock.mb_flag` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 112 | `$sql = "SELECT DISTINCT issue.*, wo.stock_id, wo.closed,` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 133 | `$sql = "SELECT issue.*, item.description, item.units` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 146 | `$sql = "SELECT issue_no FROM ".TB_PREF."wo_issues WHERE issue_no=".db_escape($issue_no);` |
| `manufacturing/includes/db/work_order_issues_db.inc` | 178 | `$sql = "UPDATE ".TB_PREF."wo_issue_items SET qty_issued = 0` |
| `manufacturing/includes/db/work_order_produce_items_db.inc` | 29 | `$sql = "INSERT INTO ".TB_PREF."wo_manufacture (workorder_id, reference, quantity, date_)` |
| `manufacturing/includes/db/work_order_produce_items_db.inc` | 107 | `$sql = "SELECT prod.*, wo.stock_id, item.description AS StockDescription, wo.closed` |
| `manufacturing/includes/db/work_order_produce_items_db.inc` | 123 | `$sql = "SELECT * FROM ".TB_PREF."wo_manufacture WHERE workorder_id="` |
| `manufacturing/includes/db/work_order_produce_items_db.inc` | 132 | `$sql = "SELECT id FROM ".TB_PREF."wo_manufacture WHERE id=".db_escape($id);` |
| `manufacturing/includes/db/work_order_produce_items_db.inc` | 167 | `$sql = "UPDATE ".TB_PREF."wo_manufacture SET quantity=0 WHERE id=".db_escape($type_no);` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 14 | `$sql = "SELECT req.*, item.description, item.mb_flag, loc.location_name,` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 32 | `$sql = "SELECT SUM(units_req*unit_cost) cost` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 46 | `$sql = "INSERT INTO ".TB_PREF."wo_requirements (workorder_id, stock_id, workcentre, units_req, loc_code)` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 57 | `$sql="DELETE FROM ".TB_PREF."wo_requirements WHERE workorder_id=".db_escape($woid);` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 68 | `$sql = "UPDATE ".TB_PREF."wo_requirements SET` |
| `manufacturing/includes/db/work_order_requirements_db.inc` | 80 | `$sql = "UPDATE ".TB_PREF."wo_requirements SET units_issued = 0` |
| `manufacturing/includes/db/work_orders_db.inc` | 33 | `$sql = "INSERT INTO ".TB_PREF."workorders (wo_ref, loc_code, units_reqd, stock_id,` |
| `manufacturing/includes/db/work_orders_db.inc` | 86 | `$sql = "UPDATE ".TB_PREF."workorders SET loc_code=".db_escape($loc_code).",` |
| `manufacturing/includes/db/work_orders_db.inc` | 92 | `db_query($sql, "could not update work order");` |
| `manufacturing/includes/db/work_orders_db.inc` | 110 | `$sql = "DELETE FROM ".TB_PREF."workorders WHERE id=".db_escape($woid);` |
| `manufacturing/includes/db/work_orders_db.inc` | 123 | `$sql = "SELECT wo.*,st.description As StockItemName,l.location_name,` |
| `manufacturing/includes/db/work_orders_db.inc` | 148 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."wo_manufacture WHERE workorder_id=".db_escape($woid);` |
| `manufacturing/includes/db/work_orders_db.inc` | 160 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."wo_issues WHERE workorder_id=".db_escape($woid);` |
| `manufacturing/includes/db/work_orders_db.inc` | 187 | `$sql = "UPDATE ".TB_PREF."workorders SET released_date='$date',` |
| `manufacturing/includes/db/work_orders_db.inc` | 204 | `$sql = "UPDATE ".TB_PREF."workorders SET closed=1 WHERE id = ".db_escape($woid);` |
| `manufacturing/includes/db/work_orders_db.inc` | 212 | `$sql = "SELECT closed FROM ".TB_PREF."workorders WHERE id = ".db_escape($woid);` |
| `manufacturing/includes/db/work_orders_db.inc` | 226 | `$sql = "UPDATE ".TB_PREF."workorders SET units_issued = units_issued + ".db_escape($quantity)."` |
| `manufacturing/includes/db/work_orders_db.inc` | 231 | `$sql = "UPDATE ".TB_PREF."workorders SET closed = ((units_issued >= units_reqd) OR ".db_escape($force_close).")` |
| `manufacturing/includes/db/work_orders_db.inc` | 248 | `$sql = "UPDATE ".TB_PREF."workorders SET closed=0 WHERE id = "` |
| `manufacturing/includes/db/work_orders_db.inc` | 290 | `$sql = "UPDATE ".TB_PREF."workorders SET closed=1,units_reqd=0,units_issued=0 WHERE id = "` |
| `manufacturing/includes/db/work_orders_db.inc` | 299 | `$sql = "SELECT` |
| `manufacturing/includes/db/work_orders_db.inc` | 359 | `$sql = "SELECT` |
| `purchasing/includes/purchasing_db.inc` | 50 | `$sql = "SELECT price, conversion_factor FROM ".TB_PREF."purch_data` |
| `purchasing/includes/purchasing_db.inc` | 68 | `$sql = "SELECT conversion_factor FROM ".TB_PREF."purch_data` |
| `purchasing/includes/purchasing_db.inc` | 87 | `$sql = "SELECT * FROM ".TB_PREF."purch_data` |
| `purchasing/includes/purchasing_db.inc` | 100 | `$sql = "INSERT INTO ".TB_PREF."purch_data (supplier_id, stock_id, price, suppliers_uom,` |
| `purchasing/includes/purchasing_db.inc` | 108 | `$sql = "UPDATE ".TB_PREF."purch_data SET price=".db_escape($price);` |
| `purchasing/includes/purchasing_db.inc` | 130 | `$sql = "SELECT DISTINCT allocs.*` |
| `purchasing/includes/db/grn_db.inc` | 44 | `$sql = "SELECT mb_flag, material_cost FROM ".TB_PREF."stock_master WHERE stock_id=".db_escape($stock_id);` |
| `purchasing/includes/db/grn_db.inc` | 72 | `$sql = "UPDATE ".TB_PREF."stock_master SET material_cost=".db_escape($material_cost)."` |
| `purchasing/includes/db/grn_db.inc` | 170 | `$sql = "INSERT INTO ".TB_PREF."grn_batch (purch_order_no, delivery_date, supplier_id, reference, loc_code, rate)` |
| `purchasing/includes/db/grn_db.inc` | 184 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/grn_db.inc` | 192 | `$sql = "INSERT INTO ".TB_PREF."grn_items (grn_batch_id, po_detail_item, item_code, description, qty_recd)` |
| `purchasing/includes/db/grn_db.inc` | 205 | `$sql = "SELECT grn_batch_id FROM ".TB_PREF."grn_items WHERE id=".db_escape($item);` |
| `purchasing/includes/db/grn_db.inc` | 213 | `$sql = "SELECT * FROM ".TB_PREF."grn_batch WHERE id=".db_escape($grn);` |
| `purchasing/includes/db/grn_db.inc` | 223 | `$sql = "SELECT grn.*, item.*` |
| `purchasing/includes/db/grn_db.inc` | 233 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/grn_db.inc` | 244 | `//$sql = "UPDATE ".TB_PREF."grn_items SET qty_recd=0, quantity_inv=0 WHERE id=$entered_grn->id";` |
| `purchasing/includes/db/grn_db.inc` | 245 | `$sql = "UPDATE ".TB_PREF."grn_items SET qty_recd=qty_recd+".db_escape($entered_grn->this_quantity_inv)` |
| `purchasing/includes/db/grn_db.inc` | 257 | `$sql = "SELECT grn.*, grn_item.*,` |
| `purchasing/includes/db/grn_db.inc` | 311 | `$sql = "SELECT grn.*, po.unit_price, grn.qty_recd - grn.quantity_inv AS QtyOstdg,` |
| `purchasing/includes/db/grn_db.inc` | 362 | `$sql= "SELECT *	FROM ".TB_PREF."grn_batch WHERE id=".db_escape($grn_batch);` |
| `purchasing/includes/db/grn_db.inc` | 390 | `$sql = "SELECT * FROM ".TB_PREF."grn_batch WHERE purch_order_no=".db_escape($po_number);` |
| `purchasing/includes/db/grn_db.inc` | 399 | `$sql = "SELECT id FROM ".TB_PREF."grn_batch WHERE id=".db_escape($grn_batch);` |
| `purchasing/includes/db/grn_db.inc` | 409 | `$sql = "SELECT inv.id` |
| `purchasing/includes/db/grn_db.inc` | 444 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/grn_db.inc` | 453 | `$sql = "UPDATE ".TB_PREF."grn_items SET qty_recd=0, quantity_inv=0` |
| `purchasing/includes/db/invoice_db.inc` | 19 | `$sql = "SELECT supp.supp_name, terms.terms, terms.days_before_due,` |
| `purchasing/includes/db/invoice_db.inc` | 70 | `$sql = "SELECT act_price, unit_price FROM ".TB_PREF."purch_order_details WHERE` |
| `purchasing/includes/db/invoice_db.inc` | 78 | `$sql = "SELECT delivery_date` |
| `purchasing/includes/db/invoice_db.inc` | 93 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/invoice_db.inc` | 102 | `$sql = "UPDATE ".TB_PREF."grn_items` |
| `purchasing/includes/db/invoice_db.inc` | 410 | `$sql = "SELECT DISTINCT trans.trans_no, trans.type,	ov_amount+ov_discount+ov_gst AS Total,` |
| `purchasing/includes/db/invoice_db.inc` | 433 | `$sql = "SELECT amount, tax_type_id as id, rate` |
| `purchasing/includes/db/invoice_db.inc` | 450 | `$sql = "SELECT trans.*, supp_name` |
| `purchasing/includes/db/invoice_db.inc` | 518 | `$sql = "SELECT *, tran_date` |
| `purchasing/includes/db/invoice_db.inc` | 574 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/invoice_db.inc` | 581 | `$sql = "UPDATE ".TB_PREF."grn_items SET qty_recd=qty_recd+".-$details_row["quantity"]."` |
| `purchasing/includes/db/invoice_db.inc` | 638 | `$sql = "SELECT account_code, account_name FROM ".TB_PREF."chart_master WHERE account_code=".db_escape($acc);` |
| `purchasing/includes/db/invoice_db.inc` | 644 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."supp_trans WHERE supplier_id="` |
| `purchasing/includes/db/invoice_db.inc` | 666 | `$sql = "UPDATE ".TB_PREF."purch_order_details` |
| `purchasing/includes/db/invoice_db.inc` | 670 | `$sql = "UPDATE ".TB_PREF."grn_items` |
| `purchasing/includes/db/invoice_db.inc` | 709 | `$sql = "SELECT DISTINCT trans.trans_no, trans.reference, trans.supp_reference` |
| `purchasing/includes/db/invoice_items_db.inc` | 17 | `$sql = "INSERT INTO ".TB_PREF."supp_invoice_items (supp_trans_type, supp_trans_no, stock_id, description, gl_code, unit_price, unit_tax, quantity,` |
| `purchasing/includes/db/invoice_items_db.inc` | 26 | `db_query($sql, "Cannot insert a supplier transaction detail record");` |
| `purchasing/includes/db/invoice_items_db.inc` | 42 | `$sql = "SELECT inv.*, grn.*, unit_price AS FullUnitPrice,` |
| `purchasing/includes/db/invoice_items_db.inc` | 58 | `$sql = "UPDATE ".TB_PREF."supp_invoice_items SET quantity=0, unit_price=0` |
| `purchasing/includes/db/po_db.inc` | 16 | `$sql = "SELECT curr_code, supp_name, tax_group_id, supp.tax_included,` |
| `purchasing/includes/db/po_db.inc` | 52 | `$sql = "DELETE FROM ".TB_PREF."purch_orders WHERE order_no=".db_escape($po);` |
| `purchasing/includes/db/po_db.inc` | 55 | `$sql = "DELETE FROM ".TB_PREF."purch_order_details WHERE order_no =".db_escape($po);` |
| `purchasing/includes/db/po_db.inc` | 72 | `$sql = "INSERT INTO ".TB_PREF."purch_orders (supplier_id, Comments, ord_date, reference,` |
| `purchasing/includes/db/po_db.inc` | 93 | `$sql = "INSERT INTO ".TB_PREF."purch_order_details (order_no, item_code, description, delivery_date,	unit_price,	quantity_ordered) VALUES (";` |
| `purchasing/includes/db/po_db.inc` | 120 | `$sql = "UPDATE ".TB_PREF."purch_orders SET Comments=" . db_escape($po_obj->Comments) . ",` |
| `purchasing/includes/db/po_db.inc` | 131 | `$sql = "DELETE FROM ".TB_PREF."purch_order_details WHERE order_no="` |
| `purchasing/includes/db/po_db.inc` | 133 | `db_query($sql, "could not delete old purch order details");` |
| `purchasing/includes/db/po_db.inc` | 138 | `$sql = "INSERT INTO ".TB_PREF."purch_order_details (po_detail_item, order_no, item_code,` |
| `purchasing/includes/db/po_db.inc` | 164 | `$sql = "SELECT po.*, supplier.*, loc.location_name` |
| `purchasing/includes/db/po_db.inc` | 210 | `$sql = "SELECT poline.*, units` |
| `purchasing/includes/db/po_db.inc` | 265 | `$sql = "SELECT item_code, quantity_ordered, quantity_received, qty_invoiced` |
| `purchasing/includes/db/po_db.inc` | 278 | `$sql = "SELECT description, units, mb_flag` |
| `purchasing/includes/db/po_db.inc` | 287 | `$sql = "SELECT` |
| `purchasing/includes/db/po_db.inc` | 347 | `$sql = "SELECT` |
| `purchasing/includes/db/supp_trans_db.inc` | 35 | `$sql = "INSERT INTO ".TB_PREF."supp_trans (trans_no, type, supplier_id, tran_date, due_date,` |
| `purchasing/includes/db/supp_trans_db.inc` | 55 | `$sql = "SELECT trans.*, (trans.ov_amount+trans.ov_gst+trans.ov_discount) AS Total,` |
| `purchasing/includes/db/supp_trans_db.inc` | 117 | `$sql = "SELECT "` |
| `purchasing/includes/db/supp_trans_db.inc` | 162 | `$sql = "SELECT trans_no FROM ".TB_PREF."supp_trans WHERE type=".db_escape($type)."` |
| `purchasing/includes/db/supp_trans_db.inc` | 173 | `$sql = "UPDATE ".TB_PREF."supp_trans SET ov_amount=0, ov_discount=0, ov_gst=0,` |
| `purchasing/includes/db/supp_trans_db.inc` | 183 | `$sql = "DELETE FROM ".TB_PREF."supp_trans` |
| `purchasing/includes/db/supp_trans_db.inc` | 219 | `$sql = "SELECT trans.type,` |
| `purchasing/includes/db/supp_trans_db.inc` | 239 | `$sql2 = "SELECT ".ST_SUPPRECEIVE." as type,` |
| `purchasing/includes/db/supp_trans_db.inc` | 272 | `$sql = "SELECT * FROM (($sql) UNION ($sql2)) as tr WHERE 1";` |
| `purchasing/includes/db/suppalloc_db.inc` | 18 | `$sql = "INSERT INTO ".TB_PREF."supp_allocations (` |
| `purchasing/includes/db/suppalloc_db.inc` | 33 | `$sql = "DELETE FROM ".TB_PREF."supp_allocations WHERE id = ".db_escape($trans_id);` |
| `purchasing/includes/db/suppalloc_db.inc` | 41 | `$sql = "SELECT (ov_amount+ov_gst-ov_discount-alloc) AS BalToAllocate` |
| `purchasing/includes/db/suppalloc_db.inc` | 55 | `$sql = "UPDATE `".TB_PREF.($trans_type==ST_PURCHORDER ? 'purch_orders' : 'supp_trans')."` trans,` |
| `purchasing/includes/db/suppalloc_db.inc` | 56 | `(SELECT person_id, sum(amt) amt from ".TB_PREF."supp_allocations` |
| `purchasing/includes/db/suppalloc_db.inc` | 79 | `$sql = "UPDATE  ".TB_PREF."supp_allocations ca` |
| `purchasing/includes/db/suppalloc_db.inc` | 93 | `$sql = "DELETE FROM ".TB_PREF."supp_allocations` |
| `purchasing/includes/db/suppalloc_db.inc` | 105 | `$sql = "SELECT` |
| `purchasing/includes/db/suppalloc_db.inc` | 139 | `$sql = "SELECT` |
| `purchasing/includes/db/suppalloc_db.inc` | 180 | `$sql = "SELECT` |
| `purchasing/includes/db/suppalloc_db.inc` | 225 | `$sql = "SELECT` |
| `purchasing/includes/db/suppalloc_db.inc` | 266 | `$sql = "SELECT` |
| `purchasing/includes/db/suppliers_db.inc` | 18 | `$sql = "INSERT INTO ".TB_PREF."suppliers (supp_name, supp_ref, address, supp_address, gst_no, website,` |
| `purchasing/includes/db/suppliers_db.inc` | 50 | `$sql = "UPDATE ".TB_PREF."suppliers SET supp_name=".db_escape($supp_name) . ",` |
| `purchasing/includes/db/suppliers_db.inc` | 76 | `$sql="DELETE FROM ".TB_PREF."suppliers WHERE supplier_id=".db_escape($supplier_id);` |
| `purchasing/includes/db/suppliers_db.inc` | 99 | `$sql = "SELECT supp.supp_name, supp.curr_code, ".TB_PREF."payment_terms.terms,` |
| `purchasing/includes/db/suppliers_db.inc` | 132 | `$sql = "SELECT * FROM ".TB_PREF."suppliers WHERE supplier_id=".db_escape($supplier_id);` |
| `purchasing/includes/db/suppliers_db.inc` | 141 | `$sql = "SELECT supp_name AS name FROM ".TB_PREF."suppliers WHERE supplier_id=".db_escape($supplier_id);` |
| `purchasing/includes/db/suppliers_db.inc` | 152 | `$sql = "SELECT payable_account,purchase_account,payment_discount_account FROM ".TB_PREF."suppliers WHERE supplier_id=".db_escape($supplier_id);` |
| `purchasing/includes/db/suppliers_db.inc` | 185 | `$sql = "SELECT curr_code FROM ".TB_PREF."suppliers WHERE supplier_id = ".db_escape($supplier_id);` |
| `purchasing/includes/db/suppliers_db.inc` | 202 | `$sql = "SELECT supplier_id, supp_name, supp_ref, address, gst_no` |
| `sales/includes/sales_db.inc` | 88 | `$sql = "SELECT price, curr_abrev, sales_type_id` |
| `sales/includes/sales_db.inc` | 183 | `$sql = "UPDATE ".TB_PREF."sales_order_details` |
| `sales/includes/sales_db.inc` | 190 | `$sql = "UPDATE ".TB_PREF."debtor_trans_details` |
| `sales/includes/sales_db.inc` | 203 | `$sql = "SELECT location.*` |
| `sales/includes/sales_db.inc` | 304 | `$sql = "SELECT child.*` |
| `sales/includes/sales_db.inc` | 338 | `$sql = "SELECT parent.*` |
| `sales/includes/sales_db.inc` | 377 | `$sql = "SELECT * FROM ".TB_PREF."debtor_trans` |
| `sales/includes/db/branches_db.inc` | 17 | `$sql = "INSERT INTO ".TB_PREF."cust_branch (debtor_no, br_name, branch_ref, br_address,` |
| `sales/includes/db/branches_db.inc` | 44 | `$sql = "UPDATE ".TB_PREF."cust_branch SET br_name = " . db_escape($br_name) . ",` |
| `sales/includes/db/branches_db.inc` | 69 | `$sql="DELETE FROM ".TB_PREF."cust_branch WHERE branch_code=".db_escape($branch_code)." AND debtor_no=".db_escape($customer_id);` |
| `sales/includes/db/branches_db.inc` | 70 | `db_query($sql,"could not delete branch");` |
| `sales/includes/db/branches_db.inc` | 75 | `$sql= "SELECT COUNT(*) FROM ".TB_PREF."$table WHERE branch_code=".db_escape($branch_code)` |
| `sales/includes/db/branches_db.inc` | 84 | `$sql = "SELECT branch.*, salesman.salesman_name` |
| `sales/includes/db/branches_db.inc` | 98 | `$sql = "SELECT * FROM ".TB_PREF."cust_branch` |
| `sales/includes/db/branches_db.inc` | 107 | `$sql = "SELECT receivables_account,sales_account, sales_discount_account, payment_discount_account` |
| `sales/includes/db/branches_db.inc` | 117 | `$sql = "SELECT br_name FROM ".TB_PREF."cust_branch` |
| `sales/includes/db/branches_db.inc` | 128 | `$sql = "SELECT branch_code, debtor_no FROM ".TB_PREF."cust_branch` |
| `sales/includes/db/branches_db.inc` | 136 | `$sql = "SELECT name, address, debtor_ref` |
| `sales/includes/db/branches_db.inc` | 144 | `$sql = "SELECT "` |
| `sales/includes/db/branches_db.inc` | 188 | `$sql = "SELECT p.*, r.action, r.type, CONCAT(r.type,'.',r.action) as ext_type` |
| `sales/includes/db/branches_db.inc` | 221 | `$sql = "SELECT p.*, r.action, r.type, CONCAT(r.type,'.',r.action) as ext_type` |
| `sales/includes/db/branches_db.inc` | 231 | `$sql = "($sql) UNION (SELECT p.*, r.action, r.type, CONCAT(r.type,'.',r.action) as ext_type` |
| `sales/includes/db/branches_db.inc` | 262 | `$sql = "SELECT *` |
| `sales/includes/db/branches_db.inc` | 279 | `$sql = "SELECT` |
| `sales/includes/db/credit_status_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."credit_status (reason_description, dissallow_invoices)` |
| `sales/includes/db/credit_status_db.inc` | 22 | `$sql = "UPDATE ".TB_PREF."credit_status SET reason_description=".db_escape($description).",` |
| `sales/includes/db/credit_status_db.inc` | 25 | `db_query($sql, "could not update credit status");` |
| `sales/includes/db/credit_status_db.inc` | 30 | `$sql = "SELECT * FROM ".TB_PREF."credit_status";` |
| `sales/includes/db/credit_status_db.inc` | 38 | `$sql = "SELECT * FROM ".TB_PREF."credit_status WHERE id=".db_escape($status_id);` |
| `sales/includes/db/credit_status_db.inc` | 47 | `$sql="DELETE FROM ".TB_PREF."credit_status WHERE id=".db_escape($status_id);` |
| `sales/includes/db/credit_status_db.inc` | 49 | `db_query($sql, "could not delete credit status");` |
| `sales/includes/db/cust_trans_db.inc` | 17 | `$sql= 'UPDATE '.TB_PREF. 'debtor_trans SET version=version+1` |
| `sales/includes/db/cust_trans_db.inc` | 37 | `$sql= 'SELECT trans_no, version FROM '.TB_PREF. 'debtor_trans` |
| `sales/includes/db/cust_trans_db.inc` | 80 | `$sql = "INSERT INTO ".TB_PREF."debtor_trans (` |
| `sales/includes/db/cust_trans_db.inc` | 99 | `$sql = "UPDATE ".TB_PREF."debtor_trans SET` |
| `sales/includes/db/cust_trans_db.inc` | 125 | `$sql = "SELECT trans.*,"` |
| `sales/includes/db/cust_trans_db.inc` | 226 | `$sql = "SELECT trans_no FROM ".TB_PREF."debtor_trans WHERE type=".db_escape($type)."` |
| `sales/includes/db/cust_trans_db.inc` | 240 | `$sql = "SELECT order_ FROM ".TB_PREF."debtor_trans WHERE type=".db_escape($type)." AND trans_no=".db_escape($type_no);` |
| `sales/includes/db/cust_trans_db.inc` | 253 | `$sql = "SELECT debtor.name, debtor.curr_code, branch.br_name` |
| `sales/includes/db/cust_trans_db.inc` | 271 | `$sql = "UPDATE ".TB_PREF."debtor_trans SET ov_amount=0, ov_discount=0, ov_gst=0, ov_freight=0,` |
| `sales/includes/db/cust_trans_db.inc` | 282 | `$sql = "DELETE FROM ".TB_PREF."debtor_trans WHERE type=".db_escape($type)." AND trans_no=".db_escape($type_no);` |
| `sales/includes/db/cust_trans_db.inc` | 310 | `$sql = "SELECT` |
| `sales/includes/db/cust_trans_db.inc` | 404 | `$sql = "SELECT trans.trans_no,` |
| `sales/includes/db/cust_trans_details_db.inc` | 19 | `$sql = "SELECT line.*,` |
| `sales/includes/db/cust_trans_details_db.inc` | 45 | `$sql = "UPDATE ".TB_PREF."debtor_trans_details SET quantity=0, unit_price=0,` |
| `sales/includes/db/cust_trans_details_db.inc` | 61 | `$sql = "UPDATE ".TB_PREF."debtor_trans_details SET` |
| `sales/includes/db/cust_trans_details_db.inc` | 72 | `$sql = "INSERT INTO ".TB_PREF."debtor_trans_details (debtor_trans_no,` |
| `sales/includes/db/custalloc_db.inc` | 18 | `$sql = "INSERT INTO ".TB_PREF."cust_allocations (` |
| `sales/includes/db/custalloc_db.inc` | 32 | `$sql = "DELETE FROM ".TB_PREF."cust_allocations WHERE id = ".db_escape($trans_id);` |
| `sales/includes/db/custalloc_db.inc` | 40 | `$sql = "SELECT * FROM ".TB_PREF."cust_allocations WHERE id = ".db_escape($trans_id);` |
| `sales/includes/db/custalloc_db.inc` | 50 | `"UPDATE `".TB_PREF.($trans_type==ST_SALESORDER ? 'sales_orders' : 'debtor_trans')."` trans,` |
| `sales/includes/db/custalloc_db.inc` | 51 | `(SELECT sum(amt) amt FROM ".TB_PREF."cust_allocations` |
| `sales/includes/db/custalloc_db.inc` | 73 | `$sql = "UPDATE  ".TB_PREF."cust_allocations ca` |
| `sales/includes/db/custalloc_db.inc` | 87 | `$sql = "DELETE FROM ".TB_PREF."cust_allocations` |
| `sales/includes/db/custalloc_db.inc` | 103 | `$sql = "SELECT` |
| `sales/includes/db/custalloc_db.inc` | 137 | `$sql = "SELECT` |
| `sales/includes/db/custalloc_db.inc` | 156 | `LEFT JOIN (SELECT order_, sum(prep_amount) amount FROM ".TB_PREF."debtor_trans dt` |
| `sales/includes/db/custalloc_db.inc` | 180 | `$sql = "SELECT` |
| `sales/includes/db/custalloc_db.inc` | 239 | `$sql = "SELECT` |
| `sales/includes/db/custalloc_db.inc` | 284 | `$sql = "SELECT` |
| `sales/includes/db/custalloc_db.inc` | 353 | `$sql = "SELECT ov_freight+ov_gst+ov_amount+ov_freight_tax as total, alloc, debtor_no FROM ".TB_PREF."debtor_trans` |
| `sales/includes/db/custalloc_db.inc` | 361 | `$sql = "SELECT * FROM ".TB_PREF."cust_allocations` |
| `sales/includes/db/customers_db.inc` | 17 | `$sql = "INSERT INTO ".TB_PREF."debtors_master (name, debtor_ref, address, tax_id,` |
| `sales/includes/db/customers_db.inc` | 34 | `$sql = "UPDATE ".TB_PREF."debtors_master SET name=" . db_escape($CustName) . ",` |
| `sales/includes/db/customers_db.inc` | 58 | `$sql = "DELETE FROM ".TB_PREF."debtors_master WHERE debtor_no=".db_escape($customer_id);;` |
| `sales/includes/db/customers_db.inc` | 59 | `db_query($sql,"cannot delete customer");` |
| `sales/includes/db/customers_db.inc` | 83 | `$sql = "SELECT debtor.name, debtor.curr_code, terms.terms, debtor.credit_limit,` |
| `sales/includes/db/customers_db.inc` | 120 | `$sql = "SELECT * FROM ".TB_PREF."debtors_master WHERE debtor_no=".db_escape($customer_id);` |
| `sales/includes/db/customers_db.inc` | 129 | `$sql = "SELECT name FROM ".TB_PREF."debtors_master WHERE debtor_no=".db_escape($customer_id);` |
| `sales/includes/db/customers_db.inc` | 140 | `$sql = "SELECT debtor.pymt_discount, credit_status.dissallow_invoices` |
| `sales/includes/db/customers_db.inc` | 181 | `$sql = "SELECT * FROM ".TB_PREF."debtors_master WHERE debtor_ref=".db_escape($reference);` |
| `sales/includes/db/customers_db.inc` | 192 | `$sql = "SELECT curr_code` |
| `sales/includes/db/customers_db.inc` | 212 | `$sql = "SELECT debtor_no, name, debtor_ref, address, tax_id FROM ".TB_PREF."debtors_master` |
| `sales/includes/db/payment_db.inc` | 146 | `$sql = "SELECT	IF(act.bank_curr_code=home_curr.value, charge.amount,` |
| `sales/includes/db/recurrent_invoices_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."recurrent_invoices (description, order_no, debtor_no,` |
| `sales/includes/db/recurrent_invoices_db.inc` | 27 | `$sql = "UPDATE ".TB_PREF."recurrent_invoices SET` |
| `sales/includes/db/recurrent_invoices_db.inc` | 43 | `$sql = "UPDATE ".TB_PREF."recurrent_invoices SET last_sent='$date' WHERE id=".db_escape($id);` |
| `sales/includes/db/recurrent_invoices_db.inc` | 50 | `$sql="DELETE FROM ".TB_PREF."recurrent_invoices WHERE id=".db_escape($selected_id);` |
| `sales/includes/db/recurrent_invoices_db.inc` | 51 | `db_query($sql,"could not delete recurrent invoice");` |
| `sales/includes/db/recurrent_invoices_db.inc` | 61 | `$sql = "SELECT *, DATE_ADD(DATE_ADD(IF(`last_sent`='0000-00-00', `begin`, `last_sent`), INTERVAL `monthly` MONTH), INTERVAL `days` DAY) <= '$date'` |
| `sales/includes/db/recurrent_invoices_db.inc` | 64 | `$sql = "SELECT * ";` |
| `sales/includes/db/recurrent_invoices_db.inc` | 73 | `$sql = "SELECT * FROM ".TB_PREF."recurrent_invoices WHERE id=".db_escape($selected_id);` |
| `sales/includes/db/recurrent_invoices_db.inc` | 81 | `$sql = "SELECT count(*) FROM ".TB_PREF."recurrent_invoices WHERE description=".db_escape($description);` |
| `sales/includes/db/recurrent_invoices_db.inc` | 95 | `$sql = "SELECT DATE_ADD(DATE_ADD(IF(`last_sent`='0000-00-00', `begin`, `last_sent`), INTERVAL `monthly` MONTH), INTERVAL `days` DAY) <= '$date'` |
| `sales/includes/db/recurrent_invoices_db.inc` | 111 | `$sql1 = "SELECT branch.*` |
| `sales/includes/db/recurrent_invoices_db.inc` | 117 | `$sql2 = "SELECT branch.*` |
| `sales/includes/db/recurrent_invoices_db.inc` | 123 | `$sql = "SELECT count(*) FROM ($sql1 UNION $sql2) a";` |
| `sales/includes/db/recurrent_invoices_db.inc` | 134 | `$sql1 = "SELECT debtor.curr_code` |
| `sales/includes/db/recurrent_invoices_db.inc` | 140 | `$sql2 = "SELECT debtor.curr_code` |
| `sales/includes/db/recurrent_invoices_db.inc` | 146 | `$sql = "SELECT distinct * FROM ($sql1 UNION $sql2) a";` |
| `sales/includes/db/sales_delivery_db.inc` | 104 | `$sql = "UPDATE ".TB_PREF."stock_master SET inactive=1, material_cost=0` |
| `sales/includes/db/sales_delivery_db.inc` | 209 | `$sql = "SELECT sum(ov_freight) as freight FROM ".TB_PREF."debtor_trans WHERE order_ = $trans_no AND type = " . ST_CUSTDELIVERY . " AND debtor_no = " . $delivery->customer_id;` |
| `sales/includes/db/sales_groups_db.inc` | 15 | `$sql = "INSERT INTO ".TB_PREF."groups (description) VALUES (".db_escape($description) . ")";` |
| `sales/includes/db/sales_groups_db.inc` | 21 | `$sql = "UPDATE ".TB_PREF."groups SET description=".db_escape($description)." WHERE id = ".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 27 | `$sql="DELETE FROM ".TB_PREF."groups WHERE id=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 28 | `db_query($sql,"could not delete sales group");` |
| `sales/includes/db/sales_groups_db.inc` | 33 | `$sql = "SELECT * FROM ".TB_PREF."groups";` |
| `sales/includes/db/sales_groups_db.inc` | 41 | `$sql = "SELECT * FROM ".TB_PREF."groups WHERE id=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 49 | `$sql = "SELECT description FROM ".TB_PREF."groups WHERE id = ".db_escape($group_no);` |
| `sales/includes/db/sales_groups_db.inc` | 57 | `$sql = "INSERT INTO ".TB_PREF."areas (description) VALUES (".db_escape($description) . ")";` |
| `sales/includes/db/sales_groups_db.inc` | 63 | `$sql = "UPDATE ".TB_PREF."areas SET description=".db_escape($description)." WHERE area_code = ".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 69 | `$sql="DELETE FROM ".TB_PREF."areas WHERE area_code=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 70 | `db_query($sql,"could not delete sales area");` |
| `sales/includes/db/sales_groups_db.inc` | 75 | `$sql = "SELECT * FROM ".TB_PREF."areas";` |
| `sales/includes/db/sales_groups_db.inc` | 82 | `$sql = "SELECT * FROM ".TB_PREF."areas WHERE area_code=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 90 | `$sql = "SELECT description FROM ".TB_PREF."areas WHERE area_code=".db_escape($id);` |
| `sales/includes/db/sales_groups_db.inc` | 101 | `$sql = "INSERT INTO ".TB_PREF."salesman (salesman_name, salesman_phone, salesman_fax, salesman_email,` |
| `sales/includes/db/sales_groups_db.inc` | 109 | `db_query($sql,"The insert of the sales person failed");` |
| `sales/includes/db/sales_groups_db.inc` | 115 | `$sql = "UPDATE ".TB_PREF."salesman SET salesman_name=".db_escape($salesman_name) . ",` |
| `sales/includes/db/sales_groups_db.inc` | 123 | `db_query($sql,"The update of the sales person failed");` |
| `sales/includes/db/sales_groups_db.inc` | 128 | `$sql="DELETE FROM ".TB_PREF."salesman WHERE salesman_code=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 134 | `$sql = "SELECT * FROM ".TB_PREF."salesman";` |
| `sales/includes/db/sales_groups_db.inc` | 141 | `$sql = "SELECT *  FROM ".TB_PREF."salesman WHERE salesman_code=".db_escape($selected_id);` |
| `sales/includes/db/sales_groups_db.inc` | 149 | `$sql = "SELECT salesman_name FROM ".TB_PREF."salesman WHERE salesman_code=".db_escape($id);` |
| `sales/includes/db/sales_invoice_db.inc` | 285 | `$sql = "SELECT IF(dt.prep_amount>0, dt.prep_amount/so.total ,0)` |
| `sales/includes/db/sales_invoice_db.inc` | 298 | `$sql = "SELECT so.total - IFNULL(SUM(inv.prep_amount),0) FROM "` |
| `sales/includes/db/sales_invoice_db.inc` | 320 | `$sql = "SELECT MIN(trans.tran_date)` |
| `sales/includes/db/sales_invoice_db.inc` | 340 | `$sql = "SELECT MIN(payment.tran_date)` |
| `sales/includes/db/sales_order_db.inc` | 23 | `$sql = "INSERT INTO ".TB_PREF."sales_orders (order_no, type, debtor_no, trans_type, branch_code, customer_ref, reference, comments, ord_date,` |
| `sales/includes/db/sales_order_db.inc` | 61 | `$sql = "INSERT INTO ".TB_PREF."sales_order_details (order_no, trans_type, stk_code, description, unit_price, quantity, discount_percent) VALUES (";` |
| `sales/includes/db/sales_order_db.inc` | 92 | `$sql = "DELETE FROM ".TB_PREF."sales_orders WHERE order_no=" . db_escape($order_no)` |
| `sales/includes/db/sales_order_db.inc` | 95 | `db_query($sql, "order Header Delete");` |
| `sales/includes/db/sales_order_db.inc` | 97 | `$sql = "DELETE FROM ".TB_PREF."sales_order_details WHERE order_no ="` |
| `sales/includes/db/sales_order_db.inc` | 99 | `db_query($sql, "order Detail Delete");` |
| `sales/includes/db/sales_order_db.inc` | 111 | `$sql= 'UPDATE '.TB_PREF.'sales_orders SET version=version+1 WHERE order_no='. db_escape($so_num).` |
| `sales/includes/db/sales_order_db.inc` | 113 | `db_query($sql, 'Concurrent editing conflict while sales order update');` |
| `sales/includes/db/sales_order_db.inc` | 135 | `$sql = "UPDATE ".TB_PREF."sales_orders SET type =".db_escape($order->so_type)." ,` |
| `sales/includes/db/sales_order_db.inc` | 164 | `$sql = "DELETE FROM ".TB_PREF."sales_order_details WHERE order_no =" . db_escape($order_no) . " AND trans_type=".$order->trans_type;` |
| `sales/includes/db/sales_order_db.inc` | 183 | `$sql = "INSERT INTO ".TB_PREF."sales_order_details` |
| `sales/includes/db/sales_order_db.inc` | 194 | `$sql = "UPDATE ".TB_PREF."sales_order_details` |
| `sales/includes/db/sales_order_db.inc` | 224 | `$sql = "SELECT sorder.*,` |
| `sales/includes/db/sales_order_db.inc` | 242 | `LEFT JOIN (SELECT trans_no_to, sum(amt) ord_allocs FROM ".TB_PREF."cust_allocations` |
| `sales/includes/db/sales_order_db.inc` | 245 | `LEFT JOIN (SELECT order_, sum(alloc) inv_allocs FROM ".TB_PREF."debtor_trans` |
| `sales/includes/db/sales_order_db.inc` | 281 | `$sql = "SELECT id, stk_code, unit_price,` |
| `sales/includes/db/sales_order_db.inc` | 355 | `$sql = "SELECT SUM(qty_sent) FROM ".TB_PREF.` |
| `sales/includes/db/sales_order_db.inc` | 365 | `$sql = "SELECT order_ FROM ".TB_PREF."debtor_trans WHERE type=".ST_CUSTDELIVERY." AND order_=".db_escape($order_no);` |
| `sales/includes/db/sales_order_db.inc` | 375 | `$sql = "UPDATE ".TB_PREF."sales_order_details` |
| `sales/includes/db/sales_order_db.inc` | 408 | `$sql = "SELECT cust.name,` |
| `sales/includes/db/sales_order_db.inc` | 439 | `$sql = "SELECT branch.br_name,` |
| `sales/includes/db/sales_order_db.inc` | 468 | `$sql = "SELECT` |
| `sales/includes/db/sales_order_db.inc` | 492 | `LEFT JOIN (SELECT trans_no_to, sum(amt) ord_payments FROM ".TB_PREF."cust_allocations WHERE trans_type_to=".ST_SALESORDER." GROUP BY trans_no_to)` |
| `sales/includes/db/sales_order_db.inc` | 494 | `LEFT JOIN (SELECT order_, sum(prep_amount) inv_payments	FROM ".TB_PREF."debtor_trans WHERE type=".ST_SALESINVOICE." GROUP BY order_)` |
| `sales/includes/db/sales_order_db.inc` | 567 | `$sql = "UPDATE ".TB_PREF."sales_order_details` |
| `sales/includes/db/sales_order_db.inc` | 579 | `$sql = "SELECT trans_no, dt.type as type, tran_date, reference, prep_amount` |
| `sales/includes/db/sales_order_db.inc` | 590 | `$sql = "SELECT count(*) FROM ".TB_PREF."sales_order_details WHERE order_no=".db_escape($order_no)." AND trans_type=".ST_SALESORDER` |
| `sales/includes/db/sales_order_db.inc` | 603 | `$sql = "UPDATE ".TB_PREF."sales_orders SET type = ".db_escape($status)." WHERE order_no=".db_escape($id);` |
| `sales/includes/db/sales_order_db.inc` | 613 | `$sql = "SELECT count(*)` |
| `sales/includes/db/sales_order_db.inc` | 615 | `((SELECT trans_no_to FROM ".TB_PREF."cust_allocations` |
| `sales/includes/db/sales_order_db.inc` | 618 | `(SELECT order_ FROM ".TB_PREF."debtor_trans` |
| `sales/includes/db/sales_points_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."sales_pos (pos_name, pos_location, pos_account, cash_sale, credit_sale) VALUES (".db_escape($name)` |
| `sales/includes/db/sales_points_db.inc` | 23 | `$sql = "UPDATE ".TB_PREF."sales_pos SET pos_name=".db_escape($name)` |
| `sales/includes/db/sales_points_db.inc` | 30 | `db_query($sql, "could not update sales type");` |
| `sales/includes/db/sales_points_db.inc` | 35 | `$sql = "SELECT pos.*, loc.location_name, acc.bank_account_name FROM "` |
| `sales/includes/db/sales_points_db.inc` | 46 | `$sql = "SELECT pos.*, loc.location_name, acc.bank_account_name FROM "` |
| `sales/includes/db/sales_points_db.inc` | 59 | `$sql = "SELECT pos_name FROM ".TB_PREF."sales_pos WHERE id=".db_escape($id);` |
| `sales/includes/db/sales_points_db.inc` | 69 | `$sql="DELETE FROM ".TB_PREF."sales_pos WHERE id=".db_escape($id);` |
| `sales/includes/db/sales_types_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."sales_types (sales_type,tax_included,factor) VALUES (".db_escape($name).","` |
| `sales/includes/db/sales_types_db.inc` | 22 | `$sql = "UPDATE ".TB_PREF."sales_types SET sales_type = ".db_escape($name).",` |
| `sales/includes/db/sales_types_db.inc` | 25 | `db_query($sql, "could not update sales type");` |
| `sales/includes/db/sales_types_db.inc` | 30 | `$sql = "SELECT * FROM ".TB_PREF."sales_types";` |
| `sales/includes/db/sales_types_db.inc` | 39 | `$sql = "SELECT * FROM ".TB_PREF."sales_types WHERE id=".db_escape($id);` |
| `sales/includes/db/sales_types_db.inc` | 48 | `$sql = "SELECT sales_type FROM ".TB_PREF."sales_types WHERE id=".db_escape($id);` |
| `sales/includes/db/sales_types_db.inc` | 58 | `$sql="DELETE FROM ".TB_PREF."sales_types WHERE id=".db_escape($id);` |
| `sales/includes/db/sales_types_db.inc` | 61 | `$sql ="DELETE FROM ".TB_PREF."prices WHERE sales_type_id=".db_escape($id);` |
| `taxes/db/item_tax_types_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."item_tax_types (name, exempt)` |
| `taxes/db/item_tax_types_db.inc` | 33 | `$sql = "UPDATE ".TB_PREF."item_tax_types SET name=".db_escape($name).` |
| `taxes/db/item_tax_types_db.inc` | 36 | `db_query($sql, "could not update item tax type");` |
| `taxes/db/item_tax_types_db.inc` | 47 | `$sql = "SELECT * FROM ".TB_PREF."item_tax_types";` |
| `taxes/db/item_tax_types_db.inc` | 56 | `$sql = "SELECT * FROM ".TB_PREF."item_tax_types WHERE id=".db_escape($id);` |
| `taxes/db/item_tax_types_db.inc` | 65 | `$sql = "SELECT item_tax_type.*` |
| `taxes/db/item_tax_types_db.inc` | 80 | `$sql = "DELETE FROM ".TB_PREF."item_tax_types WHERE id=".db_escape($id);` |
| `taxes/db/item_tax_types_db.inc` | 82 | `db_query($sql, "could not delete item tax type");` |
| `taxes/db/item_tax_types_db.inc` | 93 | `$sql = "INSERT INTO ".TB_PREF."item_tax_type_exemptions (item_tax_type_id, tax_type_id)` |
| `taxes/db/item_tax_types_db.inc` | 101 | `$sql = "DELETE FROM ".TB_PREF."item_tax_type_exemptions WHERE item_tax_type_id=".db_escape($id);` |
| `taxes/db/item_tax_types_db.inc` | 103 | `db_query($sql, "could not delete item tax type exemptions");` |
| `taxes/db/item_tax_types_db.inc` | 108 | `$sql = "SELECT * FROM ".TB_PREF."item_tax_type_exemptions WHERE item_tax_type_id=".db_escape($id);` |
| `taxes/db/tax_groups_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."tax_groups (name) VALUES (".db_escape($name).")";` |
| `taxes/db/tax_groups_db.inc` | 30 | `$sql = "UPDATE ".TB_PREF."tax_groups SET name=".db_escape($name)." WHERE id=".db_escape($id);` |
| `taxes/db/tax_groups_db.inc` | 31 | `db_query($sql, "could not update tax group");` |
| `taxes/db/tax_groups_db.inc` | 41 | `$sql = "SELECT * FROM ".TB_PREF."tax_groups";` |
| `taxes/db/tax_groups_db.inc` | 49 | `$sql = "SELECT * FROM ".TB_PREF."tax_groups WHERE id=".db_escape($type_id);` |
| `taxes/db/tax_groups_db.inc` | 60 | `$sql = "DELETE FROM ".TB_PREF."tax_groups WHERE id=".db_escape($id);` |
| `taxes/db/tax_groups_db.inc` | 62 | `db_query($sql, "could not delete tax group");` |
| `taxes/db/tax_groups_db.inc` | 73 | `$sql = "INSERT INTO ".TB_PREF."tax_group_items (tax_group_id, tax_type_id, tax_shipping)` |
| `taxes/db/tax_groups_db.inc` | 81 | `$sql = "DELETE FROM ".TB_PREF."tax_group_items WHERE tax_group_id=".db_escape($id);` |
| `taxes/db/tax_groups_db.inc` | 83 | `db_query($sql, "could not delete item tax group items");` |
| `taxes/db/tax_groups_db.inc` | 104 | `AND g.tax_group_id=". ($group_id ? db_escape($group_id) : "(SELECT MIN(id) FROM ".TB_PREF."tax_groups)")` |
| `taxes/db/tax_types_db.inc` | 14 | `$sql = "INSERT INTO ".TB_PREF."tax_types (name, sales_gl_code, purchasing_gl_code, rate)` |
| `taxes/db/tax_types_db.inc` | 23 | `$sql = "UPDATE ".TB_PREF."tax_types SET name=".db_escape($name).",` |
| `taxes/db/tax_types_db.inc` | 29 | `db_query($sql, "could not update tax type");` |
| `taxes/db/tax_types_db.inc` | 34 | `$sql = "SELECT tax_type.*,` |
| `taxes/db/tax_types_db.inc` | 49 | `$sql = "SELECT * FROM ".TB_PREF."tax_types WHERE !inactive";` |
| `taxes/db/tax_types_db.inc` | 56 | `$sql = "SELECT tax_type.*,` |
| `taxes/db/tax_types_db.inc` | 71 | `$sql = "SELECT rate FROM ".TB_PREF."tax_types WHERE id=".db_escape($type_id);` |
| `taxes/db/tax_types_db.inc` | 83 | `$sql = "DELETE FROM ".TB_PREF."tax_types WHERE id=".db_escape($type_id);` |
| `taxes/db/tax_types_db.inc` | 85 | `db_query($sql, "could not delete tax type");` |
| `taxes/db/tax_types_db.inc` | 88 | `$sql = "DELETE FROM ".TB_PREF."item_tax_type_exemptions WHERE tax_type_id=".db_escape($type_id);` |
| `taxes/db/tax_types_db.inc` | 90 | `db_query($sql, "could not delete item tax type exemptions");` |
| `taxes/db/tax_types_db.inc` | 105 | `$sql = "SELECT count(*) FROM "` |
| `taxes/db/tax_types_db.inc` | 121 | `$sql= "SELECT id FROM ".TB_PREF."tax_types WHERE` |
| `includes/db/allocations_db.inc` | 23 | `$sql = "(SELECT alloc.*, trans.tran_date FROM ".TB_PREF."cust_allocations alloc` |
| `includes/db/allocations_db.inc` | 27 | `(SELECT alloc.*, trans.tran_date FROM ".TB_PREF."supp_allocations alloc` |
| `includes/db/allocations_db.inc` | 51 | `$sql = "DELETE FROM ".TB_PREF.$allocations."` |
| `includes/db/allocations_db.inc` | 57 | `$sql = "INSERT INTO ".TB_PREF.$allocations." (amt, date_alloc, trans_type_from, trans_no_from, trans_type_to, trans_no_to, person_id)` |
| `includes/db/audit_trail_db.inc` | 18 | `$sql = "INSERT INTO ".TB_PREF."audit_trail"` |
| `includes/db/audit_trail_db.inc` | 27 | `$sql = "UPDATE ".TB_PREF."audit_trail audit LEFT JOIN ".TB_PREF."fiscal_year year ON year.begin<='$date' AND year.end>='$date'` |
| `includes/db/audit_trail_db.inc` | 33 | `db_query($sql, "Cannot update audit gl_seq");` |
| `includes/db/audit_trail_db.inc` | 39 | `$sql = "SELECT * FROM ".TB_PREF."audit_trail"` |
| `includes/db/audit_trail_db.inc` | 48 | `$sql = "SELECT * FROM ".TB_PREF."audit_trail"` |
| `includes/db/audit_trail_db.inc` | 69 | `$sql = "SELECT a.id, gl.tran_date, a.fiscal_year, a.gl_seq,` |
| `includes/db/audit_trail_db.inc` | 77 | `$result = db_query($sql, "Cannot select transactions for closing");` |
| `includes/db/audit_trail_db.inc` | 93 | `$sql2 = "UPDATE ".TB_PREF."audit_trail SET"` |
| `includes/db/audit_trail_db.inc` | 117 | `$sql = "SELECT	MAX(gl_seq) as gl_seq  FROM ".TB_PREF."audit_trail"` |
| `includes/db/class.data_set.inc` | 269 | `$sql = "SELECT * FROM ".TB_PREF.$this->name." WHERE ";` |
| `includes/db/class.data_set.inc` | 297 | `$sql = "SELECT ".implode(',', $fields)." FROM ".TB_PREF.$this->name;` |
| `includes/db/class.data_set.inc` | 321 | `$sql = "UPDATE ".TB_PREF.$this->name." SET ";` |
| `includes/db/class.data_set.inc` | 360 | `$sql = "DELETE FROM ".TB_PREF.$this->name;` |
| `includes/db/class.data_set.inc` | 388 | `$sql = "INSERT INTO ".TB_PREF.$this->name. ' (';` |
| `includes/db/class.reflines_db.inc` | 81 | `$sql = "SELECT *` |
| `includes/db/class.reflines_db.inc` | 82 | `FROM (SELECT r.* FROM ".TB_PREF."refs r` |
| `includes/db/class.reflines_db.inc` | 109 | `$sql  = "UPDATE ".TB_PREF."reflines SET `default`=(`id`=".db_escape($id).")` |
| `includes/db/class.reflines_db.inc` | 111 | `return db_query($sql, "cannot update default refline");` |
| `includes/db/class.reflines_db.inc` | 134 | `$sql = "SELECT * FROM ".TB_PREF."reflines WHERE trans_type=".db_escape($type)." AND `default`";` |
| `includes/db/class.reflines_db.inc` | 141 | `$sql = "SELECT count(*) FROM ".TB_PREF."reflines WHERE trans_type=".db_escape($type);` |
| `includes/db/class.reflines_db.inc` | 155 | `$sql = "SELECT * FROM ".TB_PREF."reflines WHERE trans_type=".db_escape($type)` |
| `includes/db/class.reflines_db.inc` | 158 | `$sql .= " UNION SELECT * FROM ".TB_PREF."reflines WHERE trans_type=".db_escape($type)." AND `prefix`=''";` |
| `includes/db/class.reflines_db.inc` | 170 | `$sql = "UPDATE ".TB_PREF."reflines SET pattern=SUBSTRING(" . db_escape(trim($reference)) .", LENGTH(`prefix`)+1)"` |
| `includes/db/comments_db.inc` | 16 | `$sql = "SELECT * FROM ".TB_PREF."comments WHERE type="` |
| `includes/db/comments_db.inc` | 29 | `$sql = "INSERT INTO ".TB_PREF."comments (type, id, date_, memo_)` |
| `includes/db/comments_db.inc` | 49 | `$sql = "UPDATE ".TB_PREF."comments SET memo_=".db_escape($memo_)` |
| `includes/db/comments_db.inc` | 52 | `db_query($sql, "could not update comments");` |
| `includes/db/comments_db.inc` | 60 | `$sql = "DELETE FROM ".TB_PREF."comments WHERE type=".db_escape($type)` |
| `includes/db/comments_db.inc` | 63 | `db_query($sql, "could not delete from comments transaction table");` |
| `includes/db/connect_db.inc` | 22 | `$result = db_query("SELECT VERSION()");` |
| `includes/db/connect_db.inc` | 103 | `$result = db_query("SELECT value FROM ".TB_PREF."sys_prefs WHERE name='version_id'");` |
| `includes/db/connect_db.inc` | 114 | `$result = db_query("SELECT @@character_set_database");` |
| `includes/db/connect_db_mysql.inc` | 78 | `if ($SysPrefs->select_trail \|\| (strstr($sql, 'SELECT') === false)) {` |
| `includes/db/connect_db_mysql.inc` | 195 | `return mysql_query("ALTER DATABASE COLLATE ".get_mysql_collation($fa_collation), $db);` |
| `includes/db/connect_db_mysql.inc` | 211 | `$sql = "CREATE DATABASE IF NOT EXISTS `" . $connection["dbname"] . "`"` |
| `includes/db/connect_db_mysql.inc` | 228 | `$sql = "DROP DATABASE IF EXISTS " . $connection["dbname"] . "";` |
| `includes/db/connect_db_mysql.inc` | 241 | `db_query("DROP TABLE `".$table['Name'] . "`");` |
| `includes/db/connect_db_mysqli.inc` | 79 | `if ($SysPrefs->select_trail \|\| (strstr($sql, 'SELECT') === false)) {` |
| `includes/db/connect_db_mysqli.inc` | 80 | `mysqli_query($db, "INSERT INTO ".$cur_prefix."sql_trail` |
| `includes/db/connect_db_mysqli.inc` | 194 | `return mysqli_query($db, "ALTER DATABASE COLLATE ".get_mysql_collation($fa_collation));` |
| `includes/db/connect_db_mysqli.inc` | 210 | `$sql = "CREATE DATABASE IF NOT EXISTS `" . $connection["dbname"] . "`"` |
| `includes/db/connect_db_mysqli.inc` | 230 | `$sql = "DROP DATABASE IF EXISTS " . $connection["dbname"] . "";` |
| `includes/db/connect_db_mysqli.inc` | 243 | `db_query("DROP TABLE `".$table['Name'] . "`");` |
| `includes/db/crm_contacts_db.inc` | 16 | `$sql = "INSERT INTO ".TB_PREF."crm_persons (ref, name, name2, address,` |
| `includes/db/crm_contacts_db.inc` | 33 | `$ret = db_query($sql, "Can't insert crm person");` |
| `includes/db/crm_contacts_db.inc` | 46 | `$sql = "UPDATE ".TB_PREF."crm_persons SET "` |
| `includes/db/crm_contacts_db.inc` | 61 | `$ret = db_query($sql, "Can't update crm person");` |
| `includes/db/crm_contacts_db.inc` | 75 | `$sql = "DELETE FROM ".TB_PREF."crm_contacts WHERE person_id=".db_escape($person);` |
| `includes/db/crm_contacts_db.inc` | 76 | `db_query($sql, "Can't delete crm contacts");` |
| `includes/db/crm_contacts_db.inc` | 78 | `$sql = "DELETE FROM ".TB_PREF."crm_persons WHERE id=".db_escape($person);` |
| `includes/db/crm_contacts_db.inc` | 79 | `$ret = db_query($sql, "Can't delete crm person");` |
| `includes/db/crm_contacts_db.inc` | 89 | `$sql = "SELECT t.*, p.*, r.id as contact_id FROM ".TB_PREF."crm_persons p,"` |
| `includes/db/crm_contacts_db.inc` | 123 | `$sql = "SELECT * FROM ".TB_PREF."crm_persons WHERE id=".db_escape($id);` |
| `includes/db/crm_contacts_db.inc` | 138 | `$sql = "SELECT t.id FROM "` |
| `includes/db/crm_contacts_db.inc` | 152 | `$sql = "DELETE FROM ".TB_PREF."crm_contacts WHERE person_id=".db_escape($id);` |
| `includes/db/crm_contacts_db.inc` | 158 | `$ret = db_query($sql, "Can't delete person contacts");` |
| `includes/db/crm_contacts_db.inc` | 165 | `$sql = "INSERT INTO ".TB_PREF."crm_contacts (person_id,type,action,entity_id)` |
| `includes/db/crm_contacts_db.inc` | 170 | `$ret = db_query($sql, "Can't update person contacts");` |
| `includes/db/crm_contacts_db.inc` | 193 | `$sql = "INSERT INTO ".TB_PREF."crm_categories (type, action, name, description)` |
| `includes/db/crm_contacts_db.inc` | 199 | `db_query($sql,"The insert of the crm category failed");` |
| `includes/db/crm_contacts_db.inc` | 204 | `$sql = "UPDATE ".TB_PREF."crm_categories SET ";` |
| `includes/db/crm_contacts_db.inc` | 212 | `db_query($sql,"The update of the crm category failed");` |
| `includes/db/crm_contacts_db.inc` | 218 | `$sql="DELETE FROM ".TB_PREF."crm_categories WHERE system=0 AND id=".db_escape($selected_id);` |
| `includes/db/crm_contacts_db.inc` | 219 | `db_query($sql,"could not delete crm category");` |
| `includes/db/crm_contacts_db.inc` | 224 | `$sql = "SELECT * FROM ".TB_PREF."crm_categories";` |
| `includes/db/crm_contacts_db.inc` | 232 | `$sql = "SELECT * FROM ".TB_PREF."crm_categories WHERE id=".db_escape($selected_id);` |
| `includes/db/crm_contacts_db.inc` | 240 | `$sql = "SELECT name FROM ".TB_PREF."crm_categories WHERE id=".db_escape($id);` |
| `includes/db/crm_contacts_db.inc` | 253 | `$sql = "INSERT INTO ".TB_PREF."crm_contacts (person_id, type, action, entity_id) VALUES ("` |
| `includes/db/crm_contacts_db.inc` | 258 | `return db_query($sql, "Can't insert crm contact");` |
| `includes/db/crm_contacts_db.inc` | 265 | `$sql = "DELETE FROM ".TB_PREF."crm_contacts WHERE id=".db_escape($id);` |
| `includes/db/crm_contacts_db.inc` | 267 | `return db_query($sql, "Can't delete crm contact");` |
| `includes/db/crm_contacts_db.inc` | 274 | `$sql = "DELETE FROM ".TB_PREF."crm_contacts WHERE ";` |
| `includes/db/crm_contacts_db.inc` | 285 | `return db_query($sql.implode(' AND ', $where), "Can't delete crm contact");` |
| `includes/db/crm_contacts_db.inc` | 293 | `$sql = "SELECT t.type, t.action, p.*, r.person_id, r.id  FROM ".TB_PREF."crm_persons p,"` |
| `includes/db/crm_contacts_db.inc` | 309 | `$sql = "SELECT COUNT(*) FROM ".TB_PREF."crm_contacts WHERE type='".$row['type']."' AND action='".$row['action']."'";` |
| `includes/db/inventory_db.inc` | 18 | `$sql = "SELECT SUM(qty)` |
| `includes/db/inventory_db.inc` | 57 | `$sql = "SELECT SUM(qty) qty, '$date' tran_date FROM ".TB_PREF."stock_moves` |
| `includes/db/inventory_db.inc` | 75 | `$sql = "SELECT  {$qos['qty']}+total qty, tran_date FROM ($rt) stock_status ORDER by total, tran_date";` |
| `includes/db/inventory_db.inc` | 89 | `$sql = "SELECT item.material_cost, item.units, unit.decimals` |
| `includes/db/inventory_db.inc` | 103 | `$sql = "SELECT material_cost` |
| `includes/db/inventory_db.inc` | 117 | `$sql = "SELECT purchase_cost` |
| `includes/db/inventory_db.inc` | 131 | `$sql = "SELECT stock_id FROM "` |
| `includes/db/inventory_db.inc` | 148 | `$sql = "SELECT SUM(qty), @q:= @q + qty, IF(@q < 0 AND @flag=0, @flag:=1,@flag:=0), IF(@q < 0 AND @flag=1, tran_date,'') AS begin_date` |
| `includes/db/inventory_db.inc` | 163 | `$sql = "SELECT qty` |
| `includes/db/inventory_db.inc` | 178 | `$sql = "SELECT * from ".TB_PREF."stock_moves` |
| `includes/db/inventory_db.inc` | 212 | `$sql = "SELECT SUM(-qty), SUM(-qty*standard_cost) FROM ".TB_PREF."stock_moves` |
| `includes/db/inventory_db.inc` | 227 | `$sql = "SELECT SUM(-qty), SUM(-qty*IF(type=".ST_SUPPRECEIVE." OR type=".ST_SUPPCREDIT.", price, standard_cost))` |
| `includes/db/inventory_db.inc` | 234 | `$sql = "SELECT IF(type=".ST_SUPPRECEIVE." OR type=".ST_SUPPCREDIT.", price, standard_cost)` |
| `includes/db/inventory_db.inc` | 242 | `$sql = "SELECT SUM(qty)` |
| `includes/db/inventory_db.inc` | 261 | `$sql = "SELECT SUM(qty), SUM(qty*standard_cost)` |
| `includes/db/inventory_db.inc` | 333 | `$sql = "SELECT mb_flag, inventory_account, cogs_account,` |
| `includes/db/inventory_db.inc` | 343 | `$sql = "SELECT purchase_cost FROM` |
| `includes/db/inventory_db.inc` | 354 | `$sql = "UPDATE ".TB_PREF."stock_master SET purchase_cost=".db_escape($price)` |
| `includes/db/inventory_db.inc` | 412 | `$sql = "INSERT INTO ".TB_PREF."stock_moves (stock_id, trans_no, type, loc_code,` |
| `includes/db/inventory_db.inc` | 426 | `$sql = "UPDATE ".TB_PREF."stock_moves SET standard_cost=".db_escape($cost)` |
| `includes/db/inventory_db.inc` | 437 | `$sql = "SELECT move.*, item.description, item.mb_flag, item.units, stock.location_name` |
| `includes/db/inventory_db.inc` | 454 | `$sql = "SELECT move.*, supplier.supplier_id` |
| `includes/db/inventory_db.inc` | 479 | `$sql = "DELETE FROM ".TB_PREF."stock_moves` |
| `includes/db/inventory_db.inc` | 489 | `$sql = "SELECT location_name FROM ".TB_PREF."locations` |
| `includes/db/inventory_db.inc` | 505 | `$sql = "SELECT mb_flag FROM ".TB_PREF."stock_master` |
| `includes/db/manufacturing_db.inc` | 15 | `$sql = "SELECT SUM(line.quantity - line.qty_sent) AS QtyDemand` |
| `includes/db/manufacturing_db.inc` | 39 | `$sql = "SELECT stock_id, SUM(qty)` |
| `includes/db/manufacturing_db.inc` | 76 | `$sql = "SELECT parent, component, quantity FROM "` |
| `includes/db/manufacturing_db.inc` | 107 | `$sql = "SELECT line.stk_code, SUM(line.quantity-line.qty_sent) AS Demmand` |
| `includes/db/manufacturing_db.inc` | 129 | `$sql = "SELECT SUM(line.quantity_ordered - line.quantity_received) AS qoo` |
| `includes/db/manufacturing_db.inc` | 152 | `$sql = "SELECT SUM((wo.units_reqd-wo.units_issued) * (req.units_req-req.units_issued)) AS qoo` |
| `includes/db/manufacturing_db.inc` | 171 | `$sql = "SELECT SUM((units_reqd-units_issued)) AS qoo` |
| `includes/db/manufacturing_db.inc` | 193 | `$sql = "INSERT INTO ".TB_PREF."bom (parent, component, workcentre_added, loc_code, quantity)` |
| `includes/db/manufacturing_db.inc` | 204 | `$sql = "UPDATE ".TB_PREF."bom SET workcentre_added=".db_escape($workcentre_added)` |
| `includes/db/manufacturing_db.inc` | 209 | `check_db_error("Could not update this bom component", $sql);` |
| `includes/db/manufacturing_db.inc` | 211 | `db_query($sql,"could not update bom");` |
| `includes/db/manufacturing_db.inc` | 216 | `$sql = "DELETE FROM ".TB_PREF."bom WHERE id=".db_escape($selected_id);` |
| `includes/db/manufacturing_db.inc` | 217 | `db_query($sql,"Could not delete this bom components");` |
| `includes/db/manufacturing_db.inc` | 222 | `$sql = "SELECT bom.*, loc.location_name,` |
| `includes/db/manufacturing_db.inc` | 242 | `$sql = "SELECT bom.*, item.description` |
| `includes/db/manufacturing_db.inc` | 264 | `$sql = "SELECT component` |
| `includes/db/manufacturing_db.inc` | 283 | `$sql = "SELECT component FROM ".TB_PREF."bom WHERE parent=".db_escape($component_to_check);` |
| `includes/db/sql_functions.inc` | 59 | `$sql = "UPDATE ".TB_PREF.$table." SET inactive = "` |
| `includes/db/sql_functions.inc` | 62 | `db_query($sql, "Can't update record status");` |

**Total functional SQL-related lines:** 908
