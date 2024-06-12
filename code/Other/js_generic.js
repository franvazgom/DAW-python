
const typeBtns = ['primary', 'success', 'danger', 'secondary', 'warning', 'info', 'dark'];
const btnClassName = {
    primary:{
        notSelected: 'btn btn-outline-primary btn-sm m-1', 
        selected: 'btn btn-primary btn-sm m-1'
    },
    success:{
        notSelected: 'btn btn-outline-success btn-sm m-1', 
        selected: 'btn btn-success btn-sm m-1'
    },
    danger:{
        notSelected: 'btn btn-outline-danger btn-sm m-1', 
        selected: 'btn btn-danger btn-sm m-1'
    },
    secondary:{
        notSelected: 'btn btn-outline-secondary btn-sm m-1', 
        selected: 'btn btn-secondary btn-sm m-1'
    },
    warning:{
        notSelected: 'btn btn-outline-warning btn-sm m-1', 
        selected: 'btn btn-warning btn-sm m-1'
    },
    info:{
        notSelected: 'btn btn-outline-info btn-sm m-1', 
        selected: 'btn btn-info btn-sm m-1'
    },
    dark:{
        notSelected: 'btn btn-outline-dark btn-sm m-1', 
        selected: 'btn btn-dark btn-sm m-1'
    }
}

function test() {
    for (let i=0; i<=10; i++) {
        let id = "btn" + String(i);
        let text = "Botonsin " + String(i);
        let btn = createBtn(id, text, btnClassName.dark.notSelected);
        addBtnContainer("container_1", btn);
    }

    for (let i=0; i<=10; i++) {
        let id = "btn" + String(i);
        let text = "Botón " + String(i);
        let btn = createBtn(id, text, btnClassName.secondary.notSelected);
        addBtnContainer("container_2", btn);
    }
}

/* 
Function: createBtn
Create a button example:  
let btn1 = createBtn("btn1", "Button Text", "btnClassName.dark.notSelected");
*/
function createBtn(id, text, className, disabled=false) {
    const btn = document.createElement('button');
    btn.id = id;
    btn.textContent = text;
    btn.className = className;
    btn.disabled = disabled;
    btn.addEventListener('click', changeBtnSelected);
    return btn;    
}

/* 
Function: changeBtnSelected
If class name's button is "selected", change to not selected class and viceversa 
*/
function changeBtnSelected() {    
    const typeBtn = getTypeBtn(this);
    if (this.className == eval("btnClassName." + typeBtn + ".selected")) {
        this.className = eval("btnClassName." + typeBtn + ".notSelected");
    }else {
        this.className = eval("btnClassName." + typeBtn + ".selected");
    }
}

/* 
Function: removeFilterContainer
For all buttons inside the container, change set the class name to not selected
*/ 
function removeFilterContainer(containerId) {    
    const buttons = document.getElementById(containerId).querySelectorAll('button');
    buttons.forEach((btn, index) => {
        const typeBtn = getTypeBtn(btn);
        btn.className = eval("btnClassName." + typeBtn + ".notSelected");        
    });
}

function addBtnContainer(containerId, btn) {
    document.getElementById(containerId).appendChild(btn);    
}

/* 
Function:getDataFiltered 
Return an array with the text content of buttons that are selected 
*/
function getDataFiltered(containerId) {
    const btns = document.getElementById(containerId).querySelectorAll('button');
    let result = [];
    const typeBtn = getTypeBtns(containerId);
    const clNameSelected = eval("btnClassName." + typeBtn + ".selected");
    btns.forEach((btn, index) => {        
        if (btn.className == clNameSelected) {
            result.push(btn.textContent);
        }
    });
    return result;
}

/* 
Function: getTypeBtns
Return type of the first button in the container, according to the const typeBtns array
*/
function getTypeBtns(containerId) {
    const fbtn = document.getElementById(containerId).querySelector('button');    
    return getTypeBtn(fbtn);
}

/* 
Function:getTypeBtn
Return type of the button, according to the const typeBtns array
*/
function getTypeBtn(btn) {    
    const className = btn.className;    
    for (let i=0; i<typeBtns.length; i++){
        if (className.includes(typeBtns[i])) {            
            return typeBtns[i];
        }
    }
    console.error("getTypeBtn: typeBtns not found, className:", className);
    return null;
}

/* 
Function:Load function
*/
document.addEventListener('DOMContentLoaded', function() {    
    test();
});
