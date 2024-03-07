from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from models import Alarm, User
from schemas import CreateAlarmRequest, CreateAlarmResponse, UpdateAlarmRequest, UpdateAlarmResponse, DeleteAlarmResponse

app = FastAPI()

@app.post("/alarms", response_model=CreateAlarmResponse)
async def create_alarm(request: CreateAlarmRequest):
    alarm = Alarm.create(**request.dict())
    return {"alarm": alarm}

# @app.get("/alarms", response_model=GetAlarmsResponse)
# async def get_alarms():
#     alarms = Alarm.all()
#     return {"alarms": alarms}

@app.put("/alarms/{alarm_id}", response_model=UpdateAlarmResponse)
async def update_alarm(alarm_id: int, request: UpdateAlarmRequest):
    alarm = Alarm.get(alarm_id)
    if not alarm:
        raise HTTPException(status_code=404, detail="Alarm not found")
    alarm.update(**request.dict())
    return {"alarm": alarm}

@app.delete("/alarms/{alarm_id}", response_model=DeleteAlarmResponse)
async def delete_alarm(alarm_id: int):
    alarm = Alarm.get(alarm_id)
    if not alarm:
        raise HTTPException(status_code=404, detail="Alarm not found")
    alarm.delete()
    return {"success": True}
