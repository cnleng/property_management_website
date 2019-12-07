DROP TABLE IF EXISTS owner;
CREATE TABLE owner (
    Owner_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    Number_Of_Properties INT NOT NULL, 
    Name VARCHAR(50) NOT NULL);

DROP TABLE IF EXISTS lease;
CREATE TABLE lease (
    Lease_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    End_Date DATE NOT NULL, 
    Length_Of_Lease INT NOT NULL, 
    Rent DECIMAL (19,2) NOT NULL); 

DROP TABLE IF EXISTS property;
CREATE TABLE property (
    Property_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    Street_Address VARCHAR(100) NOT NULL, 
    Unit_Number VARCHAR(20), Zip_Code VARCHAR(10) NOT NULL, 
    Square_Feet DECIMAL (19,2) NOT NULL, 
    Rooms INT NOT NULL, 
    Bathrooms DECIMAL (5,1) NOT NULL, 
    Management_Fee DECIMAL (19,2) NOT NULL, 
    Lease_ID INT NOT NULL);

DROP TABLE IF EXISTS tenant;
CREATE TABLE tenant (
    Tenant_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    Property_ID INT NOT NULL, 
    Lease_ID INT NOT NULL, 
    Name VARCHAR(50) NOT NULL, 
    Credit_Score INT, 
    Social_Security INT NOT NULL, 
    Date_Of_Birth DATE NOT NULL);

DROP TABLE IF EXISTS lease_owner;
CREATE TABLE lease_owner (
    lID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    Owner_ID INT NOT NULL, 
    Lease_ID INT NOT NULL, 
    FOREIGN KEY (Owner_ID) REFERENCES owner (Owner_ID), 
    FOREIGN KEY (Lease_ID) REFERENCES lease (Lease_ID) ON DELETE CASCADE);

DROP TABLE IF EXISTS property_owner;
CREATE TABLE property_owner (
    pID INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    Property_ID INT NOT NULL, 
    Owner_ID INT NOT NULL, 
    FOREIGN KEY (Property_ID) REFERENCES property (Property_ID) ON DELETE CASCADE, 
    FOREIGN KEY (Owner_ID) REFERENCES owner (Owner_ID) ON DELETE CASCADE);

INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES ('2020/12/31', '730', '1500');
INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES ('2020/12/31', '730', '1400');
INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES ('2019/12/31', '365', '1800');
INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES ('2020/12/31', '1095', '1250');

INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES ('123 Main Street', NULL, '10001', '950', '3', '1', '250', 1);
INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES ('55 Elm Street', NULL, '10173', '1300', '3', '2', '275', 2);
INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES ('99 Park Avenue', NULL, '10015', '1450', '4', '2.5', '300', 3);
INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES ('270 First Street', NULL, '10005', '1150', '3', '1.5', '250', 4);

INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (1, 1, 'Joe Smith', NULL, '111223333', '1977/05/08');
INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (2, 2, 'Jane Doe', NULL, '222334444', '1968/12/05');
INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (3, 3, 'Don Quixote', NULL, '333445555', '1857/05/17');
INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (4, 4, 'Jessica Fletcher', NULL, '444556666', '1925/03/01');

INSERT INTO owner (Number_Of_Properties, Name) VALUES (1, 'Barry Manilow');
INSERT INTO owner (Number_Of_Properties, Name) VALUES (1, 'Louis Winthorp');
INSERT INTO owner (Number_Of_Properties, Name) VALUES (1, 'Billy Ray Valentine');
INSERT INTO owner (Number_Of_Properties, Name) VALUES (1, 'ALF');

INSERT INTO lease_owner (Owner_ID, Lease_ID) VALUES (1,1);
INSERT INTO lease_owner (Owner_ID, Lease_ID) VALUES (2,2);
INSERT INTO lease_owner (Owner_ID, Lease_ID) VALUES (3,3);
INSERT INTO lease_owner (Owner_ID, Lease_ID) VALUES (4,4);

INSERT INTO property_owner (Property_ID, Owner_ID) VALUES (1, 1);
INSERT INTO property_owner (Property_ID, Owner_ID) VALUES (2, 2);
INSERT INTO property_owner (Property_ID, Owner_ID) VALUES (3, 3);
INSERT INTO property_owner (Property_ID, Owner_ID) VALUES (4, 4);


**USE THIS TO CLEAR OUT ALL TABLES, IF NEEDED**
DROP TABLE property_owner;
DROP TABLE lease_owner;
DROP TABLE tenant;
DROP TABLE property;
DROP TABLE lease;
DROP TABLE owner;
