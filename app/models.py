from app import db

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hostname = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(50), nullable=False)
    os_version = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), default="Unknown")

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    action = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=True)
    server_id = db.Column(db.Integer, db.ForeignKey("server.id"), nullable=False)

    server = db.relationship("Server", backref=db.backref("logs", lazy=True))
