-- Total ATM Events

SELECT COUNT(*) AS total_events
FROM atm_silver;

-- Failure Events

SELECT SUM(failure_events) AS failure_events
FROM atm_silver;

-- High Temperature Alerts

SELECT COUNT(*) AS high_temperature_alerts
FROM atm_silver
WHERE temperature > 80;

-- Low Cash Alerts

SELECT COUNT(*) AS low_cash_alerts
FROM atm_silver
WHERE cash_level < 20;
