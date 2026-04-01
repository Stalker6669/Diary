from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

engine = create_engine('sqlite:///Diary.db')
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String, nullable=False)  # nullable - параметр об отсутствии данных


class Record(Base):
    __tablename__ = "records"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))  # Заголовок
    content = Column(Text)
    # Передаем саму функцию utcnow БЕЗ скобок, чтобы она вызывалась в момент создания записи
    created_at = Column(DateTime, default=datetime.now)  # Автоматическая фиксация времени создания.
    # Указываем 'имя_таблицы.имя_колонки'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


def start_db():
    Base.metadata.create_all(engine)
