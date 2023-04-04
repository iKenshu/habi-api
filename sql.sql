CREATE TABLE likes (
    id INT PRIMARY KEY NOT NULL,
    created_date DATETIME NOT NULL,
    user_id INT NOT NULL,
    property_id INT NOT NULL,
    
    CONSTRAINT UC_LIKE UNIQUE (user_id, property_id)
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (property_id) REFERENCES property(id)
);
