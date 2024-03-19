import pytest
import imc_simples as imcs

class TestIMCs:
    def test_imc_simples(self):
        assert imcs.calcular_imc(85, 1.85) == 24.84
    def test_imc_simples2(self):
        assert imcs.calcular_imc(90, 1.90) == 24.93
    def test_imc_simples3(self):
        assert imcs.calcular_imc(70, 1.75) == 22.86