

class Dealer(Base):
    """ Dealer model which has all details -table names & columns"""
    __tablename__ = "dealer"
    dealerName = Column("dealer_name", String, primary_key=True)
    dealerCode = Column("dealer_code", String)
