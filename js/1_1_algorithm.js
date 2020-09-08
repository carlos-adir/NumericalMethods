function calculate_graph(f, a, b, N) {
	var xi = [];
	var yi = [];
	var i;
	var h = (b-a)/N;
	var node = math.parse(f);
	var scope = {x: a};
	f = node.compile(f);
	for ( i = 0; i < N; i++){
		xi.push(a + i*h);
	}
	xi.push(b);
	for (i = 0; i < N+1; i++)
	{
		scope.x = xi[i];
		yi[i] = f.evaluate(scope);
	}
	return [xi, yi];
}

function find_root(f, a, b, n, t){
	var i = 0;
	var fa, fb;
	var p, fp;
	var node = math.parse(f);
	var scope = {x: a};
	var error;
	f = node.compile(f);

	console.log("Inicio do algoritmo...");
	fa = f.evaluate(scope);
	console.log("Valor de f(a): " + fa.toString());
	scope.x = b;
	fb = f.evaluate(scope); 
	console.log("Valor de f(b): " + fb.toString());
	
	if (!(fa*fb < 0)){
		console.log("Nao eh possivel calcular, pois os dois extremos tem os mesmos sinais");
		return -1;
	}
	console.log("Tabela com valores das iterações:");
	console.log("Iteracao - A - M - B - fA - fM - fB - error");

	while(i < n){
		p = (a+b)/2;
		scope.x = p;
		fp = f.evaluate(scope);
		i += 1;
		error = (b-a)/2;

		console.log(i.toString() + " " + a.toString() + " " + p.toString() + " " + b.toString() + " " + fa.toString() + " " + fp.toString() + " " + fb.toString() + " " + error.toExponential(1));
		if (fp == 0 || error < t){
			break;
		}
		else if ( fa*fp > 0){
			a = p;
			fa = fp;
		} else{
			b = p;
			fb = fp;
		}
	}
	console.log("Com " + i.toString() + " iterações obtemos um erro de " + error.toExponential(1) + " e valor de raiz de " + p.toString());
	return [i, error, p];

}

function begin_calculation(f, a, b, n, t)
{
	var a, b;
	var xi, yi;
	var trace;
	var data;
	var layout;

	[xi, yi] = calculate_graph(f, a, b, 256);
	trace = {x: xi, y: yi, mode: 'lines'};
	data = [trace]
	layout = {};
	Plotly.newPlot('divgraph', data, layout);

	// verify_conditions_algorithm(f, a, b);

	find_root(f, a, b, n, t);
}
