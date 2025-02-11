# SQLAlchemy ORM Examples
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create base class for declarative models
Base = declarative_base()

# Define models
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    orders = relationship("Order", back_populates="user")
    
    def __repr__(self):
        return f"<User(name='{self.name}', email='{self.email}')>"

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    amount = Column(Float)
    user = relationship("User", back_populates="orders")
    
    def __repr__(self):
        return f"<Order(amount={self.amount})>"

def setup_database():
    """Create database and tables"""
    # Create SQLite database in memory
    engine = create_engine('sqlite:///:memory:', echo=True)
    Base.metadata.create_all(engine)
    return engine

def basic_operations(session):
    """Demonstrate basic CRUD operations"""
    # Create
    print("\nCreating new users:")
    user1 = User(name='Alice', email='alice@example.com')
    user2 = User(name='Bob', email='bob@example.com')
    session.add_all([user1, user2])
    session.commit()
    
    # Read
    print("\nQuerying users:")
    users = session.query(User).all()
    for user in users:
        print(user)
    
    # Update
    print("\nUpdating user:")
    user1.email = 'alice.new@example.com'
    session.commit()
    print(user1)
    
    # Delete
    print("\nDeleting user:")
    session.delete(user2)
    session.commit()
    print(f"Remaining users: {session.query(User).count()}")

def relationships_example(session):
    """Demonstrate relationship operations"""
    # Create user with orders
    user = User(name='Charlie', email='charlie@example.com')
    order1 = Order(amount=100.0)
    order2 = Order(amount=200.0)
    user.orders.extend([order1, order2])
    
    session.add(user)
    session.commit()
    
    # Query with relationships
    print("\nUser with orders:")
    user = session.query(User).filter_by(name='Charlie').first()
    print(f"User: {user.name}")
    print("Orders:")
    for order in user.orders:
        print(f"- Amount: ${order.amount}")

def querying_examples(session):
    """Demonstrate various querying techniques"""
    # Add sample data
    users = [
        User(name='David', email='david@example.com'),
        User(name='Eve', email='eve@example.com'),
        User(name='Frank', email='frank@example.com')
    ]
    session.add_all(users)
    session.commit()
    
    print("\nQuerying examples:")
    
    # Filter
    print("\nFiltering:")
    user = session.query(User).filter(User.name == 'David').first()
    print(f"Found user: {user}")
    
    # Like
    print("\nLike query:")
    users = session.query(User).filter(User.email.like('%@example.com')).all()
    print(f"Users with example.com email: {len(users)}")
    
    # Order by
    print("\nOrdered query:")
    users = session.query(User).order_by(User.name).all()
    for user in users:
        print(user.name)

def main():
    # Setup
    engine = setup_database()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    try:
        # Run examples
        basic_operations(session)
        relationships_example(session)
        querying_examples(session)
    finally:
        session.close()

if __name__ == "__main__":
    main() 