-- sql/create_tables.sql

CREATE TABLE property (
    property_id INT AUTO_INCREMENT PRIMARY KEY,
    property_title VARCHAR(255),
    address VARCHAR(255),
    market VARCHAR(100),
    flood VARCHAR(50),
    street_address VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(50),
    zip VARCHAR(20),
    property_type VARCHAR(100),
    year_built INT,
    sqft_basement FLOAT,
    bed INT,
    bath FLOAT,
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    subdivision VARCHAR(255),
    school_average FLOAT
);

CREATE TABLE leads (
    lead_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    reviewed_status VARCHAR(50),
    most_recent_status VARCHAR(50),
    source VARCHAR(100),
    occupancy VARCHAR(50),
    net_yield FLOAT,
    irr FLOAT,
    selling_reason VARCHAR(255),
    seller_retained_broker VARCHAR(255),
    final_reviewer VARCHAR(255),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

CREATE TABLE valuation (
    valuation_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    previous_rent DECIMAL(15,2),
    list_price DECIMAL(15,2),
    zestimate DECIMAL(15,2),
    arv DECIMAL(15,2),
    expected_rent DECIMAL(15,2),
    rent_zestimate DECIMAL(15,2),
    low_fmr DECIMAL(15,2),
    high_fmr DECIMAL(15,2),
    redfin_value DECIMAL(15,2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

CREATE TABLE hoa (
    hoa_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    hoa_flag BOOLEAN,
    hoa_amount DECIMAL(10,2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

CREATE TABLE rehab (
    rehab_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    underwriting_rehab DECIMAL(15,2),
    rehab_calculation TEXT,
    paint BOOLEAN,
    flooring_flag BOOLEAN,
    foundation_flag BOOLEAN,
    roof_flag BOOLEAN,
    hvac_flag BOOLEAN,
    kitchen_flag BOOLEAN,
    bathroom_flag BOOLEAN,
    appliances_flag BOOLEAN,
    windows_flag BOOLEAN,
    landscaping_flag BOOLEAN,
    trashout_flag BOOLEAN,
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);

CREATE TABLE taxes (
    tax_id INT AUTO_INCREMENT PRIMARY KEY,
    property_id INT,
    tax_rate FLOAT,
    tax_amount DECIMAL(15,2),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);
