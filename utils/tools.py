from os import path, scandir
from queue import Empty


def is_preposition(word: str) -> bool:
    """Returns a true value for the word contained in the list of
    prepositions, otherwise the return will be false.

    (pt-BR) Retorna um valor verdadeiro para palavra contida na lista de
    preposições, caso contrário o retorno será falso.

    Args:
        word (str): A word, which cannot be an empty or null value.

        (pt-BR) Uma palavra, não podendo esta ser um valor vazio ou nulo.

    Returns:
        bool: True or False.

        (pt-BR) Verdadeiro ou Falso.
    """

    if word is Empty or word is None:
        raise ValueError('É necessário informar uma palavra!')

    list_prepositions = [
        'por', 'a', 'para', 'de', 'em', 'pelo', 'ao', 'pro', 'do', 'no',
        'pela', 'à', 'pra', 'da', 'na', 'pelos', 'aos', 'pros', 'dos', 'nos',
        'pelas', 'às', 'pras', 'das', 'nas', 'dum', 'duma', 'duns', 'dumas',
        'dele', 'dela', 'deles', 'delas', 'deste', 'disto', 'desse', 'daquele',
        'daquilo', 'àquele', 'àquilo', 'praquilo', 'praquele', 'num', 'numa',
        'nuns', 'numas', 'nele', 'nela', 'neles', 'nelas', 'neste', 'nisto',
        'nesse', 'nisso', 'naquele', 'naquilo', 'de', 'e'
    ]
    return word.lower() in list_prepositions


def string_capitalize(value: str = None) -> str:
    """Converts the initial letters of each word, except for prepositions, so
    that all initials are capitalized.

    (pt-br) Realiza a conversão das letras iniciais de cada palavra, exceto
    as preposições, de modo que todas as iniciais passam a ser maiúsculas.

    Args:
        value (str, optional): Value of type string that will receive the
        treatment of the function so that its initials become uppercase.
        Defaults to None.

        (pt-br) Valor do tipo string que receberá o tratamento da função para
        que suas iniciais se tornem maiúsculas. O padrão é Nenhum.

    Raises:
        ValueError: Informs the user that the value must be informed.

        (pt-br) Informa ao usuário que o valor obrigatóriamente deva ser
        informado.

    Returns:
        str: Returns the string passed as a parameter (value) with all
        initials in uppercase.

        (pt-BR) Retorna a string passada como parâmetro (value) com todas as
        iniciais em maiúscula.
    """

    if value is None:
        raise ValueError('É necessário informar um valor do tipo string!')

    list_words = list(map(lambda w: w.lower() if is_preposition(w)
                      else w.capitalize(), value.split(' ')))
    return ' '.join(list_words)


def scanning_files(pathway: str = None,
                   file_list: list = None,
                   extension: str = ".*") -> list:
    """It walks through a nested directory structure listing all files, if
    an extension is specified, it will only return files that contain the same
    extension in their name attribute.

    (pt-br) Percorre uma estrutura aninhada de diretórios listando todos os
    arquivos, caso seja especificado uma extensão, este retornara somente os
    arquivos que contenha a mesma extesão em seu atributo nome.

    Args:
        pathway (str, optional): If the value is passed as a parameter, the
        scan will start from the given path and will extend along all its
        subdirectories. Defaults to None. In this case the scan will start in
        the current directory of the program and extend through its
        subdirectories.

        (pt-br) Caso o valor seja passado como parâmetro a varredura se dará a
        partir do caminho informado e se estenderá ao longo de todos os seus
        subdiretórios. O padrão é Nenhum. Neste caso a varredura iniciar-se-a
        no diretório atual do programa se estendendo por seus subdiretórios.

        file_list (list, optional): List containing file paths. It can be used
        for initial power or feedback. Defaults to None.

        (pt-br) Lista contendo caminhos de arquivos. Pode ser utilizado para
        alimentação inicial ou retroalimentação. O padrão é Nenhum.

        extension (str, optional): Extension of the file expected to filter/
        select. Defaults to ".*".

        (pt-br) Extensão do arquivo que espera-se filtrar/selecionar. O padrão
        é ".*".

    Returns:
        list: List containing the absolute path of each of the files.

        (pt-br) Lista contendo o caminho absoluto de cada um dos arquivos.
    """
    if file_list is None:
        file_list = list([])

    for item in scandir(pathway):

        if path.isdir(item.path):
            scanning_files(item.path, file_list, extension)
        else:
            if extension != ".*":
                if path.splitext(item.path)[1] == extension:
                    file_list.append(item.path)
            else:
                file_list.append(item.path)

    return file_list
