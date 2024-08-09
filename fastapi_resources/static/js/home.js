//--------------------DATA--------------------
// let crop_names = ["Crop 1", "Crop 2", "Crop 3"]
// let crop_img_paths = ["../static/imgs/crop1.png","../static/imgs/crop2.png","../static/imgs/crop3.png"]
// let humidity_times=[["00:00","14:00","15:00","16:00","18:00","20:00"],["15:00","16:00","18:00","20:00"], ["00:00","14:00"]]
// let humidity_functions=[["1","2","3"],["3","2"],["1"]]
// let light_times=[["00:00","14:00","15:00","16:00","18:00","20:00"],["15:00","16:00","18:00","20:00"], ["00:00","14:00"]]
// let light_functions=[["1","2","3"],["3","2"],["1"]]
// let temperature_times=[["00:00","14:00","15:00","16:00","18:00","20:00"],["15:00","16:00","18:00","20:00"], ["00:00","14:00"]]
// let temperature_functions=[["1","2","3"],["3","2"],["1"]]

//--------------------LOAD CROP LIST--------------------
let crop_list = document.querySelector("div.crop_list")
let current_crop_ind = 0

for(let i=0; i<crop_names.length; i++){
    let list_element_i = document.createElement("div")

    list_element_i.innerText = crop_names[i]
    list_element_i.className = "crop_list_element"

    list_element_i.addEventListener("click", () => {
        crop_list.children[current_crop_ind].classList.remove("crop_list_selected")
        crop_list.children[i].classList.add("crop_list_selected")
        current_crop_ind=i
        load_crop_info()
    })
    
    crop_list.appendChild(list_element_i)
}

crop_list.children[0].classList.add("crop_list_selected")

//--------------------LOAD CROP INFO--------------------
let current_crop_name_div = document.querySelector("div.crop_info_name")
let current_crop_img = document.querySelector("img.crop_info_image")
let humidity_table = document.querySelector("table.crop_info_humidity_table>tbody")
let temperature_table = document.querySelector("table.crop_info_temperature_table>tbody")
let light_table = document.querySelector("table.crop_info_light_table>tbody")

function load_crop_info(){
    clear_table(humidity_table)
    clear_table(temperature_table)
    clear_table(light_table)

    current_crop_name_div.innerText = crop_names[current_crop_ind]
    current_crop_img.src = crop_img_paths[current_crop_ind]

    generate_schedule(humidity_table, humidity_times[current_crop_ind], humidity_functions[current_crop_ind])
    generate_schedule(temperature_table, temperature_times[current_crop_ind], temperature_functions[current_crop_ind])
    generate_schedule(light_table, light_times[current_crop_ind], light_functions[current_crop_ind])
}

function generate_schedule(schedule_table, schedule_times, schedule_function){
    for(let i=0; i<schedule_function.length; i++){
        let tr_i = document.createElement("tr")
        let td_time_i = document.createElement("td")
        let td_func_i = document.createElement("td")
    
        td_time_i.innerText = `${schedule_times[2*i]}-${schedule_times[2*i+1]}`
        td_func_i.innerText = schedule_function[i]
    
        tr_i.appendChild(td_time_i)
        tr_i.appendChild(td_func_i)
        schedule_table.appendChild(tr_i)
    }
}

function clear_table(schedule_table){
    while (schedule_table.firstChild) {
        schedule_table.removeChild(schedule_table.firstChild);
    }
}

load_crop_info()

//--------------------UPLOAD SETTINGS--------------------
let upload_button = document.querySelector("div.upload_settings")
upload_button.addEventListener("click", () => {
    var fetch_body = {
        method: "POST",
        // body: JSON.stringify({"crop_name": crop_names[current_crop_ind], "humidity_times":humidity_times[current_crop_ind], "humidity_functions":humidity_functions[current_crop_ind],"light_times":light_times[current_crop_ind], "light_functions":light_functions[current_crop_ind],"temperature_times":temperature_times[current_crop_ind], "temperature_functions":temperature_functions[current_crop_ind],}),
        body: JSON.stringify({"crop_name": 2}),
        headers: {"Content-type": "application/json"}
    }
    fetch("/upload_settings", fetch_body)
})