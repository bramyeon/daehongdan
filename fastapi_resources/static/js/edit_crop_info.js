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

//--------------------LOAD EDITOR--------------------
let editor_button = document.querySelector("div.edit_crop_schedule_button")
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

    generate_editor_schedule(humidity_editor_table, humidity_times[current_crop_ind], humidity_functions[current_crop_ind], humidity_trs)
    generate_editor_schedule(temperature_editor_table, temperature_times[current_crop_ind], temperature_functions[current_crop_ind], temperature_trs)
    generate_editor_schedule(light_editor_table, light_times[current_crop_ind], light_functions[current_crop_ind], light_trs)

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
    humidity_times[current_crop_ind] = hl[0]
    humidity_functions[current_crop_ind] = hl[1]
    let tl = save_details(temperature_table, temperature_trs)
    temperature_times[current_crop_ind] = tl[0]
    temperature_functions[current_crop_ind] = tl[1]
    let ll = save_details(light_table, light_trs)
    light_times[current_crop_ind] = ll[0]
    light_functions[current_crop_ind] = ll[1]
    clear_editor_table(humidity_editor_table)
    clear_editor_table(temperature_editor_table)
    clear_editor_table(light_editor_table)
    editor_overlay.style["display"] = "none";

    var fetch_body = {
        method: "POST",
        body: JSON.stringify({"crop_name": crop_names[current_crop_ind], "humidity_times":humidity_times[current_crop_ind], "humidity_functions":humidity_functions[current_crop_ind],"light_times":light_times[current_crop_ind], "light_functions":light_functions[current_crop_ind],"temperature_times":temperature_times[current_crop_ind], "temperature_functions":temperature_functions[current_crop_ind]}),
        headers: {"Content-type": "application/json"}
    }

    fetch("update_settings", fetch_body)
})

close_button.addEventListener("click", () => {
    clear_editor_table(humidity_editor_table)
    clear_editor_table(temperature_editor_table)
    clear_editor_table(light_editor_table)
    editor_overlay.style["display"] = "none";
})

