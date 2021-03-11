CREATE TABLE property (
    Parcel_ID INTEGER,
	Parcel_Acreage FLOAT,
	Property_Street_Address VARCHAR,
	Property_City VARCHAR,
	Property_State VARCHAR,
	Property_Zip VARCHAR,
	Parcel_Vacancy VARCHAR,
	Conveyance_Date DATE,
	Property_Sales_Price FLOAT,
	Seller_City VARCHAR,
	Seller_State VARCHAR,
	Seller_ZIP VARCHAR,
	Title_Company VARCHAR,
	Buyer_City VARCHAR,
	Buyer_State VARCHAR,
	Buyer_ZIP VARCHAR,
	Primary_Residence VARCHAR,
	Assessed_Value_Land FLOAT,
	Assessed_Value_Improvement FLOAT,
	Total_Assessed_Value FLOAT,
	Property_Class_Code VARCHAR,
	County_ID VARCHAR
);

select * from property;