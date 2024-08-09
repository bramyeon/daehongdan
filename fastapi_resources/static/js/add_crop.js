//--------------------DATA--------------------
// let all_crops = ["Crop 1", "crop 3", "21or21o", "2112kr", "2owfwq9ef","iriierg"]

let current_crop_name = ""
var humidity_times=[]
var humidity_functions=[]
var temperature_times=[]
var temperature_functions=[]
var light_times=[]
var light_functions=[]

//--------------------LOAD EDITOR--------------------
let humidity_table = document.querySelector("table.crop_info_humidity_table>tbody")
let temperature_table = document.querySelector("table.crop_info_temperature_table>tbody")
let light_table = document.querySelector("table.crop_info_light_table>tbody")

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

let editor_button = document.querySelector("div.edit_schedules")
let editor_overlay = document.querySelector("div.edit_schedule_overlay")
let humidity_editor_table = document.querySelector("table.crop_info_humidity_editor_table>tbody")
let temperature_editor_table = document.querySelector("table.crop_info_temperature_editor_table>tbody")
let light_editor_table = document.querySelector("table.crop_info_light_editor_table>tbody")
let humidity_trs = []
let temperature_trs = []
let light_trs = []
let add_row_flags = 0

editor_button.addEventListener("click", () => {
    humidity_trs = humidity_editor_table.children
    temperature_trs = temperature_editor_table.children
    light_trs = light_editor_table.children

    console.log(humidity_times)

    generate_editor_schedule(humidity_editor_table, humidity_times, humidity_functions, humidity_trs)
    generate_editor_schedule(temperature_editor_table, temperature_times, temperature_functions, temperature_trs)
    generate_editor_schedule(light_editor_table, light_times, light_functions, light_trs)

    editor_overlay.style["display"] = "flex";
})

function generate_editor_schedule(schedule_table, schedule_times, schedule_function, schedule_trs){
    if(add_row_flags<3){
        schedule_trs[schedule_trs.length-1].addEventListener("click", () => {
            let tr_i = document.createElement("tr")
            let td_time_i = document.createElement("td")
            let td_func_i = document.createElement("td")
            let td_remove_i = document.createElement("td")
            td_time_i.innerHTML='<input type="text" class="edit_schedule_input" value="00:00">-<input type="text" class="edit_schedule_input" value="00:00">'
            td_func_i.innerHTML='<input type="text" class="edit_schedule_input func" value="0">'
            td_remove_i.innerText="-"
            
            tr_i.appendChild(td_time_i)
            tr_i.appendChild(td_func_i)
            tr_i.appendChild(td_remove_i)
    
            td_remove_i.addEventListener("click", () => {
                tr_i.remove()
            })
    
            schedule_table.insertBefore(tr_i, schedule_trs[schedule_trs.length-1])
        })
        add_row_flags+=1
    }

    for(let i=0; i<schedule_function.length; i++){
        let tr_i = document.createElement("tr")
        let td_time_i = document.createElement("td")
        let td_func_i = document.createElement("td")
        let td_remove_i = document.createElement("td")
    
        td_time_i.innerHTML=`<input type="text" class="edit_schedule_input" value="${schedule_times[2*i]}">-<input type="text" class="edit_schedule_input" value="${schedule_times[2*i+1]}">`
        td_func_i.innerHTML=`<input type="text" class="edit_schedule_input func" value="${schedule_function[i]}">`
        td_remove_i.innerText = "-"

        td_remove_i.addEventListener("click", () => {
            tr_i.remove()
        })
    
        tr_i.appendChild(td_time_i)
        tr_i.appendChild(td_func_i)
        tr_i.appendChild(td_remove_i)
        schedule_table.insertBefore(tr_i, schedule_trs[schedule_trs.length-1])
    }
}

//--------------------EXIT EDITOR--------------------
let save_button = document.querySelector("div.save_setting")
let close_button = document.querySelector("div.close_editor")

function clear_table(schedule_table){
    while (schedule_table.firstChild) {
        schedule_table.removeChild(schedule_table.firstChild);
    }
}

function clear_editor_table(schedule_table){
    while (schedule_table.firstChild) {
        if(schedule_table.children.length==1){
            break
        }
        schedule_table.removeChild(schedule_table.firstChild);
    }
}

function save_details(schedule_table, schedule_trs){
    let temp_schedule_times=[]
    let temp_schedule_functions=[]

    for(let i=0; i<schedule_trs.length-1; i++){
        let inputs_i = schedule_trs[i].querySelectorAll("input")
        temp_schedule_times.push(inputs_i[0].value)
        temp_schedule_times.push(inputs_i[1].value)
        temp_schedule_functions.push(inputs_i[2].value)
    }

    generate_schedule(schedule_table, temp_schedule_times, temp_schedule_functions)

    return [temp_schedule_times, temp_schedule_functions]
}

save_button.addEventListener("click", () => {
    clear_table(humidity_table)
    clear_table(temperature_table)
    clear_table(light_table)
    let hl = save_details(humidity_table, humidity_trs)
    humidity_times = hl[0]
    humidity_functions = hl[1]
    let tl = save_details(temperature_table, temperature_trs)
    temperature_times = tl[0]
    temperature_functions = tl[1]
    let ll = save_details(light_table, light_trs)
    light_times = ll[0]
    light_functions = ll[1]
    clear_editor_table(humidity_editor_table)
    clear_editor_table(temperature_editor_table)
    clear_editor_table(light_editor_table)
    editor_overlay.style["display"] = "none";
})

close_button.addEventListener("click", () => {
    clear_editor_table(humidity_editor_table)
    clear_editor_table(temperature_editor_table)
    clear_editor_table(light_editor_table)
    editor_overlay.style["display"] = "none";
})

//--------------------ADD IMAGE--------------------
let select_image_button = document.querySelector("div.image_upload_container")
let img_input = document.querySelector("input.img_input")

select_image_button.addEventListener("click", () => {
    img_input.click()
})

img_input.addEventListener("change", () => {
    let [img_file] = img_input.files
    if(img_file){
        let new_img = document.createElement("img")
        new_img.className="crop_img"
        new_img.src = URL.createObjectURL(img_file)
        select_image_button.appendChild(new_img)
    }
})

//--------------------SAVE CROP--------------------
let add_crop = document.querySelector("div.save_crop")
let crop_name = document.querySelector("input.crop_info_name")

add_crop.addEventListener("click", () => {
    var fetch_body = {
        method: "POST",
        body: JSON.stringify({"crop_name": crop_name.value, "humidity_times":humidity_times, "humidity_functions":humidity_functions,"light_times":light_times, "light_functions":light_functions,"temperature_times":temperature_times, "temperature_functions":temperature_functions}),
        headers: {"Content-type": "application/json"}
    }

    fetch("save_crop", fetch_body)
})