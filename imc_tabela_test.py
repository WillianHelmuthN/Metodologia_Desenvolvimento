import pytest
import imc_tabela as imct

class TestIMCt:
    def test_imc_tabela(self):
        assert imct.classificar_imc(20.2) == "Normal"
    def test_imc_tabela2(self):
        assert imct.classificar_imc(40.4) == "Obesidade grau III"
    def test_imc_tabela3(self):
        assert imct.classificar_imc(29.0) == "Sobrepeso"