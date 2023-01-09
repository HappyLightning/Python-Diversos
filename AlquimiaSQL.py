from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func  # Criar tabelas.
import datetime

Base = declarative_base()


class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=True)

    def __repr__(self):
        return "<Cliente(nome='%s')>" % self.nome


queijos_comprados = Table(
    'queijos_comprados', Base.metadata,
    Column('compra_id', Integer, ForeignKey('compras.id', primary_key=True)),
    Column('queijo_id', Integer, ForeignKey('queijos_id', primary_key=True))
)


class Queijo(Base):
    __tablename__ = 'queijos'
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=False)
    compras = relationship('Compra', secondary='queijos_comprados', back_populates='queijos')

    def __repr__(self):
        return "<Queijo(tipo='%s')>" % self.tipo


class Compra(Base):
    __tablename__ = 'compras'
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('clientes.id', primary_key=True))
    data_compra = Column(Date, nullable=False)
    cliente = relationship('Cliente')
    queijos = relationship('Queijo', secondary='queijos_comprados', back_populates='compras')

    def __repr__(self):
        return "<Compra(cliente='%s', dt='%s')>" % (self.cliente.nome, self.data_compra)


# Criar tabelas pela base declarativa:
engine = create_engine('sqlite://')
Base.metadata.create_all(engine)

# Iteração ORM.
Session = sessionmaker(bind=engine)
sess = Session()
# Queijos
leicester = Queijo(tipo='Leicester Vermelho')
camembert = Queijo(tipo='Camembert')
sess.add_all((camembert, leicester))
# Clientes
gato = Cliente(name='Gato')
sess.add(gato)
sess.commit()  # Insere alterações no banco de dados.

d = datetime.date(1971, 12, 18)
p = Compra(data_compra=d, cliente=gato)
# Os objetos do relacionamento muitos-para-muitos não são adicionados durante a instânciação - eles têm de ser acrescentados após o fato.
p.queijos.append(camembert)

# Consultas.
for row in sess.query(Compra, Queijo).filter(Compra.queijos):
    print(row)
