from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Product(db.Model):
    Code = db.Column(db.String(16), primary_key=True)
    CommutatorCode = db.Column(db.String(32))
    ElectricDiagram = db.Column(db.String(32))
    Name = db.Column(db.String(32))
    VolumeMarket = db.Column(db.String(32))
    Brand = db.Column(db.String(32))
    ClusterDescription = db.Column(db.String(32))
    EprelClusters = db.Column(db.String(32))
    Controller = db.Column(db.String(32))
    FunctionType = db.Column(db.String(32))
    Type = db.Column(db.String(32))
    Buffle = db.Column(db.String(32))
    InsulationCode = db.Column(db.String(32))
    InsulationDesc = db.Column(db.String(32))
    TypeOfLamps = db.Column(db.String(32))
    LampCode = db.Column(db.String(32))
    LampPower = db.Column(db.String(32))
    UpperResistance = db.Column(db.String(32))
    UpperHeaterPower = db.Column(db.String(32))
    UpperHeaterSurfaceLoad = db.Column(db.String(32))
    LowerResistance = db.Column(db.String(32))
    LowerHeaterPower = db.Column(db.String(32))
    LowerHeaterSurfaceLoad = db.Column(db.String(32))
    CavityResistanceCode = db.Column(db.String(32))
    CavityHeaterPower = db.Column(db.String(32))
    CavityHeaterSurfaceLoad = db.Column(db.String(32))
    CoolingFan = db.Column(db.String(32))
    CoolingFanPower = db.Column(db.String(32))
    CavityFan = db.Column(db.String(32))
    CavityFanPower = db.Column(db.String(32))
    Turnspit = db.Column(db.String(32))
    NumberOfGlass = db.Column(db.String(32))
    CavityType = db.Column(db.String(32))
    VentilationChannel = db.Column(db.String(32))
    EcoProgram = db.Column(db.String(32))
    Chimney = db.Column(db.String(32))

    tests = relationship('Test', backref='product')
    
class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Code = db.Column(db.String(10), ForeignKey('product.Code'))  # Foreign key referencing Product
    TestFunction = db.Column(Enum('Cooklight', 'Multifunction',"Static Fan", name='item_status'), nullable=False)
    MeasuredEnergyVentilatedConsumption = db.Column(db.Float(), nullable=True)
    DecleratedEEI = db.Column(Enum("A", "A+" , name = "DecleratedEEI"), nullable=True)