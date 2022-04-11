from datetime import datetime

from pandas import DataFrame, ExcelWriter, read_html

from tools import scanning_files


class DFMovements(DataFrame):

    cols = [
        "Order",
        "DateTime",
        "Code",
        "Description",
        "Amount",
        "Value",
        "Operation"
    ]

    def __init__(self, *args, **kwargs):
        super(DFMovements, self).__init__(columns=self.cols, *args, **kwargs)

        self.Order = self.Order.astype("i")
        self.DateTime = self.DateTime.astype("M")
        self.Code = self.Code.astype("i")
        self.Description = self.Description.astype("O")
        self.Amount = self.Amount.astype("i")
        self.Value = self.Value.astype("f")
        self.Operation = self.Operation.astype("O")


class Movements:

    def __init__(self, path_files: str = None):
        self.__data = DFMovements()

        try:
            self.__html_files = scanning_files(path_files, extension=".html")

            if len(self.__html_files) > 0:
                for file in self.__html_files:
                    self.__data = self.__data. \
                        append(self.__data_extraction(file),
                               ignore_index=True,
                               verify_integrity=True)

                self.__grouped = self.__data.groupby(
                    ["Code", "Description"]).sum().drop(
                        columns=["Order", "Value"])

        except (TypeError,
                NameError,
                FileNotFoundError,
                FileExistsError,
                OSError) as err:
            print(f"\n{err.args[1]}")

    @staticmethod
    def __data_extraction(filename: str = None) -> DataFrame:
        """
        Realiza a leitura e o tratamento das informações de uma tabela
        específica, Movimento Geral, retirada de um arquivo .html a fim
        de extrair as informações de movimentação de produtos.

        * Valor default para filename é None, neste caso será gerado uma
        excessão que fará com que a função retorne um DataFrame vazio, caso
        contrário retornará um DataFrame populado contendo os dados de Order,
        DateTime, Code, Description, Amount, Value e Operation.
        """

        search_keys = ('Registro de entrada de produtos',
                       'Registro de saída de produto',
                       'Devolução de etiquetas do cliente para a agência.',
                       'Suprimento de etiquetas para cliente')

        filename = None if filename == "" else filename

        new_df = DFMovements()

        try:
            df = read_html(filename, encoding="ISO-8859-1",
                           header=0, decimal=",", thousands=".")[14]
            df.columns = ["Ordem", "Data", "Desc", "Qtde", "Valor"]
            df.fillna(method="ffill", inplace=True)

            df.Ordem = df.Ordem.astype("i")
            df.Data = df.Data.astype("O")
            df.Desc = df.Desc.astype("O")
            df.Qtde = df.Qtde.map(lambda x: x.replace(
                "-", "0") if x == "-" else x).astype("i")
            df.Valor = df.Valor.map(lambda x: x.replace(
                "-", "0") if x == "-" else x).astype("f")

            df2 = df[df.Desc.isin(search_keys)]
            df3 = df[df.Data.isin(df2.Data)].query("Qtde > 0")

            for idx in df2.index:

                if df2.Desc[idx] in (search_keys[1], search_keys[3]):
                    factor = -1
                else:
                    factor = 1

                for idy in df3.index:
                    if df3.Ordem[idy] == df2.Ordem[idx] and \
                            df3.Data[idy] == df2.Data[idx]:

                        if str(df3.Desc[idy]).find("/") > 0:
                            items = {
                                "Order": df3.Ordem[idy],
                                "DateTime":
                                datetime.strptime(
                                    df3.Data[idy], "%d/%m/%Y %H:%M:%S"),
                                "Code": int(str(df3.Desc[idy])[5:14]),
                                "Description":
                                str(df3.Desc[idy])[
                                    15:str(df3.Desc[idy]).find("/")],
                                "Amount": int(df3.Qtde[idy]) * factor,
                                "Value":
                                float(f"{df3.Valor[idy]:.2f}") * factor,
                                "Operation": df2.Desc[idx]
                            }
                        else:
                            items = {
                                "Order": df3.Ordem[idy],
                                "DateTime":
                                datetime.strptime(
                                    df3.Data[idy], "%d/%m/%Y %H:%M:%S"),
                                "Code": int(str(df3.Desc[idy])[5:14]),
                                "Description": str(df3.Desc[idy])[15:],
                                "Amount": int(df3.Qtde[idy]) * factor,
                                "Value":
                                float(f"{df3.Valor[idy]:.2f}") * factor,
                                "Operation": df2.Desc[idx]
                            }

                        new_df = new_df.append(
                            items,
                            ignore_index=True,
                            verify_integrity=True
                        )

        except (ValueError, TypeError) as err:
            msg = "É necessário informar um arquivo .html válido para " + \
                "extração dos dados!"

            print(f"\n{msg}")
            print(err.args[1])

        finally:
            return new_df

    def export_results(self, format_file: str = "Excel"):
        """Exports the analysis result of product movement data to files in
        .xlsx (Excel) or .accdb (Access) format.

        (pt-br) Realiza a exportação do resultado da análise dos dados de
        movimentação de produtos para para arquivos no formato .xlsx (Excel)
        ou .accdb (Access).

        Args:
            format_file (str, optional): Choose the format of the export
            output file. Defaults to "Excel".
            (pt-br) Escolhe o formato do arquivo de saída de exportação.

        Raises:
            AttributeError: When there is no information to be exported.
            (pt-br) Quando não há informações para serem exportadas.

            PermissionError: When the file is in use/open.
            (pt-br) Quando o arquivo encontra-se em uso/aberto.
        """
        try:
            if format_file == "Excel":
                if self.__data.size <= 0:
                    raise AttributeError(
                        "Não existem dados a serem exportados!"
                    )
                else:
                    with ExcelWriter(
                        "movements.xlsx",
                        datetime_format="DD-MM-YYYY HH:MM:SS"
                    ) as writer:
                        self.__data.reset_index().drop(columns="index"). \
                            to_excel(writer,
                                     sheet_name="Movimentações",
                                     float_format="%.2f",
                                     index=False)

                        self.__grouped.reset_index(). \
                            to_excel(writer,
                                     sheet_name="Movimentações - Agrupado",
                                     float_format="%.2f",
                                     index=False
                                     )
            elif format_file == "Access":
                print("Em desenvolvimento...")

        except PermissionError as err_permission:
            print(f"\n({err_permission.args[1]})",
                  "Não foi possível realizar a exportação para .xlsx!",
                  "O arquivo encontra-se em uso!")

        except AttributeError as err_attribute:
            print(f"\n{err_attribute.args[0]}")
