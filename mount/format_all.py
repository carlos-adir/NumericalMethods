# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 20:24:19 2020

@author: carlo

Descricao: Esse eh o algoritmo principal para poder mesclar e juntar todos os arquivos
O objetivo dele eh permitir a inclusao de arquivos.
Por exemplo, se eu tenho um arquivo "index.html", e dentro desse arquivo tem uma string do tipo:
<!--#include "navegation.html"-->
Entao sera gerado um novo arquivo, pegando todo o conteudo de "navegation.html" e passando para dentro do "index.html", assim evita de copiar e colar código.
Ele faz isso recursivamente. Entao se tiver "<!--#include "exemplo.html"-->" dentro de "navegation.html", entao o conteudo de "exemplo.html" sera copiado para dentro do navegation, para depois ir para "index.html"

Para fazer isso, se utiliza as funcoes:
file_exists -> para saber se um arquivo existe.
get_all_lines -> le todo o arquivo
get_all_files -> pega todos os nomes de arquivos dentro de um diretorio
write_lines_file -> grava conteudo em um arquivo


Alem disso, consegue tratar alguns comandos. Por exemplo, o de inclusao eh um comando de:
<!--#include "exemplo.html"--> ==========> Inclui o arquivo "exemplo.html"
Alem disso, tem como fazer substituicao:
<!--#include "input/<<substituir>>/exemplo.html"--> com <<substituir>> equivalente a "1" =======> Inclui o arquivo "input/1/exemplo.html"

"""

import glob
import os
import re
import codecs


def print_lista(lista):
    for i in lista:
        print(i)

def file_exists(filename):
    '''
    Verifica se um arquivo existe
    '''
    try:
        arq = open(filename, encoding='utf8')
        arq.close()
        return True
    except:
        return False

def get_all_lines(filename):
    '''
    Pega um arquivo, e le todas as linhas dele.
    Assim, retorna uma lista com as linhas.
    '''
    if not file_exists(filename):
        print("File " + str(filename) + " does not exist")
        return []
        raise Exception("File do not exist: " + str(filename))
    else:
        try:
            arq = open(str(filename), encoding='utf8')
            lines = arq.readlines()
            for i in range(len(lines)):
                lines[i] = lines[i].split("\n")[0]
            arq.close()
            return lines
        except:
            raise Exception("Error reading all the lines from " + filename)




# def get_all_files(path = "", extension = None):
#     '''
#     Pega o nome de todos os arquivos dentro de um diretorio.
#     Se a chave "extension" for acionada, por exemplo ".png", entao ele pega todos os arquivos com extensao ".png"
#     Ele faz isso recursivamente e retorna uma lista com todos os arquivos dentro do diretorio passado como "path".
#     '''
#     files = [f for f in glob.glob(path + "**/*", recursive=True)]
#     for i in range(len(files)):
#         files[i] = files[i].replace("\\", "/")
#     if extension == None:
#         return files
#     else:
#         lista = []
#         for f in files:
#             if extension in f:
#                 lista.append(f)
#         print(lista)
#         return lista

def write_lines_file(lines, filename):
    '''
    Pega uma lista de strings e grava tudo dentro de um arquivo.
    Se o arquivo ja existir, ele sobreescreve.
    '''
    arq = open(filename, "w", encoding="utf8")
    for line in lines:
        try:
            arq.write(line + "\n")
        except:
            raise Exception("Erro na hora de gravar a linha no arquivo")
            raise Exception("Nao pode somar 'line' com '\\n'. Type(line) = " + str(type(line)))
    arq.close()

def replaces(lines, dicionario):
    for key in dicionario:
        dict_key = dicionario[key]
        for i in range(len(lines)):
            lines[i] = lines[i].replace(key, dict_key)
    return lines

def condicionais(linhas):
    
    # base_string = '<< file_exists("<<input_folder>>/<<substituir>>/resumo.html") ? "<a class="nav-link" href="#button_resumo">Resumo</a>" : "" >>'
    conditional_string = "(.*)\<\< (.*) \? \"(.*)\" : \"(.*)\" \>\>"
    for i in range(len(linhas)):
        search1 = re.search(conditional_string, linhas[i])
        if search1 != None:
            indentation = search1.group(1);
            conditional = search1.group(2);
            true_value = search1.group(3);
            false_value = search1.group(4);
            search2 = re.search("file_exists\(\"(.*)\"\)", conditional)
            if search2 != None:
                filename = search2.group(1)
                if file_exists(filename):
                    linhas[i] = indentation + true_value
                else:
                    linhas[i] = indentation + false_value
    return linhas


def command_include(lines, dicionario):
    # print("### Funcao command_include ###")
    incluiu = False
    for i in range(len(lines)):
        search = re.search('(.*)<!--#include "(.*)"-->', lines[i])
        if search != None:
            # print(search.group(2))
            indentation = search.group(1)
            filename = search.group(2)
            # print("### Search ###")
            # print("filename = " + str(filename))
            novas_linhas = import_lines(filename, dicionario, indentation)
            lines[i] = novas_linhas
            incluiu = True
    if incluiu:
        lines = treat_listas(lines)

    return incluiu, lines


def treat_listas(lines):
    '''
    Esta funcao transforma listas. De modo que o resultado seja uma unica lista.
    Por exemplo, se temos a lista: ["asd", "fff", ["kkk", "123", ["fav"]], "meu"]
    Entao a saida dessa funcao eh: ["asd", "fff", "kkk", "123", "fav", "meu"]
    Essa funcao eh recursiva
    '''
    new_lines = []
    for element in lines:
        if type(element) != list and type(element) != tuple:
            new_lines.append(element)
        else:
            tratados = treat_listas(element)
            for elem_tratado in tratados:
                new_lines.append(elem_tratado)
    return new_lines


def import_lines(filename, dicionario, before = ""):
    try:
        lines = get_all_lines(filename)
        while True:
            lines = replaces(lines, dicionario)
            lines = condicionais(lines)
            incluiu, lines = command_include(lines, dicionario)
            if not incluiu:
                break

        for i in range(len(lines)):
            lines[i] = before + lines[i]
        return lines
    except:
        raise
        return []



    # for l in linhas:
    #     line = treat_commands(l, "<<substituir>>", substituir)
    #     if '<!--#include "' in line:
    #         beforee, after = line.split('<!--#include "')
    #         name_between, after = after.split('"-->')
    #         without_includes = lines_included(name_between, substituir, before + beforee)
    #         new_linhas += without_includes
    #     else:
    #         new_linhas.append(before+line)
    #     #print("T: " + str(type(new_linhas)) + " T[0]: " + str(type(new_linhas[0])))
    return new_linhas

def conect_one(initial, end, dicionario):
    '''
    initial = arquivo inicial com varios #include e comandos
    end = nome do arquivo final
    '''
    try:
        lines = import_lines(initial, dicionario)
        # print_lista(lines)
        write_lines_file(lines, end)
    except:
        # print("initial: " + str(initial))
        # print("    end: " + str(end))
        # print("      f: " + str(f))
        pass
        raise

# tabs = ["resumo", "teoria", "erros", "restricoes", "parametros", "exemplo", "more"]
files1 = ["1", "2", "3", "4", "5", "6", "7"]
files2 = ["1_1", "1_2", "1_3", "1_4", "1_5", "1_6", \
          "2_1", "2_2", "2_3", \
          "3_1", "3_2", \
          "4_1", "4_2", "4_3", "4_4"] #, \
          # "5_1", "5_2", "5_3", "5_4", \
          # "6_1", "6_2", "6_3", \
          # "7_1", "7_2"]
files3 = ["1_1"]

zer = "_0zer.html"
pri = "_1pri.html"
sec = "_2sec.html"
ter = "_3ter.html"
inpput = "base_files"
output = "../docs/"

diction = {"<<js_folder>>": "js", \
           "<<css_folder>>": "css", \
           "<<base_files_folder>>": inpput}

conect_one(zer, output+"index.html", diction)
for f in files1:
    diction["<<substituir>>"] = f
    conect_one(pri, output+f+".html", diction)
for f in files2:
    diction["<<substituir>>"] = f
    conect_one(sec, output+f+".html", diction)
for f in files3:
    diction["<<substituir>>"] = f
    conect_one(ter, output+f+"_app.html", diction)
# os.system("cp -r css/ " + output)
# os.system("cp -r js/ " + output)
# os.system("cp -r aplication/ " + output)
