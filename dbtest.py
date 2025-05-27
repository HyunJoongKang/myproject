from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy .orm import declarative_base, sessionmaker
from datetime import datetime

# Database 지정
engine = create_engine('sqlite:///pybo.db')

# ORM 사용
Base = declarative_base()

# User 모델 정의
from pybo.models import Question, Answer

# 세션 생성
Session = sessionmaker(bind=engine)
session = Session()

# 쿼리
item = session.query(Question).filter(Question.id==2).one()
print( item.id, item.subject, item.content, item.create_date)
session.delete(item)
session.commit()

# 새로운 User 객체 생성
#q1 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())
#q2 = Question(subject='플라스크 모델 질문입니다.', content='id는 자동으로 생성되나요?', create_date=datetime.now())

#a1 = Answer(question=q1, content='chatgpt에 물어보십시오', create_date=datetime.now())
#a2 = Answer(question=q2, content='네 자동으로 생성됩니다.', create_date=datetime.now())

# 세션에 추가하고 커밋
#session.add_all([a1, a2])
#session.commit()
