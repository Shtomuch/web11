from sqlalchemy.orm import Session
from . import models, schemas

def get_contact(db: Session, contact_id: int):
    return db.query(models.Contact).filter(models.Contact.id == contact_id).first()

def get_contacts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Contact).offset(skip).limit(limit).all()

def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def update_contact(db: Session, contact_id: int, contact: schemas.ContactUpdate):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    for key, value in contact.dict().items():
        setattr(db_contact, key, value)
    db.commit()
    db.refresh(db_contact)
    return db_contact

def delete_contact(db: Session, contact_id: int):
    db_contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    db.delete(db_contact)
    db.commit()
    return db_contact

def search_contacts(db: Session, query: str):
    return db.query(models.Contact).filter(
        (models.Contact.first_name.contains(query)) |
        (models.Contact.last_name.contains(query)) |
        (models.Contact.email.contains(query))
    ).all()

def get_upcoming_birthdays(db: Session, days: int):
    from datetime import datetime, timedelta
    today = datetime.today().date()
    future_date = today + timedelta(days=days)
    return db.query(models.Contact).filter(models.Contact.birthday.between(today, future_date)).all()