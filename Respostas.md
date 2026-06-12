1 - 
## Uso de IA para geração de cenários de teste

### Função escolhida

`multiplicar(a, b)`

### Prompt utilizado

```text
Atue como um professor de Teste de Software.

Tenho a seguinte função Python:

def multiplicar(a, b):
    return a * b

Quero criar testes unitários usando unittest.

Liste pelo menos 6 cenários de teste para essa função.

Para cada cenário, informe:
- nome do cenário;
- entrada;
- resultado esperado;
- tipo do cenário: caso normal, caso de borda ou caso de erro.

Não gere código ainda.


ID,Cenário,Entrada,Resultado esperado,Tipo, Decisão
T01,Multiplicação de positivos,"multiplicar(3, 4)",12,normal, ja consta
T02,Multiplicação por zero,"multiplicar(5, 0)",0,borda, ja consta
T03,Multiplicação por um,"multiplicar(7, 1)",7,borda, selecionado
T04,Multiplicação negativos,"multiplicar(-2, -3)",6,normal, selecionado
T05,Sinal oposto,"multiplicar(-2, 3)",-6,normal, ja consta
T06,Ponto flutuante,"multiplicar(0.1, 0.2)",0.02,borda, selecionado

def test_multiplicar_com_varios_casos(self):
    casos = [
        (3, 4, 12),
        (5, 0, 0),
        (7, 1, 7),
        (-2, -3, 6),
        (-2, 3, -6),
    ]
    
    for a, b, esperado in casos:
        with self.subTest(a=a, b=b):
            self.assertEqual(multiplicar(a, b), esperado)

def test_multiplicar_ponto_flutuante(self):
    self.assertAlmostEqual(multiplicar(0.1, 0.2), 0.02, places=7)

    
