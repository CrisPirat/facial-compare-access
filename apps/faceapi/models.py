from apps import db

class User(db.Model):

    __tablename__   = 'User'

    id              = db.Column(db.Integer, primary_key=True)
    names           = db.Column(db.String(255))
    lastnames       = db.Column(db.String(255))
    #type_dni        = db.Column(db.Enum('DNI', 'PSPT'))
    dni             = db.Column(db.String(10), unique=True)
    gender          = db.Column(db.Enum('M', 'F', 'O'))
    status          = db.Column(db.Enum('A', 'I'))
    url_picture     = db.Column(db.String(255))
    base64_picture  = db.Column(db.LargeBinary)
    encoding        = db.Column(db.PickleType)


    def __repr__(self):
        return str('User --> {} - {} {}'.format(self.id, self.names, self.lastnames))
    
    def get_id(self):
        return (self.id)
    
    def getStatus(self):
        val = {
            'A':'Activo',
            'I':'Inactivo'
        }
        return(val[self.status])

    def getGender(self):
        val = {
            'F':'Femenino',
            'M':'Masculino',
            'O':'Otro'
        }
        return(val[self.gender])
    
    def toJson(self):
        return {
            'id':self.id,
            'DNI':self.dni,
            'names':self.names, 
            'lastnames':self.lastnames,
            'gender':self.getGender(),
            'status':self.getStatus(),
            'URL': self.url_picture
        }