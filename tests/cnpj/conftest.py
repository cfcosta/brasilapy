import pytest


@pytest.fixture
def cnpj_json():
    return {
        "uf": "SP",
        "cep": "07115000",
        "qsa": [
            {
                "pais": None,
                "nome_socio": "SOCIO_NOME_1",
                "codigo_pais": None,
                "faixa_etaria": "Entre XX a XX anos",
                "cnpj_cpf_do_socio": "***123321**",
                "qualificacao_socio": "Sócio-Administrador",
                "codigo_faixa_etaria": 4,
                "data_entrada_sociedade": "1987-01-01",
                "identificador_de_socio": 2,
                "cpf_representante_legal": "***000000**",
                "nome_representante_legal": "",
                "codigo_qualificacao_socio": 49,
                "qualificacao_representante_legal": "Sócio-Administrador",
                "codigo_qualificacao_representante_legal": 0,
            }
        ],
        "cnpj": "00000000000000",
        "pais": None,
        "email": None,
        "porte": "EMPRESA DE PEQUENO PORTE",
        "bairro": "CENTRO",
        "numero": "9999",
        "ddd_fax": "",
        "municipio": "MUNICIPIO",
        "logradouro": "NOME DA RUA",
        "cnae_fiscal": 90000001,
        "codigo_pais": None,
        "complemento": "",
        "codigo_porte": 3,
        "razao_social": "NOME DA RAZAO SOCIAL",
        "nome_fantasia": "NOME DE FANTASIA",
        "capital_social": 2222,
        "ddd_telefone_1": "9999999999",
        "ddd_telefone_2": "",
        "opcao_pelo_mei": False,
        "descricao_porte": "",
        "codigo_municipio": 1111,
        "cnaes_secundarios": [
            {"codigo": 1234567, "descricao": "CNAE SECUNDARIO 1"},
            {"codigo": 7654321, "descricao": "CNAE SECUNDARIO 2"},
        ],
        "natureza_juridica": "Sociedade Empresária Limitada",
        "situacao_especial": "",
        "opcao_pelo_simples": True,
        "situacao_cadastral": 2,
        "data_opcao_pelo_mei": None,
        "data_exclusao_do_mei": None,
        "cnae_fiscal_descricao": "Cnae Fiscal Descricao",
        "codigo_municipio_ibge": 7654321,
        "data_inicio_atividade": "2000-01-02",
        "data_situacao_especial": None,
        "data_opcao_pelo_simples": "2001-02-03",
        "data_situacao_cadastral": "2001-03-04",
        "nome_cidade_no_exterior": "",
        "codigo_natureza_juridica": 1111,
        "data_exclusao_do_simples": None,
        "motivo_situacao_cadastral": 0,
        "ente_federativo_responsavel": "",
        "identificador_matriz_filial": 2,
        "qualificacao_do_responsavel": 99,
        "descricao_situacao_cadastral": "ATIVA",
        "descricao_tipo_de_logradouro": "TESTE TIPO LOGRADOURO",
        "descricao_motivo_situacao_cadastral": "MOTIVO SITUACAO",
        "descricao_identificador_matriz_filial": "MATRIZ",
    }
