# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context

from app import create_app, db
from app.models.cat import Cat
from app.models.caretaker import Caretaker
from dotenv import load_dotenv

load_dotenv()

my_app = create_app()
with my_app.app_context():
    db.session.add(Caretaker(name="Jill")),
    db.session.add(Caretaker(name="Jasmine")),
    db.session.add(Caretaker(name="Monica")),
    db.session.add(Caretaker(name="Fantasia")),
    db.session.add(Caretaker(name="Lauryn")),
    db.session.add(Caretaker(name="Janet")),
    db.session.add(Cat(name="Luna", color="ash", caretaker_id=1, personality="Tomato Queen")),
    db.session.add(Cat(name="Simon", color="black", caretaker_id=2, personality="might be a human stuck in a cats body")),
    db.session.add(Cat(name="Midnight", color="black", personality="skittish")),
    db.session.add(Cat(name="Leo", color="gray tabby", caretaker_id=4, personality="friendly")),
    db.session.add(Cat(name="Ash", color="gray", personality="cranky")),
    db.session.add(Cat(name="Alder", color="auburn", personality="bouncy, trouncy, flouncy, pouncy, fun, fun, fun, fun, fun")),
    db.session.add(Cat(name="Morty", color="orange", caretaker_id=3, personality="orange")),
    db.session.add(Cat(name="fluffy", color="white", caretaker_id=3, personality="evil with a hint of benevolent")),
    db.session.add(Cat(name="Reginold", color="orange", personality="only has one brain cell, but is descendent of Reginold the Great Tabby")),
    db.session.add(Cat(name="Katosa", color="gray tabby", caretaker_id=6, personality="Crazy Hunter")),
    db.session.add(Cat(name="Milly", color="Tortoiseshell", personality="Loves you a lot but will probably sneeze all over you")),
    db.session.add(Cat(name="Meryl", color="Tortoiseshell", caretaker_id=5, personality="Bossy but tries to pass as the sweet one")),
    db.session.add(Cat(name="Zelda", color="white, gray", caretaker_id=2, personality="a mystery")),
    db.session.add(Cat(name="Jupiter", color="orange", personality="socially selective")),
    db.session.add(Cat(name="Neo", color="black", personality="stoic")),
    db.session.add(Cat(name="Gato", color="grey", caretaker_id=4, personality="fun")),
    db.session.add(Cat(name="Red XIII", color="red", personality="serious")),
    db.session.add(Cat(name="Gizzy", color="white", caretaker_id=5, personality="unbothered")),
    db.session.commit()