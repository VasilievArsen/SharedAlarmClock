from pydantic import BaseModel
from models import Alarm, User

class CreateAlarmRequest(BaseModel):
    name: str
    time: str
    # participants: list[int]   

class CreateAlarmResponse(BaseModel):
    alarm: Alarm

# class GetAlarmsResponse(BaseModel):
#     alarms: list[Alarm]

class UpdateAlarmRequest(BaseModel):
    name: str
    time: str
    # participants: list[int]

class UpdateAlarmResponse(BaseModel):
    alarm: Alarm

class DeleteAlarmResponse(BaseModel):
    success: bool
