from app import calcular_total


def test_calcular_total():
	resultado = calcular_total(1000, 2)
	assert resultado == 2000