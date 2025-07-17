from db import engine, SessionLocal
from models import Base, User

def init_db():
    Base.metadata.create_all(bind=engine)


def create_user(name: str, email: str):
    session = SessionLocal()
    user = User(name=name, email=email)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    print(f"User created: {user.name} ({user.email})")

def list_users():
    session = SessionLocal()
    users= session.query(User).all()
    for user in users:
        print(f"[{user.id}] {user.name} - {user.email}")
    session.close()

if __name__ == "__main__":
    init_db()
    create_user("Alice", "alice@example.com")
    create_user("Bob", "bob@example.com")
    list_users()

