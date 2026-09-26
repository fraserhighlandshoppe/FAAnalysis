# FA 2.4.3 SQL Query Inventory

Source root: `/home/kevin/Documents/ksf_Infrastructure/FA/2.4.3`

| File | Line | SQL Snippet / Context |
|------|------|-----------------------|
| `reporting/rep710.php` | 36 | `$sql = "SELECT a.*,` |
| `reporting/rep710.php` | 40 | `FROM ".TB_PREF."audit_trail AS a JOIN ".TB_PREF."users AS u` |
| `reporting/rep710.php` | 41 | `LEFT JOIN ".TB_PREF."gl_trans AS g ON (g.type_no=a.trans_no` |
| `reporting/rep101.php` | 37 | `$sql = "SELECT SUM(IF(t.type = ".ST_SALESINVOICE." OR (t.type = ".ST_JOURNAL." AND t.ov_amount>0),` |
| `reporting/rep101.php` | 45 | `FROM ".TB_PREF."debtor_trans t` |
| `reporting/rep101.php` | 63 | `FROM ".TB_PREF."cust_allocations alloc` |
| `reporting/rep101.php` | 69 | `FROM ".TB_PREF."cust_allocations alloc` |
| `reporting/rep101.php` | 74 | `$sql = "SELECT trans.*,` |
| `reporting/rep101.php` | 78 | `FROM ".TB_PREF."debtor_trans trans` |
| `reporting/rep101.php` | 79 | `LEFT JOIN ".TB_PREF."voided voided ON trans.type=voided.type AND trans.trans_no=voided.id` |
| `reporting/rep101.php` | 154 | `$sql = "SELECT debtor_no, name, curr_code FROM ".TB_PREF."debtors_master ";` |
| `reporting/rep102.php` | 44 | `$sql = "SELECT type, reference, tran_date,` |
| `reporting/rep102.php` | 50 | `FROM ".TB_PREF."debtor_trans trans` |
| `reporting/rep102.php` | 146 | `$sql = "SELECT debtor_no, name, curr_code FROM ".TB_PREF."debtors_master";` |
| `reporting/rep103.php` | 32 | `$sql = "SELECT debtor.debtor_no,` |
| `reporting/rep103.php` | 48 | `FROM ".TB_PREF."debtors_master debtor` |
| `reporting/rep103.php` | 49 | `INNER JOIN ".TB_PREF."cust_branch branch ON debtor.debtor_no=branch.debtor_no` |
| `reporting/rep103.php` | 50 | `INNER JOIN ".TB_PREF."sales_types pricelist	ON debtor.sales_type=pricelist.id` |
| `reporting/rep103.php` | 51 | `INNER JOIN ".TB_PREF."areas area ON branch.area = area.area_code` |
| `reporting/rep103.php` | 52 | `INNER JOIN ".TB_PREF."salesman salesman	ON branch.salesman=salesman.salesman_code` |
| `reporting/rep103.php` | 74 | `$sql = "SELECT p.*, r.action, r.type, CONCAT(r.type,'.',r.action) as ext_type` |
| `reporting/rep103.php` | 75 | `FROM ".TB_PREF."crm_persons p,"` |
| `reporting/rep103.php` | 90 | `$sql = "SELECT SUM((ov_amount+ov_freight+ov_discount)*rate) AS Turnover` |
| `reporting/rep103.php` | 91 | `FROM ".TB_PREF."debtor_trans` |
| `reporting/rep104.php` | 35 | `$sql = "SELECT item.stock_id, item.description AS name,` |
| `reporting/rep104.php` | 39 | `FROM ".TB_PREF."stock_master item,` |
| `reporting/rep104.php` | 52 | `$sql = "SELECT i.item_code AS kit_code, i.description AS kit_name, c.category_id AS cat_id, c.description AS cat_name, count(*)>1 AS kit` |
| `reporting/rep104.php` | 55 | `LEFT JOIN ".TB_PREF."stock_category c ON i.category_id=c.category_id` |
| `reporting/rep105.php` | 38 | `$sql= "SELECT sorder.order_no,` |
| `reporting/rep105.php` | 50 | `FROM ".TB_PREF."sales_orders sorder` |
| `reporting/rep105.php` | 51 | `INNER JOIN ".TB_PREF."sales_order_details line` |
| `reporting/rep105.php` | 55 | `INNER JOIN ".TB_PREF."stock_master item` |
| `reporting/rep106.php` | 38 | `$sql = "SELECT DISTINCT trans.*,` |
| `reporting/rep106.php` | 45 | `FROM ".TB_PREF."debtor_trans trans,` |
| `reporting/rep107.php` | 34 | `$sql = "SELECT trans.trans_no, trans.reference` |
| `reporting/rep107.php` | 35 | `FROM ".TB_PREF."debtor_trans trans` |
| `reporting/rep107.php` | 36 | `LEFT JOIN ".TB_PREF."voided voided ON trans.type=voided.type AND trans.trans_no=voided.id` |
| `reporting/rep108.php` | 35 | `$sql = "SELECT *,` |
| `reporting/rep108.php` | 38 | `FROM ".TB_PREF."debtor_trans` |
| `reporting/rep108.php` | 85 | `$sql = "SELECT debtor_no, name AS DebtorName, address, tax_id, curr_code, curdate() AS tran_date FROM ".TB_PREF."debtors_master";` |
| `reporting/rep112.php` | 34 | `$sql = "SELECT trans.*,` |
| `reporting/rep112.php` | 43 | `FROM ".TB_PREF."debtor_trans trans,"` |
| `reporting/rep114.php` | 36 | `$sql = "SELECT d.debtor_no, d.name AS cust_name, d.tax_id, dt.type, dt.trans_no,` |
| `reporting/rep114.php` | 39 | `FROM ".TB_PREF."debtor_trans dt` |
| `reporting/rep114.php` | 40 | `LEFT JOIN ".TB_PREF."debtors_master d ON d.debtor_no=dt.debtor_no` |
| `reporting/rep114.php` | 51 | `$sql = "SELECT included_in_price, SUM(CASE WHEN trans_type=".ST_CUSTCREDIT." THEN -amount ELSE amount END * ex_rate) AS tax` |
| `reporting/rep114.php` | 52 | `FROM ".TB_PREF."trans_tax_details WHERE trans_type=$type AND trans_no=$trans_no GROUP BY included_in_price";` |
| `reporting/rep201.php` | 34 | `$sql = "SELECT` |
| `reporting/rep201.php` | 40 | `FROM ".TB_PREF."supp_trans` |
| `reporting/rep201.php` | 53 | `$sql = "SELECT *,` |
| `reporting/rep201.php` | 57 | `FROM ".TB_PREF."supp_trans` |
| `reporting/rep201.php` | 131 | `$sql = "SELECT supplier_id, supp_name AS name, curr_code FROM ".TB_PREF."suppliers";` |
| `reporting/rep202.php` | 46 | `$sql = "SELECT trans.type,` |
| `reporting/rep202.php` | 54 | `FROM ".TB_PREF."suppliers supplier,` |
| `reporting/rep202.php` | 160 | `$sql = "SELECT supplier_id, supp_name AS name, curr_code FROM ".TB_PREF."suppliers";` |
| `reporting/rep203.php` | 35 | `$sql = "SELECT  supp_reference, tran_date, due_date, trans_no, type, rate,` |
| `reporting/rep203.php` | 38 | `FROM ".TB_PREF."supp_trans` |
| `reporting/rep203.php` | 110 | `$sql = "SELECT supplier_id, supp_name AS name, curr_code, ".TB_PREF."payment_terms.terms FROM ".TB_PREF."suppliers, ".TB_PREF."payment_terms` |
| `reporting/rep204.php` | 32 | `$sql = "SELECT grn.id,` |
| `reporting/rep204.php` | 43 | `FROM ".TB_PREF."grn_items item,` |
| `reporting/rep205.php` | 33 | `$sql = "SELECT supplier_id,	supp_name, address, supp_address, supp_ref,` |
| `reporting/rep205.php` | 35 | `FROM ".TB_PREF."suppliers` |
| `reporting/rep205.php` | 47 | `$sql = "SELECT SUM((ov_amount+ov_discount)*rate) AS Turnover` |
| `reporting/rep205.php` | 48 | `FROM ".TB_PREF."supp_trans` |
| `reporting/rep209.php` | 36 | `$sql = "SELECT po.*, supplier.supp_name, supplier.supp_account_no,supplier.tax_included,` |
| `reporting/rep209.php` | 40 | `FROM ".TB_PREF."purch_orders po,"` |
| `reporting/rep209.php` | 52 | `$sql = "SELECT poline.*, units` |
| `reporting/rep209.php` | 53 | `FROM ".TB_PREF."purch_order_details poline` |
| `reporting/rep209.php` | 54 | `LEFT JOIN ".TB_PREF."stock_master item ON poline.item_code=item.stock_id` |
| `reporting/rep210.php` | 35 | `$sql = "SELECT trans.*,` |
| `reporting/rep301.php` | 57 | `$sql = "SELECT move.*, IF(ISNULL(supplier.supplier_id), debtor.debtor_no, supplier.supplier_id) person_id` |
| `reporting/rep301.php` | 58 | `FROM ".TB_PREF."stock_moves move` |
| `reporting/rep301.php` | 59 | `LEFT JOIN ".TB_PREF."supp_trans credit ON credit.trans_no=move.trans_no AND credit.type=move.type` |
| `reporting/rep301.php` | 60 | `LEFT JOIN ".TB_PREF."grn_batch grn ON grn.id=move.trans_no AND 25=move.type` |
| `reporting/rep301.php` | 61 | `LEFT JOIN ".TB_PREF."suppliers supplier ON IFNULL(grn.supplier_id, credit.supplier_id)=supplier.supplier_id` |
| `reporting/rep301.php` | 62 | `LEFT JOIN ".TB_PREF."debtor_trans cust_trans ON cust_trans.trans_no=move.trans_no AND cust_trans.type=move.type` |
| `reporting/rep301.php` | 63 | `LEFT JOIN ".TB_PREF."debtors_master debtor ON cust_trans.debtor_no=debtor.debtor_no` |
| `reporting/rep301.php` | 93 | `$sql = "SELECT item.category_id,` |
| `reporting/rep302.php` | 34 | `$sql = "SELECT item.category_id,` |
| `reporting/rep302.php` | 40 | `FROM (".TB_PREF."stock_master item,"` |
| `reporting/rep302.php` | 42 | `LEFT JOIN ".TB_PREF."stock_moves move ON item.stock_id=move.stock_id` |
| `reporting/rep302.php` | 69 | `$sql = "SELECT SUM(CASE WHEN tran_date >= '$date0' AND tran_date < '$date1' THEN -qty ELSE 0 END) AS prd0,` |
| `reporting/rep302.php` | 74 | `FROM ".TB_PREF."stock_moves` |
| `reporting/rep303.php` | 34 | `$sql = "SELECT item.category_id,` |
| `reporting/rep303.php` | 43 | `LEFT JOIN ".TB_PREF."stock_moves move ON item.stock_id=move.stock_id` |
| `reporting/rep304.php` | 37 | `$sql = "SELECT item.category_id,` |
| `reporting/rep304.php` | 49 | `FROM ".TB_PREF."stock_master item,` |
| `reporting/rep305.php` | 37 | `$sql = "SELECT grn.id batch_no,` |
| `reporting/rep305.php` | 65 | `$sql = "SELECT` |
| `reporting/rep306.php` | 36 | `$sql = "SELECT item.category_id,` |
| `reporting/rep306.php` | 46 | `FROM ".TB_PREF."stock_moves move` |
| `reporting/rep306.php` | 47 | `LEFT JOIN ".TB_PREF."supp_trans credit ON credit.trans_no=move.trans_no AND credit.type=move.type` |
| `reporting/rep306.php` | 48 | `LEFT JOIN ".TB_PREF."grn_batch grn ON grn.id=move.trans_no AND 25=move.type` |
| `reporting/rep306.php` | 49 | `LEFT JOIN ".TB_PREF."suppliers supplier ON IFNULL(grn.supplier_id, credit.supplier_id)=supplier.supplier_id,` |
| `reporting/rep306.php` | 74 | `$sql = "SELECT trans.supp_reference` |
| `reporting/rep306.php` | 75 | `FROM ".TB_PREF."supp_trans trans,` |
| `reporting/rep307.php` | 35 | `$sql = "SELECT stock_id, stock.description AS name,` |
| `reporting/rep307.php` | 39 | `FROM ".TB_PREF."stock_master stock LEFT JOIN ".TB_PREF."stock_category cat ON stock.category_id=cat.category_id` |
| `reporting/rep307.php` | 60 | `$sql = "SELECT ".($inward ? '' : '-')."SUM(qty) FROM ".TB_PREF."stock_moves` |
| `reporting/rep308.php` | 54 | `$sql = "SELECT stock_id, stock.description AS name,` |
| `reporting/rep308.php` | 57 | `FROM ".TB_PREF."stock_master stock LEFT JOIN ".TB_PREF."stock_category cat ON stock.category_id=cat.category_id` |
| `reporting/rep308.php` | 78 | `$sql = "SELECT ".($inward ? '' : '-')."SUM(qty) FROM ".TB_PREF."stock_moves` |
| `reporting/rep308.php` | 106 | `$sql = "SELECT move.*, IF(ISNULL(supplier.supplier_id), debtor.debtor_no, supplier.supplier_id) person_id` |
| `reporting/rep308.php` | 107 | `FROM ".TB_PREF."stock_moves move` |
| `reporting/rep308.php` | 108 | `LEFT JOIN ".TB_PREF."supp_trans credit ON credit.trans_no=move.trans_no AND credit.type=move.type` |
| `reporting/rep308.php` | 109 | `LEFT JOIN ".TB_PREF."grn_batch grn ON grn.id=move.trans_no AND 25=move.type` |
| `reporting/rep308.php` | 110 | `LEFT JOIN ".TB_PREF."suppliers supplier ON IFNULL(grn.supplier_id, credit.supplier_id)=supplier.supplier_id` |
| `reporting/rep308.php` | 111 | `LEFT JOIN ".TB_PREF."debtor_trans cust_trans ON cust_trans.trans_no=move.trans_no AND cust_trans.type=move.type` |
| `reporting/rep308.php` | 112 | `LEFT JOIN ".TB_PREF."debtors_master debtor ON cust_trans.debtor_no=debtor.debtor_no` |
| `reporting/rep308.php` | 153 | `$sql = "SELECT move.*, IF(ISNULL(supplier.supplier_id), debtor.debtor_no, supplier.supplier_id) person_id` |
| `reporting/rep308.php` | 154 | `FROM ".TB_PREF."stock_moves move` |
| `reporting/rep308.php` | 155 | `LEFT JOIN ".TB_PREF."supp_trans credit ON credit.trans_no=move.trans_no AND credit.type=move.type` |
| `reporting/rep308.php` | 156 | `LEFT JOIN ".TB_PREF."grn_batch grn ON grn.id=move.trans_no AND 25=move.type` |
| `reporting/rep308.php` | 157 | `LEFT JOIN ".TB_PREF."suppliers supplier ON IFNULL(grn.supplier_id, credit.supplier_id)=supplier.supplier_id` |
| `reporting/rep308.php` | 158 | `LEFT JOIN ".TB_PREF."debtor_trans cust_trans ON cust_trans.trans_no=move.trans_no AND cust_trans.type=move.type` |
| `reporting/rep308.php` | 159 | `LEFT JOIN ".TB_PREF."debtors_master debtor ON cust_trans.debtor_no=debtor.debtor_no` |
| `reporting/rep309.php` | 36 | `$sql = "SELECT item.category_id,` |
| `reporting/rep309.php` | 42 | `FROM ".TB_PREF."stock_master item,` |
| `reporting/rep401.php` | 33 | `$sql = "SELECT bom.parent,` |
| `reporting/rep402.php` | 34 | `$sql = "SELECT` |
| `reporting/rep402.php` | 46 | `FROM ".TB_PREF."workorders as workorder,"` |
| `reporting/rep451.php` | 32 | `$sql = "SELECT loc_code FROM ".TB_PREF."stock_moves WHERE stock_id = ".db_escape($stock_id)." AND` |
| `reporting/rep501.php` | 32 | `$sql = "SELECT *` |
| `reporting/rep501.php` | 49 | `$sql = "SELECT SUM(amount) AS Balance` |
| `reporting/rep601.php` | 35 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."bank_trans WHERE bank_act='$account'` |
| `reporting/rep601.php` | 46 | `$sql = "SELECT * FROM ".TB_PREF."bank_trans` |
| `reporting/rep602.php` | 36 | `$sql = "SELECT SUM(amount) FROM ".TB_PREF."bank_trans WHERE bank_act='$account'` |
| `reporting/rep602.php` | 47 | `$sql = "SELECT trans.*, com.memo_` |
| `reporting/rep602.php` | 50 | `LEFT JOIN ".TB_PREF."comments com ON trans.type = com.type AND trans.trans_no = com.id` |
| `reporting/rep602.php` | 177 | `$sql = "SELECT SUM(IF(reconciled<='$date' AND reconciled !='0000-00-00', amount, 0)) as reconciled,` |
| `reporting/rep602.php` | 179 | `FROM ".TB_PREF."bank_trans trans` |
| `reporting/rep705.php` | 49 | `$sql = "SELECT SUM(CASE WHEN tran_date >= '$date01' AND tran_date < '$date02' THEN amount / 1000 ELSE 0 END) AS per01,` |
| `reporting/rep705.php` | 61 | `FROM ".TB_PREF."gl_trans` |
| `reporting/rep705.php` | 210 | `$sql = "SELECT begin, end, YEAR(end) AS yr, MONTH(end) AS mo FROM ".TB_PREF."fiscal_year WHERE id=".db_escape($year);` |
| `reporting/rep709.php` | 36 | `$sql = "SELECT tt.name as taxname, taxrec.*, taxrec.amount*ex_rate AS amount,` |
| `reporting/rep709.php` | 42 | `FROM ".TB_PREF."trans_tax_details taxrec` |
| `reporting/rep709.php` | 43 | `LEFT JOIN ".TB_PREF."tax_types tt` |
| `reporting/rep709.php` | 45 | `LEFT JOIN ".TB_PREF."gl_trans gl` |
| `reporting/rep709.php` | 48 | `LEFT JOIN ".TB_PREF."supp_trans strans` |
| `reporting/rep709.php` | 50 | `LEFT JOIN ".TB_PREF."suppliers as supp ON strans.supplier_id=supp.supplier_id` |
| `reporting/rep709.php` | 51 | `LEFT JOIN ".TB_PREF."debtor_trans dtrans` |
| `reporting/rep709.php` | 53 | `LEFT JOIN ".TB_PREF."debtors_master as debt ON dtrans.debtor_no=debt.debtor_no` |
| `reporting/rep709.php` | 54 | `LEFT JOIN ".TB_PREF."cust_branch as branch ON dtrans.branch_code=branch.branch_code` |
| `reporting/rep709.php` | 66 | `$sql = "SELECT * FROM ".TB_PREF."tax_types ORDER BY id";` |
| `reporting/rep709.php` | 72 | `$sql = "SELECT * FROM ".TB_PREF."tax_types WHERE id=$id";` |
| `sql/alter.sql` | 16 | `-- ALTER TABLE` |
| `sql/alter.sql` | 19 | `DROP TABLE IF EXISTS `0_item_units`;` |
| `sql/alter.sql` | 20 | `CREATE TABLE IF NOT EXISTS `0_item_units` (` |
| `sql/alter.sql` | 28 | `INSERT INTO `0_item_units` (`abbr`, `name`, `decimals`) SELECT DISTINCT `units`, CONCAT(UPPER(SUBSTRING(`units`, 1, 1)), LOWER(SUBSTRING(`units`, 2))), 0 FROM `0_stock_master` ;` |
| `sql/alter.sql` | 29 | `UPDATE `0_debtor_trans` SET `ov_amount`=-`ov_amount`, `ov_gst`=-`ov_gst`, `ov_freight`=-`ov_freight`, `ov_discount`=-`ov_discount` WHERE `ov_amount` < 0 AND `type` <> 10 AND `type` <> 13 ;` |
| `sql/alter.sql` | 31 | `DROP TABLE IF EXISTS `0_form_items`;` |
| `sql/alter.sql` | 33 | `ALTER TABLE `0_tax_types` DROP INDEX `name`, ADD UNIQUE `name` ( `name` , `rate` );` |
| `sql/alter.sql` | 35 | `ALTER TABLE `0_tax_group_items` DROP `included_in_price`;` |
| `sql/alter.sql` | 36 | `ALTER TABLE `0_debtor_trans` ADD `ov_freight_tax` DOUBLE DEFAULT '0' NOT NULL AFTER `ov_freight` ;` |
| `sql/alter.sql` | 37 | `ALTER TABLE `0_sales_types` ADD `tax_included` INT( 1 ) DEFAULT '0' NOT NULL AFTER `sales_type` ;` |
| `sql/alter.sql` | 38 | `ALTER TABLE `0_sales_types` ADD `factor` DOUBLE DEFAULT '1' NOT NULL AFTER `tax_included` ;` |
| `sql/alter.sql` | 40 | `ALTER TABLE `0_bom` CHANGE `workcentre_added` `workcentre_added` INT( 11 ) NOT NULL DEFAULT '0';` |
| `sql/alter.sql` | 41 | `ALTER TABLE `0_wo_requirements` CHANGE `workcentre` `workcentre` INT( 11 ) NOT NULL DEFAULT '0';` |
| `sql/alter.sql` | 43 | `ALTER TABLE `0_debtor_trans` ADD `version` TINYINT(1) UNSIGNED DEFAULT '0' NOT NULL AFTER `type`;` |
| `sql/alter.sql` | 44 | `ALTER TABLE `0_sales_orders` ADD `version` TINYINT(1) UNSIGNED DEFAULT '0' NOT NULL AFTER `order_no`;` |
| `sql/alter.sql` | 45 | `ALTER TABLE `0_sales_orders` ADD `type` TINYINT(1) NOT NULL DEFAULT '0' AFTER `version`;` |
| `sql/alter.sql` | 47 | `ALTER TABLE `0_tax_types` DROP `out`;` |
| `sql/alter.sql` | 48 | `ALTER TABLE `0_debtor_trans_details` ADD COLUMN `qty_done` double NOT NULL default '0';` |
| `sql/alter.sql` | 50 | `ALTER TABLE `0_debtor_trans` ADD COLUMN `trans_link` int(11) NOT NULL default '0';` |
| `sql/alter.sql` | 51 | `INSERT INTO `0_sys_types` VALUES ('13', 'Delivery', '1', '1');` |
| `sql/alter.sql` | 52 | `ALTER TABLE `0_sales_order_details` CHANGE `qty_invoiced` `qty_sent` DOUBLE NOT NULL default '0';` |
| `sql/alter.sql` | 54 | `ALTER TABLE `0_supp_invoice_items` CHANGE `gl_code` `gl_code` VARCHAR(11) NOT NULL DEFAULT '0';` |
| `sql/alter.sql` | 55 | `ALTER TABLE `0_sales_order_details` DROP PRIMARY KEY;` |
| `sql/alter.sql` | 56 | `ALTER TABLE `0_sales_order_details` ADD `id` INTEGER(11) NOT NULL AUTO_INCREMENT FIRST, ADD PRIMARY KEY (`id`);` |
| `sql/alter.sql` | 58 | `ALTER TABLE `0_company` ADD `no_item_list` TINYINT(1) NOT NULL DEFAULT '0' AFTER `f_year`;` |
| `sql/alter.sql` | 59 | `ALTER TABLE `0_company` ADD `no_customer_list` TINYINT(1) NOT NULL DEFAULT '0' AFTER `no_item_list`;` |
| `sql/alter.sql` | 60 | `ALTER TABLE `0_company` ADD `no_supplier_list` TINYINT(1) NOT NULL DEFAULT '0' AFTER `no_customer_list`;` |
| `sql/alter.sql` | 61 | `ALTER TABLE `0_company` ADD `base_sales` INT( 11 ) DEFAULT '-1' NOT NULL AFTER `no_supplier_list` ;` |
| `sql/alter.sql` | 63 | `ALTER TABLE `0_salesman` ADD `provision` DOUBLE NOT NULL DEFAULT '0' AFTER `salesman_email`;` |
| `sql/alter.sql` | 64 | `ALTER TABLE `0_salesman` ADD `break_pt` DOUBLE NOT NULL DEFAULT '0' AFTER `provision`;` |
| `sql/alter.sql` | 65 | `ALTER TABLE `0_salesman` ADD `provision2` DOUBLE NOT NULL DEFAULT '0' AFTER `break_pt`;` |
| `sql/alter2.1.php` | 35 | `$sql = "SELECT id, account_code FROM ".TB_PREF."bank_accounts";` |
| `sql/alter2.1.php` | 42 | `$sql = "UPDATE ".TB_PREF."bank_trans SET bank_act='"` |
| `sql/alter2.1.php` | 51 | `$sql = "SELECT `stock_id`,`description`,`category_id` FROM ".TB_PREF."stock_master";` |
| `sql/alter2.1.php` | 59 | `$sql = "INSERT IGNORE "` |
| `sql/alter2.1.php` | 73 | `$sql = "DROP TABLE IF EXISTS `".TB_PREF."bank_trans_types`";` |
| `sql/alter2.1.php` | 86 | `FROM ".TB_PREF."debtor_trans_tax_details dt` |
| `sql/alter2.1.php` | 87 | `LEFT JOIN ".TB_PREF."trans_tax_details tt` |
| `sql/alter2.1.php` | 99 | `FROM ".TB_PREF."supp_invoice_tax_items st` |
| `sql/alter2.1.php` | 100 | `LEFT JOIN ".TB_PREF."trans_tax_details tt` |
| `sql/alter2.1.php` | 110 | `$res = db_query($sql, "Cannot retrieve trans tax details from $tbl");` |
| `sql/alter2.1.php` | 116 | `$sql2 = "INSERT INTO ".TB_PREF."trans_tax_details` |
| `sql/alter2.1.php` | 124 | `db_query($sql2, "Cannot move trans tax details from $tbl");` |
| `sql/alter2.1.php` | 126 | `db_query("DROP TABLE ".TB_PREF.$tbl, "cannot remove $tbl");` |
| `sql/alter2.1.sql` | 7 | `#	* Precede all CREATE TABLE statment with DROP TABLE IF EXISTS` |
| `sql/alter2.1.sql` | 8 | `#	* Precede all ALTER TABLE statements using ADD column with respective` |
| `sql/alter2.1.sql` | 9 | `#		ALTER TABLE with DROP column` |
| `sql/alter2.1.sql` | 10 | `#	* Move all other DROP queries (e.g. removing obsolete tables) to installer` |
| `sql/alter2.1.sql` | 14 | `DROP TABLE IF EXISTS `0_attachments`;` |
| `sql/alter2.1.sql` | 16 | `CREATE TABLE `0_attachments` (` |
| `sql/alter2.1.sql` | 30 | `DROP TABLE IF EXISTS `0_groups`;` |
| `sql/alter2.1.sql` | 32 | `CREATE TABLE `0_groups` (` |
| `sql/alter2.1.sql` | 40 | `INSERT INTO `0_groups` VALUES ('1', 'Small', '0');` |
| `sql/alter2.1.sql` | 41 | `INSERT INTO `0_groups` VALUES ('2', 'Medium', '0');` |
| `sql/alter2.1.sql` | 42 | `INSERT INTO `0_groups` VALUES ('3', 'Large', '0');` |
| `sql/alter2.1.sql` | 44 | `DROP TABLE IF EXISTS `0_recurrent_invoices`;` |
| `sql/alter2.1.sql` | 46 | `CREATE TABLE `0_recurrent_invoices` (` |
| `sql/alter2.1.sql` | 61 | `ALTER TABLE `0_cust_branch` ADD `group_no` int(11) NOT NULL default '0';` |
| `sql/alter2.1.sql` | 63 | `ALTER TABLE `0_debtor_trans` ADD `dimension_id` int(11) NOT NULL default '0';` |
| `sql/alter2.1.sql` | 64 | `ALTER TABLE `0_debtor_trans` ADD `dimension2_id` int(11) NOT NULL default '0';` |
| `sql/alter2.1.sql` | 66 | `ALTER TABLE `0_bank_accounts` DROP PRIMARY KEY;` |
| `sql/alter2.1.sql` | 67 | `ALTER TABLE `0_bank_accounts` ADD `id` SMALLINT(6) AUTO_INCREMENT PRIMARY KEY;` |
| `sql/alter2.1.sql` | 68 | `ALTER TABLE `0_bank_accounts` ADD `last_reconciled_date` timestamp NOT NULL default '0000-00-00';` |
| `sql/alter2.1.sql` | 69 | `ALTER TABLE `0_bank_accounts` ADD `ending_reconcile_balance` double NOT NULL default '0';` |
| `sql/alter2.1.sql` | 71 | `ALTER TABLE `0_bank_trans` DROP COLUMN `bank_trans_type_id`;` |
| `sql/alter2.1.sql` | 72 | `ALTER TABLE `0_bank_trans` ADD `reconciled` date default NULL;` |
| `sql/alter2.1.sql` | 74 | `ALTER TABLE `0_users` ADD `query_size` TINYINT(1) DEFAULT '10';` |
| `sql/alter2.1.sql` | 76 | `ALTER TABLE `0_users` ADD `graphic_links` TINYINT(1) DEFAULT '1';` |
| `sql/alter2.1.sql` | 78 | `DROP TABLE IF EXISTS `0_sales_pos`;` |
| `sql/alter2.1.sql` | 80 | `CREATE TABLE `0_sales_pos` (` |
| `sql/alter2.1.sql` | 93 | `INSERT INTO `0_sales_pos` VALUES ('1', 'Default', '0', '1', 'DEF', '1', '0');` |
| `sql/alter2.1.sql` | 95 | `ALTER TABLE `0_users` ADD `pos` SMALLINT(6) DEFAULT '1';` |
| `sql/alter2.1.sql` | 97 | `DROP TABLE IF EXISTS `0_quick_entries`;` |
| `sql/alter2.1.sql` | 99 | `CREATE TABLE `0_quick_entries` (` |
| `sql/alter2.1.sql` | 109 | `INSERT INTO `0_quick_entries` VALUES ('1', '1', 'Maintenance', '0', 'Amount');` |
| `sql/alter2.1.sql` | 110 | `INSERT INTO `0_quick_entries` VALUES ('2', '1', 'Phone', '0', 'Amount');` |
| `sql/alter2.1.sql` | 111 | `INSERT INTO `0_quick_entries` VALUES ('3', '2', 'Cash Sales', '0', 'Amount');` |
| `sql/alter2.1.sql` | 113 | `DROP TABLE IF EXISTS `0_quick_entry_lines`;` |
| `sql/alter2.1.sql` | 115 | `CREATE TABLE `0_quick_entry_lines` (` |
| `sql/alter2.1.sql` | 127 | `INSERT INTO `0_quick_entry_lines` VALUES ('1', '1','0','=', '6600', '0', '0');` |
| `sql/alter2.1.sql` | 128 | `INSERT INTO `0_quick_entry_lines` VALUES ('2', '2','0','=', '6730', '0', '0');` |
| `sql/alter2.1.sql` | 129 | `INSERT INTO `0_quick_entry_lines` VALUES ('3', '3','0','=', '3000', '0', '0');` |
| `sql/alter2.1.sql` | 131 | `ALTER TABLE `0_users` ADD `print_profile` VARCHAR(30) NOT NULL DEFAULT '1';` |
| `sql/alter2.1.sql` | 132 | `ALTER TABLE `0_users` ADD `rep_popup` TINYINT(1) DEFAULT '1';` |
| `sql/alter2.1.sql` | 134 | `DROP TABLE IF EXISTS `0_print_profiles`;` |
| `sql/alter2.1.sql` | 135 | `CREATE TABLE `0_print_profiles` (` |
| `sql/alter2.1.sql` | 144 | `INSERT INTO `0_print_profiles` VALUES ('1', 'Out of office', '', '0');` |
| `sql/alter2.1.sql` | 145 | `INSERT INTO `0_print_profiles` VALUES ('2', 'Sales Department', '', '0');` |
| `sql/alter2.1.sql` | 146 | `INSERT INTO `0_print_profiles` VALUES ('3', 'Central', '', '2');` |
| `sql/alter2.1.sql` | 147 | `INSERT INTO `0_print_profiles` VALUES ('4', 'Sales Department', '104', '2');` |
| `sql/alter2.1.sql` | 148 | `INSERT INTO `0_print_profiles` VALUES ('5', 'Sales Department', '105', '2');` |
| `sql/alter2.1.sql` | 149 | `INSERT INTO `0_print_profiles` VALUES ('6', 'Sales Department', '107', '2');` |
| `sql/alter2.1.sql` | 150 | `INSERT INTO `0_print_profiles` VALUES ('7', 'Sales Department', '109', '2');` |
| `sql/alter2.1.sql` | 151 | `INSERT INTO `0_print_profiles` VALUES ('8', 'Sales Department', '110', '2');` |
| `sql/alter2.1.sql` | 152 | `INSERT INTO `0_print_profiles` VALUES ('9', 'Sales Department', '201', '2');` |
| `sql/alter2.1.sql` | 154 | `DROP TABLE IF EXISTS `0_printers`;` |
| `sql/alter2.1.sql` | 156 | `CREATE TABLE `0_printers` (` |
| `sql/alter2.1.sql` | 168 | `INSERT INTO `0_printers` VALUES ('1', 'QL500', 'Label printer', 'QL500', 'server', '127', '20');` |
| `sql/alter2.1.sql` | 169 | `INSERT INTO `0_printers` VALUES ('2', 'Samsung', 'Main network printer', 'scx4521F', 'server', '515', '5');` |
| `sql/alter2.1.sql` | 170 | `INSERT INTO `0_printers` VALUES ('3', 'Local', 'Local print server at user IP', 'lp', '', '515', '10');` |
| `sql/alter2.1.sql` | 172 | `DROP TABLE IF EXISTS `0_item_codes`;` |
| `sql/alter2.1.sql` | 174 | `CREATE TABLE `0_item_codes` (` |
| `sql/alter2.1.sql` | 187 | `ALTER TABLE `0_company` ADD `foreign_codes` TINYINT(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 189 | `ALTER TABLE `0_company` ADD `accumulate_shipping` TINYINT(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 191 | `ALTER TABLE `0_company` ADD `legal_text` tinytext NOT NULL DEFAULT '';` |
| `sql/alter2.1.sql` | 193 | `ALTER TABLE `0_suppliers` ADD `supp_address` tinytext NOT NULL DEFAULT '' AFTER `address`;` |
| `sql/alter2.1.sql` | 195 | `ALTER TABLE `0_suppliers` ADD `phone` varchar(30) NOT NULL DEFAULT '' AFTER `supp_address`;` |
| `sql/alter2.1.sql` | 197 | `ALTER TABLE `0_suppliers` ADD `fax` varchar(30) NOT NULL DEFAULT '' AFTER `phone`;` |
| `sql/alter2.1.sql` | 199 | `ALTER TABLE `0_suppliers` ADD `gst_no` varchar(25) NOT NULL DEFAULT '' AFTER `fax`;` |
| `sql/alter2.1.sql` | 201 | `ALTER TABLE `0_suppliers` ADD `contact` varchar(60) NOT NULL DEFAULT '' AFTER `gst_no`;` |
| `sql/alter2.1.sql` | 203 | `ALTER TABLE `0_suppliers` ADD `credit_limit` double NOT NULL DEFAULT '0' AFTER `tax_group_id`;` |
| `sql/alter2.1.sql` | 205 | `ALTER TABLE `0_suppliers` ADD `supp_account_no` varchar(40) NOT NULL DEFAULT '' AFTER `contact`;` |
| `sql/alter2.1.sql` | 207 | `ALTER TABLE `0_suppliers` ADD `website` varchar(100) NOT NULL DEFAULT '' AFTER `email`;` |
| `sql/alter2.1.sql` | 209 | `ALTER TABLE `0_suppliers` ADD `notes` tinytext NOT NULL DEFAULT '';` |
| `sql/alter2.1.sql` | 211 | `ALTER TABLE `0_chart_types` DROP INDEX `name`, ADD INDEX `name` ( `name` );` |
| `sql/alter2.1.sql` | 213 | `DROP TABLE IF EXISTS `0_sql_trail`;` |
| `sql/alter2.1.sql` | 215 | `CREATE TABLE IF NOT EXISTS `0_sql_trail` (` |
| `sql/alter2.1.sql` | 223 | `ALTER TABLE `0_tax_types` DROP COLUMN `out`;` |
| `sql/alter2.1.sql` | 225 | `ALTER TABLE `0_chart_master` DROP COLUMN `tax_code`;` |
| `sql/alter2.1.sql` | 227 | `ALTER TABLE `0_chart_master` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 229 | `ALTER TABLE `0_currencies` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 231 | `ALTER TABLE `0_bank_accounts` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 233 | `ALTER TABLE `0_debtors_master` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 235 | `ALTER TABLE `0_stock_master` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 237 | `ALTER TABLE `0_workcentres` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 239 | `ALTER TABLE `0_locations` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 241 | `ALTER TABLE `0_sales_types` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 243 | `ALTER TABLE `0_areas` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 245 | `ALTER TABLE `0_salesman` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 247 | `ALTER TABLE `0_shippers` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 249 | `ALTER TABLE `0_credit_status` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 251 | `ALTER TABLE `0_payment_terms` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 253 | `ALTER TABLE `0_suppliers` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 255 | `ALTER TABLE `0_stock_category` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 257 | `ALTER TABLE `0_item_units` ADD `inactive` tinyint(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.1.sql` | 259 | `DROP TABLE IF EXISTS `0_trans_tax_details`;` |
| `sql/alter2.1.sql` | 261 | `CREATE TABLE `0_trans_tax_details` (` |
| `sql/alter2.2.php` | 50 | `$sql = "UPDATE ".TB_PREF."stock_category SET "` |
| `sql/alter2.2.php` | 66 | `$sql = "SELECT DISTINCT {$info[2]} as id,{$info[3]} as ref FROM $tbl";` |
| `sql/alter2.2.php` | 72 | `$res2 = db_query("INSERT INTO ".TB_PREF."refs VALUES("` |
| `sql/alter2.2.php` | 83 | `if (!($ret = db_query("SELECT MAX(`order_no`) FROM `".TB_PREF."sales_orders`")) \|\|` |
| `sql/alter2.2.php` | 92 | `$sql = "UPDATE `".TB_PREF."sys_types`` |
| `sql/alter2.2.php` | 193 | `$sql = "UPDATE ".TB_PREF."users set role_id=".$new_ids[$old_id].` |
| `sql/alter2.2.php` | 195 | `$ret = db_query($sql, 'cannot update users roles');` |
| `sql/alter2.2.php` | 203 | `$sql = "INSERT INTO ".TB_PREF."security_roles (role, description, sections, areas)` |
| `sql/alter2.2.php` | 258 | `$tresult = db_query($tsql, "Cannot select all tables with prefix '$pref'");` |
| `sql/alter2.2.php` | 262 | `$cresult = db_query($csql, "Cannot select column names for table '$table'");` |
| `sql/alter2.2.php` | 282 | `$sql = "SELECT ".implode(',', array_unique(array_merge($keys,$textcols)))` |
| `sql/alter2.2.php` | 285 | `$result = db_query($sql, "Cannot select all suspicious fields in $table");` |
| `sql/alter2.2.php` | 289 | `$sql = "UPDATE {$table} SET ";` |
| `sql/alter2.2.php` | 302 | `db_query($sql, 'cannot update record');` |
| `sql/alter2.2.sql` | 1 | `ALTER TABLE `0_company` DROP COLUMN `custom1_name`;` |
| `sql/alter2.2.sql` | 2 | `ALTER TABLE `0_company` DROP COLUMN `custom2_name`;` |
| `sql/alter2.2.sql` | 3 | `ALTER TABLE `0_company` DROP COLUMN `custom3_name`;` |
| `sql/alter2.2.sql` | 4 | `ALTER TABLE `0_company` DROP COLUMN `custom1_value`;` |
| `sql/alter2.2.sql` | 5 | `ALTER TABLE `0_company` DROP COLUMN `custom2_value`;` |
| `sql/alter2.2.sql` | 6 | `ALTER TABLE `0_company` DROP COLUMN `custom3_value`;` |
| `sql/alter2.2.sql` | 8 | `ALTER TABLE `0_company` ADD COLUMN `default_delivery_required` SMALLINT(6) NULL DEFAULT '1';` |
| `sql/alter2.2.sql` | 9 | `ALTER TABLE `0_company` ADD COLUMN `version_id` VARCHAR(11) NOT NULL DEFAULT '';` |
| `sql/alter2.2.sql` | 10 | `ALTER TABLE `0_company` DROP COLUMN `purch_exchange_diff_act`;` |
| `sql/alter2.2.sql` | 11 | `ALTER TABLE `0_company` ADD COLUMN`profit_loss_year_act` VARCHAR(11) NOT NULL DEFAULT '' AFTER `exchange_diff_act`;` |
| `sql/alter2.2.sql` | 12 | `ALTER TABLE `0_company` ADD COLUMN `time_zone` TINYINT(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.2.sql` | 13 | `ALTER TABLE `0_company` ADD COLUMN `add_pct` INT(5) NOT NULL DEFAULT '-1';` |
| `sql/alter2.2.sql` | 14 | `ALTER TABLE `0_company` ADD COLUMN `round_to` INT(5) NOT NULL DEFAULT '1';` |
| `sql/alter2.2.sql` | 15 | `ALTER TABLE `0_company` CHANGE `grn_act` `bank_charge_act` VARCHAR(11) NOT NULL DEFAULT '';` |
| `sql/alter2.2.sql` | 16 | `#INSERT INTO `0_chart_master` VALUES ('9990', '', 'Profit and Loss this year', '52', '0');` |
| `sql/alter2.2.sql` | 17 | `UPDATE `0_company` SET `profit_loss_year_act`='9990', `version_id`='2.2' WHERE `coy_code`=1;` |
| `sql/alter2.2.sql` | 19 | `ALTER TABLE `0_stock_category` DROP COLUMN `stock_act`;` |
| `sql/alter2.2.sql` | 20 | `ALTER TABLE `0_stock_category` DROP COLUMN `cogs_act`;` |
| `sql/alter2.2.sql` | 21 | `ALTER TABLE `0_stock_category` DROP COLUMN `adj_gl_act`;` |
| `sql/alter2.2.sql` | 22 | `ALTER TABLE `0_stock_category` DROP COLUMN `purch_price_var_act`;` |
| `sql/alter2.2.sql` | 24 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_tax_type` int(11) NOT NULL default '1';` |
| `sql/alter2.2.sql` | 25 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_units` varchar(20) NOT NULL default 'each';` |
| `sql/alter2.2.sql` | 26 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_mb_flag` char(1) NOT NULL default 'B';` |
| `sql/alter2.2.sql` | 27 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_sales_act` varchar(11) NOT NULL default '';` |
| `sql/alter2.2.sql` | 28 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_cogs_act` varchar(11) NOT NULL default '';` |
| `sql/alter2.2.sql` | 29 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_inventory_act` varchar(11) NOT NULL default '';` |
| `sql/alter2.2.sql` | 30 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_adjustment_act` varchar(11) NOT NULL default '';` |
| `sql/alter2.2.sql` | 31 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_assembly_act` varchar(11) NOT NULL default '';` |
| `sql/alter2.2.sql` | 32 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_dim1` int(11) default NULL;` |
| `sql/alter2.2.sql` | 33 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_dim2` int(11) default NULL;` |
| `sql/alter2.2.sql` | 34 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_no_sale` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 36 | `ALTER TABLE `0_users` ADD COLUMN `sticky_doc_date` TINYINT(1) DEFAULT '0';` |
| `sql/alter2.2.sql` | 37 | `ALTER TABLE `0_users` ADD COLUMN `startup_tab` VARCHAR(20) NOT NULL default 'orders' AFTER `sticky_doc_date`;` |
| `sql/alter2.2.sql` | 39 | `ALTER TABLE `0_debtors_master` MODIFY COLUMN `name` varchar(100) NOT NULL default '';` |
| `sql/alter2.2.sql` | 41 | `ALTER TABLE `0_cust_branch` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 43 | `ALTER TABLE `0_sys_types` DROP COLUMN `type_name`;` |
| `sql/alter2.2.sql` | 45 | `ALTER TABLE `0_chart_class` CHANGE `balance_sheet` `ctype` TINYINT(1) NOT NULL DEFAULT '0';` |
| `sql/alter2.2.sql` | 47 | `ALTER TABLE `0_chart_class` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 48 | `ALTER TABLE `0_chart_types` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 49 | `ALTER TABLE `0_movement_types` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 50 | `ALTER TABLE `0_item_tax_types` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 51 | `ALTER TABLE `0_tax_types` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 52 | `ALTER TABLE `0_tax_groups` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 54 | `ALTER TABLE `0_users` DROP PRIMARY KEY;` |
| `sql/alter2.2.sql` | 55 | `ALTER TABLE `0_users` ADD `id` SMALLINT(6) AUTO_INCREMENT PRIMARY KEY FIRST;` |
| `sql/alter2.2.sql` | 56 | `ALTER TABLE `0_users` ADD UNIQUE KEY (`user_id`);` |
| `sql/alter2.2.sql` | 57 | `ALTER TABLE `0_users` ADD COLUMN `inactive` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 59 | `DROP TABLE IF EXISTS `0_audit_trail`;` |
| `sql/alter2.2.sql` | 61 | `CREATE TABLE `0_audit_trail` (` |
| `sql/alter2.2.sql` | 75 | `ALTER TABLE `0_stock_master` ADD COLUMN `no_sale` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.2.sql` | 76 | `ALTER TABLE `0_currencies` ADD COLUMN `auto_update` tinyint(1) NOT NULL default '1';` |
| `sql/alter2.2.sql` | 78 | `ALTER TABLE `0_debtors_master` ADD COLUMN `debtor_ref` varchar(30) NOT NULL;` |
| `sql/alter2.2.sql` | 79 | `UPDATE `0_debtors_master` SET `debtor_ref`=`name` WHERE 1;` |
| `sql/alter2.2.sql` | 80 | `ALTER TABLE `0_suppliers` ADD COLUMN `supp_ref` varchar(30) NOT NULL;` |
| `sql/alter2.2.sql` | 81 | `UPDATE `0_suppliers` SET `supp_ref`=`supp_name` WHERE 1;` |
| `sql/alter2.2.sql` | 82 | `ALTER TABLE `0_cust_branch` ADD COLUMN `branch_ref`	varchar(30) NOT NULL;` |
| `sql/alter2.2.sql` | 83 | `UPDATE `0_cust_branch` SET `branch_ref`=`br_name` WHERE 1;` |
| `sql/alter2.2.sql` | 85 | `DROP TABLE IF EXISTS `0_security_roles`;` |
| `sql/alter2.2.sql` | 87 | `CREATE TABLE `0_security_roles` (` |
| `sql/alter2.2.sql` | 98 | `ALTER TABLE `0_company` ADD COLUMN `login_tout` SMALLINT(6) NOT NULL DEFAULT '600';` |
| `sql/alter2.2.sql` | 99 | `ALTER TABLE `0_users` CHANGE COLUMN `full_access` `role_id` int(11) NOT NULL default '1';` |
| `sql/alter2.2.sql` | 101 | `ALTER TABLE `0_sales_order_details` ADD COLUMN `trans_type` SMALLINT(6) NOT NULL DEFAULT '30' AFTER `order_no`;` |
| `sql/alter2.2.sql` | 102 | `ALTER TABLE `0_sales_orders` CHANGE COLUMN `order_no` `order_no` int(11) NOT NULL;` |
| `sql/alter2.2.sql` | 103 | `ALTER TABLE `0_sales_orders` ADD COLUMN `trans_type` SMALLINT(6) NOT NULL DEFAULT '30' AFTER `order_no`;` |
| `sql/alter2.2.sql` | 104 | `ALTER TABLE `0_sales_orders` ADD COLUMN `reference` varchar(100) NOT NULL DEFAULT '' AFTER `branch_code`;` |
| `sql/alter2.2.sql` | 105 | `ALTER TABLE `0_sales_orders` DROP PRIMARY KEY;` |
| `sql/alter2.2.sql` | 106 | `ALTER TABLE `0_sales_orders` ADD PRIMARY KEY ( `trans_type` , `order_no` );` |
| `sql/alter2.2.sql` | 107 | `UPDATE `0_sales_orders`	SET `reference`=`order_no` WHERE 1;` |
| `sql/alter2.2.sql` | 108 | `INSERT INTO `0_sys_types` (`type_id`, `type_no`, `next_reference`) VALUES (32, 0, '1');` |
| `sql/alter2.2.sql` | 110 | `ALTER TABLE `0_bank_accounts` ADD COLUMN `dflt_curr_act` TINYINT(1) NOT NULL default '0' AFTER `bank_curr_code`;` |
| `sql/alter2.2.sql` | 112 | `DROP TABLE IF EXISTS `0_tags`;` |
| `sql/alter2.2.sql` | 114 | `CREATE TABLE `0_tags` (` |
| `sql/alter2.2.sql` | 124 | `DROP TABLE IF EXISTS `0_tag_associations`;` |
| `sql/alter2.2.sql` | 126 | `CREATE TABLE `0_tag_associations` (` |
| `sql/alter2.2.sql` | 132 | `DROP TABLE IF EXISTS `0_useronline` ;` |
| `sql/alter2.2.sql` | 134 | `CREATE TABLE `0_useronline` (` |
| `sql/alter2.2.sql` | 143 | `ALTER TABLE `0_suppliers` ADD COLUMN `phone2` varchar(30) NOT NULL default '' AFTER `phone`;` |
| `sql/alter2.2.sql` | 144 | `ALTER TABLE `0_cust_branch` ADD COLUMN `phone2` varchar(30) NOT NULL default '' AFTER `phone`;` |
| `sql/alter2.2.sql` | 145 | `ALTER TABLE `0_shippers` ADD COLUMN `phone2` varchar(30) NOT NULL default '' AFTER `phone`;` |
| `sql/alter2.2.sql` | 146 | `ALTER TABLE `0_locations` ADD COLUMN `phone2` varchar(30) NOT NULL default '' AFTER `phone`;` |
| `sql/alter2.2.sql` | 147 | `ALTER TABLE `0_debtors_master` ADD COLUMN `notes` tinytext NULL default '' AFTER `credit_limit`;` |
| `sql/alter2.2.sql` | 148 | `ALTER TABLE `0_cust_branch` ADD COLUMN `notes` tinytext NULL default '' AFTER `group_no`;` |
| `sql/alter2.2rc.sql` | 1 | `# Patch for upgrade from 2.2beta to 2.2RC/final` |
| `sql/alter2.2rc.sql` | 3 | `ALTER TABLE `0_tag_associations` DROP COLUMN `id`;` |
| `sql/alter2.2rc.sql` | 4 | `ALTER TABLE `0_tag_associations` ADD  UNIQUE KEY(`record_id`,`tag_id`);` |
| `sql/alter2.2rc.sql` | 6 | `DROP TABLE IF EXISTS `0_useronline` ;` |
| `sql/alter2.2rc.sql` | 8 | `CREATE TABLE `0_useronline` (` |
| `sql/alter2.3.php` | 39 | `$sql = "SELECT debtor_no, payment_terms FROM ".TB_PREF."debtors_master";` |
| `sql/alter2.3.php` | 49 | `$sql = "UPDATE ".TB_PREF."debtor_trans SET "` |
| `sql/alter2.3.php` | 57 | `$sql = "UPDATE ".TB_PREF."sales_orders SET "` |
| `sql/alter2.3.php` | 86 | `if (db_query("ALTER TABLE `".TB_PREF."{$table}` DROP `$col`")==false) {` |
| `sql/alter2.3.php` | 92 | `$sql = "DROP TABLE IF EXISTS `".TB_PREF."company`";` |
| `sql/alter2.3.php` | 125 | `$sql = "SELECT order_no, trans_type FROM ".TB_PREF."sales_orders";` |
| `sql/alter2.3.php` | 131 | `$result = db_query("UPDATE ".TB_PREF."sales_orders` |
| `sql/alter2.3.php` | 138 | `$sql = "SELECT order_no FROM ".TB_PREF."purch_orders";` |
| `sql/alter2.3.php` | 144 | `$result = db_query("UPDATE ".TB_PREF."purch_orders SET total=".$cart->get_trans_total());` |
| `sql/alter2.3.php` | 155 | `$sql = 'SELECT trans_link FROM` |
| `sql/alter2.3.php` | 167 | `$sql = 'SELECT trans_no FROM` |
| `sql/alter2.3.php` | 193 | `$sql =	"SELECT d.type, trans_no, order_ FROM ".TB_PREF."debtor_trans d` |
| `sql/alter2.3.php` | 194 | `LEFT JOIN ".TB_PREF."voided v ON d.type=v.type AND d.trans_no=v.id` |
| `sql/alter2.3.php` | 238 | `$sql = "UPDATE ".TB_PREF."debtor_trans_details SET src_id = {$src_line['id']}` |
| `sql/alter2.3.sql` | 1 | `ALTER TABLE 0_comments ADD KEY `type_and_id` (`type`, `id`);` |
| `sql/alter2.3.sql` | 2 | `ALTER TABLE 0_quick_entries ADD COLUMN `bal_type` TINYINT(1) NOT NULL default '0';` |
| `sql/alter2.3.sql` | 5 | `ALTER TABLE 0_fiscal_year ADD UNIQUE KEY(`begin`), ADD UNIQUE KEY(`end`);` |
| `sql/alter2.3.sql` | 6 | `ALTER TABLE 0_useronline ADD KEY(`ip`);` |
| `sql/alter2.3.sql` | 7 | `ALTER TABLE 0_dimensions ADD KEY(`date_`), ADD KEY(`due_date`), ADD KEY(`type_`);` |
| `sql/alter2.3.sql` | 8 | `ALTER TABLE 0_gl_trans ADD KEY (`dimension_id`), ADD KEY (`dimension2_id`), ADD KEY (`tran_date`), ADD KEY `account_and_tran_date` (`account`, `tran_date`);` |
| `sql/alter2.3.sql` | 9 | `ALTER TABLE 0_chart_master DROP KEY `account_code`;` |
| `sql/alter2.3.sql` | 10 | `ALTER TABLE 0_chart_types ADD KEY(`class_id`);` |
| `sql/alter2.3.sql` | 11 | `ALTER TABLE 0_bank_accounts ADD KEY (`account_code`);` |
| `sql/alter2.3.sql` | 12 | `ALTER TABLE 0_bank_trans ADD KEY (`bank_act`,`reconciled`), ADD KEY (`bank_act`,`trans_date`);` |
| `sql/alter2.3.sql` | 13 | `ALTER TABLE 0_budget_trans ADD KEY `Account` (`account`, `tran_date`, `dimension_id`, `dimension2_id`);` |
| `sql/alter2.3.sql` | 14 | `ALTER TABLE 0_trans_tax_details ADD KEY `Type_and_Number` (`trans_type`,`trans_no`), ADD KEY (`tran_date`);` |
| `sql/alter2.3.sql` | 15 | `ALTER TABLE 0_audit_trail DROP KEY `fiscal_year`, ADD KEY `Seq` (`fiscal_year`, `gl_date`, `gl_seq`), ADD KEY `Type_and_Number` (`type`,`trans_no`);` |
| `sql/alter2.3.sql` | 16 | `ALTER TABLE 0_item_codes ADD KEY (`item_code`);` |
| `sql/alter2.3.sql` | 17 | `ALTER TABLE 0_stock_moves ADD KEY `Move` (`stock_id`,`loc_code`, `tran_date`);` |
| `sql/alter2.3.sql` | 18 | `ALTER TABLE 0_wo_issues ADD KEY (`workorder_id`);` |
| `sql/alter2.3.sql` | 19 | `ALTER TABLE 0_wo_manufacture ADD KEY (`workorder_id`);` |
| `sql/alter2.3.sql` | 20 | `ALTER TABLE 0_wo_requirements ADD KEY (`workorder_id`);` |
| `sql/alter2.3.sql` | 21 | `ALTER TABLE 0_bom DROP KEY `Parent_2`;` |
| `sql/alter2.3.sql` | 22 | `ALTER TABLE 0_refs ADD KEY `Type_and_Reference` (`type`,`reference`);` |
| `sql/alter2.3.sql` | 23 | `ALTER TABLE 0_grn_items ADD KEY (`grn_batch_id`);` |
| `sql/alter2.3.sql` | 24 | `ALTER TABLE 0_grn_batch ADD KEY (`delivery_date`), ADD KEY (`purch_order_no`);` |
| `sql/alter2.3.sql` | 25 | `ALTER TABLE 0_supp_invoice_items ADD KEY `Transaction` (`supp_trans_type`, `supp_trans_no`, `stock_id`);` |
| `sql/alter2.3.sql` | 26 | `ALTER TABLE 0_purch_order_details ADD KEY `order` (`order_no`, `po_detail_item`);` |
| `sql/alter2.3.sql` | 27 | `ALTER TABLE 0_purch_orders ADD KEY (`ord_date`);` |
| `sql/alter2.3.sql` | 28 | `ALTER TABLE 0_supp_trans ADD KEY (`tran_date`), DROP PRIMARY KEY, ADD PRIMARY KEY (`type`, `trans_no`);` |
| `sql/alter2.3.sql` | 29 | `ALTER TABLE 0_suppliers ADD KEY (`supp_ref`);` |
| `sql/alter2.3.sql` | 30 | `ALTER TABLE 0_supp_allocations ADD KEY `From` (`trans_type_from`, `trans_no_from`), ADD KEY `To` (`trans_type_to`, `trans_no_to`);` |
| `sql/alter2.3.sql` | 31 | `ALTER TABLE 0_cust_branch DROP KEY `br_name`, ADD KEY (`branch_ref`), ADD KEY (`group_no`);` |
| `sql/alter2.3.sql` | 32 | `ALTER TABLE 0_debtors_master ADD KEY (`debtor_ref`);` |
| `sql/alter2.3.sql` | 33 | `ALTER TABLE 0_debtor_trans DROP PRIMARY KEY, ADD PRIMARY KEY (`type`, `trans_no`), ADD KEY (`tran_date`);` |
| `sql/alter2.3.sql` | 34 | `ALTER TABLE 0_debtor_trans_details ADD KEY `Transaction` (`debtor_trans_type`, `debtor_trans_no`);` |
| `sql/alter2.3.sql` | 35 | `ALTER TABLE 0_cust_allocations ADD KEY `From` (`trans_type_from`, `trans_no_from`), ADD KEY `To` (`trans_type_to`, `trans_no_to`);` |
| `sql/alter2.3.sql` | 36 | `ALTER TABLE 0_sales_order_details ADD KEY `sorder` (`trans_type`, `order_no`);` |
| `sql/alter2.3.sql` | 37 | `ALTER TABLE 0_chart_master ADD KEY `accounts_by_type` (`account_type`, `account_code`);` |
| `sql/alter2.3.sql` | 38 | `# fix invalid constraint on databases generated from 2.2 version on en_US-new.sql` |
| `sql/alter2.3.sql` | 39 | `#ALTER TABLE `0_tax_types` DROP KEY `name`;` |
| `sql/alter2.3.sql` | 41 | `DROP TABLE IF EXISTS `0_sys_prefs`;` |
| `sql/alter2.3.sql` | 43 | `CREATE TABLE `0_sys_prefs` (` |
| `sql/alter2.3.sql` | 54 | `INSERT INTO `0_sys_prefs` SELECT 'coy_name','setup.company', 'varchar','60', c.coy_name FROM `0_company` c;` |
| `sql/alter2.3.sql` | 55 | `INSERT INTO `0_sys_prefs` SELECT 'gst_no','setup.company', 'varchar','25', c.gst_no FROM `0_company` c;` |
| `sql/alter2.3.sql` | 56 | `INSERT INTO `0_sys_prefs` SELECT 'coy_no','setup.company', 'varchar','25', c.coy_no FROM `0_company` c;` |
| `sql/alter2.3.sql` | 57 | `INSERT INTO `0_sys_prefs` SELECT 'tax_prd','setup.company', 'int','11', c.tax_prd FROM `0_company` c;` |
| `sql/alter2.3.sql` | 58 | `INSERT INTO `0_sys_prefs` SELECT 'tax_last','setup.company', 'int','11', c.tax_last FROM `0_company` c;` |
| `sql/alter2.3.sql` | 59 | `INSERT INTO `0_sys_prefs` SELECT 'postal_address','setup.company', 'tinytext','0', c.postal_address FROM `0_company` c;` |
| `sql/alter2.3.sql` | 60 | `INSERT INTO `0_sys_prefs` SELECT 'phone','setup.company', 'varchar','30', c.phone FROM `0_company` c;` |
| `sql/alter2.3.sql` | 61 | `INSERT INTO `0_sys_prefs` SELECT 'fax','setup.company', 'varchar','30',c.fax FROM `0_company` c;` |
| `sql/alter2.3.sql` | 62 | `INSERT INTO `0_sys_prefs` SELECT 'email','setup.company', 'varchar','100', c.email FROM `0_company` c;` |
| `sql/alter2.3.sql` | 63 | `INSERT INTO `0_sys_prefs` SELECT 'coy_logo','setup.company', 'varchar','100', c.coy_logo FROM `0_company` c;` |
| `sql/alter2.3.sql` | 64 | `INSERT INTO `0_sys_prefs` SELECT 'domicile','setup.company', 'varchar','55', c.domicile FROM `0_company` c;` |
| `sql/alter2.3.sql` | 65 | `INSERT INTO `0_sys_prefs` SELECT 'curr_default','setup.company', 'char','3', c.curr_default FROM `0_company` c;` |
| `sql/alter2.3.sql` | 66 | `INSERT INTO `0_sys_prefs` SELECT 'use_dimension','setup.company', 'tinyint','1', c.use_dimension FROM `0_company` c;` |
| `sql/alter2.3.sql` | 67 | `INSERT INTO `0_sys_prefs` SELECT 'f_year','setup.company', 'int','11', c.f_year FROM `0_company` c;` |
| `sql/alter2.3.sql` | 68 | `INSERT INTO `0_sys_prefs` SELECT 'no_item_list','setup.company', 'tinyint','1', c.no_item_list FROM `0_company` c;` |
| `sql/alter2.3.sql` | 69 | `INSERT INTO `0_sys_prefs` SELECT 'no_customer_list','setup.company', 'tinyint','1', c.no_customer_list FROM `0_company` c;` |
| `sql/alter2.3.sql` | 70 | `INSERT INTO `0_sys_prefs` SELECT 'no_supplier_list','setup.company', 'tinyint','1', c.no_supplier_list FROM `0_company` c;` |
| `sql/alter2.3.sql` | 71 | `INSERT INTO `0_sys_prefs` SELECT 'base_sales','setup.company', 'int','11', c.base_sales FROM `0_company` c;` |
| `sql/alter2.3.sql` | 72 | `INSERT INTO `0_sys_prefs` SELECT 'time_zone','setup.company', 'tinyint','1', c.time_zone FROM `0_company` c;` |
| `sql/alter2.3.sql` | 73 | `INSERT INTO `0_sys_prefs` SELECT 'add_pct','setup.company', 'int','5', c.add_pct FROM `0_company` c;` |
| `sql/alter2.3.sql` | 74 | `INSERT INTO `0_sys_prefs` SELECT 'round_to','setup.company', 'int','5', c.round_to FROM `0_company` c;` |
| `sql/alter2.3.sql` | 75 | `INSERT INTO `0_sys_prefs` SELECT 'login_tout','setup.company', 'smallint','6', c.login_tout FROM `0_company` c;` |
| `sql/alter2.3.sql` | 76 | `#INSERT INTO `0_sys_prefs` SELECT 'foreign_codes','setup.company', 'tinyint','1', c.foreign_codes FROM `0_company` c;` |
| `sql/alter2.3.sql` | 78 | `INSERT INTO `0_sys_prefs` SELECT 'past_due_days','glsetup.general', 'int','11', c.past_due_days FROM `0_company` c;` |
| `sql/alter2.3.sql` | 79 | `INSERT INTO `0_sys_prefs` SELECT 'profit_loss_year_act','glsetup.general', 'varchar','15', c.profit_loss_year_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 80 | `INSERT INTO `0_sys_prefs` SELECT 'retained_earnings_act','glsetup.general', 'varchar','15', c.retained_earnings_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 81 | `INSERT INTO `0_sys_prefs` SELECT 'bank_charge_act','glsetup.general', 'varchar','15',  c.bank_charge_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 82 | `INSERT INTO `0_sys_prefs` SELECT 'exchange_diff_act','glsetup.general', 'varchar','15', c.exchange_diff_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 84 | `INSERT INTO `0_sys_prefs` SELECT 'default_credit_limit','glsetup.customer', 'int','11', c.default_credit_limit FROM `0_company` c;` |
| `sql/alter2.3.sql` | 85 | `INSERT INTO `0_sys_prefs` SELECT 'accumulate_shipping','glsetup.customer', 'tinyint','1', c.accumulate_shipping FROM `0_company` c;` |
| `sql/alter2.3.sql` | 86 | `INSERT INTO `0_sys_prefs` SELECT 'legal_text','glsetup.customer', 'tinytext','0', c.legal_text FROM `0_company` c;` |
| `sql/alter2.3.sql` | 87 | `INSERT INTO `0_sys_prefs` SELECT 'freight_act','glsetup.customer', 'varchar','15', c.freight_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 89 | `INSERT INTO `0_sys_prefs` SELECT 'debtors_act','glsetup.sales', 'varchar','15', c.debtors_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 90 | `INSERT INTO `0_sys_prefs` SELECT 'default_sales_act','glsetup.sales', 'varchar','15', c.default_sales_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 91 | `INSERT INTO `0_sys_prefs` SELECT 'default_sales_discount_act','glsetup.sales', 'varchar','15', c.default_sales_discount_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 92 | `INSERT INTO `0_sys_prefs` SELECT 'default_prompt_payment_act','glsetup.sales', 'varchar','15', c.default_prompt_payment_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 93 | `INSERT INTO `0_sys_prefs` SELECT 'default_delivery_required','glsetup.sales', 'smallint','6', c.default_delivery_required FROM `0_company` c;` |
| `sql/alter2.3.sql` | 95 | `INSERT INTO `0_sys_prefs` SELECT 'default_dim_required','glsetup.dims', 'int','11', c.default_dim_required FROM `0_company` c;` |
| `sql/alter2.3.sql` | 97 | `INSERT INTO `0_sys_prefs` SELECT 'pyt_discount_act','glsetup.purchase', 'varchar','15', c.pyt_discount_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 98 | `INSERT INTO `0_sys_prefs` SELECT 'creditors_act','glsetup.purchase', 'varchar','15', c.creditors_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 99 | `INSERT INTO `0_sys_prefs` SELECT 'po_over_receive','glsetup.purchase', 'int','11', c.po_over_receive FROM `0_company` c;` |
| `sql/alter2.3.sql` | 100 | `INSERT INTO `0_sys_prefs` SELECT 'po_over_charge','glsetup.purchase', 'int','11', c.po_over_charge FROM `0_company` c;` |
| `sql/alter2.3.sql` | 102 | `INSERT INTO `0_sys_prefs` SELECT 'allow_negative_stock','glsetup.inventory', 'tinyint','1', c.allow_negative_stock FROM `0_company` c;` |
| `sql/alter2.3.sql` | 104 | `INSERT INTO `0_sys_prefs` SELECT 'default_inventory_act','glsetup.items', 'varchar','15', c.default_inventory_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 105 | `INSERT INTO `0_sys_prefs` SELECT 'default_cogs_act','glsetup.items', 'varchar','15', c.default_cogs_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 106 | `INSERT INTO `0_sys_prefs` SELECT 'default_adj_act','glsetup.items', 'varchar','15', c.default_adj_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 107 | `INSERT INTO `0_sys_prefs` SELECT 'default_inv_sales_act','glsetup.items', 'varchar','15', c.default_inv_sales_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 108 | `INSERT INTO `0_sys_prefs` SELECT 'default_assembly_act','glsetup.items', 'varchar','15', c.default_assembly_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 110 | `INSERT INTO `0_sys_prefs` SELECT 'default_workorder_required','glsetup.manuf', 'int', '11', c.default_workorder_required FROM `0_company` c;` |
| `sql/alter2.3.sql` | 112 | `#INSERT INTO `0_sys_prefs` SELECT 'payroll_act','glsetup.payroll', 'varchar','15', c.payroll_act FROM `0_company` c;` |
| `sql/alter2.3.sql` | 113 | `INSERT INTO `0_sys_prefs` SELECT 'version_id', 'system', 'varchar', '11', c.version_id FROM `0_company` c;` |
| `sql/alter2.3.sql` | 115 | `ALTER TABLE `0_stock_master` ADD COLUMN `editable` TINYINT(1) NOT NULL default '0';` |
| `sql/alter2.3.sql` | 116 | `ALTER TABLE `0_debtor_trans` ADD COLUMN `payment_terms` int(11) default NULL;` |
| `sql/alter2.3.sql` | 117 | `ALTER TABLE `0_sales_orders` ADD COLUMN `payment_terms` int(11) default NULL;` |
| `sql/alter2.3.sql` | 118 | `ALTER TABLE `0_sales_orders` ADD COLUMN `total` double NOT NULL default '0';` |
| `sql/alter2.3.sql` | 119 | `ALTER TABLE `0_purch_orders` ADD COLUMN `total` double NOT NULL default '0';` |
| `sql/alter2.3.sql` | 122 | `ALTER TABLE `0_bank_accounts` CHANGE `account_code` `account_code` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 123 | `ALTER TABLE `0_bank_trans` CHANGE `bank_act` `bank_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 124 | `ALTER TABLE `0_budget_trans` CHANGE `account` `account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 125 | `ALTER TABLE `0_chart_master` CHANGE `account_code` `account_code` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 126 | `ALTER TABLE `0_chart_master` CHANGE `account_code2` `account_code2` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 127 | `ALTER TABLE `0_cust_branch` CHANGE `sales_account` `sales_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 128 | `ALTER TABLE `0_cust_branch` CHANGE `sales_discount_account` `sales_discount_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 129 | `ALTER TABLE `0_cust_branch` CHANGE `receivables_account` `receivables_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 130 | `ALTER TABLE `0_cust_branch` CHANGE `payment_discount_account` `payment_discount_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 131 | `ALTER TABLE `0_gl_trans` CHANGE `account` `account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 132 | `ALTER TABLE `0_quick_entry_lines` CHANGE `dest_id` `dest_id` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 133 | `ALTER TABLE `0_stock_category` CHANGE `dflt_sales_act` `dflt_sales_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 134 | `ALTER TABLE `0_stock_category` CHANGE `dflt_cogs_act` `dflt_cogs_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 135 | `ALTER TABLE `0_stock_category` CHANGE `dflt_inventory_act` `dflt_inventory_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 136 | `ALTER TABLE `0_stock_category` CHANGE `dflt_adjustment_act` `dflt_adjustment_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 137 | `ALTER TABLE `0_stock_category` CHANGE `dflt_assembly_act` `dflt_assembly_act` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 138 | `ALTER TABLE `0_stock_master` CHANGE `sales_account` `sales_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 139 | `ALTER TABLE `0_stock_master` CHANGE `cogs_account` `cogs_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 140 | `ALTER TABLE `0_stock_master` CHANGE `inventory_account` `inventory_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 141 | `ALTER TABLE `0_stock_master` CHANGE `adjustment_account` `adjustment_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 142 | `ALTER TABLE `0_stock_master` CHANGE `assembly_account` `assembly_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 143 | `ALTER TABLE `0_supp_invoice_items` CHANGE `gl_code` `gl_code` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 144 | `ALTER TABLE `0_suppliers` CHANGE `purchase_account` `purchase_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 145 | `ALTER TABLE `0_suppliers` CHANGE `payable_account` `payable_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 146 | `ALTER TABLE `0_suppliers` CHANGE `payment_discount_account` `payment_discount_account` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 147 | `ALTER TABLE `0_tax_types` CHANGE `sales_gl_code` `sales_gl_code` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 148 | `ALTER TABLE `0_tax_types` CHANGE `purchasing_gl_code` `purchasing_gl_code` VARCHAR(15) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 149 | `ALTER TABLE `0_tag_associations` CHANGE `record_id` `record_id` VARCHAR(15) NOT NULL;` |
| `sql/alter2.3.sql` | 150 | `ALTER TABLE `0_chart_class` CHANGE `cid` `cid` VARCHAR(3) NOT NULL;` |
| `sql/alter2.3.sql` | 151 | `ALTER TABLE `0_chart_master` CHANGE `account_type` `account_type` VARCHAR(10) NOT NULL DEFAULT '0';` |
| `sql/alter2.3.sql` | 152 | `ALTER TABLE `0_chart_types` CHANGE `id` `id` VARCHAR(10) NOT NULL;` |
| `sql/alter2.3.sql` | 153 | `ALTER TABLE `0_chart_types` CHANGE `parent` `parent` VARCHAR(10) NOT NULL DEFAULT '-1';` |
| `sql/alter2.3.sql` | 154 | `ALTER TABLE `0_chart_types` CHANGE `class_id` `class_id` VARCHAR(3) NOT NULL DEFAULT '';` |
| `sql/alter2.3.sql` | 156 | `UPDATE `0_chart_types` SET parent='' WHERE parent='0' OR parent='-1';` |
| `sql/alter2.3.sql` | 158 | `INSERT INTO `0_sys_prefs` (name, category, type, length, value) VALUES ('auto_curr_reval','setup.company', 'smallint','6', '1');` |
| `sql/alter2.3.sql` | 160 | `DROP TABLE IF EXISTS `0_crm_categories`;` |
| `sql/alter2.3.sql` | 161 | `CREATE TABLE `0_crm_categories` (` |
| `sql/alter2.3.sql` | 175 | `INSERT INTO `0_crm_categories` VALUES (1, 'cust_branch', 'general', 'General', 'General contact data for customer branch (overrides company setting)', 1, 0);` |
| `sql/alter2.3.sql` | 176 | `INSERT INTO `0_crm_categories` VALUES (2, 'cust_branch', 'invoice', 'Invoices', 'Invoice posting (overrides company setting)', 1, 0);` |
| `sql/alter2.3.sql` | 177 | `INSERT INTO `0_crm_categories` VALUES (3, 'cust_branch', 'order', 'Orders', 'Order confirmation (overrides company setting)', 1, 0);` |
| `sql/alter2.3.sql` | 178 | `INSERT INTO `0_crm_categories` VALUES (4, 'cust_branch', 'delivery', 'Deliveries', 'Delivery coordination (overrides company setting)', 1, 0);` |
| `sql/alter2.3.sql` | 179 | `INSERT INTO `0_crm_categories` VALUES (5, 'customer', 'general', 'General', 'General contact data for customer', 1, 0);` |
| `sql/alter2.3.sql` | 180 | `INSERT INTO `0_crm_categories` VALUES (6, 'customer', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/alter2.3.sql` | 181 | `INSERT INTO `0_crm_categories` VALUES (7, 'customer', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/alter2.3.sql` | 182 | `INSERT INTO `0_crm_categories` VALUES (8, 'customer', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/alter2.3.sql` | 183 | `INSERT INTO `0_crm_categories` VALUES (9, 'supplier', 'general', 'General', 'General contact data for supplier', 1, 0);` |
| `sql/alter2.3.sql` | 184 | `INSERT INTO `0_crm_categories` VALUES (10,'supplier', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/alter2.3.sql` | 185 | `INSERT INTO `0_crm_categories` VALUES (11,'supplier', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/alter2.3.sql` | 186 | `INSERT INTO `0_crm_categories` VALUES (12,'supplier', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/alter2.3.sql` | 188 | `DROP TABLE IF EXISTS `0_crm_persons`;` |
| `sql/alter2.3.sql` | 190 | `CREATE TABLE `0_crm_persons` (` |
| `sql/alter2.3.sql` | 209 | `DROP TABLE IF EXISTS `0_crm_contacts`;` |
| `sql/alter2.3.sql` | 211 | `CREATE TABLE `0_crm_contacts` (` |
| `sql/alter2.3.sql` | 225 | `INSERT INTO `0_crm_persons` (`ref`, `email`, `lang`, `tmp_id`, `tmp_class`)` |
| `sql/alter2.3.sql` | 226 | `SELECT `debtor_ref`, `email`, if(`curr_code`=d.`lang`, NULL, 'en_GB'), `debtor_no`, 'customer'` |
| `sql/alter2.3.sql` | 227 | `FROM `0_debtors_master`,` |
| `sql/alter2.3.sql` | 228 | `(SELECT `value` as lang FROM `0_sys_prefs` WHERE name='curr_default') d;` |
| `sql/alter2.3.sql` | 230 | `INSERT INTO `0_crm_persons` (`ref`, `name`, `address`, `phone`, `phone2`,` |
| `sql/alter2.3.sql` | 232 | `SELECT `branch_ref`, `contact_name`, `br_address`, `phone`, `phone2`,` |
| `sql/alter2.3.sql` | 233 | ``fax`,`email`,`branch_code`, 'cust_branch' FROM `0_cust_branch`;` |
| `sql/alter2.3.sql` | 235 | `INSERT INTO `0_crm_persons` (`ref`, `name`, `address`, `phone`, `phone2`,` |
| `sql/alter2.3.sql` | 237 | `SELECT `supp_ref`, `contact`, `supp_address`, `phone`, `phone2`,` |
| `sql/alter2.3.sql` | 239 | `FROM `0_suppliers`,` |
| `sql/alter2.3.sql` | 240 | `(SELECT `value` as lang FROM `0_sys_prefs` WHERE name='curr_default') d;` |
| `sql/alter2.3.sql` | 243 | `INSERT INTO `0_crm_contacts` (`person_id`, `type`, `action`, `entity_id`)` |
| `sql/alter2.3.sql` | 244 | `SELECT `id`, `tmp_class`, 'general', `tmp_id`` |
| `sql/alter2.3.sql` | 245 | `FROM `0_crm_persons`;` |
| `sql/alter2.3.sql` | 247 | `ALTER TABLE `0_debtor_trans_details` ADD COLUMN `src_id` int(11) default NULL;` |
| `sql/alter2.3.sql` | 248 | `ALTER TABLE `0_debtor_trans_details` ADD KEY (`src_id`);` |
| `sql/alter2.3.sql` | 249 | `ALTER TABLE `0_suppliers` ADD COLUMN `tax_included` tinyint(1) NOT NULL default '0' AFTER `payment_terms`;` |
| `sql/alter2.3.sql` | 250 | `ALTER TABLE `0_supp_trans` ADD COLUMN `tax_included` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.3.sql` | 251 | `ALTER TABLE `0_purch_orders` ADD COLUMN `tax_included` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.3rc.sql` | 1 | `ALTER TABLE `0_supp_trans` ADD COLUMN `tax_included` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.3rc.sql` | 2 | `ALTER TABLE `0_purch_orders` ADD COLUMN `tax_included` tinyint(1) NOT NULL default '0';` |
| `sql/alter2.3rc.sql` | 3 | `UPDATE `0_crm_persons` SET `lang`='C' WHERE `lang`='en_GB';` |
| `sql/alter2.3rc.sql` | 4 | `UPDATE `0_users` SET `language`='C' WHERE `language`='en_GB';` |
| `sql/alter2.3rc.sql` | 5 | `UPDATE `0_suppliers` SET `purchase_account`='';` |
| `sql/alter2.4.php` | 109 | `db_query("DROP TABLE IF EXISTS " . $pref . 'wo_costing');` |
| `sql/alter2.4.php` | 110 | `db_query("DROP TABLE IF EXISTS " . $pref . 'stock_fa_class');` |
| `sql/alter2.4.php` | 111 | `db_query("DELETE FROM ".$pref."sys_prefs` |
| `sql/alter2.4.php` | 124 | `$sql = "SELECT DISTINCT type, type_no, tran_date, person_id FROM ".TB_PREF."gl_trans WHERE `type`=".ST_WORKORDER` |
| `sql/alter2.4.php` | 134 | `$sql1 = "UPDATE ".TB_PREF."gl_trans SET `type`=".ST_JOURNAL.", type_no={$journal_id},` |
| `sql/alter2.4.php` | 140 | `$sql2 = "INSERT INTO ".TB_PREF."wo_costing (workorder_id, cost_type, trans_no)` |
| `sql/alter2.4.php` | 176 | `$tresult = db_query($tsql, "Cannot select all tables with prefix '$pref'");` |
| `sql/alter2.4.php` | 180 | `db_query("ALTER TABLE `$table` CONVERT TO CHARACTER SET $old_encoding"); // convert encoding on utf-8 tables` |
| `sql/alter2.4.php` | 183 | `db_query("ALTER TABLE `$table` CHARSET $new_encoding");` |
| `sql/alter2.4.php` | 185 | `$cresult = db_query($csql, "Cannot select column names for table '$table'");` |
| `sql/alter2.4.php` | 211 | `$sql = "ALTER TABLE `$table` ".implode(',',$to_binary);` |
| `sql/alter2.4.php` | 213 | `$sql = "ALTER TABLE `$table` ".implode(',',$to_default);` |
| `sql/alter2.4.php` | 215 | `$sql = "ALTER TABLE `$table` ".implode(',',$to_utf);` |
| `sql/alter2.4.php` | 218 | `db_query("ALTER TABLE `$table` COLLATE $collation");` |
| `sql/alter2.4.php` | 220 | `db_query("ALTER DATABASE COLLATE $collation");` |
| `sql/alter2.4.php` | 228 | `$sql = "SELECT grn.id, grn.delivery_date, supp.curr_code` |
| `sql/alter2.4.php` | 229 | `FROM ".TB_PREF."grn_batch grn, ".TB_PREF."suppliers supp` |
| `sql/alter2.4.php` | 236 | `$sql = "UPDATE ".TB_PREF."grn_batch SET rate=%s WHERE id=%d";` |
| `sql/alter2.4.php` | 259 | `if (db_query("ALTER TABLE `".TB_PREF."{$table}` DROP `$col`") == false) {` |
| `sql/alter2.4.sql` | 1 | `INSERT INTO `0_sys_prefs` VALUES('tax_algorithm','glsetup.customer', 'tinyint', 1, '1');` |
| `sql/alter2.4.sql` | 2 | `INSERT INTO `0_sys_prefs` VALUES('gl_closing_date','setup.closing_date', 'date', 8, '');` |
| `sql/alter2.4.sql` | 3 | `ALTER TABLE `0_audit_trail` CHANGE `fiscal_year` `fiscal_year` int(11) NOT NULL default 0;` |
| `sql/alter2.4.sql` | 6 | `UPDATE `0_audit_trail` audit` |
| `sql/alter2.4.sql` | 7 | `LEFT JOIN `0_gl_trans` gl ON  gl.`type`=audit.`type` AND gl.type_no=audit.trans_no` |
| `sql/alter2.4.sql` | 8 | `LEFT JOIN `0_fiscal_year` year ON year.begin<=gl.tran_date AND year.end>=gl.tran_date` |
| `sql/alter2.4.sql` | 12 | `DROP TABLE IF EXISTS `0_wo_costing`;` |
| `sql/alter2.4.sql` | 14 | `CREATE TABLE `0_wo_costing` (` |
| `sql/alter2.4.sql` | 24 | `UPDATE `0_gl_trans` gl` |
| `sql/alter2.4.sql` | 25 | `LEFT JOIN `0_cust_branch` br ON br.receivables_account=gl.account AND br.debtor_no=gl.person_id AND gl.person_type_id=2` |
| `sql/alter2.4.sql` | 26 | `LEFT JOIN `0_suppliers` sup ON sup.payable_account=gl.account AND sup.supplier_id=gl.person_id AND gl.person_type_id=3` |
| `sql/alter2.4.sql` | 30 | `ALTER TABLE `0_tax_group_items` ADD COLUMN `tax_shipping` tinyint(1) NOT NULL default '0' AFTER `rate`;` |
| `sql/alter2.4.sql` | 31 | `UPDATE `0_tax_group_items` tgi` |
| `sql/alter2.4.sql` | 33 | `WHERE tgi.rate=(SELECT 0_tax_types.rate FROM 0_tax_types, 0_tax_groups` |
| `sql/alter2.4.sql` | 36 | `ALTER TABLE `0_sales_order_details` ADD KEY `stkcode` (`stk_code`);` |
| `sql/alter2.4.sql` | 37 | `ALTER TABLE `0_purch_order_details` ADD KEY `itemcode` (`item_code`);` |
| `sql/alter2.4.sql` | 38 | `ALTER TABLE `0_sys_prefs` CHANGE `value` `value` TEXT NOT NULL DEFAULT '';` |
| `sql/alter2.4.sql` | 39 | `ALTER TABLE `0_cust_branch` ADD COLUMN `bank_account` varchar(60) DEFAULT NULL AFTER `notes`;` |
| `sql/alter2.4.sql` | 41 | `ALTER TABLE `0_debtor_trans` ADD COLUMN `tax_included` tinyint(1) unsigned NOT NULL default '0' AFTER `payment_terms`;` |
| `sql/alter2.4.sql` | 42 | `UPDATE `0_debtor_trans` tr, `0_trans_tax_details` td SET tr.tax_included=td.included_in_price` |
| `sql/alter2.4.sql` | 45 | `ALTER TABLE `0_bank_accounts` ADD COLUMN `bank_charge_act` varchar(15) NOT NULL DEFAULT '' AFTER `id`;` |
| `sql/alter2.4.sql` | 46 | `UPDATE `0_bank_accounts` SET `bank_charge_act`=(SELECT `value` FROM 0_sys_prefs WHERE name='bank_charge_act');` |
| `sql/alter2.4.sql` | 48 | `ALTER TABLE `0_users` ADD `transaction_days` INT( 6 ) NOT NULL default '30' COMMENT 'Transaction days' AFTER `startup_tab`;` |
| `sql/alter2.4.sql` | 50 | `ALTER TABLE `0_purch_orders` ADD COLUMN `prep_amount` double NOT NULL DEFAULT 0 AFTER `total`;` |
| `sql/alter2.4.sql` | 51 | `ALTER TABLE `0_purch_orders` ADD COLUMN `alloc` double NOT NULL DEFAULT 0 AFTER `prep_amount`;` |
| `sql/alter2.4.sql` | 53 | `ALTER TABLE `0_sales_orders` ADD COLUMN `prep_amount` double NOT NULL DEFAULT 0 AFTER `total`;` |
| `sql/alter2.4.sql` | 54 | `ALTER TABLE `0_sales_orders` ADD COLUMN `alloc` double NOT NULL DEFAULT 0 AFTER `prep_amount`;` |
| `sql/alter2.4.sql` | 56 | `ALTER TABLE `0_cust_allocations` ADD  UNIQUE KEY(`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`);` |
| `sql/alter2.4.sql` | 57 | `ALTER TABLE `0_supp_allocations` ADD  UNIQUE KEY(`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`);` |
| `sql/alter2.4.sql` | 59 | `ALTER TABLE `0_sales_order_details` ADD COLUMN `invoiced` double NOT NULL DEFAULT 0 AFTER `quantity`;` |
| `sql/alter2.4.sql` | 61 | `# update sales_order_details.invoiced with sum of invoiced quantities on all related SI` |
| `sql/alter2.4.sql` | 62 | `UPDATE `0_sales_order_details` so` |
| `sql/alter2.4.sql` | 63 | `LEFT JOIN `0_debtor_trans_details` delivery ON delivery.`debtor_trans_type`=13 AND src_id=so.id` |
| `sql/alter2.4.sql` | 64 | `LEFT JOIN (SELECT src_id, sum(quantity) as qty FROM `0_debtor_trans_details` WHERE `debtor_trans_type`=10 GROUP BY src_id) inv` |
| `sql/alter2.4.sql` | 68 | `ALTER TABLE `0_debtor_trans` ADD COLUMN `prep_amount` double NOT NULL DEFAULT 0 AFTER `alloc`;` |
| `sql/alter2.4.sql` | 70 | `INSERT INTO `0_sys_prefs` VALUES ('deferred_income_act', 'glsetup.sales', 'varchar', '15', '');` |
| `sql/alter2.4.sql` | 73 | `UPDATE `0_security_roles` SET `sections`=CONCAT_WS(';', `sections`, '768'), `areas`='775'` |
| `sql/alter2.4.sql` | 76 | `UPDATE `0_security_roles` SET `areas`=CONCAT_WS(';', `areas`, '775')` |
| `sql/alter2.4.sql` | 79 | `ALTER TABLE `0_stock_master` ADD COLUMN `no_purchase` tinyint(1) NOT NULL default '0' AFTER `no_sale`;` |
| `sql/alter2.4.sql` | 80 | `ALTER TABLE `0_stock_category` ADD COLUMN `dflt_no_purchase` tinyint(1) NOT NULL default '0' AFTER `dflt_no_sale`;` |
| `sql/alter2.4.sql` | 83 | `ALTER TABLE `0_grn_batch` ADD COLUMN `rate` double NULL default '1' AFTER `loc_code`;` |
| `sql/alter2.4.sql` | 84 | `ALTER TABLE `0_users` CHANGE `query_size` `query_size` TINYINT(1) UNSIGNED NOT NULL DEFAULT 10;` |
| `sql/alter2.4.sql` | 86 | `ALTER TABLE `0_users` ADD `save_report_selections` SMALLINT( 6 ) NOT NULL default '0' COMMENT 'Save Report Selection Days' AFTER `transaction_days`;` |
| `sql/alter2.4.sql` | 87 | `ALTER TABLE `0_users` ADD `use_date_picker` TINYINT(1) NOT NULL default '1' COMMENT 'Use Date Picker for all Date Values' AFTER `save_report_selections`;` |
| `sql/alter2.4.sql` | 88 | `ALTER TABLE `0_users` ADD `def_print_destination` TINYINT(1) NOT NULL default '0' COMMENT 'Default Report Destination' AFTER `use_date_picker`;` |
| `sql/alter2.4.sql` | 89 | `ALTER TABLE `0_users` ADD `def_print_orientation` TINYINT(1) NOT NULL default '0' COMMENT 'Default Report Orientation' AFTER `def_print_destination`;` |
| `sql/alter2.4.sql` | 91 | `INSERT INTO `0_sys_prefs` VALUES('no_zero_lines_amount', 'glsetup.sales', 'tinyint', 1, '1');` |
| `sql/alter2.4.sql` | 92 | `INSERT INTO `0_sys_prefs` VALUES('show_po_item_codes', 'glsetup.purchase', 'tinyint', 1, '0');` |
| `sql/alter2.4.sql` | 93 | `INSERT INTO `0_sys_prefs` VALUES('accounts_alpha', 'glsetup.general', 'tinyint', 1, '0');` |
| `sql/alter2.4.sql` | 94 | `INSERT INTO `0_sys_prefs` VALUES('loc_notification', 'glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/alter2.4.sql` | 95 | `INSERT INTO `0_sys_prefs` VALUES('print_invoice_no', 'glsetup.sales', 'tinyint', 1, '0');` |
| `sql/alter2.4.sql` | 96 | `INSERT INTO `0_sys_prefs` VALUES('allow_negative_prices', 'glsetup.inventory', 'tinyint', 1, '1');` |
| `sql/alter2.4.sql` | 97 | `INSERT INTO `0_sys_prefs` VALUES('print_item_images_on_quote', 'glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/alter2.4.sql` | 98 | `INSERT INTO `0_sys_prefs` VALUES('default_receival_required', 'glsetup.purchase', 'smallint', 6, '10');` |
| `sql/alter2.4.sql` | 101 | `ALTER TABLE `0_areas` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 102 | `ALTER TABLE `0_attachments` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 103 | `ALTER TABLE `0_bank_accounts` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 104 | `ALTER TABLE `0_bom` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 105 | `ALTER TABLE `0_chart_class` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 106 | `ALTER TABLE `0_chart_master` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 107 | `ALTER TABLE `0_chart_types` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 108 | `ALTER TABLE `0_credit_status` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 109 | `ALTER TABLE `0_currencies` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 110 | `ALTER TABLE `0_cust_branch` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 111 | `ALTER TABLE `0_debtors_master` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 112 | `ALTER TABLE `0_exchange_rates` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 113 | `ALTER TABLE `0_groups` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 114 | `ALTER TABLE `0_item_codes` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 115 | `ALTER TABLE `0_item_units` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 116 | `ALTER TABLE `0_locations` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 117 | `ALTER TABLE `0_payment_terms` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 118 | `ALTER TABLE `0_prices` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 119 | `ALTER TABLE `0_printers` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 120 | `ALTER TABLE `0_print_profiles` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 121 | `ALTER TABLE `0_purch_data` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 122 | `ALTER TABLE `0_quick_entries` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 123 | `ALTER TABLE `0_quick_entry_lines` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 124 | `ALTER TABLE `0_salesman` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 125 | `ALTER TABLE `0_sales_pos` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 126 | `ALTER TABLE `0_sales_types` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 127 | `ALTER TABLE `0_security_roles` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 128 | `ALTER TABLE `0_shippers` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 129 | `ALTER TABLE `0_sql_trail` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 130 | `ALTER TABLE `0_stock_category` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 131 | `ALTER TABLE `0_suppliers` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 132 | `ALTER TABLE `0_sys_prefs` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 133 | `ALTER TABLE `0_tags` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 134 | `ALTER TABLE `0_tag_associations` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 135 | `ALTER TABLE `0_useronline` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 136 | `ALTER TABLE `0_users` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 137 | `ALTER TABLE `0_workcentres` ENGINE=InnoDB;` |
| `sql/alter2.4.sql` | 139 | `ALTER TABLE `0_gl_trans` CHANGE `type_no` `type_no` int(11) NOT NULL default '0';` |
| `sql/alter2.4.sql` | 140 | `ALTER TABLE `0_loc_stock` CHANGE `reorder_level` `reorder_level` double NOT NULL default '0';` |
| `sql/alter2.4.sql` | 143 | `ALTER TABLE `0_supp_invoice_items` ADD COLUMN `dimension_id` int(11) NOT NULL DEFAULT '0' AFTER `memo_`;` |
| `sql/alter2.4.sql` | 144 | `ALTER TABLE `0_supp_invoice_items` ADD COLUMN `dimension2_id` int(11) NOT NULL DEFAULT '0' AFTER `dimension_id`;` |
| `sql/alter2.4.sql` | 146 | `UPDATE `0_supp_invoice_items` si` |
| `sql/alter2.4.sql` | 147 | `LEFT JOIN `0_gl_trans` gl ON si.supp_trans_type=gl.`type` AND si.supp_trans_no=gl.type_no AND si.gl_code=gl.account` |
| `sql/alter2.4.sql` | 151 | `ALTER TABLE `0_quick_entries` ADD COLUMN `usage` varchar(120) NULL AFTER `description`;` |
| `sql/alter2.4.sql` | 152 | `ALTER TABLE `0_quick_entry_lines` ADD COLUMN `memo` tinytext NOT NULL AFTER `amount`;` |
| `sql/alter2.4.sql` | 155 | `ALTER TABLE `0_cust_allocations` ADD COLUMN `person_id` int(11) DEFAULT NULL AFTER `id`;` |
| `sql/alter2.4.sql` | 156 | `UPDATE `0_cust_allocations` alloc LEFT JOIN `0_debtor_trans` trans ON alloc.trans_no_to=trans.trans_no AND alloc.trans_type_to=trans.type` |
| `sql/alter2.4.sql` | 159 | `ALTER TABLE `0_supp_allocations` ADD COLUMN `person_id` int(11) DEFAULT NULL AFTER `id`;` |
| `sql/alter2.4.sql` | 160 | `UPDATE `0_supp_allocations` alloc LEFT JOIN `0_supp_trans` trans ON alloc.trans_no_to=trans.trans_no AND alloc.trans_type_to=trans.type` |
| `sql/alter2.4.sql` | 163 | `ALTER TABLE `0_cust_allocations` DROP KEY `trans_type_from`;` |
| `sql/alter2.4.sql` | 164 | `ALTER TABLE `0_cust_allocations` ADD  UNIQUE KEY(`person_id`,`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`);` |
| `sql/alter2.4.sql` | 165 | `ALTER TABLE `0_supp_allocations` DROP KEY `trans_type_from`;` |
| `sql/alter2.4.sql` | 166 | `ALTER TABLE `0_supp_allocations` ADD  UNIQUE KEY(`person_id`,`trans_type_from`,`trans_no_from`,`trans_type_to`,`trans_no_to`);` |
| `sql/alter2.4.sql` | 169 | `DROP TABLE IF EXISTS `0_journal`;` |
| `sql/alter2.4.sql` | 170 | `CREATE TABLE `0_journal` (` |
| `sql/alter2.4.sql` | 185 | `INSERT INTO `0_journal` (`type`, `trans_no`, `tran_date`, `reference`, `event_date`,`doc_date`,`currency`,`amount`)` |
| `sql/alter2.4.sql` | 186 | `SELECT `gl`.`type`, `gl`.`type_no`, `gl`.`tran_date`, `ref`.`reference`, `gl`.`tran_date`,` |
| `sql/alter2.4.sql` | 188 | `FROM `0_gl_trans` gl LEFT JOIN `0_refs` ref ON gl.type = ref.type AND gl.type_no=ref.id` |
| `sql/alter2.4.sql` | 189 | `LEFT JOIN `0_sys_prefs` sys_curr ON `sys_curr`.`name`='curr_default'` |
| `sql/alter2.4.sql` | 194 | `ALTER TABLE `0_debtor_trans` DROP PRIMARY KEY;` |
| `sql/alter2.4.sql` | 195 | `ALTER TABLE `0_debtor_trans` ADD  PRIMARY KEY (`type`,`trans_no`, `debtor_no`);` |
| `sql/alter2.4.sql` | 196 | `ALTER TABLE `0_supp_trans` DROP PRIMARY KEY;` |
| `sql/alter2.4.sql` | 197 | `ALTER TABLE `0_supp_trans` ADD  PRIMARY KEY (`type`,`trans_no`, `supplier_id`);` |
| `sql/alter2.4.sql` | 199 | `ALTER TABLE  `0_trans_tax_details` ADD COLUMN `reg_type` tinyint(1) DEFAULT NULL AFTER `memo`;` |
| `sql/alter2.4.sql` | 201 | `UPDATE `0_trans_tax_details` reg` |
| `sql/alter2.4.sql` | 205 | `UPDATE `0_trans_tax_details` reg` |
| `sql/alter2.4.sql` | 209 | `INSERT IGNORE INTO `0_sys_prefs` VALUES` |
| `sql/alter2.4.sql` | 220 | `DELETE moves` |
| `sql/alter2.4.sql` | 221 | `FROM `0_stock_moves` moves` |
| `sql/alter2.4.sql` | 222 | `INNER JOIN (SELECT * FROM `0_stock_moves` WHERE `type`=11 AND `qty`<0) writeoffs ON writeoffs.`trans_no`=moves.`trans_no` AND writeoffs.`type`=11` |
| `sql/alter2.4.sql` | 227 | `UPDATE `0_stock_moves` SET` |
| `sql/alter2.4.sql` | 230 | `DROP TABLE IF EXISTS `0_movement_types`;` |
| `sql/alter2.4.sql` | 233 | `UPDATE `0_salesman`` |
| `sql/alter2.4.sql` | 238 | `DROP TABLE IF EXISTS `0_reflines`;` |
| `sql/alter2.4.sql` | 239 | `CREATE TABLE `0_reflines` (` |
| `sql/alter2.4.sql` | 251 | `INSERT INTO `0_reflines` (`trans_type`, `pattern`, `default`) SELECT `type_id`, `next_reference`, 1 FROM `0_sys_types`;` |
| `sql/alter2.4.sql` | 253 | `DROP TABLE `0_sys_types`;` |
| `sql/alter2.4.sql` | 255 | `ALTER TABLE `0_cust_branch` DROP KEY `branch_code`;` |
| `sql/alter2.4.sql` | 256 | `ALTER TABLE `0_supp_trans` DROP KEY `SupplierID_2`;` |
| `sql/alter2.4.sql` | 257 | `ALTER TABLE `0_supp_trans` DROP KEY `type`;` |
| `sql/alter2.4.sql` | 260 | `ALTER TABLE `0_locations` ADD COLUMN `fixed_asset` tinyint(1) NOT NULL DEFAULT '0' after `contact`;` |
| `sql/alter2.4.sql` | 262 | `DROP TABLE IF EXISTS `0_stock_fa_class`;` |
| `sql/alter2.4.sql` | 263 | `CREATE TABLE `0_stock_fa_class` (` |
| `sql/alter2.4.sql` | 273 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_method` char(1) NOT NULL DEFAULT 'S' AFTER `editable`;` |
| `sql/alter2.4.sql` | 274 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_rate` double NOT NULL DEFAULT '0' AFTER `depreciation_method`;` |
| `sql/alter2.4.sql` | 275 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_factor` double NOT NULL DEFAULT '0' AFTER `depreciation_rate`;` |
| `sql/alter2.4.sql` | 276 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_start` date NOT NULL DEFAULT '0000-00-00' AFTER `depreciation_factor`;` |
| `sql/alter2.4.sql` | 277 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_date` date NOT NULL DEFAULT '0000-00-00' AFTER `depreciation_start`;` |
| `sql/alter2.4.sql` | 278 | `ALTER TABLE `0_stock_master` ADD COLUMN `fa_class_id` varchar(20) NOT NULL DEFAULT '' AFTER `depreciation_date`;` |
| `sql/alter2.4.sql` | 279 | `ALTER TABLE `0_stock_master` CHANGE `actual_cost` `purchase_cost` double NOT NULL default 0;` |
| `sql/alter2.4.sql` | 281 | `INSERT IGNORE INTO `0_sys_prefs` VALUES` |
| `sql/alter2.4.sql` | 288 | `ALTER TABLE `0_wo_issue_items` ADD COLUMN  `unit_cost` double NOT NULL default '0' AFTER `qty_issued`;` |
| `sql/alter2.4.sql` | 289 | `ALTER TABLE `0_wo_requirements` CHANGE COLUMN `std_cost` `unit_cost` double NOT NULL default '0';` |
| `sql/alter2.4.sql` | 291 | `ALTER TABLE `0_stock_master` DROP COLUMN `last_cost`;` |
| `sql/alter2.4.sql` | 292 | `UPDATE `0_stock_master` SET `material_cost`=`material_cost`+`labour_cost`+`overhead_cost`;` |
| `sql/alter2.4.sql` | 294 | `ALTER TABLE `0_stock_master` CHANGE COLUMN `assembly_account` `wip_account` VARCHAR(15) NOT NULL default '';` |
| `sql/alter2.4.sql` | 295 | `ALTER TABLE `0_stock_category` CHANGE COLUMN `dflt_assembly_act` `dflt_wip_act` VARCHAR(15) NOT NULL default '';` |
| `sql/alter2.4.sql` | 296 | `UPDATE `0_sys_prefs` SET `name`='default_wip_act' WHERE `name`='default_assembly_act';` |
| `sql/alter2.4.sql` | 298 | `UPDATE `0_wo_issue_items` i, `0_stock_moves` m` |
| `sql/alter2.4.sql` | 302 | `UPDATE `0_wo_requirements` r, `0_stock_moves` m` |
| `sql/alter2.4.sql` | 306 | `UPDATE `0_bank_trans` SET person_id=trans_no WHERE person_type_id=26;` |
| `sql/alter2.4.sql` | 308 | `ALTER TABLE `0_budget_trans` CHANGE `counter` `id` int(11) NOT NULL AUTO_INCREMENT;` |
| `sql/alter2.4.sql` | 309 | `ALTER TABLE `0_sys_prefs` CHANGE `value` `value` text NOT NULL default '';` |
| `sql/alter2.4.sql` | 311 | `ALTER TABLE `0_debtor_trans`` |
| `sql/alter2.4.sql` | 313 | `DROP PRIMARY KEY,` |
| `sql/alter2.4.sql` | 316 | `ALTER TABLE `0_supp_trans`` |
| `sql/alter2.4.sql` | 318 | `DROP PRIMARY KEY,` |
| `sql/alter2.4rc1.php` | 68 | `if (!db_query("UPDATE ".$pref."sys_prefs SET value=".db_escape($this->fixed_disposal_act)` |
| `sql/alter2.4rc1.php` | 82 | `db_query("DROP TABLE IF EXISTS " . $pref . 'stock_fa_class');` |
| `sql/alter2.4rc1.php` | 84 | `db_query("DELETE FROM ".$pref."sys_prefs "` |
| `sql/alter2.4rc1.sql` | 2 | `ALTER TABLE `0_locations` ADD COLUMN `fixed_asset` tinyint(1) NOT NULL DEFAULT '0' after `contact`;` |
| `sql/alter2.4rc1.sql` | 4 | `DROP TABLE IF EXISTS `0_stock_fa_class`;` |
| `sql/alter2.4rc1.sql` | 5 | `CREATE TABLE `0_stock_fa_class` (` |
| `sql/alter2.4rc1.sql` | 15 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_method` char(1) NOT NULL DEFAULT 'S' AFTER `editable`;` |
| `sql/alter2.4rc1.sql` | 16 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_rate` double NOT NULL DEFAULT '0' AFTER `depreciation_method`;` |
| `sql/alter2.4rc1.sql` | 17 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_factor` double NOT NULL DEFAULT '0' AFTER `depreciation_rate`;` |
| `sql/alter2.4rc1.sql` | 18 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_start` date NOT NULL DEFAULT '0000-00-00' AFTER `depreciation_factor`;` |
| `sql/alter2.4rc1.sql` | 19 | `ALTER TABLE `0_stock_master` ADD COLUMN `depreciation_date` date NOT NULL DEFAULT '0000-00-00' AFTER `depreciation_start`;` |
| `sql/alter2.4rc1.sql` | 20 | `ALTER TABLE `0_stock_master` ADD COLUMN `fa_class_id` varchar(20) NOT NULL DEFAULT '' AFTER `depreciation_date`;` |
| `sql/alter2.4rc1.sql` | 21 | `ALTER TABLE `0_stock_master` CHANGE `actual_cost` `purchase_cost` double NOT NULL default 0;` |
| `sql/alter2.4rc1.sql` | 23 | `INSERT IGNORE INTO `0_sys_prefs` VALUES` |
| `sql/alter2.4rc1.sql` | 30 | `ALTER TABLE `0_wo_issue_items` ADD COLUMN  `unit_cost` double NOT NULL default '0' AFTER `qty_issued`;` |
| `sql/alter2.4rc1.sql` | 31 | `ALTER TABLE `0_wo_requirements` CHANGE COLUMN `std_cost` `unit_cost` double NOT NULL default '0';` |
| `sql/alter2.4rc1.sql` | 33 | `ALTER TABLE `0_stock_master` DROP COLUMN `last_cost`;` |
| `sql/alter2.4rc1.sql` | 34 | `UPDATE `0_stock_master` SET `material_cost`=`material_cost`+`labour_cost`+`overhead_cost`;` |
| `sql/alter2.4rc1.sql` | 36 | `ALTER TABLE `0_stock_master` CHANGE COLUMN `assembly_account` `wip_account` VARCHAR(15) NOT NULL default '';` |
| `sql/alter2.4rc1.sql` | 37 | `ALTER TABLE `0_stock_category` CHANGE COLUMN `dflt_assembly_act` `dflt_wip_act` VARCHAR(15) NOT NULL default '';` |
| `sql/alter2.4rc1.sql` | 38 | `UPDATE `0_sys_prefs` SET `name`='default_wip_act' WHERE `name`='default_assembly_act';` |
| `sql/alter2.4rc1.sql` | 40 | `UPDATE `0_wo_issue_items` i, `0_stock_moves` m` |
| `sql/alter2.4rc1.sql` | 44 | `UPDATE `0_wo_requirements` r, `0_stock_moves` m` |
| `sql/alter2.4rc1.sql` | 48 | `UPDATE `0_bank_trans` SET person_id=trans_no WHERE person_type_id=26;` |
| `sql/alter2.4rc1.sql` | 50 | `ALTER TABLE `0_budget_trans` CHANGE `counter` `id` int(11) NOT NULL AUTO_INCREMENT;` |
| `sql/alter2.4rc1.sql` | 51 | `ALTER TABLE `0_sys_prefs` CHANGE `value` `value` text NOT NULL default '';` |
| `sql/alter2.4rc1.sql` | 53 | `ALTER TABLE `0_debtor_trans`` |
| `sql/alter2.4rc1.sql` | 55 | `DROP PRIMARY KEY,` |
| `sql/alter2.4rc1.sql` | 58 | `ALTER TABLE `0_supp_trans`` |
| `sql/alter2.4rc1.sql` | 60 | `DROP PRIMARY KEY,` |
| `sql/alter2.sql` | 1 | `ALTER TABLE `0_users` ADD `show_hints` TINYINT(1) DEFAULT '0' NOT NULL AFTER `show_codes` ;` |
| `sql/en_US-demo.sql` | 22 | `DROP TABLE IF EXISTS `0_areas`;` |
| `sql/en_US-demo.sql` | 23 | `CREATE TABLE IF NOT EXISTS `0_areas` (` |
| `sql/en_US-demo.sql` | 35 | `INSERT INTO `0_areas` VALUES (1, 'Global', 0);` |
| `sql/en_US-demo.sql` | 43 | `DROP TABLE IF EXISTS `0_attachments`;` |
| `sql/en_US-demo.sql` | 44 | `CREATE TABLE IF NOT EXISTS `0_attachments` (` |
| `sql/en_US-demo.sql` | 68 | `DROP TABLE IF EXISTS `0_audit_trail`;` |
| `sql/en_US-demo.sql` | 69 | `CREATE TABLE IF NOT EXISTS `0_audit_trail` (` |
| `sql/en_US-demo.sql` | 88 | `INSERT INTO `0_audit_trail` VALUES` |
| `sql/en_US-demo.sql` | 124 | `DROP TABLE IF EXISTS `0_bank_accounts`;` |
| `sql/en_US-demo.sql` | 125 | `CREATE TABLE IF NOT EXISTS `0_bank_accounts` (` |
| `sql/en_US-demo.sql` | 149 | `INSERT INTO `0_bank_accounts` VALUES ('1060', 0, 'Current account', 'N/A', 'N/A', '', 'USD', 1, 1, '5690', '0000-00-00 00:00:00', 0, 0);` |
| `sql/en_US-demo.sql` | 150 | `INSERT INTO `0_bank_accounts` VALUES ('1065', 3, 'Petty Cash account', 'N/A', 'N/A', '', 'USD', 0, 2, '5690', '0000-00-00 00:00:00', 0, 0);` |
| `sql/en_US-demo.sql` | 158 | `DROP TABLE IF EXISTS `0_bank_trans`;` |
| `sql/en_US-demo.sql` | 159 | `CREATE TABLE IF NOT EXISTS `0_bank_trans` (` |
| `sql/en_US-demo.sql` | 183 | `INSERT INTO `0_bank_trans` VALUES` |
| `sql/en_US-demo.sql` | 195 | `DROP TABLE IF EXISTS `0_bom`;` |
| `sql/en_US-demo.sql` | 196 | `CREATE TABLE IF NOT EXISTS `0_bom` (` |
| `sql/en_US-demo.sql` | 215 | `INSERT INTO `0_bom` VALUES` |
| `sql/en_US-demo.sql` | 227 | `DROP TABLE IF EXISTS `0_budget_trans`;` |
| `sql/en_US-demo.sql` | 228 | `CREATE TABLE IF NOT EXISTS `0_budget_trans` (` |
| `sql/en_US-demo.sql` | 250 | `DROP TABLE IF EXISTS `0_chart_class`;` |
| `sql/en_US-demo.sql` | 251 | `CREATE TABLE IF NOT EXISTS `0_chart_class` (` |
| `sql/en_US-demo.sql` | 263 | `INSERT INTO `0_chart_class` VALUES ('1', 'Assets', 1, 0);` |
| `sql/en_US-demo.sql` | 264 | `INSERT INTO `0_chart_class` VALUES ('2', 'Liabilities', 2, 0);` |
| `sql/en_US-demo.sql` | 265 | `INSERT INTO `0_chart_class` VALUES ('3', 'Income', 4, 0);` |
| `sql/en_US-demo.sql` | 266 | `INSERT INTO `0_chart_class` VALUES ('4', 'Costs', 6, 0);` |
| `sql/en_US-demo.sql` | 274 | `DROP TABLE IF EXISTS `0_chart_master`;` |
| `sql/en_US-demo.sql` | 275 | `CREATE TABLE IF NOT EXISTS `0_chart_master` (` |
| `sql/en_US-demo.sql` | 290 | `INSERT INTO `0_chart_master` VALUES ('1060', '', 'Checking Account', '1', 0);` |
| `sql/en_US-demo.sql` | 291 | `INSERT INTO `0_chart_master` VALUES ('1065', '', 'Petty Cash', '1', 0);` |
| `sql/en_US-demo.sql` | 292 | `INSERT INTO `0_chart_master` VALUES ('1200', '', 'Accounts Receivables', '1', 0);` |
| `sql/en_US-demo.sql` | 293 | `INSERT INTO `0_chart_master` VALUES ('1205', '', 'Allowance for doubtful accounts', '1', 0);` |
| `sql/en_US-demo.sql` | 294 | `INSERT INTO `0_chart_master` VALUES ('1510', '', 'Inventory', '2', 0);` |
| `sql/en_US-demo.sql` | 295 | `INSERT INTO `0_chart_master` VALUES ('1520', '', 'Stocks of Raw Materials', '2', 0);` |
| `sql/en_US-demo.sql` | 296 | `INSERT INTO `0_chart_master` VALUES ('1530', '', 'Stocks of Work In Progress', '2', 0);` |
| `sql/en_US-demo.sql` | 297 | `INSERT INTO `0_chart_master` VALUES ('1540', '', 'Stocks of Finished Goods', '2', 0);` |
| `sql/en_US-demo.sql` | 298 | `INSERT INTO `0_chart_master` VALUES ('1550', '', 'Goods Received Clearing account', '2', 0);` |
| `sql/en_US-demo.sql` | 299 | `INSERT INTO `0_chart_master` VALUES ('1820', '', 'Office Furniture &amp; Equipment', '3', 0);` |
| `sql/en_US-demo.sql` | 300 | `INSERT INTO `0_chart_master` VALUES ('1825', '', 'Accum. Amort. -Furn. &amp; Equip.', '3', 0);` |
| `sql/en_US-demo.sql` | 301 | `INSERT INTO `0_chart_master` VALUES ('1840', '', 'Vehicle', '3', 0);` |
| `sql/en_US-demo.sql` | 302 | `INSERT INTO `0_chart_master` VALUES ('1845', '', 'Accum. Amort. -Vehicle', '3', 0);` |
| `sql/en_US-demo.sql` | 303 | `INSERT INTO `0_chart_master` VALUES ('2100', '', 'Accounts Payable', '4', 0);` |
| `sql/en_US-demo.sql` | 304 | `INSERT INTO `0_chart_master` VALUES ('2110', '', 'Accrued Income Tax - Federal', '4', 0);` |
| `sql/en_US-demo.sql` | 305 | `INSERT INTO `0_chart_master` VALUES ('2120', '', 'Accrued Income Tax - State', '4', 0);` |
| `sql/en_US-demo.sql` | 306 | `INSERT INTO `0_chart_master` VALUES ('2130', '', 'Accrued Franchise Tax', '4', 0);` |
| `sql/en_US-demo.sql` | 307 | `INSERT INTO `0_chart_master` VALUES ('2140', '', 'Accrued Real &amp; Personal Prop Tax', '4', 0);` |
| `sql/en_US-demo.sql` | 308 | `INSERT INTO `0_chart_master` VALUES ('2150', '', 'Sales Tax', '4', 0);` |
| `sql/en_US-demo.sql` | 309 | `INSERT INTO `0_chart_master` VALUES ('2160', '', 'Accrued Use Tax Payable', '4', 0);` |
| `sql/en_US-demo.sql` | 310 | `INSERT INTO `0_chart_master` VALUES ('2210', '', 'Accrued Wages', '4', 0);` |
| `sql/en_US-demo.sql` | 311 | `INSERT INTO `0_chart_master` VALUES ('2220', '', 'Accrued Comp Time', '4', 0);` |
| `sql/en_US-demo.sql` | 312 | `INSERT INTO `0_chart_master` VALUES ('2230', '', 'Accrued Holiday Pay', '4', 0);` |
| `sql/en_US-demo.sql` | 313 | `INSERT INTO `0_chart_master` VALUES ('2240', '', 'Accrued Vacation Pay', '4', 0);` |
| `sql/en_US-demo.sql` | 314 | `INSERT INTO `0_chart_master` VALUES ('2310', '', 'Accr. Benefits - 401K', '4', 0);` |
| `sql/en_US-demo.sql` | 315 | `INSERT INTO `0_chart_master` VALUES ('2320', '', 'Accr. Benefits - Stock Purchase', '4', 0);` |
| `sql/en_US-demo.sql` | 316 | `INSERT INTO `0_chart_master` VALUES ('2330', '', 'Accr. Benefits - Med, Den', '4', 0);` |
| `sql/en_US-demo.sql` | 317 | `INSERT INTO `0_chart_master` VALUES ('2340', '', 'Accr. Benefits - Payroll Taxes', '4', 0);` |
| `sql/en_US-demo.sql` | 318 | `INSERT INTO `0_chart_master` VALUES ('2350', '', 'Accr. Benefits - Credit Union', '4', 0);` |
| `sql/en_US-demo.sql` | 319 | `INSERT INTO `0_chart_master` VALUES ('2360', '', 'Accr. Benefits - Savings Bond', '4', 0);` |
| `sql/en_US-demo.sql` | 320 | `INSERT INTO `0_chart_master` VALUES ('2370', '', 'Accr. Benefits - Garnish', '4', 0);` |
| `sql/en_US-demo.sql` | 321 | `INSERT INTO `0_chart_master` VALUES ('2380', '', 'Accr. Benefits - Charity Cont.', '4', 0);` |
| `sql/en_US-demo.sql` | 322 | `INSERT INTO `0_chart_master` VALUES ('2620', '', 'Bank Loans', '5', 0);` |
| `sql/en_US-demo.sql` | 323 | `INSERT INTO `0_chart_master` VALUES ('2680', '', 'Loans from Shareholders', '5', 0);` |
| `sql/en_US-demo.sql` | 324 | `INSERT INTO `0_chart_master` VALUES ('3350', '', 'Common Shares', '6', 0);` |
| `sql/en_US-demo.sql` | 325 | `INSERT INTO `0_chart_master` VALUES ('3590', '', 'Retained Earnings - prior years', '7', 0);` |
| `sql/en_US-demo.sql` | 326 | `INSERT INTO `0_chart_master` VALUES ('4010', '', 'Sales', '8', 0);` |
| `sql/en_US-demo.sql` | 327 | `INSERT INTO `0_chart_master` VALUES ('4430', '', 'Shipping &amp; Handling', '9', 0);` |
| `sql/en_US-demo.sql` | 328 | `INSERT INTO `0_chart_master` VALUES ('4440', '', 'Interest', '9', 0);` |
| `sql/en_US-demo.sql` | 329 | `INSERT INTO `0_chart_master` VALUES ('4450', '', 'Foreign Exchange Gain', '9', 0);` |
| `sql/en_US-demo.sql` | 330 | `INSERT INTO `0_chart_master` VALUES ('4500', '', 'Prompt Payment Discounts', '9', 0);` |
| `sql/en_US-demo.sql` | 331 | `INSERT INTO `0_chart_master` VALUES ('4510', '', 'Discounts Given', '9', 0);` |
| `sql/en_US-demo.sql` | 332 | `INSERT INTO `0_chart_master` VALUES ('5010', '', 'Cost of Goods Sold - Retail', '10', 0);` |
| `sql/en_US-demo.sql` | 333 | `INSERT INTO `0_chart_master` VALUES ('5020', '', 'Material Usage Varaiance', '10', 0);` |
| `sql/en_US-demo.sql` | 334 | `INSERT INTO `0_chart_master` VALUES ('5030', '', 'Consumable Materials', '10', 0);` |
| `sql/en_US-demo.sql` | 335 | `INSERT INTO `0_chart_master` VALUES ('5040', '', 'Purchase price Variance', '10', 0);` |
| `sql/en_US-demo.sql` | 336 | `INSERT INTO `0_chart_master` VALUES ('5050', '', 'Purchases of materials', '10', 0);` |
| `sql/en_US-demo.sql` | 337 | `INSERT INTO `0_chart_master` VALUES ('5060', '', 'Discounts Received', '10', 0);` |
| `sql/en_US-demo.sql` | 338 | `INSERT INTO `0_chart_master` VALUES ('5100', '', 'Freight', '10', 0);` |
| `sql/en_US-demo.sql` | 339 | `INSERT INTO `0_chart_master` VALUES ('5410', '', 'Wages &amp; Salaries', '11', 0);` |
| `sql/en_US-demo.sql` | 340 | `INSERT INTO `0_chart_master` VALUES ('5420', '', 'Wages - Overtime', '11', 0);` |
| `sql/en_US-demo.sql` | 341 | `INSERT INTO `0_chart_master` VALUES ('5430', '', 'Benefits - Comp Time', '11', 0);` |
| `sql/en_US-demo.sql` | 342 | `INSERT INTO `0_chart_master` VALUES ('5440', '', 'Benefits - Payroll Taxes', '11', 0);` |
| `sql/en_US-demo.sql` | 343 | `INSERT INTO `0_chart_master` VALUES ('5450', '', 'Benefits - Workers Comp', '11', 0);` |
| `sql/en_US-demo.sql` | 344 | `INSERT INTO `0_chart_master` VALUES ('5460', '', 'Benefits - Pension', '11', 0);` |
| `sql/en_US-demo.sql` | 345 | `INSERT INTO `0_chart_master` VALUES ('5470', '', 'Benefits - General Benefits', '11', 0);` |
| `sql/en_US-demo.sql` | 346 | `INSERT INTO `0_chart_master` VALUES ('5510', '', 'Inc Tax Exp - Federal', '11', 0);` |
| `sql/en_US-demo.sql` | 347 | `INSERT INTO `0_chart_master` VALUES ('5520', '', 'Inc Tax Exp - State', '11', 0);` |
| `sql/en_US-demo.sql` | 348 | `INSERT INTO `0_chart_master` VALUES ('5530', '', 'Taxes - Real Estate', '11', 0);` |
| `sql/en_US-demo.sql` | 349 | `INSERT INTO `0_chart_master` VALUES ('5540', '', 'Taxes - Personal Property', '11', 0);` |
| `sql/en_US-demo.sql` | 350 | `INSERT INTO `0_chart_master` VALUES ('5550', '', 'Taxes - Franchise', '11', 0);` |
| `sql/en_US-demo.sql` | 351 | `INSERT INTO `0_chart_master` VALUES ('5560', '', 'Taxes - Foreign Withholding', '11', 0);` |
| `sql/en_US-demo.sql` | 352 | `INSERT INTO `0_chart_master` VALUES ('5610', '', 'Accounting &amp; Legal', '12', 0);` |
| `sql/en_US-demo.sql` | 353 | `INSERT INTO `0_chart_master` VALUES ('5615', '', 'Advertising &amp; Promotions', '12', 0);` |
| `sql/en_US-demo.sql` | 354 | `INSERT INTO `0_chart_master` VALUES ('5620', '', 'Bad Debts', '12', 0);` |
| `sql/en_US-demo.sql` | 355 | `INSERT INTO `0_chart_master` VALUES ('5660', '', 'Amortization Expense', '12', 0);` |
| `sql/en_US-demo.sql` | 356 | `INSERT INTO `0_chart_master` VALUES ('5685', '', 'Insurance', '12', 0);` |
| `sql/en_US-demo.sql` | 357 | `INSERT INTO `0_chart_master` VALUES ('5690', '', 'Interest &amp; Bank Charges', '12', 0);` |
| `sql/en_US-demo.sql` | 358 | `INSERT INTO `0_chart_master` VALUES ('5700', '', 'Office Supplies', '12', 0);` |
| `sql/en_US-demo.sql` | 359 | `INSERT INTO `0_chart_master` VALUES ('5760', '', 'Rent', '12', 0);` |
| `sql/en_US-demo.sql` | 360 | `INSERT INTO `0_chart_master` VALUES ('5765', '', 'Repair &amp; Maintenance', '12', 0);` |
| `sql/en_US-demo.sql` | 361 | `INSERT INTO `0_chart_master` VALUES ('5780', '', 'Telephone', '12', 0);` |
| `sql/en_US-demo.sql` | 362 | `INSERT INTO `0_chart_master` VALUES ('5785', '', 'Travel &amp; Entertainment', '12', 0);` |
| `sql/en_US-demo.sql` | 363 | `INSERT INTO `0_chart_master` VALUES ('5790', '', 'Utilities', '12', 0);` |
| `sql/en_US-demo.sql` | 364 | `INSERT INTO `0_chart_master` VALUES ('5795', '', 'Registrations', '12', 0);` |
| `sql/en_US-demo.sql` | 365 | `INSERT INTO `0_chart_master` VALUES ('5800', '', 'Licenses', '12', 0);` |
| `sql/en_US-demo.sql` | 366 | `INSERT INTO `0_chart_master` VALUES ('5810', '', 'Foreign Exchange Loss', '12', 0);` |
| `sql/en_US-demo.sql` | 367 | `INSERT INTO `0_chart_master` VALUES ('9990', '', 'Year Profit/Loss', '12', 0);` |
| `sql/en_US-demo.sql` | 375 | `DROP TABLE IF EXISTS `0_chart_types`;` |
| `sql/en_US-demo.sql` | 376 | `CREATE TABLE IF NOT EXISTS `0_chart_types` (` |
| `sql/en_US-demo.sql` | 391 | `INSERT INTO `0_chart_types` VALUES ('1', 'Current Assets', '1', '', 0);` |
| `sql/en_US-demo.sql` | 392 | `INSERT INTO `0_chart_types` VALUES ('2', 'Inventory Assets', '1', '', 0);` |
| `sql/en_US-demo.sql` | 393 | `INSERT INTO `0_chart_types` VALUES ('3', 'Capital Assets', '1', '', 0);` |
| `sql/en_US-demo.sql` | 394 | `INSERT INTO `0_chart_types` VALUES ('4', 'Current Liabilities', '2', '', 0);` |
| `sql/en_US-demo.sql` | 395 | `INSERT INTO `0_chart_types` VALUES ('5', 'Long Term Liabilities', '2', '', 0);` |
| `sql/en_US-demo.sql` | 396 | `INSERT INTO `0_chart_types` VALUES ('6', 'Share Capital', '2', '', 0);` |
| `sql/en_US-demo.sql` | 397 | `INSERT INTO `0_chart_types` VALUES ('7', 'Retained Earnings', '2', '', 0);` |
| `sql/en_US-demo.sql` | 398 | `INSERT INTO `0_chart_types` VALUES ('8', 'Sales Revenue', '3', '', 0);` |
| `sql/en_US-demo.sql` | 399 | `INSERT INTO `0_chart_types` VALUES ('9', 'Other Revenue', '3', '', 0);` |
| `sql/en_US-demo.sql` | 400 | `INSERT INTO `0_chart_types` VALUES ('10', 'Cost of Goods Sold', '4', '', 0);` |
| `sql/en_US-demo.sql` | 401 | `INSERT INTO `0_chart_types` VALUES ('11', 'Payroll Expenses', '4', '', 0);` |
| `sql/en_US-demo.sql` | 402 | `INSERT INTO `0_chart_types` VALUES ('12', 'General &amp; Administrative expenses', '4', '', 0);` |
| `sql/en_US-demo.sql` | 410 | `DROP TABLE IF EXISTS `0_comments`;` |
| `sql/en_US-demo.sql` | 411 | `CREATE TABLE IF NOT EXISTS `0_comments` (` |
| `sql/en_US-demo.sql` | 423 | `INSERT INTO `0_comments` VALUES` |
| `sql/en_US-demo.sql` | 436 | `DROP TABLE IF EXISTS `0_credit_status`;` |
| `sql/en_US-demo.sql` | 437 | `CREATE TABLE IF NOT EXISTS `0_credit_status` (` |
| `sql/en_US-demo.sql` | 450 | `INSERT INTO `0_credit_status` VALUES (1, 'Good History', 0, 0);` |
| `sql/en_US-demo.sql` | 451 | `INSERT INTO `0_credit_status` VALUES (3, 'No more work until payment received', 1, 0);` |
| `sql/en_US-demo.sql` | 452 | `INSERT INTO `0_credit_status` VALUES (4, 'In liquidation', 1, 0);` |
| `sql/en_US-demo.sql` | 460 | `DROP TABLE IF EXISTS `0_crm_categories`;` |
| `sql/en_US-demo.sql` | 461 | `CREATE TABLE IF NOT EXISTS `0_crm_categories` (` |
| `sql/en_US-demo.sql` | 478 | `INSERT INTO `0_crm_categories` VALUES (1, 'cust_branch', 'general', 'General', 'General contact data for customer branch (overrides company setting)', 1, 0);` |
| `sql/en_US-demo.sql` | 479 | `INSERT INTO `0_crm_categories` VALUES (2, 'cust_branch', 'invoice', 'Invoices', 'Invoice posting (overrides company setting)', 1, 0);` |
| `sql/en_US-demo.sql` | 480 | `INSERT INTO `0_crm_categories` VALUES (3, 'cust_branch', 'order', 'Orders', 'Order confirmation (overrides company setting)', 1, 0);` |
| `sql/en_US-demo.sql` | 481 | `INSERT INTO `0_crm_categories` VALUES (4, 'cust_branch', 'delivery', 'Deliveries', 'Delivery coordination (overrides company setting)', 1, 0);` |
| `sql/en_US-demo.sql` | 482 | `INSERT INTO `0_crm_categories` VALUES (5, 'customer', 'general', 'General', 'General contact data for customer', 1, 0);` |
| `sql/en_US-demo.sql` | 483 | `INSERT INTO `0_crm_categories` VALUES (6, 'customer', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/en_US-demo.sql` | 484 | `INSERT INTO `0_crm_categories` VALUES (7, 'customer', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/en_US-demo.sql` | 485 | `INSERT INTO `0_crm_categories` VALUES (8, 'customer', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/en_US-demo.sql` | 486 | `INSERT INTO `0_crm_categories` VALUES (9, 'supplier', 'general', 'General', 'General contact data for supplier', 1, 0);` |
| `sql/en_US-demo.sql` | 487 | `INSERT INTO `0_crm_categories` VALUES (10, 'supplier', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/en_US-demo.sql` | 488 | `INSERT INTO `0_crm_categories` VALUES (11, 'supplier', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/en_US-demo.sql` | 489 | `INSERT INTO `0_crm_categories` VALUES (12, 'supplier', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/en_US-demo.sql` | 497 | `DROP TABLE IF EXISTS `0_crm_contacts`;` |
| `sql/en_US-demo.sql` | 498 | `CREATE TABLE IF NOT EXISTS `0_crm_contacts` (` |
| `sql/en_US-demo.sql` | 512 | `INSERT INTO `0_crm_contacts` VALUES` |
| `sql/en_US-demo.sql` | 526 | `DROP TABLE IF EXISTS `0_crm_persons`;` |
| `sql/en_US-demo.sql` | 527 | `CREATE TABLE IF NOT EXISTS `0_crm_persons` (` |
| `sql/en_US-demo.sql` | 548 | `INSERT INTO `0_crm_persons` VALUES` |
| `sql/en_US-demo.sql` | 560 | `DROP TABLE IF EXISTS `0_currencies`;` |
| `sql/en_US-demo.sql` | 561 | `CREATE TABLE IF NOT EXISTS `0_currencies` (` |
| `sql/en_US-demo.sql` | 576 | `INSERT INTO `0_currencies` VALUES ('US Dollars', 'USD', '$', 'United States', 'Cents', 1, 0);` |
| `sql/en_US-demo.sql` | 577 | `INSERT INTO `0_currencies` VALUES ('CA Dollars', 'CAD', '$', 'Canada', 'Cents', 1, 0);` |
| `sql/en_US-demo.sql` | 578 | `INSERT INTO `0_currencies` VALUES ('Euro', 'EUR', '€', 'Europe', 'Cents', 1, 0);` |
| `sql/en_US-demo.sql` | 579 | `INSERT INTO `0_currencies` VALUES ('Pounds', 'GBP', '£', 'England', 'Pence', 1, 0);` |
| `sql/en_US-demo.sql` | 587 | `DROP TABLE IF EXISTS `0_cust_allocations`;` |
| `sql/en_US-demo.sql` | 588 | `CREATE TABLE IF NOT EXISTS `0_cust_allocations` (` |
| `sql/en_US-demo.sql` | 599 | `KEY `From` (`trans_type_from`,`trans_no_from`),` |
| `sql/en_US-demo.sql` | 607 | `INSERT INTO `0_cust_allocations` VALUES` |
| `sql/en_US-demo.sql` | 618 | `DROP TABLE IF EXISTS `0_cust_branch`;` |
| `sql/en_US-demo.sql` | 619 | `CREATE TABLE IF NOT EXISTS `0_cust_branch` (` |
| `sql/en_US-demo.sql` | 648 | `INSERT INTO `0_cust_branch` VALUES` |
| `sql/en_US-demo.sql` | 658 | `DROP TABLE IF EXISTS `0_debtors_master`;` |
| `sql/en_US-demo.sql` | 659 | `CREATE TABLE IF NOT EXISTS `0_debtors_master` (` |
| `sql/en_US-demo.sql` | 686 | `INSERT INTO `0_debtors_master` VALUES` |
| `sql/en_US-demo.sql` | 696 | `DROP TABLE IF EXISTS `0_debtor_trans`;` |
| `sql/en_US-demo.sql` | 697 | `CREATE TABLE IF NOT EXISTS `0_debtor_trans` (` |
| `sql/en_US-demo.sql` | 732 | `INSERT INTO `0_debtor_trans` VALUES` |
| `sql/en_US-demo.sql` | 751 | `DROP TABLE IF EXISTS `0_debtor_trans_details`;` |
| `sql/en_US-demo.sql` | 752 | `CREATE TABLE IF NOT EXISTS `0_debtor_trans_details` (` |
| `sql/en_US-demo.sql` | 774 | `INSERT INTO `0_debtor_trans_details` VALUES` |
| `sql/en_US-demo.sql` | 794 | `DROP TABLE IF EXISTS `0_dimensions`;` |
| `sql/en_US-demo.sql` | 795 | `CREATE TABLE IF NOT EXISTS `0_dimensions` (` |
| `sql/en_US-demo.sql` | 814 | `INSERT INTO `0_dimensions` VALUES ('1', '001/2016', 'Cost Centre', '1', '0', '2016-05-05', '2016-05-25');` |
| `sql/en_US-demo.sql` | 822 | `DROP TABLE IF EXISTS `0_exchange_rates`;` |
| `sql/en_US-demo.sql` | 823 | `CREATE TABLE IF NOT EXISTS `0_exchange_rates` (` |
| `sql/en_US-demo.sql` | 837 | `INSERT INTO `0_exchange_rates` VALUES ('1', 'EUR', '1.123', '1.123', '2016-05-07');` |
| `sql/en_US-demo.sql` | 845 | `DROP TABLE IF EXISTS `0_fiscal_year`;` |
| `sql/en_US-demo.sql` | 846 | `CREATE TABLE IF NOT EXISTS `0_fiscal_year` (` |
| `sql/en_US-demo.sql` | 860 | `INSERT INTO `0_fiscal_year` VALUES (1, '2016-01-01', '2016-12-31', 0);` |
| `sql/en_US-demo.sql` | 868 | `DROP TABLE IF EXISTS `0_gl_trans`;` |
| `sql/en_US-demo.sql` | 869 | `CREATE TABLE IF NOT EXISTS `0_gl_trans` (` |
| `sql/en_US-demo.sql` | 893 | `INSERT INTO `0_gl_trans` VALUES` |
| `sql/en_US-demo.sql` | 939 | `DROP TABLE IF EXISTS `0_grn_batch`;` |
| `sql/en_US-demo.sql` | 940 | `CREATE TABLE IF NOT EXISTS `0_grn_batch` (` |
| `sql/en_US-demo.sql` | 957 | `INSERT INTO `0_grn_batch` VALUES` |
| `sql/en_US-demo.sql` | 967 | `DROP TABLE IF EXISTS `0_grn_items`;` |
| `sql/en_US-demo.sql` | 968 | `CREATE TABLE IF NOT EXISTS `0_grn_items` (` |
| `sql/en_US-demo.sql` | 984 | `INSERT INTO `0_grn_items` VALUES` |
| `sql/en_US-demo.sql` | 996 | `DROP TABLE IF EXISTS `0_groups`;` |
| `sql/en_US-demo.sql` | 997 | `CREATE TABLE IF NOT EXISTS `0_groups` (` |
| `sql/en_US-demo.sql` | 1009 | `INSERT INTO `0_groups` VALUES (1, 'Small', 0);` |
| `sql/en_US-demo.sql` | 1010 | `INSERT INTO `0_groups` VALUES (2, 'Medium', 0);` |
| `sql/en_US-demo.sql` | 1011 | `INSERT INTO `0_groups` VALUES (3, 'Large', 0);` |
| `sql/en_US-demo.sql` | 1019 | `DROP TABLE IF EXISTS `0_item_codes`;` |
| `sql/en_US-demo.sql` | 1020 | `CREATE TABLE IF NOT EXISTS `0_item_codes` (` |
| `sql/en_US-demo.sql` | 1038 | `INSERT INTO `0_item_codes` VALUES` |
| `sql/en_US-demo.sql` | 1054 | `DROP TABLE IF EXISTS `0_item_tax_types`;` |
| `sql/en_US-demo.sql` | 1055 | `CREATE TABLE IF NOT EXISTS `0_item_tax_types` (` |
| `sql/en_US-demo.sql` | 1068 | `INSERT INTO `0_item_tax_types` VALUES (1, 'Regular', 0, 0);` |
| `sql/en_US-demo.sql` | 1076 | `DROP TABLE IF EXISTS `0_item_tax_type_exemptions`;` |
| `sql/en_US-demo.sql` | 1077 | `CREATE TABLE IF NOT EXISTS `0_item_tax_type_exemptions` (` |
| `sql/en_US-demo.sql` | 1093 | `DROP TABLE IF EXISTS `0_item_units`;` |
| `sql/en_US-demo.sql` | 1094 | `CREATE TABLE IF NOT EXISTS `0_item_units` (` |
| `sql/en_US-demo.sql` | 1107 | `INSERT INTO `0_item_units` VALUES ('each', 'Each', 0, 0);` |
| `sql/en_US-demo.sql` | 1108 | `INSERT INTO `0_item_units` VALUES ('hr', 'Hours', 0, 0);` |
| `sql/en_US-demo.sql` | 1116 | `DROP TABLE IF EXISTS `0_journal`;` |
| `sql/en_US-demo.sql` | 1117 | `CREATE TABLE `0_journal` (` |
| `sql/en_US-demo.sql` | 1142 | `DROP TABLE IF EXISTS `0_locations`;` |
| `sql/en_US-demo.sql` | 1143 | `CREATE TABLE IF NOT EXISTS `0_locations` (` |
| `sql/en_US-demo.sql` | 1161 | `INSERT INTO `0_locations` VALUES ('DEF', 'Default', 'N/A', '', '', '', '', '', 0, 0);` |
| `sql/en_US-demo.sql` | 1169 | `DROP TABLE IF EXISTS `0_loc_stock`;` |
| `sql/en_US-demo.sql` | 1170 | `CREATE TABLE IF NOT EXISTS `0_loc_stock` (` |
| `sql/en_US-demo.sql` | 1182 | `INSERT INTO `0_loc_stock` VALUES` |
| `sql/en_US-demo.sql` | 1196 | `DROP TABLE IF EXISTS `0_payment_terms`;` |
| `sql/en_US-demo.sql` | 1197 | `CREATE TABLE IF NOT EXISTS `0_payment_terms` (` |
| `sql/en_US-demo.sql` | 1211 | `INSERT INTO `0_payment_terms` VALUES (1, 'Due 15th Of the Following Month', 0, 17, 0);` |
| `sql/en_US-demo.sql` | 1212 | `INSERT INTO `0_payment_terms` VALUES (2, 'Due By End Of The Following Month', 0, 30, 0);` |
| `sql/en_US-demo.sql` | 1213 | `INSERT INTO `0_payment_terms` VALUES (3, 'Payment due within 10 days', 10, 0, 0);` |
| `sql/en_US-demo.sql` | 1214 | `INSERT INTO `0_payment_terms` VALUES (4, 'Cash Only', 0, 0, 0);` |
| `sql/en_US-demo.sql` | 1222 | `DROP TABLE IF EXISTS `0_prices`;` |
| `sql/en_US-demo.sql` | 1223 | `CREATE TABLE IF NOT EXISTS `0_prices` (` |
| `sql/en_US-demo.sql` | 1237 | `INSERT INTO `0_prices` VALUES` |
| `sql/en_US-demo.sql` | 1248 | `DROP TABLE IF EXISTS `0_printers`;` |
| `sql/en_US-demo.sql` | 1249 | `CREATE TABLE IF NOT EXISTS `0_printers` (` |
| `sql/en_US-demo.sql` | 1265 | `INSERT INTO `0_printers` VALUES (1, 'QL500', 'Label printer', 'QL500', 'server', 127, 20);` |
| `sql/en_US-demo.sql` | 1266 | `INSERT INTO `0_printers` VALUES (2, 'Samsung', 'Main network printer', 'scx4521F', 'server', 515, 5);` |
| `sql/en_US-demo.sql` | 1267 | `INSERT INTO `0_printers` VALUES (3, 'Local', 'Local print server at user IP', 'lp', '', 515, 10);` |
| `sql/en_US-demo.sql` | 1275 | `DROP TABLE IF EXISTS `0_print_profiles`;` |
| `sql/en_US-demo.sql` | 1276 | `CREATE TABLE IF NOT EXISTS `0_print_profiles` (` |
| `sql/en_US-demo.sql` | 1289 | `INSERT INTO `0_print_profiles` VALUES (1, 'Out of office', '', 0);` |
| `sql/en_US-demo.sql` | 1290 | `INSERT INTO `0_print_profiles` VALUES (2, 'Sales Department', '', 0);` |
| `sql/en_US-demo.sql` | 1291 | `INSERT INTO `0_print_profiles` VALUES (3, 'Central', '', 2);` |
| `sql/en_US-demo.sql` | 1292 | `INSERT INTO `0_print_profiles` VALUES (4, 'Sales Department', '104', 2);` |
| `sql/en_US-demo.sql` | 1293 | `INSERT INTO `0_print_profiles` VALUES (5, 'Sales Department', '105', 2);` |
| `sql/en_US-demo.sql` | 1294 | `INSERT INTO `0_print_profiles` VALUES (6, 'Sales Department', '107', 2);` |
| `sql/en_US-demo.sql` | 1295 | `INSERT INTO `0_print_profiles` VALUES (7, 'Sales Department', '109', 2);` |
| `sql/en_US-demo.sql` | 1296 | `INSERT INTO `0_print_profiles` VALUES (8, 'Sales Department', '110', 2);` |
| `sql/en_US-demo.sql` | 1297 | `INSERT INTO `0_print_profiles` VALUES (9, 'Sales Department', '201', 2);` |
| `sql/en_US-demo.sql` | 1305 | `DROP TABLE IF EXISTS `0_purch_data`;` |
| `sql/en_US-demo.sql` | 1306 | `CREATE TABLE IF NOT EXISTS `0_purch_data` (` |
| `sql/en_US-demo.sql` | 1320 | `INSERT INTO `0_purch_data` VALUES` |
| `sql/en_US-demo.sql` | 1331 | `DROP TABLE IF EXISTS `0_purch_orders`;` |
| `sql/en_US-demo.sql` | 1332 | `CREATE TABLE IF NOT EXISTS `0_purch_orders` (` |
| `sql/en_US-demo.sql` | 1353 | `INSERT INTO `0_purch_orders` VALUES` |
| `sql/en_US-demo.sql` | 1363 | `DROP TABLE IF EXISTS `0_purch_order_details`;` |
| `sql/en_US-demo.sql` | 1364 | `CREATE TABLE IF NOT EXISTS `0_purch_order_details` (` |
| `sql/en_US-demo.sql` | 1385 | `INSERT INTO `0_purch_order_details` VALUES` |
| `sql/en_US-demo.sql` | 1397 | `DROP TABLE IF EXISTS `0_quick_entries`;` |
| `sql/en_US-demo.sql` | 1398 | `CREATE TABLE IF NOT EXISTS `0_quick_entries` (` |
| `sql/en_US-demo.sql` | 1414 | `INSERT INTO `0_quick_entries` VALUES (1, 1, 'Maintenance', NULL, 0, 'Amount', 0);` |
| `sql/en_US-demo.sql` | 1415 | `INSERT INTO `0_quick_entries` VALUES (2, 4, 'Phone', NULL, 0, 'Amount', 0);` |
| `sql/en_US-demo.sql` | 1416 | `INSERT INTO `0_quick_entries` VALUES (3, 2, 'Cash Sales', 'Retail sales without invoice', 0, 'Amount', 0);` |
| `sql/en_US-demo.sql` | 1424 | `DROP TABLE IF EXISTS `0_quick_entry_lines`;` |
| `sql/en_US-demo.sql` | 1425 | `CREATE TABLE IF NOT EXISTS `0_quick_entry_lines` (` |
| `sql/en_US-demo.sql` | 1442 | `INSERT INTO `0_quick_entry_lines` VALUES (1, 1, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-demo.sql` | 1443 | `INSERT INTO `0_quick_entry_lines` VALUES (2, 2, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-demo.sql` | 1444 | `INSERT INTO `0_quick_entry_lines` VALUES (3, 3, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-demo.sql` | 1445 | `INSERT INTO `0_quick_entry_lines` VALUES (4, 3, 0, '', '=', '4010', 0, 0);` |
| `sql/en_US-demo.sql` | 1446 | `INSERT INTO `0_quick_entry_lines` VALUES (5, 1, 0, '', '=', '5765', 0, 0);` |
| `sql/en_US-demo.sql` | 1447 | `INSERT INTO `0_quick_entry_lines` VALUES (6, 2, 0, '', '=', '5780', 0, 0);` |
| `sql/en_US-demo.sql` | 1455 | `DROP TABLE IF EXISTS `0_recurrent_invoices`;` |
| `sql/en_US-demo.sql` | 1456 | `CREATE TABLE IF NOT EXISTS `0_recurrent_invoices` (` |
| `sql/en_US-demo.sql` | 1475 | `INSERT INTO `0_recurrent_invoices` VALUES ('1', 'Weekly Maintenance', '6', '1', '1', '7', '0', '2016-04-01', '2020-05-07', '2016-04-08');` |
| `sql/en_US-demo.sql` | 1483 | `DROP TABLE IF EXISTS `0_reflines`;` |
| `sql/en_US-demo.sql` | 1485 | `CREATE TABLE `0_reflines` (` |
| `sql/en_US-demo.sql` | 1501 | `INSERT INTO `0_reflines` VALUES` |
| `sql/en_US-demo.sql` | 1531 | `DROP TABLE IF EXISTS `0_refs`;` |
| `sql/en_US-demo.sql` | 1532 | `CREATE TABLE IF NOT EXISTS `0_refs` (` |
| `sql/en_US-demo.sql` | 1544 | `INSERT INTO `0_refs` VALUES` |
| `sql/en_US-demo.sql` | 1570 | `DROP TABLE IF EXISTS `0_salesman`;` |
| `sql/en_US-demo.sql` | 1571 | `CREATE TABLE IF NOT EXISTS `0_salesman` (` |
| `sql/en_US-demo.sql` | 1589 | `INSERT INTO `0_salesman` VALUES (1, 'Sales Person', '', '', '', 5, 1000, 4, 0);` |
| `sql/en_US-demo.sql` | 1597 | `DROP TABLE IF EXISTS `0_sales_orders`;` |
| `sql/en_US-demo.sql` | 1598 | `CREATE TABLE IF NOT EXISTS `0_sales_orders` (` |
| `sql/en_US-demo.sql` | 1629 | `INSERT INTO `0_sales_orders` VALUES` |
| `sql/en_US-demo.sql` | 1644 | `DROP TABLE IF EXISTS `0_sales_order_details`;` |
| `sql/en_US-demo.sql` | 1645 | `CREATE TABLE IF NOT EXISTS `0_sales_order_details` (` |
| `sql/en_US-demo.sql` | 1665 | `INSERT INTO `0_sales_order_details` VALUES` |
| `sql/en_US-demo.sql` | 1683 | `DROP TABLE IF EXISTS `0_sales_pos`;` |
| `sql/en_US-demo.sql` | 1684 | `CREATE TABLE IF NOT EXISTS `0_sales_pos` (` |
| `sql/en_US-demo.sql` | 1700 | `INSERT INTO `0_sales_pos` VALUES (1, 'Default', 1, 1, 'DEF', 2, 0);` |
| `sql/en_US-demo.sql` | 1708 | `DROP TABLE IF EXISTS `0_sales_types`;` |
| `sql/en_US-demo.sql` | 1709 | `CREATE TABLE IF NOT EXISTS `0_sales_types` (` |
| `sql/en_US-demo.sql` | 1723 | `INSERT INTO `0_sales_types` VALUES (1, 'Retail', 1, 1, 0);` |
| `sql/en_US-demo.sql` | 1724 | `INSERT INTO `0_sales_types` VALUES (2, 'Wholesale', 0, 0.7, 0);` |
| `sql/en_US-demo.sql` | 1732 | `DROP TABLE IF EXISTS `0_security_roles`;` |
| `sql/en_US-demo.sql` | 1733 | `CREATE TABLE IF NOT EXISTS `0_security_roles` (` |
| `sql/en_US-demo.sql` | 1748 | `INSERT INTO `0_security_roles` VALUES (1, 'Inquiries', 'Inquiries', '768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15872;16128', '257;258;259;260;513;514;515;516;517;518;519;520;521;522;523;524;525;773;774;2822;3073;3075;3076;3077;3329;3330;3331;3332;3333;3334;3335;5377;5633;5640;5889;5890;5891;7937;7938;7939;7940;8193;8194;8450;8451;104` |
| `sql/en_US-demo.sql` | 1749 | `INSERT INTO `0_security_roles` VALUES (2, 'System Administrator', 'System Administrator', '256;512;768;2816;3072;3328;5376;5632;5888;7936;8192;8448;9472;9728;10496;10752;11008;13056;13312;15616;15872;16128', '257;258;259;260;513;514;515;516;517;518;519;520;521;522;523;524;525;526;769;770;771;772;773;774;2817;2818;2819;2820;2821;2822;2823;3073;3074;` |
| `sql/en_US-demo.sql` | 1750 | `INSERT INTO `0_security_roles` VALUES (3, 'Salesman', 'Salesman', '768;3072;5632;8192;15872', '773;774;3073;3075;3081;5633;8194;15873;775', 0);` |
| `sql/en_US-demo.sql` | 1751 | `INSERT INTO `0_security_roles` VALUES (4, 'Stock Manager', 'Stock Manager', '768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15872;16128', '2818;2822;3073;3076;3077;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5640;5889;5890;5891;8193;8194;8450;8451;10753;11009;11010;11012;13313;13315;15882;16129;16130;16131;16132;775', 0);` |
| `sql/en_US-demo.sql` | 1752 | `INSERT INTO `0_security_roles` VALUES (5, 'Production Manager', 'Production Manager', '512;768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;2818;2819;2820;2821;2822;2823;3073;3074;3076;3077;3078;3079;3080;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5640;5640;5889;5890;5891;8193;8194;8196;8197` |
| `sql/en_US-demo.sql` | 1753 | `INSERT INTO `0_security_roles` VALUES (6, 'Purchase Officer', 'Purchase Officer', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;2818;2819;2820;2821;2822;2823;3073;3074;3076;3077;3078;3079;3080;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5377;5633;5635;5640;5640;5889;5890;5891;8193;819` |
| `sql/en_US-demo.sql` | 1754 | `INSERT INTO `0_security_roles` VALUES (7, 'AR Officer', 'AR Officer', '512;768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;771;773;774;2818;2819;2820;2821;2822;2823;3073;3073;3074;3075;3076;3077;3078;3079;3080;3081;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5633;5634;5637;5638;5639;5640;564` |
| `sql/en_US-demo.sql` | 1755 | `INSERT INTO `0_security_roles` VALUES (8, 'AP Officer', 'AP Officer', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;769;770;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3082;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5635;5640;5889;5890;` |
| `sql/en_US-demo.sql` | 1756 | `INSERT INTO `0_security_roles` VALUES (9, 'Accountant', 'New Accountant', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3075;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5634;5635;5637;5638;5639` |
| `sql/en_US-demo.sql` | 1757 | `INSERT INTO `0_security_roles` VALUES (10, 'Sub Admin', 'Sub Admin', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3082;3075;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5634;5635;5637;5638;5639` |
| `sql/en_US-demo.sql` | 1765 | `DROP TABLE IF EXISTS `0_shippers`;` |
| `sql/en_US-demo.sql` | 1766 | `CREATE TABLE IF NOT EXISTS `0_shippers` (` |
| `sql/en_US-demo.sql` | 1782 | `INSERT INTO `0_shippers` VALUES (1, 'Default', '', '', '', '', 0);` |
| `sql/en_US-demo.sql` | 1790 | `DROP TABLE IF EXISTS `0_sql_trail`;` |
| `sql/en_US-demo.sql` | 1791 | `CREATE TABLE IF NOT EXISTS `0_sql_trail` (` |
| `sql/en_US-demo.sql` | 1809 | `DROP TABLE IF EXISTS `0_stock_category`;` |
| `sql/en_US-demo.sql` | 1810 | `CREATE TABLE IF NOT EXISTS `0_stock_category` (` |
| `sql/en_US-demo.sql` | 1834 | `INSERT INTO `0_stock_category` VALUES (1, 'Components', 1, 'each', 'B', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-demo.sql` | 1835 | `INSERT INTO `0_stock_category` VALUES (2, 'Charges', 1, 'each', 'D', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-demo.sql` | 1836 | `INSERT INTO `0_stock_category` VALUES (3, 'Systems', 1, 'each', 'M', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-demo.sql` | 1837 | `INSERT INTO `0_stock_category` VALUES (4, 'Services', 1, 'hr', 'D', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-demo.sql` | 1845 | `DROP TABLE IF EXISTS `0_stock_fa_class`;` |
| `sql/en_US-demo.sql` | 1846 | `CREATE TABLE `0_stock_fa_class` (` |
| `sql/en_US-demo.sql` | 1862 | `DROP TABLE IF EXISTS `0_stock_master`;` |
| `sql/en_US-demo.sql` | 1863 | `CREATE TABLE IF NOT EXISTS `0_stock_master` (` |
| `sql/en_US-demo.sql` | 1899 | `INSERT INTO `0_stock_master` VALUES` |
| `sql/en_US-demo.sql` | 1913 | `DROP TABLE IF EXISTS `0_stock_moves`;` |
| `sql/en_US-demo.sql` | 1914 | `CREATE TABLE `0_stock_moves` (` |
| `sql/en_US-demo.sql` | 1934 | `INSERT INTO `0_stock_moves` VALUES` |
| `sql/en_US-demo.sql` | 1957 | `DROP TABLE IF EXISTS `0_suppliers`;` |
| `sql/en_US-demo.sql` | 1958 | `CREATE TABLE IF NOT EXISTS `0_suppliers` (` |
| `sql/en_US-demo.sql` | 1989 | `INSERT INTO `0_suppliers` VALUES` |
| `sql/en_US-demo.sql` | 1999 | `DROP TABLE IF EXISTS `0_supp_allocations`;` |
| `sql/en_US-demo.sql` | 2000 | `CREATE TABLE IF NOT EXISTS `0_supp_allocations` (` |
| `sql/en_US-demo.sql` | 2011 | `KEY `From` (`trans_type_from`,`trans_no_from`),` |
| `sql/en_US-demo.sql` | 2025 | `DROP TABLE IF EXISTS `0_supp_invoice_items`;` |
| `sql/en_US-demo.sql` | 2026 | `CREATE TABLE IF NOT EXISTS `0_supp_invoice_items` (` |
| `sql/en_US-demo.sql` | 2049 | `INSERT INTO `0_supp_invoice_items` VALUES ('1', '1', '20', '0', '4', '4', '101', 'iPad Air 2 16GB', '15', '200', '10', NULL, '0', '0');` |
| `sql/en_US-demo.sql` | 2057 | `DROP TABLE IF EXISTS `0_supp_trans`;` |
| `sql/en_US-demo.sql` | 2058 | `CREATE TABLE IF NOT EXISTS `0_supp_trans` (` |
| `sql/en_US-demo.sql` | 2082 | `INSERT INTO `0_supp_trans` VALUES ('1', '20', '1', '001/2016', 'rr4', '2016-05-05', '2016-05-15', '3000', '0', '150', '1', '0', '0');` |
| `sql/en_US-demo.sql` | 2090 | `DROP TABLE IF EXISTS `0_sys_prefs`;` |
| `sql/en_US-demo.sql` | 2091 | `CREATE TABLE IF NOT EXISTS `0_sys_prefs` (` |
| `sql/en_US-demo.sql` | 2105 | `INSERT INTO `0_sys_prefs` VALUES ('coy_name', 'setup.company', 'varchar', 60, 'Training Co');` |
| `sql/en_US-demo.sql` | 2106 | `INSERT INTO `0_sys_prefs` VALUES ('gst_no', 'setup.company', 'varchar', 25, '33445566');` |
| `sql/en_US-demo.sql` | 2107 | `INSERT INTO `0_sys_prefs` VALUES ('coy_no', 'setup.company', 'varchar', 25, '');` |
| `sql/en_US-demo.sql` | 2108 | `INSERT INTO `0_sys_prefs` VALUES ('tax_prd', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-demo.sql` | 2109 | `INSERT INTO `0_sys_prefs` VALUES ('tax_last', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-demo.sql` | 2110 | `INSERT INTO `0_sys_prefs` VALUES ('postal_address', 'setup.company', 'tinytext', 0, 'N/A');` |
| `sql/en_US-demo.sql` | 2111 | `INSERT INTO `0_sys_prefs` VALUES ('phone', 'setup.company', 'varchar', 30, '');` |
| `sql/en_US-demo.sql` | 2112 | `INSERT INTO `0_sys_prefs` VALUES ('fax', 'setup.company', 'varchar', 30, '');` |
| `sql/en_US-demo.sql` | 2113 | `INSERT INTO `0_sys_prefs` VALUES ('email', 'setup.company', 'varchar', 100, 'delta@delta.com');` |
| `sql/en_US-demo.sql` | 2114 | `INSERT INTO `0_sys_prefs` VALUES ('coy_logo', 'setup.company', 'varchar', 100, 'logo_frontaccounting.jpg');` |
| `sql/en_US-demo.sql` | 2115 | `INSERT INTO `0_sys_prefs` VALUES ('domicile', 'setup.company', 'varchar', 55, '');` |
| `sql/en_US-demo.sql` | 2116 | `INSERT INTO `0_sys_prefs` VALUES ('curr_default', 'setup.company', 'char', 3, 'USD');` |
| `sql/en_US-demo.sql` | 2117 | `INSERT INTO `0_sys_prefs` VALUES ('use_dimension', 'setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2118 | `INSERT INTO `0_sys_prefs` VALUES ('f_year', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-demo.sql` | 2119 | `INSERT INTO `0_sys_prefs` VALUES ('shortname_name_in_list','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2120 | `INSERT INTO `0_sys_prefs` VALUES ('no_item_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2121 | `INSERT INTO `0_sys_prefs` VALUES ('no_customer_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2122 | `INSERT INTO `0_sys_prefs` VALUES ('no_supplier_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2123 | `INSERT INTO `0_sys_prefs` VALUES ('base_sales', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-demo.sql` | 2124 | `INSERT INTO `0_sys_prefs` VALUES ('time_zone', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2125 | `INSERT INTO `0_sys_prefs` VALUES ('add_pct', 'setup.company', 'int', 5, '-1');` |
| `sql/en_US-demo.sql` | 2126 | `INSERT INTO `0_sys_prefs` VALUES ('round_to', 'setup.company', 'int', 5, '1');` |
| `sql/en_US-demo.sql` | 2127 | `INSERT INTO `0_sys_prefs` VALUES ('login_tout', 'setup.company', 'smallint', 6, '600');` |
| `sql/en_US-demo.sql` | 2128 | `INSERT INTO `0_sys_prefs` VALUES ('past_due_days', 'glsetup.general', 'int', 11, '30');` |
| `sql/en_US-demo.sql` | 2129 | `INSERT INTO `0_sys_prefs` VALUES ('profit_loss_year_act', 'glsetup.general', 'varchar', 15, '9990');` |
| `sql/en_US-demo.sql` | 2130 | `INSERT INTO `0_sys_prefs` VALUES ('retained_earnings_act', 'glsetup.general', 'varchar', 15, '3590');` |
| `sql/en_US-demo.sql` | 2131 | `INSERT INTO `0_sys_prefs` VALUES ('bank_charge_act', 'glsetup.general', 'varchar', 15, '5690');` |
| `sql/en_US-demo.sql` | 2132 | `INSERT INTO `0_sys_prefs` VALUES ('exchange_diff_act', 'glsetup.general', 'varchar', 15, '4450');` |
| `sql/en_US-demo.sql` | 2133 | `INSERT INTO `0_sys_prefs` VALUES ('tax_algorithm', 'glsetup.customer', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2134 | `INSERT INTO `0_sys_prefs` VALUES ('default_credit_limit', 'glsetup.customer', 'int', 11, '1000');` |
| `sql/en_US-demo.sql` | 2135 | `INSERT INTO `0_sys_prefs` VALUES ('accumulate_shipping', 'glsetup.customer', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2136 | `INSERT INTO `0_sys_prefs` VALUES ('legal_text', 'glsetup.customer', 'tinytext', 0, '');` |
| `sql/en_US-demo.sql` | 2137 | `INSERT INTO `0_sys_prefs` VALUES ('freight_act', 'glsetup.customer', 'varchar', 15, '4430');` |
| `sql/en_US-demo.sql` | 2138 | `INSERT INTO `0_sys_prefs` VALUES ('debtors_act', 'glsetup.sales', 'varchar', 15, '1200');` |
| `sql/en_US-demo.sql` | 2139 | `INSERT INTO `0_sys_prefs` VALUES ('default_sales_act', 'glsetup.sales', 'varchar', 15, '4010');` |
| `sql/en_US-demo.sql` | 2140 | `INSERT INTO `0_sys_prefs` VALUES ('default_sales_discount_act', 'glsetup.sales', 'varchar', 15, '4510');` |
| `sql/en_US-demo.sql` | 2141 | `INSERT INTO `0_sys_prefs` VALUES ('default_prompt_payment_act', 'glsetup.sales', 'varchar', 15, '4500');` |
| `sql/en_US-demo.sql` | 2142 | `INSERT INTO `0_sys_prefs` VALUES ('default_delivery_required', 'glsetup.sales', 'smallint', 6, '1');` |
| `sql/en_US-demo.sql` | 2143 | `INSERT INTO `0_sys_prefs` VALUES ('default_receival_required', 'glsetup.purchase', 'smallint', 6, '10');` |
| `sql/en_US-demo.sql` | 2144 | `INSERT INTO `0_sys_prefs` VALUES ('default_quote_valid_days', 'glsetup.sales', 'smallint', 6, '30');` |
| `sql/en_US-demo.sql` | 2145 | `INSERT INTO `0_sys_prefs` VALUES ('default_dim_required', 'glsetup.dims', 'int', 11, '20');` |
| `sql/en_US-demo.sql` | 2146 | `INSERT INTO `0_sys_prefs` VALUES ('pyt_discount_act', 'glsetup.purchase', 'varchar', 15, '5060');` |
| `sql/en_US-demo.sql` | 2147 | `INSERT INTO `0_sys_prefs` VALUES ('creditors_act', 'glsetup.purchase', 'varchar', 15, '2100');` |
| `sql/en_US-demo.sql` | 2148 | `INSERT INTO `0_sys_prefs` VALUES ('po_over_receive', 'glsetup.purchase', 'int', 11, '10');` |
| `sql/en_US-demo.sql` | 2149 | `INSERT INTO `0_sys_prefs` VALUES ('po_over_charge', 'glsetup.purchase', 'int', 11, '10');` |
| `sql/en_US-demo.sql` | 2150 | `INSERT INTO `0_sys_prefs` VALUES ('allow_negative_stock', 'glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2151 | `INSERT INTO `0_sys_prefs` VALUES ('default_inventory_act', 'glsetup.items', 'varchar', 15, '1510');` |
| `sql/en_US-demo.sql` | 2152 | `INSERT INTO `0_sys_prefs` VALUES ('default_cogs_act', 'glsetup.items', 'varchar', 15, '5010');` |
| `sql/en_US-demo.sql` | 2153 | `INSERT INTO `0_sys_prefs` VALUES ('default_adj_act', 'glsetup.items', 'varchar', 15, '5040');` |
| `sql/en_US-demo.sql` | 2154 | `INSERT INTO `0_sys_prefs` VALUES ('default_inv_sales_act', 'glsetup.items', 'varchar', 15, '4010');` |
| `sql/en_US-demo.sql` | 2155 | `INSERT INTO `0_sys_prefs` VALUES ('default_wip_act', 'glsetup.items', 'varchar', 15, '1530');` |
| `sql/en_US-demo.sql` | 2156 | `INSERT INTO `0_sys_prefs` VALUES ('default_workorder_required', 'glsetup.manuf', 'int', 11, '20');` |
| `sql/en_US-demo.sql` | 2157 | `INSERT INTO `0_sys_prefs` VALUES ('version_id', 'system', 'varchar', 11, '2.4.1');` |
| `sql/en_US-demo.sql` | 2158 | `INSERT INTO `0_sys_prefs` VALUES ('auto_curr_reval', 'setup.company', 'smallint', 6, '1');` |
| `sql/en_US-demo.sql` | 2159 | `INSERT INTO `0_sys_prefs` VALUES ('grn_clearing_act', 'glsetup.purchase', 'varchar', 15, '1550');` |
| `sql/en_US-demo.sql` | 2160 | `INSERT INTO `0_sys_prefs` VALUES ('bcc_email', 'setup.company', 'varchar', 100, '');` |
| `sql/en_US-demo.sql` | 2161 | `INSERT INTO `0_sys_prefs` VALUES ('deferred_income_act', 'glsetup.sales', 'varchar', '15', '');` |
| `sql/en_US-demo.sql` | 2162 | `INSERT INTO `0_sys_prefs` VALUES ('gl_closing_date','setup.closing_date', 'date', 8, '');` |
| `sql/en_US-demo.sql` | 2163 | `INSERT INTO `0_sys_prefs` VALUES ('alternative_tax_include_on_docs','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2164 | `INSERT INTO `0_sys_prefs` VALUES ('no_zero_lines_amount','glsetup.sales', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2165 | `INSERT INTO `0_sys_prefs` VALUES ('show_po_item_codes','glsetup.purchase', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2166 | `INSERT INTO `0_sys_prefs` VALUES ('accounts_alpha','glsetup.general', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2167 | `INSERT INTO `0_sys_prefs` VALUES ('loc_notification','glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2168 | `INSERT INTO `0_sys_prefs` VALUES ('print_invoice_no','glsetup.sales', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2169 | `INSERT INTO `0_sys_prefs` VALUES ('allow_negative_prices','glsetup.inventory', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2170 | `INSERT INTO `0_sys_prefs` VALUES ('print_item_images_on_quote','glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2171 | `INSERT INTO `0_sys_prefs` VALUES ('suppress_tax_rates','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2172 | `INSERT INTO `0_sys_prefs` VALUES ('company_logo_report','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-demo.sql` | 2173 | `INSERT INTO `0_sys_prefs` VALUES ('default_loss_on_asset_disposal_act', 'glsetup.items', 'varchar', '15', '5660');` |
| `sql/en_US-demo.sql` | 2174 | `INSERT INTO `0_sys_prefs` VALUES ('depreciation_period', 'glsetup.company', 'tinyint', '1', '1');` |
| `sql/en_US-demo.sql` | 2175 | `INSERT INTO `0_sys_prefs` VALUES ('use_manufacturing','setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2176 | `INSERT INTO `0_sys_prefs` VALUES ('use_fixed_assets','setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-demo.sql` | 2185 | `DROP TABLE IF EXISTS `0_tags`;` |
| `sql/en_US-demo.sql` | 2186 | `CREATE TABLE IF NOT EXISTS `0_tags` (` |
| `sql/en_US-demo.sql` | 2206 | `DROP TABLE IF EXISTS `0_tag_associations`;` |
| `sql/en_US-demo.sql` | 2207 | `CREATE TABLE IF NOT EXISTS `0_tag_associations` (` |
| `sql/en_US-demo.sql` | 2223 | `DROP TABLE IF EXISTS `0_tax_groups`;` |
| `sql/en_US-demo.sql` | 2224 | `CREATE TABLE IF NOT EXISTS `0_tax_groups` (` |
| `sql/en_US-demo.sql` | 2236 | `INSERT INTO `0_tax_groups` VALUES (1, 'Tax', 0);` |
| `sql/en_US-demo.sql` | 2237 | `INSERT INTO `0_tax_groups` VALUES (2, 'Tax Exempt', 0);` |
| `sql/en_US-demo.sql` | 2245 | `DROP TABLE IF EXISTS `0_tax_group_items`;` |
| `sql/en_US-demo.sql` | 2246 | `CREATE TABLE IF NOT EXISTS `0_tax_group_items` (` |
| `sql/en_US-demo.sql` | 2257 | `INSERT INTO `0_tax_group_items` VALUES (1, 1, 1);` |
| `sql/en_US-demo.sql` | 2265 | `DROP TABLE IF EXISTS `0_tax_types`;` |
| `sql/en_US-demo.sql` | 2266 | `CREATE TABLE IF NOT EXISTS `0_tax_types` (` |
| `sql/en_US-demo.sql` | 2280 | `INSERT INTO `0_tax_types` VALUES (1, 5, '2150', '2150', 'Tax', 0);` |
| `sql/en_US-demo.sql` | 2288 | `DROP TABLE IF EXISTS `0_trans_tax_details`;` |
| `sql/en_US-demo.sql` | 2289 | `CREATE TABLE IF NOT EXISTS `0_trans_tax_details` (` |
| `sql/en_US-demo.sql` | 2311 | `INSERT INTO `0_trans_tax_details` VALUES` |
| `sql/en_US-demo.sql` | 2326 | `DROP TABLE IF EXISTS `0_useronline`;` |
| `sql/en_US-demo.sql` | 2327 | `CREATE TABLE IF NOT EXISTS `0_useronline` (` |
| `sql/en_US-demo.sql` | 2347 | `DROP TABLE IF EXISTS `0_users`;` |
| `sql/en_US-demo.sql` | 2348 | `CREATE TABLE IF NOT EXISTS `0_users` (` |
| `sql/en_US-demo.sql` | 2392 | `INSERT INTO `0_users` VALUES (1, 'admin', '5f4dcc3b5aa765d61d8327deb882cf99', 'Administrator', 2, '', 'adm@example.com', 'C', 0, 0, 0, 0, 'default', 'Letter', 2, 2, 4, 1, 1, 0, 0, '2016-05-07 13:58:33', 10, 1, 1, '1', 1, 0, 'orders', 30, 0, 1, 0, 0, 0);` |
| `sql/en_US-demo.sql` | 2400 | `DROP TABLE IF EXISTS `0_voided`;` |
| `sql/en_US-demo.sql` | 2401 | `CREATE TABLE IF NOT EXISTS `0_voided` (` |
| `sql/en_US-demo.sql` | 2419 | `DROP TABLE IF EXISTS `0_workcentres`;` |
| `sql/en_US-demo.sql` | 2420 | `CREATE TABLE IF NOT EXISTS `0_workcentres` (` |
| `sql/en_US-demo.sql` | 2433 | `INSERT INTO `0_workcentres` VALUES ('1', 'Work Centre', '', '0');` |
| `sql/en_US-demo.sql` | 2441 | `DROP TABLE IF EXISTS `0_workorders`;` |
| `sql/en_US-demo.sql` | 2442 | `CREATE TABLE IF NOT EXISTS `0_workorders` (` |
| `sql/en_US-demo.sql` | 2464 | `INSERT INTO `0_workorders` VALUES` |
| `sql/en_US-demo.sql` | 2475 | `DROP TABLE IF EXISTS `0_wo_costing`;` |
| `sql/en_US-demo.sql` | 2476 | `CREATE TABLE `0_wo_costing` (` |
| `sql/en_US-demo.sql` | 2496 | `DROP TABLE IF EXISTS `0_wo_issues`;` |
| `sql/en_US-demo.sql` | 2497 | `CREATE TABLE IF NOT EXISTS `0_wo_issues` (` |
| `sql/en_US-demo.sql` | 2518 | `DROP TABLE IF EXISTS `0_wo_issue_items`;` |
| `sql/en_US-demo.sql` | 2519 | `CREATE TABLE IF NOT EXISTS `0_wo_issue_items` (` |
| `sql/en_US-demo.sql` | 2538 | `DROP TABLE IF EXISTS `0_wo_manufacture`;` |
| `sql/en_US-demo.sql` | 2539 | `CREATE TABLE IF NOT EXISTS `0_wo_manufacture` (` |
| `sql/en_US-demo.sql` | 2559 | `DROP TABLE IF EXISTS `0_wo_requirements`;` |
| `sql/en_US-demo.sql` | 2560 | `CREATE TABLE IF NOT EXISTS `0_wo_requirements` (` |
| `sql/en_US-demo.sql` | 2577 | `INSERT INTO `0_wo_requirements` VALUES` |
| `sql/en_US-new.sql` | 20 | `DROP TABLE IF EXISTS `0_areas`;` |
| `sql/en_US-new.sql` | 21 | `CREATE TABLE IF NOT EXISTS `0_areas` (` |
| `sql/en_US-new.sql` | 33 | `INSERT INTO `0_areas` VALUES (1, 'Global', 0);` |
| `sql/en_US-new.sql` | 41 | `DROP TABLE IF EXISTS `0_attachments`;` |
| `sql/en_US-new.sql` | 42 | `CREATE TABLE IF NOT EXISTS `0_attachments` (` |
| `sql/en_US-new.sql` | 66 | `DROP TABLE IF EXISTS `0_audit_trail`;` |
| `sql/en_US-new.sql` | 67 | `CREATE TABLE IF NOT EXISTS `0_audit_trail` (` |
| `sql/en_US-new.sql` | 92 | `DROP TABLE IF EXISTS `0_bank_accounts`;` |
| `sql/en_US-new.sql` | 93 | `CREATE TABLE IF NOT EXISTS `0_bank_accounts` (` |
| `sql/en_US-new.sql` | 117 | `INSERT INTO `0_bank_accounts` VALUES ('1060', 0, 'Current account', 'N/A', 'N/A', '', 'USD', 1, 1, '5690', '0000-00-00 00:00:00', 0, 0);` |
| `sql/en_US-new.sql` | 118 | `INSERT INTO `0_bank_accounts` VALUES ('1065', 3, 'Petty Cash account', 'N/A', 'N/A', '', 'USD', 0, 2, '5690', '0000-00-00 00:00:00', 0, 0);` |
| `sql/en_US-new.sql` | 126 | `DROP TABLE IF EXISTS `0_bank_trans`;` |
| `sql/en_US-new.sql` | 127 | `CREATE TABLE IF NOT EXISTS `0_bank_trans` (` |
| `sql/en_US-new.sql` | 157 | `DROP TABLE IF EXISTS `0_bom`;` |
| `sql/en_US-new.sql` | 158 | `CREATE TABLE IF NOT EXISTS `0_bom` (` |
| `sql/en_US-new.sql` | 183 | `DROP TABLE IF EXISTS `0_budget_trans`;` |
| `sql/en_US-new.sql` | 184 | `CREATE TABLE IF NOT EXISTS `0_budget_trans` (` |
| `sql/en_US-new.sql` | 206 | `DROP TABLE IF EXISTS `0_chart_class`;` |
| `sql/en_US-new.sql` | 207 | `CREATE TABLE IF NOT EXISTS `0_chart_class` (` |
| `sql/en_US-new.sql` | 219 | `INSERT INTO `0_chart_class` VALUES ('1', 'Assets', 1, 0);` |
| `sql/en_US-new.sql` | 220 | `INSERT INTO `0_chart_class` VALUES ('2', 'Liabilities', 2, 0);` |
| `sql/en_US-new.sql` | 221 | `INSERT INTO `0_chart_class` VALUES ('3', 'Income', 4, 0);` |
| `sql/en_US-new.sql` | 222 | `INSERT INTO `0_chart_class` VALUES ('4', 'Costs', 6, 0);` |
| `sql/en_US-new.sql` | 230 | `DROP TABLE IF EXISTS `0_chart_master`;` |
| `sql/en_US-new.sql` | 231 | `CREATE TABLE IF NOT EXISTS `0_chart_master` (` |
| `sql/en_US-new.sql` | 246 | `INSERT INTO `0_chart_master` VALUES ('1060', '', 'Checking Account', '1', 0);` |
| `sql/en_US-new.sql` | 247 | `INSERT INTO `0_chart_master` VALUES ('1065', '', 'Petty Cash', '1', 0);` |
| `sql/en_US-new.sql` | 248 | `INSERT INTO `0_chart_master` VALUES ('1200', '', 'Accounts Receivables', '1', 0);` |
| `sql/en_US-new.sql` | 249 | `INSERT INTO `0_chart_master` VALUES ('1205', '', 'Allowance for doubtful accounts', '1', 0);` |
| `sql/en_US-new.sql` | 250 | `INSERT INTO `0_chart_master` VALUES ('1510', '', 'Inventory', '2', 0);` |
| `sql/en_US-new.sql` | 251 | `INSERT INTO `0_chart_master` VALUES ('1520', '', 'Stocks of Raw Materials', '2', 0);` |
| `sql/en_US-new.sql` | 252 | `INSERT INTO `0_chart_master` VALUES ('1530', '', 'Stocks of Work In Progress', '2', 0);` |
| `sql/en_US-new.sql` | 253 | `INSERT INTO `0_chart_master` VALUES ('1540', '', 'Stocks of Finished Goods', '2', 0);` |
| `sql/en_US-new.sql` | 254 | `INSERT INTO `0_chart_master` VALUES ('1550', '', 'Goods Received Clearing account', '2', 0);` |
| `sql/en_US-new.sql` | 255 | `INSERT INTO `0_chart_master` VALUES ('1820', '', 'Office Furniture &amp; Equipment', '3', 0);` |
| `sql/en_US-new.sql` | 256 | `INSERT INTO `0_chart_master` VALUES ('1825', '', 'Accum. Amort. -Furn. &amp; Equip.', '3', 0);` |
| `sql/en_US-new.sql` | 257 | `INSERT INTO `0_chart_master` VALUES ('1840', '', 'Vehicle', '3', 0);` |
| `sql/en_US-new.sql` | 258 | `INSERT INTO `0_chart_master` VALUES ('1845', '', 'Accum. Amort. -Vehicle', '3', 0);` |
| `sql/en_US-new.sql` | 259 | `INSERT INTO `0_chart_master` VALUES ('2100', '', 'Accounts Payable', '4', 0);` |
| `sql/en_US-new.sql` | 260 | `INSERT INTO `0_chart_master` VALUES ('2110', '', 'Accrued Income Tax - Federal', '4', 0);` |
| `sql/en_US-new.sql` | 261 | `INSERT INTO `0_chart_master` VALUES ('2120', '', 'Accrued Income Tax - State', '4', 0);` |
| `sql/en_US-new.sql` | 262 | `INSERT INTO `0_chart_master` VALUES ('2130', '', 'Accrued Franchise Tax', '4', 0);` |
| `sql/en_US-new.sql` | 263 | `INSERT INTO `0_chart_master` VALUES ('2140', '', 'Accrued Real &amp; Personal Prop Tax', '4', 0);` |
| `sql/en_US-new.sql` | 264 | `INSERT INTO `0_chart_master` VALUES ('2150', '', 'Sales Tax', '4', 0);` |
| `sql/en_US-new.sql` | 265 | `INSERT INTO `0_chart_master` VALUES ('2160', '', 'Accrued Use Tax Payable', '4', 0);` |
| `sql/en_US-new.sql` | 266 | `INSERT INTO `0_chart_master` VALUES ('2210', '', 'Accrued Wages', '4', 0);` |
| `sql/en_US-new.sql` | 267 | `INSERT INTO `0_chart_master` VALUES ('2220', '', 'Accrued Comp Time', '4', 0);` |
| `sql/en_US-new.sql` | 268 | `INSERT INTO `0_chart_master` VALUES ('2230', '', 'Accrued Holiday Pay', '4', 0);` |
| `sql/en_US-new.sql` | 269 | `INSERT INTO `0_chart_master` VALUES ('2240', '', 'Accrued Vacation Pay', '4', 0);` |
| `sql/en_US-new.sql` | 270 | `INSERT INTO `0_chart_master` VALUES ('2310', '', 'Accr. Benefits - 401K', '4', 0);` |
| `sql/en_US-new.sql` | 271 | `INSERT INTO `0_chart_master` VALUES ('2320', '', 'Accr. Benefits - Stock Purchase', '4', 0);` |
| `sql/en_US-new.sql` | 272 | `INSERT INTO `0_chart_master` VALUES ('2330', '', 'Accr. Benefits - Med, Den', '4', 0);` |
| `sql/en_US-new.sql` | 273 | `INSERT INTO `0_chart_master` VALUES ('2340', '', 'Accr. Benefits - Payroll Taxes', '4', 0);` |
| `sql/en_US-new.sql` | 274 | `INSERT INTO `0_chart_master` VALUES ('2350', '', 'Accr. Benefits - Credit Union', '4', 0);` |
| `sql/en_US-new.sql` | 275 | `INSERT INTO `0_chart_master` VALUES ('2360', '', 'Accr. Benefits - Savings Bond', '4', 0);` |
| `sql/en_US-new.sql` | 276 | `INSERT INTO `0_chart_master` VALUES ('2370', '', 'Accr. Benefits - Garnish', '4', 0);` |
| `sql/en_US-new.sql` | 277 | `INSERT INTO `0_chart_master` VALUES ('2380', '', 'Accr. Benefits - Charity Cont.', '4', 0);` |
| `sql/en_US-new.sql` | 278 | `INSERT INTO `0_chart_master` VALUES ('2620', '', 'Bank Loans', '5', 0);` |
| `sql/en_US-new.sql` | 279 | `INSERT INTO `0_chart_master` VALUES ('2680', '', 'Loans from Shareholders', '5', 0);` |
| `sql/en_US-new.sql` | 280 | `INSERT INTO `0_chart_master` VALUES ('3350', '', 'Common Shares', '6', 0);` |
| `sql/en_US-new.sql` | 281 | `INSERT INTO `0_chart_master` VALUES ('3590', '', 'Retained Earnings - prior years', '7', 0);` |
| `sql/en_US-new.sql` | 282 | `INSERT INTO `0_chart_master` VALUES ('4010', '', 'Sales', '8', 0);` |
| `sql/en_US-new.sql` | 283 | `INSERT INTO `0_chart_master` VALUES ('4430', '', 'Shipping &amp; Handling', '9', 0);` |
| `sql/en_US-new.sql` | 284 | `INSERT INTO `0_chart_master` VALUES ('4440', '', 'Interest', '9', 0);` |
| `sql/en_US-new.sql` | 285 | `INSERT INTO `0_chart_master` VALUES ('4450', '', 'Foreign Exchange Gain', '9', 0);` |
| `sql/en_US-new.sql` | 286 | `INSERT INTO `0_chart_master` VALUES ('4500', '', 'Prompt Payment Discounts', '9', 0);` |
| `sql/en_US-new.sql` | 287 | `INSERT INTO `0_chart_master` VALUES ('4510', '', 'Discounts Given', '9', 0);` |
| `sql/en_US-new.sql` | 288 | `INSERT INTO `0_chart_master` VALUES ('5010', '', 'Cost of Goods Sold - Retail', '10', 0);` |
| `sql/en_US-new.sql` | 289 | `INSERT INTO `0_chart_master` VALUES ('5020', '', 'Material Usage Varaiance', '10', 0);` |
| `sql/en_US-new.sql` | 290 | `INSERT INTO `0_chart_master` VALUES ('5030', '', 'Consumable Materials', '10', 0);` |
| `sql/en_US-new.sql` | 291 | `INSERT INTO `0_chart_master` VALUES ('5040', '', 'Purchase price Variance', '10', 0);` |
| `sql/en_US-new.sql` | 292 | `INSERT INTO `0_chart_master` VALUES ('5050', '', 'Purchases of materials', '10', 0);` |
| `sql/en_US-new.sql` | 293 | `INSERT INTO `0_chart_master` VALUES ('5060', '', 'Discounts Received', '10', 0);` |
| `sql/en_US-new.sql` | 294 | `INSERT INTO `0_chart_master` VALUES ('5100', '', 'Freight', '10', 0);` |
| `sql/en_US-new.sql` | 295 | `INSERT INTO `0_chart_master` VALUES ('5410', '', 'Wages &amp; Salaries', '11', 0);` |
| `sql/en_US-new.sql` | 296 | `INSERT INTO `0_chart_master` VALUES ('5420', '', 'Wages - Overtime', '11', 0);` |
| `sql/en_US-new.sql` | 297 | `INSERT INTO `0_chart_master` VALUES ('5430', '', 'Benefits - Comp Time', '11', 0);` |
| `sql/en_US-new.sql` | 298 | `INSERT INTO `0_chart_master` VALUES ('5440', '', 'Benefits - Payroll Taxes', '11', 0);` |
| `sql/en_US-new.sql` | 299 | `INSERT INTO `0_chart_master` VALUES ('5450', '', 'Benefits - Workers Comp', '11', 0);` |
| `sql/en_US-new.sql` | 300 | `INSERT INTO `0_chart_master` VALUES ('5460', '', 'Benefits - Pension', '11', 0);` |
| `sql/en_US-new.sql` | 301 | `INSERT INTO `0_chart_master` VALUES ('5470', '', 'Benefits - General Benefits', '11', 0);` |
| `sql/en_US-new.sql` | 302 | `INSERT INTO `0_chart_master` VALUES ('5510', '', 'Inc Tax Exp - Federal', '11', 0);` |
| `sql/en_US-new.sql` | 303 | `INSERT INTO `0_chart_master` VALUES ('5520', '', 'Inc Tax Exp - State', '11', 0);` |
| `sql/en_US-new.sql` | 304 | `INSERT INTO `0_chart_master` VALUES ('5530', '', 'Taxes - Real Estate', '11', 0);` |
| `sql/en_US-new.sql` | 305 | `INSERT INTO `0_chart_master` VALUES ('5540', '', 'Taxes - Personal Property', '11', 0);` |
| `sql/en_US-new.sql` | 306 | `INSERT INTO `0_chart_master` VALUES ('5550', '', 'Taxes - Franchise', '11', 0);` |
| `sql/en_US-new.sql` | 307 | `INSERT INTO `0_chart_master` VALUES ('5560', '', 'Taxes - Foreign Withholding', '11', 0);` |
| `sql/en_US-new.sql` | 308 | `INSERT INTO `0_chart_master` VALUES ('5610', '', 'Accounting &amp; Legal', '12', 0);` |
| `sql/en_US-new.sql` | 309 | `INSERT INTO `0_chart_master` VALUES ('5615', '', 'Advertising &amp; Promotions', '12', 0);` |
| `sql/en_US-new.sql` | 310 | `INSERT INTO `0_chart_master` VALUES ('5620', '', 'Bad Debts', '12', 0);` |
| `sql/en_US-new.sql` | 311 | `INSERT INTO `0_chart_master` VALUES ('5660', '', 'Amortization Expense', '12', 0);` |
| `sql/en_US-new.sql` | 312 | `INSERT INTO `0_chart_master` VALUES ('5685', '', 'Insurance', '12', 0);` |
| `sql/en_US-new.sql` | 313 | `INSERT INTO `0_chart_master` VALUES ('5690', '', 'Interest &amp; Bank Charges', '12', 0);` |
| `sql/en_US-new.sql` | 314 | `INSERT INTO `0_chart_master` VALUES ('5700', '', 'Office Supplies', '12', 0);` |
| `sql/en_US-new.sql` | 315 | `INSERT INTO `0_chart_master` VALUES ('5760', '', 'Rent', '12', 0);` |
| `sql/en_US-new.sql` | 316 | `INSERT INTO `0_chart_master` VALUES ('5765', '', 'Repair &amp; Maintenance', '12', 0);` |
| `sql/en_US-new.sql` | 317 | `INSERT INTO `0_chart_master` VALUES ('5780', '', 'Telephone', '12', 0);` |
| `sql/en_US-new.sql` | 318 | `INSERT INTO `0_chart_master` VALUES ('5785', '', 'Travel &amp; Entertainment', '12', 0);` |
| `sql/en_US-new.sql` | 319 | `INSERT INTO `0_chart_master` VALUES ('5790', '', 'Utilities', '12', 0);` |
| `sql/en_US-new.sql` | 320 | `INSERT INTO `0_chart_master` VALUES ('5795', '', 'Registrations', '12', 0);` |
| `sql/en_US-new.sql` | 321 | `INSERT INTO `0_chart_master` VALUES ('5800', '', 'Licenses', '12', 0);` |
| `sql/en_US-new.sql` | 322 | `INSERT INTO `0_chart_master` VALUES ('5810', '', 'Foreign Exchange Loss', '12', 0);` |
| `sql/en_US-new.sql` | 323 | `INSERT INTO `0_chart_master` VALUES ('9990', '', 'Year Profit/Loss', '12', 0);` |
| `sql/en_US-new.sql` | 331 | `DROP TABLE IF EXISTS `0_chart_types`;` |
| `sql/en_US-new.sql` | 332 | `CREATE TABLE IF NOT EXISTS `0_chart_types` (` |
| `sql/en_US-new.sql` | 347 | `INSERT INTO `0_chart_types` VALUES ('1', 'Current Assets', '1', '', 0);` |
| `sql/en_US-new.sql` | 348 | `INSERT INTO `0_chart_types` VALUES ('2', 'Inventory Assets', '1', '', 0);` |
| `sql/en_US-new.sql` | 349 | `INSERT INTO `0_chart_types` VALUES ('3', 'Capital Assets', '1', '', 0);` |
| `sql/en_US-new.sql` | 350 | `INSERT INTO `0_chart_types` VALUES ('4', 'Current Liabilities', '2', '', 0);` |
| `sql/en_US-new.sql` | 351 | `INSERT INTO `0_chart_types` VALUES ('5', 'Long Term Liabilities', '2', '', 0);` |
| `sql/en_US-new.sql` | 352 | `INSERT INTO `0_chart_types` VALUES ('6', 'Share Capital', '2', '', 0);` |
| `sql/en_US-new.sql` | 353 | `INSERT INTO `0_chart_types` VALUES ('7', 'Retained Earnings', '2', '', 0);` |
| `sql/en_US-new.sql` | 354 | `INSERT INTO `0_chart_types` VALUES ('8', 'Sales Revenue', '3', '', 0);` |
| `sql/en_US-new.sql` | 355 | `INSERT INTO `0_chart_types` VALUES ('9', 'Other Revenue', '3', '', 0);` |
| `sql/en_US-new.sql` | 356 | `INSERT INTO `0_chart_types` VALUES ('10', 'Cost of Goods Sold', '4', '', 0);` |
| `sql/en_US-new.sql` | 357 | `INSERT INTO `0_chart_types` VALUES ('11', 'Payroll Expenses', '4', '', 0);` |
| `sql/en_US-new.sql` | 358 | `INSERT INTO `0_chart_types` VALUES ('12', 'General &amp; Administrative expenses', '4', '', 0);` |
| `sql/en_US-new.sql` | 366 | `DROP TABLE IF EXISTS `0_comments`;` |
| `sql/en_US-new.sql` | 367 | `CREATE TABLE IF NOT EXISTS `0_comments` (` |
| `sql/en_US-new.sql` | 385 | `DROP TABLE IF EXISTS `0_credit_status`;` |
| `sql/en_US-new.sql` | 386 | `CREATE TABLE IF NOT EXISTS `0_credit_status` (` |
| `sql/en_US-new.sql` | 399 | `INSERT INTO `0_credit_status` VALUES (1, 'Good History', 0, 0);` |
| `sql/en_US-new.sql` | 400 | `INSERT INTO `0_credit_status` VALUES (3, 'No more work until payment received', 1, 0);` |
| `sql/en_US-new.sql` | 401 | `INSERT INTO `0_credit_status` VALUES (4, 'In liquidation', 1, 0);` |
| `sql/en_US-new.sql` | 409 | `DROP TABLE IF EXISTS `0_crm_categories`;` |
| `sql/en_US-new.sql` | 410 | `CREATE TABLE IF NOT EXISTS `0_crm_categories` (` |
| `sql/en_US-new.sql` | 427 | `INSERT INTO `0_crm_categories` VALUES (1, 'cust_branch', 'general', 'General', 'General contact data for customer branch (overrides company setting)', 1, 0);` |
| `sql/en_US-new.sql` | 428 | `INSERT INTO `0_crm_categories` VALUES (2, 'cust_branch', 'invoice', 'Invoices', 'Invoice posting (overrides company setting)', 1, 0);` |
| `sql/en_US-new.sql` | 429 | `INSERT INTO `0_crm_categories` VALUES (3, 'cust_branch', 'order', 'Orders', 'Order confirmation (overrides company setting)', 1, 0);` |
| `sql/en_US-new.sql` | 430 | `INSERT INTO `0_crm_categories` VALUES (4, 'cust_branch', 'delivery', 'Deliveries', 'Delivery coordination (overrides company setting)', 1, 0);` |
| `sql/en_US-new.sql` | 431 | `INSERT INTO `0_crm_categories` VALUES (5, 'customer', 'general', 'General', 'General contact data for customer', 1, 0);` |
| `sql/en_US-new.sql` | 432 | `INSERT INTO `0_crm_categories` VALUES (6, 'customer', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/en_US-new.sql` | 433 | `INSERT INTO `0_crm_categories` VALUES (7, 'customer', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/en_US-new.sql` | 434 | `INSERT INTO `0_crm_categories` VALUES (8, 'customer', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/en_US-new.sql` | 435 | `INSERT INTO `0_crm_categories` VALUES (9, 'supplier', 'general', 'General', 'General contact data for supplier', 1, 0);` |
| `sql/en_US-new.sql` | 436 | `INSERT INTO `0_crm_categories` VALUES (10, 'supplier', 'order', 'Orders', 'Order confirmation', 1, 0);` |
| `sql/en_US-new.sql` | 437 | `INSERT INTO `0_crm_categories` VALUES (11, 'supplier', 'delivery', 'Deliveries', 'Delivery coordination', 1, 0);` |
| `sql/en_US-new.sql` | 438 | `INSERT INTO `0_crm_categories` VALUES (12, 'supplier', 'invoice', 'Invoices', 'Invoice posting', 1, 0);` |
| `sql/en_US-new.sql` | 446 | `DROP TABLE IF EXISTS `0_crm_contacts`;` |
| `sql/en_US-new.sql` | 447 | `CREATE TABLE IF NOT EXISTS `0_crm_contacts` (` |
| `sql/en_US-new.sql` | 467 | `DROP TABLE IF EXISTS `0_crm_persons`;` |
| `sql/en_US-new.sql` | 468 | `CREATE TABLE IF NOT EXISTS `0_crm_persons` (` |
| `sql/en_US-new.sql` | 495 | `DROP TABLE IF EXISTS `0_currencies`;` |
| `sql/en_US-new.sql` | 496 | `CREATE TABLE IF NOT EXISTS `0_currencies` (` |
| `sql/en_US-new.sql` | 511 | `INSERT INTO `0_currencies` VALUES ('US Dollars', 'USD', '$', 'United States', 'Cents', 1, 0);` |
| `sql/en_US-new.sql` | 512 | `INSERT INTO `0_currencies` VALUES ('CA Dollars', 'CAD', '$', 'Canada', 'Cents', 1, 0);` |
| `sql/en_US-new.sql` | 513 | `INSERT INTO `0_currencies` VALUES ('Euro', 'EUR', '€', 'Europe', 'Cents', 1, 0);` |
| `sql/en_US-new.sql` | 514 | `INSERT INTO `0_currencies` VALUES ('Pounds', 'GBP', '£', 'England', 'Pence', 1, 0);` |
| `sql/en_US-new.sql` | 522 | `DROP TABLE IF EXISTS `0_cust_allocations`;` |
| `sql/en_US-new.sql` | 523 | `CREATE TABLE IF NOT EXISTS `0_cust_allocations` (` |
| `sql/en_US-new.sql` | 534 | `KEY `From` (`trans_type_from`,`trans_no_from`),` |
| `sql/en_US-new.sql` | 548 | `DROP TABLE IF EXISTS `0_cust_branch`;` |
| `sql/en_US-new.sql` | 549 | `CREATE TABLE IF NOT EXISTS `0_cust_branch` (` |
| `sql/en_US-new.sql` | 584 | `DROP TABLE IF EXISTS `0_debtors_master`;` |
| `sql/en_US-new.sql` | 585 | `CREATE TABLE IF NOT EXISTS `0_debtors_master` (` |
| `sql/en_US-new.sql` | 617 | `DROP TABLE IF EXISTS `0_debtor_trans`;` |
| `sql/en_US-new.sql` | 618 | `CREATE TABLE IF NOT EXISTS `0_debtor_trans` (` |
| `sql/en_US-new.sql` | 658 | `DROP TABLE IF EXISTS `0_debtor_trans_details`;` |
| `sql/en_US-new.sql` | 659 | `CREATE TABLE IF NOT EXISTS `0_debtor_trans_details` (` |
| `sql/en_US-new.sql` | 687 | `DROP TABLE IF EXISTS `0_dimensions`;` |
| `sql/en_US-new.sql` | 688 | `CREATE TABLE IF NOT EXISTS `0_dimensions` (` |
| `sql/en_US-new.sql` | 713 | `DROP TABLE IF EXISTS `0_exchange_rates`;` |
| `sql/en_US-new.sql` | 714 | `CREATE TABLE IF NOT EXISTS `0_exchange_rates` (` |
| `sql/en_US-new.sql` | 734 | `DROP TABLE IF EXISTS `0_fiscal_year`;` |
| `sql/en_US-new.sql` | 735 | `CREATE TABLE IF NOT EXISTS `0_fiscal_year` (` |
| `sql/en_US-new.sql` | 749 | `INSERT INTO `0_fiscal_year` VALUES (1, '2016-01-01', '2016-12-31', 0);` |
| `sql/en_US-new.sql` | 757 | `DROP TABLE IF EXISTS `0_gl_trans`;` |
| `sql/en_US-new.sql` | 758 | `CREATE TABLE IF NOT EXISTS `0_gl_trans` (` |
| `sql/en_US-new.sql` | 788 | `DROP TABLE IF EXISTS `0_grn_batch`;` |
| `sql/en_US-new.sql` | 789 | `CREATE TABLE IF NOT EXISTS `0_grn_batch` (` |
| `sql/en_US-new.sql` | 812 | `DROP TABLE IF EXISTS `0_grn_items`;` |
| `sql/en_US-new.sql` | 813 | `CREATE TABLE IF NOT EXISTS `0_grn_items` (` |
| `sql/en_US-new.sql` | 835 | `DROP TABLE IF EXISTS `0_groups`;` |
| `sql/en_US-new.sql` | 836 | `CREATE TABLE IF NOT EXISTS `0_groups` (` |
| `sql/en_US-new.sql` | 848 | `INSERT INTO `0_groups` VALUES (1, 'Small', 0);` |
| `sql/en_US-new.sql` | 849 | `INSERT INTO `0_groups` VALUES (2, 'Medium', 0);` |
| `sql/en_US-new.sql` | 850 | `INSERT INTO `0_groups` VALUES (3, 'Large', 0);` |
| `sql/en_US-new.sql` | 858 | `DROP TABLE IF EXISTS `0_item_codes`;` |
| `sql/en_US-new.sql` | 859 | `CREATE TABLE IF NOT EXISTS `0_item_codes` (` |
| `sql/en_US-new.sql` | 883 | `DROP TABLE IF EXISTS `0_item_tax_types`;` |
| `sql/en_US-new.sql` | 884 | `CREATE TABLE IF NOT EXISTS `0_item_tax_types` (` |
| `sql/en_US-new.sql` | 897 | `INSERT INTO `0_item_tax_types` VALUES (1, 'Regular', 0, 0);` |
| `sql/en_US-new.sql` | 905 | `DROP TABLE IF EXISTS `0_item_tax_type_exemptions`;` |
| `sql/en_US-new.sql` | 906 | `CREATE TABLE IF NOT EXISTS `0_item_tax_type_exemptions` (` |
| `sql/en_US-new.sql` | 922 | `DROP TABLE IF EXISTS `0_item_units`;` |
| `sql/en_US-new.sql` | 923 | `CREATE TABLE IF NOT EXISTS `0_item_units` (` |
| `sql/en_US-new.sql` | 936 | `INSERT INTO `0_item_units` VALUES ('each', 'Each', 0, 0);` |
| `sql/en_US-new.sql` | 937 | `INSERT INTO `0_item_units` VALUES ('hr', 'Hours', 0, 0);` |
| `sql/en_US-new.sql` | 945 | `DROP TABLE IF EXISTS `0_journal`;` |
| `sql/en_US-new.sql` | 946 | `CREATE TABLE `0_journal` (` |
| `sql/en_US-new.sql` | 971 | `DROP TABLE IF EXISTS `0_locations`;` |
| `sql/en_US-new.sql` | 972 | `CREATE TABLE IF NOT EXISTS `0_locations` (` |
| `sql/en_US-new.sql` | 990 | `INSERT INTO `0_locations` VALUES ('DEF', 'Default', 'N/A', '', '', '', '', '', 0, 0);` |
| `sql/en_US-new.sql` | 998 | `DROP TABLE IF EXISTS `0_loc_stock`;` |
| `sql/en_US-new.sql` | 999 | `CREATE TABLE IF NOT EXISTS `0_loc_stock` (` |
| `sql/en_US-new.sql` | 1017 | `DROP TABLE IF EXISTS `0_payment_terms`;` |
| `sql/en_US-new.sql` | 1018 | `CREATE TABLE IF NOT EXISTS `0_payment_terms` (` |
| `sql/en_US-new.sql` | 1032 | `INSERT INTO `0_payment_terms` VALUES (1, 'Due 15th Of the Following Month', 0, 17, 0);` |
| `sql/en_US-new.sql` | 1033 | `INSERT INTO `0_payment_terms` VALUES (2, 'Due By End Of The Following Month', 0, 30, 0);` |
| `sql/en_US-new.sql` | 1034 | `INSERT INTO `0_payment_terms` VALUES (3, 'Payment due within 10 days', 10, 0, 0);` |
| `sql/en_US-new.sql` | 1035 | `INSERT INTO `0_payment_terms` VALUES (4, 'Cash Only', 0, 0, 0);` |
| `sql/en_US-new.sql` | 1043 | `DROP TABLE IF EXISTS `0_prices`;` |
| `sql/en_US-new.sql` | 1044 | `CREATE TABLE IF NOT EXISTS `0_prices` (` |
| `sql/en_US-new.sql` | 1064 | `DROP TABLE IF EXISTS `0_printers`;` |
| `sql/en_US-new.sql` | 1065 | `CREATE TABLE IF NOT EXISTS `0_printers` (` |
| `sql/en_US-new.sql` | 1081 | `INSERT INTO `0_printers` VALUES (1, 'QL500', 'Label printer', 'QL500', 'server', 127, 20);` |
| `sql/en_US-new.sql` | 1082 | `INSERT INTO `0_printers` VALUES (2, 'Samsung', 'Main network printer', 'scx4521F', 'server', 515, 5);` |
| `sql/en_US-new.sql` | 1083 | `INSERT INTO `0_printers` VALUES (3, 'Local', 'Local print server at user IP', 'lp', '', 515, 10);` |
| `sql/en_US-new.sql` | 1091 | `DROP TABLE IF EXISTS `0_print_profiles`;` |
| `sql/en_US-new.sql` | 1092 | `CREATE TABLE IF NOT EXISTS `0_print_profiles` (` |
| `sql/en_US-new.sql` | 1105 | `INSERT INTO `0_print_profiles` VALUES (1, 'Out of office', '', 0);` |
| `sql/en_US-new.sql` | 1106 | `INSERT INTO `0_print_profiles` VALUES (2, 'Sales Department', '', 0);` |
| `sql/en_US-new.sql` | 1107 | `INSERT INTO `0_print_profiles` VALUES (3, 'Central', '', 2);` |
| `sql/en_US-new.sql` | 1108 | `INSERT INTO `0_print_profiles` VALUES (4, 'Sales Department', '104', 2);` |
| `sql/en_US-new.sql` | 1109 | `INSERT INTO `0_print_profiles` VALUES (5, 'Sales Department', '105', 2);` |
| `sql/en_US-new.sql` | 1110 | `INSERT INTO `0_print_profiles` VALUES (6, 'Sales Department', '107', 2);` |
| `sql/en_US-new.sql` | 1111 | `INSERT INTO `0_print_profiles` VALUES (7, 'Sales Department', '109', 2);` |
| `sql/en_US-new.sql` | 1112 | `INSERT INTO `0_print_profiles` VALUES (8, 'Sales Department', '110', 2);` |
| `sql/en_US-new.sql` | 1113 | `INSERT INTO `0_print_profiles` VALUES (9, 'Sales Department', '201', 2);` |
| `sql/en_US-new.sql` | 1121 | `DROP TABLE IF EXISTS `0_purch_data`;` |
| `sql/en_US-new.sql` | 1122 | `CREATE TABLE IF NOT EXISTS `0_purch_data` (` |
| `sql/en_US-new.sql` | 1142 | `DROP TABLE IF EXISTS `0_purch_orders`;` |
| `sql/en_US-new.sql` | 1143 | `CREATE TABLE IF NOT EXISTS `0_purch_orders` (` |
| `sql/en_US-new.sql` | 1170 | `DROP TABLE IF EXISTS `0_purch_order_details`;` |
| `sql/en_US-new.sql` | 1171 | `CREATE TABLE IF NOT EXISTS `0_purch_order_details` (` |
| `sql/en_US-new.sql` | 1198 | `DROP TABLE IF EXISTS `0_quick_entries`;` |
| `sql/en_US-new.sql` | 1199 | `CREATE TABLE IF NOT EXISTS `0_quick_entries` (` |
| `sql/en_US-new.sql` | 1215 | `INSERT INTO `0_quick_entries` VALUES (1, 1, 'Maintenance', NULL, 0, 'Amount', 0);` |
| `sql/en_US-new.sql` | 1216 | `INSERT INTO `0_quick_entries` VALUES (2, 4, 'Phone', NULL, 0, 'Amount', 0);` |
| `sql/en_US-new.sql` | 1217 | `INSERT INTO `0_quick_entries` VALUES (3, 2, 'Cash Sales', 'Retail sales without invoice', 0, 'Amount', 0);` |
| `sql/en_US-new.sql` | 1225 | `DROP TABLE IF EXISTS `0_quick_entry_lines`;` |
| `sql/en_US-new.sql` | 1226 | `CREATE TABLE IF NOT EXISTS `0_quick_entry_lines` (` |
| `sql/en_US-new.sql` | 1243 | `INSERT INTO `0_quick_entry_lines` VALUES (1, 1, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-new.sql` | 1244 | `INSERT INTO `0_quick_entry_lines` VALUES (2, 2, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-new.sql` | 1245 | `INSERT INTO `0_quick_entry_lines` VALUES (3, 3, 0, '', 't-', '1', 0, 0);` |
| `sql/en_US-new.sql` | 1246 | `INSERT INTO `0_quick_entry_lines` VALUES (4, 3, 0, '', '=', '4010', 0, 0);` |
| `sql/en_US-new.sql` | 1247 | `INSERT INTO `0_quick_entry_lines` VALUES (5, 1, 0, '', '=', '5765', 0, 0);` |
| `sql/en_US-new.sql` | 1248 | `INSERT INTO `0_quick_entry_lines` VALUES (6, 2, 0, '', '=', '5780', 0, 0);` |
| `sql/en_US-new.sql` | 1256 | `DROP TABLE IF EXISTS `0_recurrent_invoices`;` |
| `sql/en_US-new.sql` | 1257 | `CREATE TABLE IF NOT EXISTS `0_recurrent_invoices` (` |
| `sql/en_US-new.sql` | 1282 | `DROP TABLE IF EXISTS `0_reflines`;` |
| `sql/en_US-new.sql` | 1284 | `CREATE TABLE `0_reflines` (` |
| `sql/en_US-new.sql` | 1300 | `INSERT INTO `0_reflines` VALUES` |
| `sql/en_US-new.sql` | 1330 | `DROP TABLE IF EXISTS `0_refs`;` |
| `sql/en_US-new.sql` | 1331 | `CREATE TABLE IF NOT EXISTS `0_refs` (` |
| `sql/en_US-new.sql` | 1349 | `DROP TABLE IF EXISTS `0_salesman`;` |
| `sql/en_US-new.sql` | 1350 | `CREATE TABLE IF NOT EXISTS `0_salesman` (` |
| `sql/en_US-new.sql` | 1368 | `INSERT INTO `0_salesman` VALUES (1, 'Sales Person', '', '', '', 5, 1000, 4, 0);` |
| `sql/en_US-new.sql` | 1376 | `DROP TABLE IF EXISTS `0_sales_orders`;` |
| `sql/en_US-new.sql` | 1377 | `CREATE TABLE IF NOT EXISTS `0_sales_orders` (` |
| `sql/en_US-new.sql` | 1414 | `DROP TABLE IF EXISTS `0_sales_order_details`;` |
| `sql/en_US-new.sql` | 1415 | `CREATE TABLE IF NOT EXISTS `0_sales_order_details` (` |
| `sql/en_US-new.sql` | 1441 | `DROP TABLE IF EXISTS `0_sales_pos`;` |
| `sql/en_US-new.sql` | 1442 | `CREATE TABLE IF NOT EXISTS `0_sales_pos` (` |
| `sql/en_US-new.sql` | 1458 | `INSERT INTO `0_sales_pos` VALUES (1, 'Default', 1, 1, 'DEF', 2, 0);` |
| `sql/en_US-new.sql` | 1466 | `DROP TABLE IF EXISTS `0_sales_types`;` |
| `sql/en_US-new.sql` | 1467 | `CREATE TABLE IF NOT EXISTS `0_sales_types` (` |
| `sql/en_US-new.sql` | 1481 | `INSERT INTO `0_sales_types` VALUES (1, 'Retail', 1, 1, 0);` |
| `sql/en_US-new.sql` | 1482 | `INSERT INTO `0_sales_types` VALUES (2, 'Wholesale', 0, 0.7, 0);` |
| `sql/en_US-new.sql` | 1490 | `DROP TABLE IF EXISTS `0_security_roles`;` |
| `sql/en_US-new.sql` | 1491 | `CREATE TABLE IF NOT EXISTS `0_security_roles` (` |
| `sql/en_US-new.sql` | 1506 | `INSERT INTO `0_security_roles` VALUES (1, 'Inquiries', 'Inquiries', '768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15872;16128', '257;258;259;260;513;514;515;516;517;518;519;520;521;522;523;524;525;773;774;2822;3073;3075;3076;3077;3329;3330;3331;3332;3333;3334;3335;5377;5633;5640;5889;5890;5891;7937;7938;7939;7940;8193;8194;8450;8451;104` |
| `sql/en_US-new.sql` | 1507 | `INSERT INTO `0_security_roles` VALUES (2, 'System Administrator', 'System Administrator', '256;512;768;2816;3072;3328;5376;5632;5888;7936;8192;8448;9472;9728;10496;10752;11008;13056;13312;15616;15872;16128', '257;258;259;260;513;514;515;516;517;518;519;520;521;522;523;524;525;526;769;770;771;772;773;774;2817;2818;2819;2820;2821;2822;2823;3073;3074;` |
| `sql/en_US-new.sql` | 1508 | `INSERT INTO `0_security_roles` VALUES (3, 'Salesman', 'Salesman', '768;3072;5632;8192;15872', '773;774;3073;3075;3081;5633;8194;15873;775', 0);` |
| `sql/en_US-new.sql` | 1509 | `INSERT INTO `0_security_roles` VALUES (4, 'Stock Manager', 'Stock Manager', '768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15872;16128', '2818;2822;3073;3076;3077;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5640;5889;5890;5891;8193;8194;8450;8451;10753;11009;11010;11012;13313;13315;15882;16129;16130;16131;16132;775', 0);` |
| `sql/en_US-new.sql` | 1510 | `INSERT INTO `0_security_roles` VALUES (5, 'Production Manager', 'Production Manager', '512;768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;2818;2819;2820;2821;2822;2823;3073;3074;3076;3077;3078;3079;3080;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5640;5640;5889;5890;5891;8193;8194;8196;8197` |
| `sql/en_US-new.sql` | 1511 | `INSERT INTO `0_security_roles` VALUES (6, 'Purchase Officer', 'Purchase Officer', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;2818;2819;2820;2821;2822;2823;3073;3074;3076;3077;3078;3079;3080;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5377;5633;5635;5640;5640;5889;5890;5891;8193;819` |
| `sql/en_US-new.sql` | 1512 | `INSERT INTO `0_security_roles` VALUES (7, 'AR Officer', 'AR Officer', '512;768;2816;3072;3328;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '521;523;524;771;773;774;2818;2819;2820;2821;2822;2823;3073;3073;3074;3075;3076;3077;3078;3079;3080;3081;3081;3329;3330;3330;3330;3331;3331;3332;3333;3334;3335;5633;5633;5634;5637;5638;5639;5640;564` |
| `sql/en_US-new.sql` | 1513 | `INSERT INTO `0_security_roles` VALUES (8, 'AP Officer', 'AP Officer', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;769;770;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3082;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5635;5640;5889;5890;` |
| `sql/en_US-new.sql` | 1514 | `INSERT INTO `0_security_roles` VALUES (9, 'Accountant', 'New Accountant', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3075;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5634;5635;5637;5638;5639` |
| `sql/en_US-new.sql` | 1515 | `INSERT INTO `0_security_roles` VALUES (10, 'Sub Admin', 'Sub Admin', '512;768;2816;3072;3328;5376;5632;5888;8192;8448;10752;11008;13312;15616;15872;16128', '257;258;259;260;521;523;524;771;772;773;774;2818;2819;2820;2821;2822;2823;3073;3074;3082;3075;3076;3077;3078;3079;3080;3081;3329;3330;3331;3332;3333;3334;3335;5377;5633;5634;5635;5637;5638;5639` |
| `sql/en_US-new.sql` | 1523 | `DROP TABLE IF EXISTS `0_shippers`;` |
| `sql/en_US-new.sql` | 1524 | `CREATE TABLE IF NOT EXISTS `0_shippers` (` |
| `sql/en_US-new.sql` | 1540 | `INSERT INTO `0_shippers` VALUES (1, 'Default', '', '', '', '', 0);` |
| `sql/en_US-new.sql` | 1548 | `DROP TABLE IF EXISTS `0_sql_trail`;` |
| `sql/en_US-new.sql` | 1549 | `CREATE TABLE IF NOT EXISTS `0_sql_trail` (` |
| `sql/en_US-new.sql` | 1567 | `DROP TABLE IF EXISTS `0_stock_category`;` |
| `sql/en_US-new.sql` | 1568 | `CREATE TABLE IF NOT EXISTS `0_stock_category` (` |
| `sql/en_US-new.sql` | 1592 | `INSERT INTO `0_stock_category` VALUES (1, 'Components', 1, 'each', 'B', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-new.sql` | 1593 | `INSERT INTO `0_stock_category` VALUES (2, 'Charges', 1, 'each', 'D', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-new.sql` | 1594 | `INSERT INTO `0_stock_category` VALUES (3, 'Systems', 1, 'each', 'M', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-new.sql` | 1595 | `INSERT INTO `0_stock_category` VALUES (4, 'Services', 1, 'hr', 'D', '4010', '5010', '1510', '5040', '1530', 0, 0, 0, 0, 0);` |
| `sql/en_US-new.sql` | 1603 | `DROP TABLE IF EXISTS `0_stock_fa_class`;` |
| `sql/en_US-new.sql` | 1604 | `CREATE TABLE `0_stock_fa_class` (` |
| `sql/en_US-new.sql` | 1620 | `DROP TABLE IF EXISTS `0_stock_master`;` |
| `sql/en_US-new.sql` | 1621 | `CREATE TABLE IF NOT EXISTS `0_stock_master` (` |
| `sql/en_US-new.sql` | 1663 | `DROP TABLE IF EXISTS `0_stock_moves`;` |
| `sql/en_US-new.sql` | 1664 | `CREATE TABLE `0_stock_moves` (` |
| `sql/en_US-new.sql` | 1690 | `DROP TABLE IF EXISTS `0_suppliers`;` |
| `sql/en_US-new.sql` | 1691 | `CREATE TABLE IF NOT EXISTS `0_suppliers` (` |
| `sql/en_US-new.sql` | 1728 | `DROP TABLE IF EXISTS `0_supp_allocations`;` |
| `sql/en_US-new.sql` | 1729 | `CREATE TABLE IF NOT EXISTS `0_supp_allocations` (` |
| `sql/en_US-new.sql` | 1740 | `KEY `From` (`trans_type_from`,`trans_no_from`),` |
| `sql/en_US-new.sql` | 1754 | `DROP TABLE IF EXISTS `0_supp_invoice_items`;` |
| `sql/en_US-new.sql` | 1755 | `CREATE TABLE IF NOT EXISTS `0_supp_invoice_items` (` |
| `sql/en_US-new.sql` | 1784 | `DROP TABLE IF EXISTS `0_supp_trans`;` |
| `sql/en_US-new.sql` | 1785 | `CREATE TABLE IF NOT EXISTS `0_supp_trans` (` |
| `sql/en_US-new.sql` | 1814 | `DROP TABLE IF EXISTS `0_sys_prefs`;` |
| `sql/en_US-new.sql` | 1815 | `CREATE TABLE IF NOT EXISTS `0_sys_prefs` (` |
| `sql/en_US-new.sql` | 1829 | `INSERT INTO `0_sys_prefs` VALUES ('coy_name', 'setup.company', 'varchar', 60, 'Company name');` |
| `sql/en_US-new.sql` | 1830 | `INSERT INTO `0_sys_prefs` VALUES ('gst_no', 'setup.company', 'varchar', 25, '');` |
| `sql/en_US-new.sql` | 1831 | `INSERT INTO `0_sys_prefs` VALUES ('coy_no', 'setup.company', 'varchar', 25, '');` |
| `sql/en_US-new.sql` | 1832 | `INSERT INTO `0_sys_prefs` VALUES ('tax_prd', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-new.sql` | 1833 | `INSERT INTO `0_sys_prefs` VALUES ('tax_last', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-new.sql` | 1834 | `INSERT INTO `0_sys_prefs` VALUES ('postal_address', 'setup.company', 'tinytext', 0, 'N/A');` |
| `sql/en_US-new.sql` | 1835 | `INSERT INTO `0_sys_prefs` VALUES ('phone', 'setup.company', 'varchar', 30, '');` |
| `sql/en_US-new.sql` | 1836 | `INSERT INTO `0_sys_prefs` VALUES ('fax', 'setup.company', 'varchar', 30, '');` |
| `sql/en_US-new.sql` | 1837 | `INSERT INTO `0_sys_prefs` VALUES ('email', 'setup.company', 'varchar', 100, '');` |
| `sql/en_US-new.sql` | 1838 | `INSERT INTO `0_sys_prefs` VALUES ('coy_logo', 'setup.company', 'varchar', 100, '');` |
| `sql/en_US-new.sql` | 1839 | `INSERT INTO `0_sys_prefs` VALUES ('domicile', 'setup.company', 'varchar', 55, '');` |
| `sql/en_US-new.sql` | 1840 | `INSERT INTO `0_sys_prefs` VALUES ('curr_default', 'setup.company', 'char', 3, 'USD');` |
| `sql/en_US-new.sql` | 1841 | `INSERT INTO `0_sys_prefs` VALUES ('use_dimension', 'setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1842 | `INSERT INTO `0_sys_prefs` VALUES ('f_year', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-new.sql` | 1843 | `INSERT INTO `0_sys_prefs` VALUES ('shortname_name_in_list','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1844 | `INSERT INTO `0_sys_prefs` VALUES ('no_item_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1845 | `INSERT INTO `0_sys_prefs` VALUES ('no_customer_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1846 | `INSERT INTO `0_sys_prefs` VALUES ('no_supplier_list', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1847 | `INSERT INTO `0_sys_prefs` VALUES ('base_sales', 'setup.company', 'int', 11, '1');` |
| `sql/en_US-new.sql` | 1848 | `INSERT INTO `0_sys_prefs` VALUES ('time_zone', 'setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1849 | `INSERT INTO `0_sys_prefs` VALUES ('add_pct', 'setup.company', 'int', 5, '-1');` |
| `sql/en_US-new.sql` | 1850 | `INSERT INTO `0_sys_prefs` VALUES ('round_to', 'setup.company', 'int', 5, '1');` |
| `sql/en_US-new.sql` | 1851 | `INSERT INTO `0_sys_prefs` VALUES ('login_tout', 'setup.company', 'smallint', 6, '600');` |
| `sql/en_US-new.sql` | 1852 | `INSERT INTO `0_sys_prefs` VALUES ('past_due_days', 'glsetup.general', 'int', 11, '30');` |
| `sql/en_US-new.sql` | 1853 | `INSERT INTO `0_sys_prefs` VALUES ('profit_loss_year_act', 'glsetup.general', 'varchar', 15, '9990');` |
| `sql/en_US-new.sql` | 1854 | `INSERT INTO `0_sys_prefs` VALUES ('retained_earnings_act', 'glsetup.general', 'varchar', 15, '3590');` |
| `sql/en_US-new.sql` | 1855 | `INSERT INTO `0_sys_prefs` VALUES ('bank_charge_act', 'glsetup.general', 'varchar', 15, '5690');` |
| `sql/en_US-new.sql` | 1856 | `INSERT INTO `0_sys_prefs` VALUES ('exchange_diff_act', 'glsetup.general', 'varchar', 15, '4450');` |
| `sql/en_US-new.sql` | 1857 | `INSERT INTO `0_sys_prefs` VALUES ('tax_algorithm', 'glsetup.customer', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1858 | `INSERT INTO `0_sys_prefs` VALUES ('default_credit_limit', 'glsetup.customer', 'int', 11, '1000');` |
| `sql/en_US-new.sql` | 1859 | `INSERT INTO `0_sys_prefs` VALUES ('accumulate_shipping', 'glsetup.customer', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1860 | `INSERT INTO `0_sys_prefs` VALUES ('legal_text', 'glsetup.customer', 'tinytext', 0, '');` |
| `sql/en_US-new.sql` | 1861 | `INSERT INTO `0_sys_prefs` VALUES ('freight_act', 'glsetup.customer', 'varchar', 15, '4430');` |
| `sql/en_US-new.sql` | 1862 | `INSERT INTO `0_sys_prefs` VALUES ('debtors_act', 'glsetup.sales', 'varchar', 15, '1200');` |
| `sql/en_US-new.sql` | 1863 | `INSERT INTO `0_sys_prefs` VALUES ('default_sales_act', 'glsetup.sales', 'varchar', 15, '4010');` |
| `sql/en_US-new.sql` | 1864 | `INSERT INTO `0_sys_prefs` VALUES ('default_sales_discount_act', 'glsetup.sales', 'varchar', 15, '4510');` |
| `sql/en_US-new.sql` | 1865 | `INSERT INTO `0_sys_prefs` VALUES ('default_prompt_payment_act', 'glsetup.sales', 'varchar', 15, '4500');` |
| `sql/en_US-new.sql` | 1866 | `INSERT INTO `0_sys_prefs` VALUES ('default_delivery_required', 'glsetup.sales', 'smallint', 6, '1');` |
| `sql/en_US-new.sql` | 1867 | `INSERT INTO `0_sys_prefs` VALUES ('default_receival_required', 'glsetup.purchase', 'smallint', 6, '10');` |
| `sql/en_US-new.sql` | 1868 | `INSERT INTO `0_sys_prefs` VALUES ('default_quote_valid_days', 'glsetup.sales', 'smallint', 6, '30');` |
| `sql/en_US-new.sql` | 1869 | `INSERT INTO `0_sys_prefs` VALUES ('default_dim_required', 'glsetup.dims', 'int', 11, '20');` |
| `sql/en_US-new.sql` | 1870 | `INSERT INTO `0_sys_prefs` VALUES ('pyt_discount_act', 'glsetup.purchase', 'varchar', 15, '5060');` |
| `sql/en_US-new.sql` | 1871 | `INSERT INTO `0_sys_prefs` VALUES ('creditors_act', 'glsetup.purchase', 'varchar', 15, '2100');` |
| `sql/en_US-new.sql` | 1872 | `INSERT INTO `0_sys_prefs` VALUES ('po_over_receive', 'glsetup.purchase', 'int', 11, '10');` |
| `sql/en_US-new.sql` | 1873 | `INSERT INTO `0_sys_prefs` VALUES ('po_over_charge', 'glsetup.purchase', 'int', 11, '10');` |
| `sql/en_US-new.sql` | 1874 | `INSERT INTO `0_sys_prefs` VALUES ('allow_negative_stock', 'glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1875 | `INSERT INTO `0_sys_prefs` VALUES ('default_inventory_act', 'glsetup.items', 'varchar', 15, '1510');` |
| `sql/en_US-new.sql` | 1876 | `INSERT INTO `0_sys_prefs` VALUES ('default_cogs_act', 'glsetup.items', 'varchar', 15, '5010');` |
| `sql/en_US-new.sql` | 1877 | `INSERT INTO `0_sys_prefs` VALUES ('default_adj_act', 'glsetup.items', 'varchar', 15, '5040');` |
| `sql/en_US-new.sql` | 1878 | `INSERT INTO `0_sys_prefs` VALUES ('default_inv_sales_act', 'glsetup.items', 'varchar', 15, '4010');` |
| `sql/en_US-new.sql` | 1879 | `INSERT INTO `0_sys_prefs` VALUES ('default_wip_act', 'glsetup.items', 'varchar', 15, '1530');` |
| `sql/en_US-new.sql` | 1880 | `INSERT INTO `0_sys_prefs` VALUES ('default_workorder_required', 'glsetup.manuf', 'int', 11, '20');` |
| `sql/en_US-new.sql` | 1881 | `INSERT INTO `0_sys_prefs` VALUES ('version_id', 'system', 'varchar', 11, '2.4.1');` |
| `sql/en_US-new.sql` | 1882 | `INSERT INTO `0_sys_prefs` VALUES ('auto_curr_reval', 'setup.company', 'smallint', 6, '1');` |
| `sql/en_US-new.sql` | 1883 | `INSERT INTO `0_sys_prefs` VALUES ('grn_clearing_act', 'glsetup.purchase', 'varchar', 15, '1550');` |
| `sql/en_US-new.sql` | 1884 | `INSERT INTO `0_sys_prefs` VALUES ('bcc_email', 'setup.company', 'varchar', 100, '');` |
| `sql/en_US-new.sql` | 1885 | `INSERT INTO `0_sys_prefs` VALUES ('deferred_income_act', 'glsetup.sales', 'varchar', '15', '');` |
| `sql/en_US-new.sql` | 1886 | `INSERT INTO `0_sys_prefs` VALUES ('gl_closing_date','setup.closing_date', 'date', 8, '');` |
| `sql/en_US-new.sql` | 1887 | `INSERT INTO `0_sys_prefs` VALUES ('alternative_tax_include_on_docs','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1888 | `INSERT INTO `0_sys_prefs` VALUES ('no_zero_lines_amount','glsetup.sales', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1889 | `INSERT INTO `0_sys_prefs` VALUES ('show_po_item_codes','glsetup.purchase', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1890 | `INSERT INTO `0_sys_prefs` VALUES ('accounts_alpha','glsetup.general', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1891 | `INSERT INTO `0_sys_prefs` VALUES ('loc_notification','glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1892 | `INSERT INTO `0_sys_prefs` VALUES ('print_invoice_no','glsetup.sales', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1893 | `INSERT INTO `0_sys_prefs` VALUES ('allow_negative_prices','glsetup.inventory', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1894 | `INSERT INTO `0_sys_prefs` VALUES ('print_item_images_on_quote','glsetup.inventory', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1895 | `INSERT INTO `0_sys_prefs` VALUES ('suppress_tax_rates','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1896 | `INSERT INTO `0_sys_prefs` VALUES ('company_logo_report','setup.company', 'tinyint', 1, '0');` |
| `sql/en_US-new.sql` | 1897 | `INSERT INTO `0_sys_prefs` VALUES ('default_loss_on_asset_disposal_act', 'glsetup.items', 'varchar', '15', '5660');` |
| `sql/en_US-new.sql` | 1898 | `INSERT INTO `0_sys_prefs` VALUES ('depreciation_period', 'glsetup.company', 'tinyint', '1', '1');` |
| `sql/en_US-new.sql` | 1899 | `INSERT INTO `0_sys_prefs` VALUES ('use_manufacturing','setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1900 | `INSERT INTO `0_sys_prefs` VALUES ('use_fixed_assets','setup.company', 'tinyint', 1, '1');` |
| `sql/en_US-new.sql` | 1908 | `DROP TABLE IF EXISTS `0_tags`;` |
| `sql/en_US-new.sql` | 1909 | `CREATE TABLE IF NOT EXISTS `0_tags` (` |
| `sql/en_US-new.sql` | 1929 | `DROP TABLE IF EXISTS `0_tag_associations`;` |
| `sql/en_US-new.sql` | 1930 | `CREATE TABLE IF NOT EXISTS `0_tag_associations` (` |
| `sql/en_US-new.sql` | 1946 | `DROP TABLE IF EXISTS `0_tax_groups`;` |
| `sql/en_US-new.sql` | 1947 | `CREATE TABLE IF NOT EXISTS `0_tax_groups` (` |
| `sql/en_US-new.sql` | 1959 | `INSERT INTO `0_tax_groups` VALUES (1, 'Tax', 0);` |
| `sql/en_US-new.sql` | 1960 | `INSERT INTO `0_tax_groups` VALUES (2, 'Tax Exempt', 0);` |
| `sql/en_US-new.sql` | 1968 | `DROP TABLE IF EXISTS `0_tax_group_items`;` |
| `sql/en_US-new.sql` | 1969 | `CREATE TABLE IF NOT EXISTS `0_tax_group_items` (` |
| `sql/en_US-new.sql` | 1980 | `INSERT INTO `0_tax_group_items` VALUES (1, 1, 1);` |
| `sql/en_US-new.sql` | 1988 | `DROP TABLE IF EXISTS `0_tax_types`;` |
| `sql/en_US-new.sql` | 1989 | `CREATE TABLE IF NOT EXISTS `0_tax_types` (` |
| `sql/en_US-new.sql` | 2003 | `INSERT INTO `0_tax_types` VALUES (1, 5, '2150', '2150', 'Tax', 0);` |
| `sql/en_US-new.sql` | 2011 | `DROP TABLE IF EXISTS `0_trans_tax_details`;` |
| `sql/en_US-new.sql` | 2012 | `CREATE TABLE IF NOT EXISTS `0_trans_tax_details` (` |
| `sql/en_US-new.sql` | 2040 | `DROP TABLE IF EXISTS `0_useronline`;` |
| `sql/en_US-new.sql` | 2041 | `CREATE TABLE IF NOT EXISTS `0_useronline` (` |
| `sql/en_US-new.sql` | 2061 | `DROP TABLE IF EXISTS `0_users`;` |
| `sql/en_US-new.sql` | 2062 | `CREATE TABLE IF NOT EXISTS `0_users` (` |
| `sql/en_US-new.sql` | 2106 | `INSERT INTO `0_users` VALUES (1, 'admin', '5f4dcc3b5aa765d61d8327deb882cf99', 'Administrator', 2, '', 'adm@example.com', 'en_US', 0, 0, 0, 0, 'default', 'Letter', 2, 2, 4, 1, 1, 0, 0, '2008-04-04 12:34:29', 10, 1, 1, '1', 1, 0, 'orders', 30, 0, 1, 0, 0, 0);` |
| `sql/en_US-new.sql` | 2114 | `DROP TABLE IF EXISTS `0_voided`;` |
| `sql/en_US-new.sql` | 2115 | `CREATE TABLE IF NOT EXISTS `0_voided` (` |
| `sql/en_US-new.sql` | 2133 | `DROP TABLE IF EXISTS `0_workcentres`;` |
| `sql/en_US-new.sql` | 2134 | `CREATE TABLE IF NOT EXISTS `0_workcentres` (` |
| `sql/en_US-new.sql` | 2153 | `DROP TABLE IF EXISTS `0_workorders`;` |
| `sql/en_US-new.sql` | 2154 | `CREATE TABLE IF NOT EXISTS `0_workorders` (` |
| `sql/en_US-new.sql` | 2182 | `DROP TABLE IF EXISTS `0_wo_costing`;` |
| `sql/en_US-new.sql` | 2183 | `CREATE TABLE `0_wo_costing` (` |
| `sql/en_US-new.sql` | 2203 | `DROP TABLE IF EXISTS `0_wo_issues`;` |
| `sql/en_US-new.sql` | 2204 | `CREATE TABLE IF NOT EXISTS `0_wo_issues` (` |
| `sql/en_US-new.sql` | 2225 | `DROP TABLE IF EXISTS `0_wo_issue_items`;` |
| `sql/en_US-new.sql` | 2226 | `CREATE TABLE IF NOT EXISTS `0_wo_issue_items` (` |
| `sql/en_US-new.sql` | 2245 | `DROP TABLE IF EXISTS `0_wo_manufacture`;` |
| `sql/en_US-new.sql` | 2246 | `CREATE TABLE IF NOT EXISTS `0_wo_manufacture` (` |
| `sql/en_US-new.sql` | 2266 | `DROP TABLE IF EXISTS `0_wo_requirements`;` |
| `sql/en_US-new.sql` | 2267 | `CREATE TABLE IF NOT EXISTS `0_wo_requirements` (` |

**Total SQL-related lines captured:** 1631
