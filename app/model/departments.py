from app import db

class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    start_date = db.Column(db.DateTime(timezone=False), nullable= True)
    sede_id = db.Column(db.Integer, nullable= True)
    affiliate_id = db.Column(db.String(15), nullable= True)