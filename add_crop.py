from fastapi import FastAPI, Request
import utils
add_app=FastAPI()

@add_app.post("/save_crop")
async def upload_settings(request: Request):
    data = await request.json()
    utils.add_crop(data["crop_name"], data["humidity_times"], data["humidity_functions"], data["light_times"], \
        data["light_functions"], data["temperature_times"], data["temperature_functions"])
    return {"message":"message"}