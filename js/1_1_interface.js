

function get_f(){
  return entry_f.value;
}
function get_a(){
  return entry_a.value;
}
function get_b(){
  return entry_b.value;
}
function get_n(){
  return entry_n.value;
}
function get_t(){
  return entry_t.value;
}
function get_all_entry(){
	var f = get_f();
	var a = get_a();
	var b = get_b();
	var n = get_n();
	var t = get_t();

	return [f, a, b, n, t];
}




function verify_function(f){
	if ( f == "" )
		throw "Funcao vazia!";
 	var node = math.parse(f);
}
function verify_interval(a, b){

	var float_a = Number(a);
	var float_b = Number(b);
	var valid_a = isNaN(float_a) ? false : true;
	var valid_b = isNaN(float_b) ? false : true;

	if ( float_a >= float_b )
		throw "Valor de A eh maior ou igual ao B";
	else if ( a == "" && b == "" ) 
		throw "Ambos intervalos sao vazios!";
	else if ( valid_a && b == "" )
		throw "O valor de B esta em branco!";
	else if ( a == "" && valid_b )
		throw "O valor de A esta em branco!";
	else if ( !valid_a )
		throw "O valor de A nao eh valido!";
	else if ( !valid_b )
		throw "O valor de B nao eh valido!";
}
function verify_iteraction(n){
	if ( n < 2 )
		throw "Numero de iteracoes muito pequeno!";
}
function verify_tolerance(t){
	if (t <= 0)
		throw "Valor da tolerância deve ser positivo!"
}
function verify_all_entry(f, a, b, n, t)
{
	verify_function(f);
	verify_interval(a, b);
	verify_iteraction(n);
	verify_tolerance(t);
}






function update_function(evt){
	var f = get_f();
	var own_name = "function";

	try{
		verify_function(f);
		show_icon(own_name, "correct");
	} catch (err) {
		if (f == "")
			show_icon(own_name, "none");
		else
			show_icon(own_name, "error");
	}
}
function update_interval(){
	var a = get_a();
	var b = get_b();
	
	var own_name = "interval";

	try{
		verify_interval(a, b);
		show_icon(own_name, "correct");
	} catch (err) {
		if ( a == "" || b == "" )
			show_icon(own_name, "none");
		else
			show_icon(own_name, "error");
	}
}
function update_iteraction(){
	var n = get_n();
	var own_name = "n";

	try{
		verify_iteraction(n);
		show_icon(own_name, "correct");
	} catch (err) {
		if (n == "")
			show_icon(own_name, "none");
		else
			show_icon(own_name, "error");
	}
}
function update_tolerance(){
	var t = get_t();
	var own_name = "tol";
	try{
		verify_tolerance(t);
		show_icon(own_name, "correct");
	} catch (err) {
		if (t == "")
			show_icon(own_name, "none");
		else
			show_icon(own_name, "error");
	}
}



function show_icon(param, state){
	document.getElementById("icon_correct_" + param).style.display = "none";
	document.getElementById("icon_warning_" + param).style.display = "none";
	document.getElementById("icon_error_" + param).style.display = "none";
	if(state == "correct")
		document.getElementById("icon_correct_" + param).style.display = "block";
	else if(state == "warning")
		document.getElementById("icon_warning_" + param).style.display = "block";
	else if(state == "error")
		document.getElementById("icon_error_" + param).style.display = "block";
}



function is_Digit(charCode){
	if ( 47 < charCode && charCode < 58 )
		return true;
	return false;
}
function is_Float(charCode){
	// 43: +
	// 45: -
	// 46: .
	// 69: E
	// 101: e
    if ( is_Digit(charCode) )
        return true;
   	if ( charCode == 45 || charCode == 46 )
   		return true;
   	if ( charCode == 43 || charCode == 69 || charCode == 101 )
   		return true;
    return false;
}
function validation_natural(evt){
	var charCode = (evt.which) ? evt.which : evt.keyCode;
    if ( charCode > 31 )
	    return is_Digit(charCode);
	else
		return true;
}
function validation_float(evt){
	var charCode = (evt.which) ? evt.which : evt.keyCode;
    if ( charCode > 31 ){
    	return is_Float(charCode);
	}
	else
		return true;
}



function treat_function(f){
	return f;
}
function treat_interval(a, b){
	a = parseFloat(a);
	b = parseFloat(b);
	return [a, b];
}
function treat_iteractions(n){
	return parseInt(n);
}
function treat_tolerance(t){
	return parseFloat(t);
}
function treat_all(f, a, b, n, t){

	f = treat_function(f);
	[a, b] = treat_interval(a, b);
	n = treat_iteractions(n);
	t = treat_tolerance(t);

	return [f, a, b, n, t];
}




function get_downloadable_input(){
	var msg = "";
	var f, a, b, n, t;
	[f, a, b, n, t] = get_all_entry();
	verify_all_entry(f, a, b, n, t);
	[f, a, b, n, t] = treat_all(f, a, b, n, t);

	msg += "Function: " + f + "\n";
	msg += "Interval: [" + a.toString() + ", " + b.toString() + "]\n";
	msg += "Iteractions: " + n.toString() + "\n";
	msg += "Tolerance: " + t.toString();
	return msg;
}




function click_Calcular(){
	var f, a, b, n, t;

	try{
		[f, a, b, n, t] = get_all_entry();
		verify_all_entry(f, a, b, n, t);
		[f, a, b, n, t] = get_all_entry();
		[f, a, b, n, t] = treat_all(f, a, b, n, t);
		begin_calculation(f, a, b, n, t);	
	} catch (err){
		throw err;
	}
}



function give_to_parameters(txt) {
	const filtro_natural = /([0-9]*)/
	const filtro_float = /[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?/;
	const filtro_funcao = /Function: (.*)/;
	const filtro_intervalo = /Interval: \[(.*), (.*)\]/;
	const filtro_iteracoes = /Iteractions: (.*)/;
	const filtro_tolerancia = /Tolerance: (.*)/;
	let res_f = filtro_funcao.exec(txt);
	let res_L = filtro_intervalo.exec(txt);
	let res_n = filtro_iteracoes.exec(txt);
	let res_t = filtro_tolerancia.exec(txt);


	if (!(res_f && res_L && res_n && res_t)){
		throw "Arquivo invalido!";
	}else if( false){
		throw "Arquivo invalido!";
	}

	let f = res_f[1];
	let a = res_L[1];
	let b = res_L[2];
	let n = res_n[1];
	let t = res_t[1];

	try{
		verify_all_entry(f, a, b, n, t);

		entry_f.value = f;
		entry_a.value = a;
		entry_b.value = b;
		entry_n.value = n;
		entry_t.value = t;
	}catch(err){
		throw "Nao foi possivel importar o arquivo. " + err.toString();
	}
	// let res_L = filtro_float

	// var f = res_f[1]
	// var [a, b] = filtro_float.exec(res_L[1])[1];
	// var n = filtro_float.exec(res_n[1])[1];
	// var t = filtro_float.exec(res_t[1])[1];

	// console.log(f);
	// console.log(a);
	// console.log(b);
	// console.log(n);
	// console.log(t);
} 
