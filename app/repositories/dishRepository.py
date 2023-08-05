from uuid import UUID

from models import models
from schemas import schemas
from sqlalchemy.orm import Session


def get_dishes(submenu_id: UUID, db: Session) -> list[models.Dish]:
    return db.query(models.Dish).filter(models.Dish.submenu_id == submenu_id).all()


def get_dish(id: UUID, db: Session) -> models.Dish:
    return db.query(models.Dish).filter(models.Dish.id == id).first()


def create_dish(payload: schemas.DishSchema, submenu_id: UUID, db: Session) -> models.Dish:
    dish = models.Dish(**payload.model_dump(), submenu_id=submenu_id)
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


def update_dish(id: UUID, payload: schemas.DishSchema, db: Session) -> models.Dish | None:
    query = db.query(models.Dish).filter(models.Dish.id == id)
    dish = query.first()
    if not dish:
        return None
    update_data = payload.model_dump(exclude_unset=True)
    query.filter(models.Dish.id == id).update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(dish)
    return dish


def delete_dish(id: UUID, db: Session) -> dict[str, bool]:
    query = db.query(models.Dish).filter(models.Dish.id == id)
    dish = query.first()
    if not dish:
        return {'ok': False}
    query.delete(synchronize_session=False)
    db.commit()
    return {'ok': True}
