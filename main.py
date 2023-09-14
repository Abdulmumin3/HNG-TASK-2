from fastapi import FastAPI, Depends, HTTPException, status
from starlette.background import P
import schemas, models
from sqlalchemy.orm import Session
from database import SessionLocal, engine



app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.post('/api', status_code=status.HTTP_201_CREATED)
def create_person(request: schemas.Person, db: Session = Depends(get_db),):
	new_person = models.Person(name=request.name, age=request.age, track=request.track)
	db.add(new_person)
	db.commit()
	db.refresh(new_person)
	return new_person



# The code you provided defines two API endpoints using the FastAPI framework.
@app.get('/api/', status_code=status.HTTP_200_OK)
def fetch_people(db: Session = Depends(get_db)):
	people = db.query(models.Person).all()
	return people

@app.get('/api/{user_id}', status_code=status.HTTP_200_OK)
def get_person_by_name(user_id: str, db: Session = Depends(get_db)):
	person = db.query(models.Person).filter(models.Person.name == user_id).first()
	if person is None:
		raise HTTPException(status_code=404, detail='User not found')
	return person

@app.delete('/api/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_person_by_name(user_id: str, db: Session = Depends(get_db)):
    db.query(models.Person).filter(models.Person.name == user_id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@app.put('/api/{user_id}', status_code=status.HTTP_202_ACCEPTED)
def update_person_by_name(user_id: str, request: schemas.Person, db: Session = Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.name == user_id)
    if not person.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User `{user_id}` not found")
    person_data = request.dict()
    person.update(person_data)
    db.commit()
    return 'updated'