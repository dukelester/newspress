INSERT INTO user (username, phone, email, fullname, password)
VALUES ('testuser', '0756780034', 'testuser@gmail.com', 'test user',
'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'
),
('otheruser', '073456789', 'otheruser@gmaul.com', 'other user',
'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO blog (author_id, title, body, category, photo, video_url, tags) VALUES
(1, 'test blog', 'a test blog post for testing', 'testing', 'testing/photo.png','https://test.com/test',
'test, testing, user test, test blog'),
(1, 'test blog 2', 'a test blog 2 post for testing', 'testing', 'testing/photo.png','https://test.com/test',
'test, testing, user test, test blog'),
(2, 'test blog 3', 'a test blog post 3 for testing', 'testing', 'testing/photo.png','https://test.com/test',
'test, testing, user test, test blog');

INSERT INTO products (title, price, detailed_description, photo, seller_id) VALUES
('testing products', '2000', ' good testing product to test', 'testing', 'test, testing, additional test', 'testing/photo.png', 1),
('testing product 2', '2700', ' good testing product to test', 'testing', 'test, testing, additional test', 'testing/photo.png', 3);

INSERT INTO contact (first_name, last_name, email, phone, subject, comment) VALUES
('test', 'user', 'testuser@gmail.com', '073467822', 'testing', 'Testing the application'),
('test2', 'user2', 'testuser2@gmail.com', '0709467822', 'testing', 'Testing the application'),
('john', 'user', 'john@gmail.com', '07456782', 'testing', 'Testing the application again and again');