import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from edit_crop import edit_app
from add_crop import add_app
import utils
#--------------------FASTAPI SETUP--------------------
app=FastAPI()
templates = Jinja2Templates(directory="./fastapi_resources/templates")
app.mount("/static", StaticFiles(directory="./fastapi_resources/static"), name="static")

#--------------------MAIN APP SETUP--------------------
@app.get("/")
def root(request: Request):
    crop_names, crop_img_paths, humidity_times,humidity_vals,light_times,light_vals,temperature_times,temperature_vals = utils.process_crop_info()
    return templates.TemplateResponse("home.html", {"request": request, "crop_names":crop_names, "crop_img_paths":crop_img_paths, \
        "humidity_times":humidity_times, "humidity_functions":humidity_vals,"light_times":light_times, "light_functions":light_vals,\
        "temperature_times":temperature_times, "temperature_functions":temperature_vals})

@app.post("/upload_settings")
async def upload_settings(request: Request):
    _ = await request.json()
    print("UPLOADING SETTINGS")
    return {"message":"message"}

#--------------------TEMPLATING APPS--------------------
@edit_app.get("/")
def edit_root(request: Request):
    crop_names, crop_img_paths, humidity_times,humidity_vals,light_times,light_vals,temperature_times,temperature_vals = utils.process_crop_info()
    return templates.TemplateResponse("edit_crop_info.html", {"request": request, "crop_names":crop_names, "crop_img_paths":crop_img_paths, \
        "humidity_times":humidity_times, "humidity_functions":humidity_vals,"light_times":light_times, "light_functions":light_vals,\
        "temperature_times":temperature_times, "temperature_functions":temperature_vals})
edit_app.mount("/static", StaticFiles(directory="./fastapi_resources/static"), name="static")

@add_app.get("/")
def edit_root(request: Request):
    crop_names, crop_img_paths, humidity_times,humidity_vals,light_times,light_vals,temperature_times,temperature_vals = utils.process_crop_info()
    return templates.TemplateResponse("add_crop.html", {"request": request, "crop_names":crop_names, "crop_img_paths":crop_img_paths, \
    "humidity_times":humidity_times, "humidity_functions":humidity_vals,"light_times":light_times, "light_functions":light_vals,\
    "temperature_times":temperature_times, "temperature_functions":temperature_vals})
add_app.mount("/static", StaticFiles(directory="./fastapi_resources/static"), name="static")

#--------------------MOUNTING APPS--------------------
app.mount("/edit_crop_info", edit_app)
app.mount("/add_crop", add_app)

#--------------------RUNNING--------------------
if __name__ == "__main__":
    uvicorn.run(app)