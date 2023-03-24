
USE cbse_compsci_proj;
CREATE TABLE ntry_xit_details
(
date_of_scan  DATE,
time_of_scan  TIME,
_status_  char(20),
employee_code CHAR(10) NOT NULL,
employee_name CHAR(20) NOT NULL,
gender CHAR(10),
department char(20) NOT NULL,
post_held char(20) NOT NULL,
phone INT(10) NOT NULL
);

-- ALTER TABLE ntry_xit_details 
-- CHANGE  date_of_entry date_of_scan ;
-- ALTER TABLE ntry_xit_details RENAME 
-- COLUMN  time_of_entry TO time_of_scan;
USE cbse_compsci_proj;
ALTER TABLE ntry_xit_details 
RENAME TO scan_report;

DESC scan_report;
SELECT * FROM scan_report;