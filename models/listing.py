from models import Base
from sqlalchemy import Integer, String, DateTime, Float, Column, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Listing(Base):
    __tablename__ = 'listing'

    id = Column(Integer, primary_key=True)

    property_type = Column(String)

    building_style = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)

    root_url = Column(String)
    root_website = Column(String)

    urls = relationship('Url', back_populates='listing_id')
    prices = relationship('Price', back_populates='listing_id')
    rooms = relationship('Room', back_populates='listing_id')

    bedroom_nb = Column(Integer)
    bathroom_nb = Column(Integer)

    lot_area = Column(Float)
    house_width = Column(Float)
    house_length = Column(Float)
    year_built = Column(Integer)

    municipal_assessment = Column(Float)

    municipal_taxes = Column(Float)
    school_taxed = Column(Float)

    windows = Column(String)
    foundation = Column(String)
    siding = Column(String)
    roofing = Column(String)

    kitchen_cabinet = Column(String)
    basement = Column(String)

    description= Column(String)


    def __init__(self, root_url, root_website):
        self.root_url = root_url
        self.root_website = root_website

    def add_price(self, price, observation_date=None):
        self.prices.append(Price(price, observation_date))

    def add_room(self, room_name):
        self.rooms.append(Room(room_name))

    def add_url(self, url, website):
        self.urls.append(Url(url, website))


class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listing.id'))

    url = Column(String)
    website = Column(String)

    listing = relationship('Listing', back_populates='urls')


class Price(Base):
    __tablename__ = 'price'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listing.id'))

    price = Column(Float)
    observation_date = Column(DateTime)

    listing = relationship('Listing', back_populates='prices')

    def __init__(self, price, observation_date=None):
        self.price = price
        if observation_date is None:
            self.observation_date = datetime.now()
        else:
            self.observation_date = observation_date


class Room(Base):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listing.id'))

    width = Column(Float)
    length = Column(Float)

    name = Column(String)
    level = Column(String)
    flooring = Column(String)
    description = Column(String)

    listing = relationship('Listing', back_populates='rooms')

    def __init__(self, name):
        self.name = name
