from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///./tasks.db',
    connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(bind=engine)