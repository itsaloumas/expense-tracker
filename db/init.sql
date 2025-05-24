CREATE TABLE IF NOT EXISTS expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  description VARCHAR(255) NOT NULL,
  amount DOUBLE NOT NULL,
  category VARCHAR(255) NOT NULL,
  date DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO expenses (description, amount, category)
VALUES  ('Lunch – sandwich', 6.50, 'Food'),
        ('Monthly bus pass', 30.00, 'Transport'),
        ('Netflix subscription', 12.99, 'Entertainment');