from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Menu(Base):
    __tablename__ = 'menus'
    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: str = Column(String(200), nullable=False)
    description: str = Column(String(200), nullable=False)


class Submenu(Base):
    __tablename__ = 'submenus'
    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: str = Column(String(200), nullable=False)
    description: str = Column(String(200), nullable=False)
    menu_id: UUID = Column(UUID(as_uuid=True), ForeignKey('menus.id', ondelete='CASCADE'))


class Dish(Base):
    __tablename__ = 'dishes'
    id: UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title: str = Column(String(200), nullable=False)
    description: str = Column(String(200), nullable=False)
    price: str = Column(String(), nullable=False)
    submenu_id: UUID = Column(UUID(as_uuid=True), ForeignKey('submenus.id', ondelete='CASCADE'))
