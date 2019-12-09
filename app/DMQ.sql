--get Lease information for dropdown
SELECT * FROM lease;

--get Owner information for dropdown
SELECT * FROM owner;

--get Property information for dropdown
SELECT Property_ID, Street_Address, Unit_Number, Zip_Code FROM property;

--get Tenant information for dropdown
SELECT * FROM tenant;


--get information to Update a Lease form
SELECT * FROM lease WHERE Lease_ID = :Lease_ID_selected_from_browse_lease_page;

--get information to Update an Owner form
SELECT * FROM owner WHERE Owner_ID = :Owner_ID_selected_from_browse_owner_page;

--get information to Update a Tenant form
SELECT * FROM tenant WHERE Tenant_ID = :Tenant_ID_selected_from_browse_tenant_page;

--get information to Update a Property form
SELECT Management_Fee FROM property WHERE Property_ID = :Property_ID_selected_from_browse_property_page;

-- add a new lease
INSERT INTO lease (End_Date, Length_Of_Lease, Rent) VALUES (:enddateInput, :lengthInput, :rentInput);

-- add a new property
INSERT INTO property (Street_Address, Unit_Number, Zip_Code, Square_Feet, Rooms, Bathrooms, Management_Fee, Lease_ID) VALUES (:addressInput, :unitInput, :zipInput, :sqfeetInput, :roomsInput, :bathInput, :feeInput, :leaseidInput);

-- add a new tenant
INSERT INTO tenant (Property_ID, Lease_ID, Name, Credit_Score, Social_Security, Date_Of_Birth) VALUES (:propidInput, :leaseidInput, :nameInput, :creditInput, :ssnInput, :dobInput);

-- add a new owner
INSERT INTO owner (Number_Of_Properties, Name) VALUES (:numpropsInput, :nameInput);


-- associate a lease with an owner 
INSERT INTO lease_owner (Owner_ID, Lease_ID) VALUES (:Owner_ID_from_dropdown_input, :Lease_ID_ from_dropdown_input);

--associate a property with an owner
INSERT INTO property_owner (Property_ID, Owner_ID) VALUES (:Property_ID_from_dropdown_input, :Owner_ID_ from_dropdown_input);

--delete a lease
DELETE FROM lease WHERE id = :Lease_ID_selected_from_browse_lease_page;

--delete a property
DELETE FROM property WHERE id = :Property_ID_selected_from_browse_property_page;

--delete a tenant
DELETE FROM tenant WHERE id = :Tenant_ID_selected_from_browse_tenant_page;

--delete an owner
DELETE FROM owner WHERE id = :Owner_ID_selected_from_browse_owner_page;

--update an owner
UPDATE owner SET Number_Of_Properties = :numpropsUpdate, Name = :nameUpdate WHERE Owner_ID = :Owner_ID_From_Update_Form; 

--update a lease
UPDATE lease SET End_Date = :enddateInput, Length_Of_Lease = :lengthInput, Rent = :rentInput WHERE Lease_ID = :Lease_ID_From_Update_Form;

--update a property
UPDATE property SET Street_Address = :addressInput, Unit_Number = :uniInput, Zip_Code = :zipInput, Square_Feet = :sqfeetInput, Rooms = :roomsInput, Bathrooms = :bathInput, Management_Fee = :feeInput, Lease_ID = :leaseidInput WHERE property_ID = :Property_ID_From_Update_Form;

--update a tenant
UPDATE tenant SET Property_ID = :propidInput, Lease_ID = :leaseidInput, Name = :nameInput, Credit_Score = :creditInput, Social_Security = :ssnInput, Date_Of_Birth = :dobInput  WHERE Tenant_ID = :Tenant_ID_From_Update_Form;


