function hideAll(){
    let i = 0;
    for (i = 0; i < 8; i++) {
        if(abas_elem[i] != null)
            abas_elem[i].style.display = "none";
        else{
            console.log("hummm....");
            console.log(i);
        }
    }
}
function call(name) {
    let divname = "div_" + name;
    var x = document.getElementById(divname);
    if (x != null){
        hideAll();
        x.style.display = "block";
    }else{
        console.log("hummm....");
        throw ("Elemento desconhecido: " + divname);
    }
};

let i = 0;
const abas_names = ["resumo", "teoria", "erros", "restricoes", "parametros", "exemplo", "mais", "aplicacao"];
let abas_elem = [];
for(i = 0; i < 8; i++){
	abas_elem.push(document.getElementById("div_" + abas_names[i]));
}
// hideAll();
// document.getElementById(abas_names[0]).style.display = "block"
call(abas_names[0]);