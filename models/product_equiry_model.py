# Model for data base table
class ProductEnquiry(Base):
    """ Product enquiry form model which has all details -table names & columns"""
    __tablename__ = "productenquiry"
    createdDate = Column("created_date", String)
    dealerCode = Column("dealer_code", String)
    customerName= Column("customer_name", String)
    mobileNumber = Column("mobile_number", Integer, primary_key=True)
    emailId = Column("email", String)
    vehicleModel=Column("vehicle_model",String)
    state=Column("state",String)
    district=Column("district",String)
    city=Column("city",String)
    existingVehicle=Column("existing_vehicle",String)
    wantTestDrive = Column("want_to_take_a_test_ride", BOOLEAN)
    dealerState=Column("dealer_state",String)
    dealerTown=Column("dealer_town",String)
    dealer=Column("dealer",String)
    briefAboutEnquery = Column("brief_about_enquiry", String)
    expectedDateOfPurchase=Column("expected_date_of_purchase", String)
    gender=Column("gender",String)
    age = Column("age", Integer)
    occupation=Column("occupation",String)
    intendedUsage=Column("intended_usage", String)
