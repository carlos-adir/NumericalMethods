#include <stdio.h>
#include <stdlib.h>
#include "kbhitgetch.h"

typedef struct 
{
	double x, y;
}ponto;

ponto *aloca_memoria(int quantidade)
{
	ponto *P;
	P = (ponto *) malloc(quantidade * sizeof(ponto));
	return P;
}

int main()
{
	int i, n;
	double x, y;
	ponto *P;
	printf("Digite a quantidade de pontos:\n");
	scanf("%d", &n);
	P = aloca_memoria(n);
	if(P == NULL)
	{
		printf("Nao foi possivel alocar a memoria necessaria.\n");
		printf("Encerramento do programa.\n\n");
		return 1;
	}
	printf("A seguir, digite os numeros(double) x e y separados por espaços.\n");
	printf("Pra melhor visualizacao, coloque cada par em uma linha.\n");
	for(i = 0; i < n; i++)
	{	
		while( scanf("%lf %lf", &x, &y) != 2)
		{
			limpa_buffer();
			printf("Numeros digitados invalidos. Digite somente numeros validos...\n");
		}
		(P+i)->x = x;
		(P+i)->y = y;
	}
	printf("Os pares digitados foram:\n\n");
	for(i = 0; i < n; i++)
	{
		printf("%d) %.3lf %.3lf\n", i+1, (P+i)->x, (P+i)->y);
	}
	return 0;
}