INSERT INTO customers (name, email, phone, registration_date) VALUES
('Arjun Kumar', 'arjun.kumar@email.com', '03001234567', '2023-01-15 10:30:00'),
('Fatima Hassan', 'fatima.hassan@email.com', '03009876543', '2023-02-20 14:15:00'),
('Ali Raza', 'ali.raza@email.com', '03105555678', '2023-03-10 09:45:00'),
('Sara Ahmed', 'sara.ahmed@email.com', '03215432109', '2023-04-05 16:20:00'),
('Hassan Malik', 'hassan.malik@email.com', '03325678901', '2023-05-12 11:00:00'),
('Ayesha Khan', 'ayesha.khan@email.com', '03435789012', '2023-06-18 13:30:00'),
('Muhammad Usman', 'muhamm.usman@email.com', '03501234567', '2023-07-22 15:45:00'),
('Zainab Siddiqui', 'zainab.siddiqui@email.com', '03119876543', '2023-08-08 12:10:00'),
('Bilal Ahmed', 'bilal.ahmed@email.com', '03215432198', '2023-09-14 10:25:00'),
('Hira Khan', 'hira.khan@email.com', '03325687654', '2023-10-30 17:50:00');

INSERT INTO menu_items (name, category, price, is_available) VALUES
('Spring Rolls', 'Appetizer', 250.00, TRUE),
('Samosa Basket', 'Appetizer', 180.00, TRUE),
('Paneer Pakora', 'Appetizer', 220.00, TRUE),
('Tikka Appetizer', 'Appetizer', 290.00, FALSE),
('Butter Chicken', 'Main', 520.00, TRUE),
('Biryani Hyderabadi', 'Main', 450.00, TRUE),
('Nihari', 'Main', 380.00, TRUE),
('Karahi Gosht', 'Main', 590.00, TRUE),
('Chocolate Cake', 'Dessert', 280.00, TRUE),
('Gulab Jamun', 'Dessert', 150.00, TRUE),
('Mango Lassi', 'Beverage', 120.00, TRUE),
('Fresh Juice Combo', 'Beverage', 180.00, TRUE);

INSERT INTO orders (customer_id, order_date, total_amount, order_status, payment_method) VALUES
(1, '2024-01-05 18:30:00', 1040.00, 'Completed', 'Card'),
(2, '2024-01-10 19:15:00', 900.00, 'Completed', 'Online'),
(3, '2024-01-15 12:45:00', 760.00, 'Pending', 'Cash'),
(4, '2024-01-20 20:00:00', 1180.00, 'Completed', 'Card'),
(5, '2024-01-25 18:20:00', 970.00, 'Completed', 'Online'),
(6, '2024-02-01 19:45:00', 1000.00, 'Cancelled', 'Card'),
(7, '2024-02-05 17:30:00', 1540.00, 'Completed', 'Online'),
(8, '2024-02-10 20:15:00', 850.00, 'Pending', 'Cash'),
(9, '2024-02-15 18:50:00', 1100.00, 'Completed', 'Card'),
(10, '2024-02-20 19:30:00', 1010.00, 'Completed', 'Online');


INSERT INTO order_items (order_id, menu_item_id, quantity, subtotal) VALUES
-- Order 1: 1040.00
(1, 5, 2, 1040.00),

-- Order 2: 900.00
(2, 6, 2, 900.00),

-- Order 3: 760.00
(3, 7, 2, 760.00),

-- Order 4: 1180.00
(4, 8, 2, 1180.00),

-- Order 5: 970.00
(5, 5, 1, 520.00),
(5, 6, 1, 450.00),

-- Order 6: 1000.00
(6, 1, 2, 500.00),
(6, 2, 2, 360.00),
(6, 11, 1, 120.00),

-- Order 7: 1540.00
(7, 8, 2, 1180.00),
(7, 9, 1, 280.00),
(7, 11, 2, 240.00),

-- Order 8: 850.00
(8, 5, 1, 520.00),
(8, 3, 2, 440.00),
(8, 11, 1, 110.00),

-- Order 9: 1100.00
(9, 7, 1, 380.00),
(9, 8, 1, 590.00),
(9, 9, 1, 280.00),
(9, 11, 1, 150.00),

-- Order 10: 1010.00
(10, 6, 2, 900.00),
(10, 12, 1, 110.00);

INSERT INTO staff_payments (staff_name, role, payment_date, amount_paid) VALUES
('Karim', 'Chef', '2024-01-05', 15000.00),
('Fatima', 'Waiter', '2024-01-05', 8000.00),
('Ahmad', 'Chef', '2024-01-10', 15000.00),
('Leena', 'Waiter', '2024-01-10', 8000.00),
('Omar', 'Manager', '2024-01-15', 25000.00),
('Nida', 'Waiter', '2024-01-20', 8000.00),
('Rashid', 'Chef', '2024-01-25', 15500.00),
('Sana', 'Waiter', '2024-02-01', 8500.00),
('Hassan', 'Manager', '2024-02-10', 25000.00),
('Amina', 'Waiter', '2024-02-15', 8000.00);