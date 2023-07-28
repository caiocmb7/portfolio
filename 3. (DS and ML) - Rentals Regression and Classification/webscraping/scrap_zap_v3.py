# Bibliotecas
import requests as rq
import json
import pandas as pd
from pandas import json_normalize
import logging


# Configura o display do pandas
pd.options.display.max_columns = 99
pd.options.display.max_rows = 99
logging.basicConfig(level=logging.INFO)

# Imita um navegador para passar restricoes
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
headers = {"User-Agent": user_agent}


# Variaveis fixas
vPagFinal = (
    100  # Numero total de paginas a serem buscadas, se houver menos o script controla
)
vTransacao = "aluguel"  # Tipo de transacao: venda ou aluguel
# vUF = "ce"  # Unidade Federativa: rj, sp, mg, etc

# Listas para o script pegar automaticamente, pode aumentar ou diminuir com novos dados
vImovelLista = ["casas"]  # "casas","casas-de-vila","casas-de-condominio"
# vCidadeLista = [
#     "rio-de-janeiro"
# ]  # Coloca o estado no formato "rio-de-janeiro","sao-paulo", ou "TODOS" sendo que tem q ajustar a vUF para pegar o estado
vZonaLista = [
    "TODOS"
]  # "zona-norte","centro","zona-sul", "zona-oeste", "zona-leste", "TODOS", etc
vBairroLista = [
    "TODOS"
]  # "barra-da-tijuca","pechincha","freguesia-jacarepagua","anil" ou "TODOS" para pesquisar todos de determinada area
vQuartos = 4  # Quantidade de quartos
vValorMin = 100  # Valor Minimo
vValorMax = 2000000  # Valor Maximo

vUFs = ["rj"]
for vUF in vUFs:
    for vZona in vZonaLista:
        # Para cada bairro na lista de Bairros
        for vBairro in vBairroLista:
            # Para cada imovel na lista de imoveis
            for vImovel in vImovelLista:

                # Define a pagina inicial
                vPagina = 1

                # Print dos dados para acompanhar
                print(
                    vZona
                    + " -> "
                    + vBairro
                    + " -> "
                    + vUF
                    + " -> "
                    + vImovel
                    + " -> "
                    + str(vQuartos)
                )

                # Teste se o Bairro é unico, alguns ou todos
                if vBairro == "TODOS":
                    if vZona == "TODOS":
                        vURL_B = (
                                "https://www.zapimoveis.com.br/"
                                + vTransacao
                                + "/"
                                + vImovel
                                + "/"
                                + vUF
                                + "/"
                                + str(vQuartos)
                                + "-quartos"
                            )
                    else:
                        vURL_B = (
                            "https://www.zapimoveis.com.br/"
                            + vTransacao
                            + "/"
                            + vImovel
                            + "/"
                            + vUF
                            + "/"
                            + str(vQuartos)
                            + "-quartos"
                        )
                else:
                    vURL_B = (
                        "https://www.zapimoveis.com.br/"
                        + vTransacao
                        + "/"
                        + vImovel
                        + "/"
                        + vUF
                        + "+"
                        + vZona
                        + "+"
                        + vBairro
                        + "/"
                        + str(vQuartos)
                        + "-quartos"
                    )

                # Cria o dicionario
                dfs = {}

                # Itera entre as paginas
                while vPagina <= vPagFinal:

                    # URL
                    vURL = (
                        vURL_B
                        + "/?pagina="
                        + str(vPagina)
                        + "&precoMinimo="
                        + str(vValorMin)
                        + "&precoMaximo="
                        + str(vValorMax)
                    )

                    vResp = rq.get(vURL, headers=headers)
                    vStat = vResp.status_code

                    # Se codigo 200, entao vai adiante
                    if vStat == 200:
                        vHTML = vResp.text
                        vHTML = str(vHTML)

                        # Valida se a pagina existe ou nao
                        vValPag = (
                            "OK" if "Não encontramos resultados" in vHTML else "NOK"
                        )

                        # Continua se a pagina existir
                        if vValPag == "NOK":

                            # Pega apenas a parte do Json do codigo fonte
                            vHTML = vHTML.split('"results":{"listings":[', 1)[1]
                            vHTML = vHTML.split('],"nearbyListings":[]', 1)[0]
                            vHTML = vHTML.split(',"type":"nearby"}]', 1)[0]
                            if vHTML[-2:] == "}}":
                                v1 = '{"listings":[' + vHTML + "]}"
                            elif vHTML[-10:] == '"premium"}':
                                vHTML = vHTML.split(',"type":"premium"}', 1)[0]
                                # vHTML = vHTML.split(vHTML[-18],1)[0]
                                v1 = '{"listings":[' + vHTML + "}]}"
                            else:
                                v1 = '{"listings":[' + vHTML + "}]}"
                            v1 = v1.replace("R$ ", "")
                            v1 = v1.replace(',"superPremiumListings":[}]}', "}")
                            v1 = v1.split(";(function", 1)[0]
                            v1 = v1.split(',"advertisers"', 1)[0]
                            j = json.loads(v1)

                            # Cria o dataframe do pandas, já normalizando o json
                            df = json_normalize(j["listings"])
                            
                            columns = [
                                    # "listing.advertiserContact.phones",
                                    # "listing.whatsappNumber",
                                    # "link.href",
                                    "type",
                                    "account.name",
                                    "listing.usableAreas",
                                    "listing.totalAreas",
                                    "listing.title",
                                    "listing.description",
                                    "listing.createdAt",
                                    "listing.updatedAt",
                                    "listing.floors",
                                    "listing.parkingSpaces",
                                    "listing.address.zipCode",
                                    "listing.address.street",
                                    "listing.address.neighborhood",
                                    "listing.address.streetNumber",
                                    "listing.suites",
                                    "listing.bathrooms",
                                    "listing.bedrooms",
                                    "listing.pricingInfo.salePrice",
                                    "listing.pricingInfo.yearlyIptu",
                                    "listing.pricingInfo.monthlyCondoFee",
                                    "listing.publicationType",
                                    "listing.unitTypes",
                                    "listing.unitSubTypes",
                                    "listing.usageTypes",
                                    "listing.amenities",
                                    "listing.address.point.lat",
                                    "listing.pricingInfo.businessType",
                                    "listing.address.zone",
                                    "listing.acceptExchange",
                                    "listing.subtitle",
                                    "account.licenseNumber",
                                    "listing.pricingInfo.price",
                                    "listing.unitFloor",
                                    "listing.address.point.lon",
                                    "listing.preview",
                                    "listing.listingType",
                                    "listing.address.point.source",
                                    "listing.propertyType",
                                    "listing.unitsOnTheFloor",
                                    "listing.isInactive",
                                    "listing.externalId",
                                    "listing.pricingInfo.isRent",
                                    "listing.address.state",
                                    "listing.address.precision",
                                    "listing.pricingInfo.isSale",
                                    "listing.legacyId",
                                    "listing.pricingInfo.businessLabel",
                                    "listing.address.country",
                                    "listing.address.level",
                                    "listing.advertiserId",
                                    "listing.link",
                                    "listing.portal",
                                    "listing.id",
                                    "listing.businessTypeContext",
                                    "listing.displayAddressType",
                                    "listing.address.city",
                                    "listing.address.confidence",
                                    "listing.pricingInfo.period",
                                    "listing.pricingInfo.rentalTotalPrice",
                                    "listing.pricingInfo.rentalPrice",
                                ]
                            valid_columns = [col for col in columns if col in df.columns]
                            # Deixa somente as colunas utilizaveis
                            df = df[valid_columns]

                            # Insere a coluna com o tipo de imovel
                            df["imvl_type"] = vImovel

                            # Tratamento dos dados
                            df["listing.publicationType"] = df[
                                "listing.publicationType"
                            ].fillna("Standard")

                            # Retira o colchetes, transformando a lista em string dentro da coluna
                            df["listing.floors"] = [
                                "".join(map(str, l)) for l in df["listing.floors"]
                            ]
                            df["listing.unitTypes"] = [
                                "".join(map(str, l)) for l in df["listing.unitTypes"]
                            ]
                            df["listing.unitSubTypes"] = [
                                "|".join(map(str, l))
                                for l in df["listing.unitSubTypes"]
                            ]
                            df["listing.parkingSpaces"] = [
                                "".join(map(str, l))
                                for l in df["listing.parkingSpaces"]
                            ]
                            df["listing.suites"] = [
                                "".join(map(str, l)) for l in df["listing.suites"]
                            ]
                            df["listing.bathrooms"] = [
                                "".join(map(str, l)) for l in df["listing.bathrooms"]
                            ]
                            df["listing.usageTypes"] = [
                                "|".join(map(str, l)) for l in df["listing.usageTypes"]
                            ]
                            df["listing.totalAreas"] = [
                                "".join(map(str, l)) for l in df["listing.totalAreas"]
                            ]
                            df["listing.bedrooms"] = [
                                "".join(map(str, l)) for l in df["listing.bedrooms"]
                            ]
                            df["listing.amenities"] = [
                                "|".join(map(str, l)) for l in df["listing.amenities"]
                            ]
                            df["listing.usableAreas"] = [
                                "".join(map(str, l)) for l in df["listing.usableAreas"]
                            ]

                            # Cria colunas baseadas na coluna listing.amenities
                            df["listing.pool"] = df["listing.amenities"].map(
                                lambda x: "True" if "POOL" in x else "False"
                            )  # Piscina sim ou nao
                            df["listing.sauna"] = df["listing.amenities"].map(
                                lambda x: "True" if "SAUNA" in x else "False"
                            )  # Sauna sim ou nao
                            df["listing.backyard"] = df["listing.amenities"].map(
                                lambda x: "True" if "BACKYARD" in x else "False"
                            )  # Quintal sim ou nao
                            df["listing.garden"] = df["listing.amenities"].map(
                                lambda x: "True" if "GARDEN" in x else "False"
                            )  # Jardim sim ou nao
                            df["listing.barbgrill"] = df["listing.amenities"].map(
                                lambda x: "True" if "BARBECUE_GRILL" in x else "False"
                            )  # Churrasqueira sim ou nao
                            df["listing.partyhall"] = df["listing.amenities"].map(
                                lambda x: "True" if "PARTY_HALL" in x else "False"
                            )  # Salao de festas sim ou nao
                            df["listing.tenniscourt"] = df["listing.amenities"].map(
                                lambda x: "True" if "TENNIS_COURT" in x else "False"
                            )  # Quadra de Tennis sim ou nao
                            df["listing.sportcourt"] = df["listing.amenities"].map(
                                lambda x: "True" if "SPORTS_COURT" in x else "False"
                            )  # Quadra de Esportes sim ou nao
                            df["listing.bathtub"] = df["listing.amenities"].map(
                                lambda x: "True" if "BATHTUB" in x else "False"
                            )  # Banheira sim ou nao
                            df["listing.soundproofing"] = df["listing.amenities"].map(
                                lambda x: "True" if "SOUNDPROOFING" in x else "False"
                            )  # Prova de som sim ou nao
                            df["listing.fireplace"] = df["listing.amenities"].map(
                                lambda x: "True" if "FIREPLACE" in x else "False"
                            )  # Lareira sim ou nao
                            df["listing.gym"] = df["listing.amenities"].map(
                                lambda x: "True" if "GYM" in x else "False"
                            )  # Academia sim ou nao
                            df["listing.hottub"] = df["listing.amenities"].map(
                                lambda x: "True" if "HOT_TUB" in x else "False"
                            )  # Hidromassagem sim ou nao
                            df["listing.furnished"] = df["listing.amenities"].map(
                                lambda x: "True" if "FURNISHED" in x else "False"
                            )  # Mobiliado sim ou nao
                            df["listing.guestpark"] = df["listing.amenities"].map(
                                lambda x: "True" if "GUEST_PARKING" in x else "False"
                            )  # Estacionamento Visitantes sim ou nao
                            df["listing.playground"] = df["listing.amenities"].map(
                                lambda x: "True" if "PLAYGROUND" in x else "False"
                            )  # Playground sim ou nao
                            df["listing.mountainview"] = df["listing.amenities"].map(
                                lambda x: "True" if "MOUNTAIN_VIEW" in x else "False"
                            )  # Vista da montanha sim ou nao

                            # Cria a entrada variavel no dicionario
                            dfs["df_" + str(vPagina)] = df

                            # Incrementa um na pagina
                            vPagina = vPagina + 1

                        else:
                            vPagina = vPagina + 1

                        # vStat = vResp.status_code
                        # Sai do Loop
                    else:
                        print(vURL)
                        print("\n")
                        print(vStat)
                        break

                # Cria a lista
                vAcaoFimLista = []

                # Para cada entrada dinamica criada no Dicionário, adiciona na lista
                for i in dfs.keys():
                    # print(i)
                    vAcaoFimLista.append(dfs[i])
                    # df_acoes = pandas.DataFrame().append(dfs[i], ignore_index=False)

                # Concatena os dados da lista em um unico dataframe
                df_Zap = pd.concat(vAcaoFimLista, sort=False)

                # Exporta pra csv, usando encoding do windows

                print(
                    "\nCriando o arquivo dataZAP_"
                    + vTransacao
                    + "_"
                    + vImovel
                    + "_"
                    + vBairro
                    + ".csv com os dados"
                )
                # df_Zap.to_csv(
                #     "dataZAP_" + vTransacao + "_" + vImovel + "_" + vBairro + "_" + str(vQuartos) + ".csv",
                #     sep=";",
                #     index=False,
                # )
                df_Zap.to_csv(f"./webscraping-datasets/dataZap_{vUF}_{vTransacao}_{vImovel}_{vBairro}_{str(vQuartos)}.csv", sep = ";", index = False)
                print("\nArquivo criado\n")
                print("Webscraping finalizado!")