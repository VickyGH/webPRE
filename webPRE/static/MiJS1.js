function resulta(){
        num1 = document.getElementById("monto_asignado").value;
        num2 = document.getElementById("monto_ejercido").value;
        document.getElementById("resultado").value = num1 - num2;
}

$(document).ready(function(){


function randomColorChange(){
    return '#'+(Math.floor(Math.random()*16777216)&0xFFFFFF).toString(16);
}


}