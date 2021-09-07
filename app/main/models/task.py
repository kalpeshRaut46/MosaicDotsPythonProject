from datetime import datetime
from flask import Flask
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, BigInteger, Numeric
from sqlalchemy.orm import relationship, declarative_base

from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy.dialects.postgresql import UUID
import uuid

from ..util.db_module import DatabaseModule

engine = DatabaseModule.provide_sqlite_connection

app = Flask(__name__)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# ProjectTask model
class ProjectTask(Base):
    __tablename__ = 'ProjectTask'
    ID = Column(UUID(as_uuid=True), default=uuid.uuid4, nullable=False, primary_key=True)
    Name = Column(String(1000), nullable=False)
    Description = Column(String(1000), nullable=True)
    TaskNumber = Column(Integer, nullable=False)
    DisplayOrder = Column(Integer, nullable=False)
    PriorityID = Column(Integer, ForeignKey('Priority.id'), nullable=False)
    StatusID = Column(Integer, ForeignKey('Status.id'), nullable=False)
    StartDate = Column(DateTime, nullable=False)
    EndDate = Column(DateTime, nullable=False)
    AssignedUserID = Column(UUID(as_uuid=True), ForeignKey('AssignedUser.id'), default=uuid.uuid4, nullable=False)
    DeactivationDate = Column(DateTime, nullable=True)
    TransactionHeaderID = Column(BigInteger, ForeignKey('TransactionHeader.id'), nullable=False)
    IsExecutionMilestone = Column(Boolean, default=0, nullable=False)
    IsFiscalMilestone = Column(Boolean, default=0, nullable=False)
    ProjectDivisionID = Column(UUID(as_uuid=True), ForeignKey('ProjectDivision.id'), default=uuid.uuid4, nullable=False)
    ParentProjectTaskID = Column(UUID(as_uuid=True), ForeignKey('ParentProjectTask.id'), default=uuid.uuid4, nullable=False)
    SysStartTime = Column(DateTime, default=datetime.utcnow)
    SysEndTime = Column(DateTime, default=datetime.utcnow)
    ProjectZoneID = Column(UUID(as_uuid=True), ForeignKey('ProjectZone.id'), default=uuid.uuid4, nullable=False)
    ProjectID = Column(UUID(as_uuid=True), ForeignKey('Project.id'), default=uuid.uuid4, nullable=False)
    IsEngineeringMilestone = Column(Boolean, default=0, nullable=False)
    Duration = Column(Integer, nullable=True)

    # AssignedUserIDFk = relationship("AssignedUserID", backref="AssignedUser_ID")
    # ProjectIDFk = relationship("ProjectID", backref="Project_ID")
    # ProjectZoneIDFk = relationship("ProjectZoneID", backref="Project_Zone_ID")
    # ProjectDivisionIDFk = relationship("ProjectDivisionID", backref="Project_Division_ID")
    # ParentProjectTaskIDFk = relationship("ParentProjectTaskID", backref="Parent_Project_Task_ID")
    # PriorityIDFk = relationship("PriorityID", backref="Priority_ID")
    # TransactionHeaderIDFk = relationship("TransactionHeaderID", backref="transaction_header_id")
    # StatusIDFk = relationship("StatusID", backref="Status_ID")


if __name__ == "__main__":
    app.run(debug=True)
