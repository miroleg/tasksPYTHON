import sys
import os
""" Программа сортировки слиянием из несколких отсортированных TXT файлов (числа и строки)  """
"начало разработки 05.09.2019 "
" автор Мироненко О.Г "

"-----------------------константы--------------------------"
S_max = "яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя"
S_min = "                                                                "
I_max = sys.maxsize
I_min = -sys.maxsize - 1
" ------------------------ ПЕРЕМЕННЫЕ ---------------------"
i_error = [0]*3
str_error = [""]*3
error_list = []
line = ""
files_list = []
input_files = []
output_files = []
" ------------------------ ФУНКЦИИ ------------------------"


"проверка введенной строки   целые числа по возрастанию"


def che_inp_int_a(line_in, last_value, fil_num):
    global i_error, str_error
    try:
        ich = int(line_in)
    except ValueError:
        print('ОШИБКА! Это не число : ', line_in, " в файле", str(fil_num))
        i_error[fil_num] = 1
        str_error[int(fil_num)] = line_in
        return I_max     # ставим барьер
    except Exception:
        print('ОШИБКА! Это неправильное число : ', line_in, " в файле", str(fil_num))
        i_error[fil_num] = 1
        str_error[int(fil_num)] = line_in
        return I_max     # ставим барьер
    else:
        if ich >= last_value:
            return ich      # print('Всё хорошо.')
        else:
            print(" ОШИБКА! нарушен порядок сортировки в файле", fil_num, " :")
            print("         предыдущее значение :", last_value)
            print("         меньше (<) текущего :", ich)
            i_error[fil_num] = 1
            str_error[fil_num] = line_in
            return I_max     # ставим барьер


"проверка введенной строки   целые числа по убыванию"


def che_inp_int_d(line_in, last_value, fil_num):
    global i_error, str_error
    try:
        ich = int(line_in)
    except ValueError:
        print('ОШИБКА! Это не число : ', line_in, " в файле", str(fil_num))
        i_error[fil_num] = 1
        str_error[int(fil_num)] = line_in
        return I_min        # ставим барьер
    except Exception:                     # сделать выбор исключений
        print('ОШИБКА! Это неправильное число : ', line_in, " в файле", str(fil_num))
        i_error[fil_num] = 1
        str_error[fil_num] = line_in
        return I_min
    else:
        if ich <= last_value:
            return ich
        else:
            print(" ОШИБКА! нарушен порядок сортировки в файле", str(fil_num), " :")
            print("         предыдущее значение :", last_value)
            print("         больше (>) текущего :", ich)
            i_error[fil_num] = 1
            str_error[fil_num] = line_in
            return I_min


"проверка введенной строки   строки по возрастанию"


def che_inp_str(line_in, last_value, fil_num):
    global i_error, str_error
    line_out = line_in
    if " " in line_in:
        print(" ОШИБКА!     пробел в строке входного файла", str(fil_num), " :", line_in)
        line_out = line_in.split(' ')[0] + "\n"
        print("    строка  в файле", str(fil_num), "будет обрезана до пробела:", line_out)
    if line_in >= last_value:
        return line_out     # ('Всё хорошо.')
    else:
        print(" ОШИБКА! нарушен порядок сортировки в файле", str(fil_num), " :")
        print("         предыдущее значение :", last_value, end="")
        print("         больше (>) текущего :", line_in)
        i_error[fil_num] = 1
        str_error[fil_num] = line_in
        return S_max         # ставим барьер


"проверка введенной строки   строки по убыванию"


def che_inp_str_d(line_in, last_value, fil_num):
    global i_error, str_error
    line_out = line_in
    if " " in line_in:
        print(" ОШИБКА!     пробел в строке входного файла", str(fil_num), " :", line_in)
        line_out = line_in.split(' ')[0] + "\n"
        print("    строка  в файле", str(fil_num), "будет обрезана до пробела:", line_out)
    if line_in <= last_value:
        return line_out     # ('Всё хорошо.')
    else:
        print(" ОШИБКА! нарушен порядок сортировки в файле", str(fil_num), " :")
        print("         предыдущее значение :", last_value, end="")
        print("         меньше (<) текущего :", line_in)
        i_error[fil_num] = 1
        str_error[fil_num] = line_in
        return S_min         # ставим барьер


"сортируем целые числа по возрастанию"


def sort_int_a(file_1, file_2):
    i_a_last = I_min
    i_b_last = I_min
    i_line = file_1.readline()
    if not i_line:
        ia = I_max
    else:
        ia = che_inp_int_a(i_line, i_a_last, 1)
        i_a_last = ia
    i_line = file_2.readline()
    if not i_line:
        ib = I_max
    else:
        ib = che_inp_int_a(i_line, i_b_last, 2)
        i_b_last = ib
    while ia < I_max or ib < I_max:
        if ia <= ib and ia < I_max:
            fileout.write(str(ia) + '\n')
            i_line = file_1.readline()
            if not i_line:
                ia = I_max
            else:
                ia = che_inp_int_a(i_line, i_a_last, 1)
                i_a_last = ia
        else:
            if ib < ia:
                fileout.write(str(ib) + '\n')
                i_line = file_2.readline()
                if not i_line:
                    ib = I_max
                else:
                    ib = che_inp_int_a(i_line, i_b_last, 2)
                    i_b_last = ib


"сортируем целые числа по убыванию"


def sort_int_d(file_1, file_2):
    i_a_last = I_max
    i_b_last = I_max
    i_line = file_1.readline()
    if not i_line:
        ia = I_min
    else:
        ia = che_inp_int_d(i_line, i_a_last, 1)
        i_a_last = ia

    i_line = file_2.readline()
    if not i_line:
        ib = I_min
    else:
        ib = che_inp_int_d(i_line, i_b_last, 2)
        i_b_last = ib
    while ia > I_min or ib > I_min:
        if ia >= ib and ia > I_min:
            fileout.write(str(ia) + '\n')
            i_line = file_1.readline()
            if not i_line:
                ia = I_min
            else:
                ia = che_inp_int_d(i_line, i_a_last, 1)
                i_a_last = ia
        else:
            if ib > ia:
                fileout.write(str(ib) + '\n')
                i_line = file_2.readline()
                if not i_line:
                    ib = I_min
                else:
                    ib = che_inp_int_d(i_line, i_b_last, 2)
                    i_b_last = ib


"сортируем строки по возрастанию"


def sort_str_a(file_1, file_2):
    s_a_last = S_min
    s_b_last = S_min
    s_line = file_1.readline()
    if not s_line:
        sa = S_max
    else:
        sa = che_inp_str(s_line, s_a_last, 1)
        s_a_last = sa
        s_line = file_2.readline()
    if not s_line:
        sb = S_max
    else:
        sb = che_inp_str(s_line, s_b_last, 2)
        s_b_last = sb
    while sa < S_max or sb < S_max:
        if sa <= sb and sa < S_max:
            fileout.write(sa)
            s_line = file_1.readline()
            if not s_line:
                sa = S_max
            else:
                sa = che_inp_str(s_line, s_a_last, 1)
                s_a_last = sa
        else:
            if sb < sa:
                fileout.write(sb)
                s_line = file_2.readline()
                if not s_line:
                    sb = S_max
                else:
                    sb = che_inp_str(s_line, s_b_last, 2)
                    s_b_last = sb


"сортируем строки по убыванию"


def sort_str_d(file_1, file_2):
    s_a_last = S_max
    s_b_last = S_max
    if Str_bool and Dec_bool:
        s_line = file_1.readline()
        if not s_line:
            sa = S_min
        else:
            sa = che_inp_str_d(s_line, s_a_last, 1)
            s_a_last = sa
        s_line = file_2.readline()
        if not s_line:
            sb = S_min
        else:
            sb = che_inp_str_d(s_line, s_b_last, 2)
            s_b_last = sb
        while sa > S_min or sb > S_min:
            if sa >= sb and sa > S_min:
                fileout.write(sa)
                s_line = file_1.readline()
                if not s_line:
                    sa = S_min
                else:
                    sa = che_inp_str_d(s_line, s_a_last, 1)
                    s_a_last = sa
            else:
                if sb > sa:
                    fileout.write(sb)
                    s_line = file_2.readline()
                    if not s_line:
                        sb = S_min
                    else:
                        sb = che_inp_str_d(s_line, s_b_last, 2)
                        s_b_last = sb


" ------------- Программа  sort --------------------------------------"
" Анализ параметров программы в командной строке"


print(len(sys.argv))
print(sys.argv)
Str_bool = '-s' in sys.argv  # флаг СТРОКИ
IntegerNum_bool = '-i' in sys.argv  # флаг ЦЕЛЫЕ ЧИСЛА
Dec_bool = '-d' in sys.argv       # флаг сортировки по убыванию
Prom_bool = '-prom' in sys.argv    # флаг вывода промежуточных результатов сортировки
if Str_bool and IntegerNum_bool:
    print(" ОШИБКА!  тип данных: или строки (-s), или целые числа (-i)")
    print(" Удалите лишний параметр")
    raise SystemExit(1)
if not Str_bool and not IntegerNum_bool:
    print(" ОШИБКА!  не указан тип данных:  -s или -i")
    raise SystemExit(1)
else:
    " Анализ списка файлов в командной строке "
    files_list = []
    sub = '.txt'
    for text in sys.argv:
        if sub in text.lower():
            files_list.append(text)
    if len(files_list) < 2:
        print(" ОШИБКА!  указано мало файлов (меньше 2-х)")
        print(" добавьте в командной строке файлы согласно инструкции")
        raise SystemExit(1)
    if len(files_list) == 2:
        print(" Предупреждение!  указан только 1 входной файл")
        print(" будет только проверка строк файла")
        text = "empty.txt"  # пустой файл
        file2 = open("empty.txt", "w")
        file2.close()
        files_list.append(text)
    input_files = files_list
    "здесь напрашивается сортировка списка input_files  ПО РАЗМЕРУ ФАЙЛА! от меньшего к большему для оптимизации"
    output_files.append(files_list[0])
    i = 1                                           # указатель на 1-ый входной файл
    file_protocol = open("PROTOCOL.txt", "w")       # открываем файл протокола"
    while i < len(input_files)-1:       #
        i_error = [0]*3
        str_error = [""]*3
        if i < len(input_files)-2:
            output_files.append(files_list[0].split(".txt")[0] + "_" + str(i)+".txt")
        else:
            output_files.append(files_list[0])
        if i > 1:
            input_file_name_1 = output_files[i-1]
        else:
            input_file_name_1 = input_files[i]
        input_file_name_2 = input_files[i+1]
        " открываем файл для слияния двух файлов"
        fileout = open(output_files[i], "w")
        try:
            file1 = open(input_file_name_1, "r")
            file2 = open(input_file_name_2, "r")
        except IOError:
            print(" ОШИБКА! НЕВОЗМОЖНО ОТКРЫТЬ ФАЙЛЫ ", input_file_name_1, " или ", input_file_name_2)
        else:
            file_protocol.write(output_files[i]+" "+input_file_name_1+" "+input_file_name_2+'\n')
            print(" читаем входные файлы :  1 - ", input_file_name_1, " 2 - ", input_file_name_2)
            print(" пишем в файл :  ", output_files[i])
            if Str_bool and not Dec_bool:
                sort_str_a(file1, file2)        # сортируем строки по возрастанию
            if Str_bool and Dec_bool:
                sort_str_d(file1, file2)        # сортируем строки по убыванию
            if IntegerNum_bool and not Dec_bool:
                sort_int_a(file1, file2)        # сортируем целые числа по возрастанию
            if IntegerNum_bool and Dec_bool:
                sort_int_d(file1, file2)        # сортируем целые числа по убыванию

            print(input_file_name_1, " и ", input_file_name_2, " слиты в файл  : ", output_files[i])
            file_protocol.write(input_file_name_1+" и "+input_file_name_2+" слиты в файл  : "+output_files[i]+'\n')
            if i_error[1]:
                er_fil_name = "error1"+str(i)+".txt"
                file_error = open(er_fil_name, "w")
                error_list.append(er_fil_name)
                file_protocol.write("строки с ошибками в файле  ---->  : " + er_fil_name + '\n')
                file_error.write(str_error[1])
                while True:
                    line = file1.readline()
                    file_error.write(line)
                    if not line:  # конец файла
                        break
                file_error.close()

            if i_error[2]:
                er_fil_name = "error2"+str(i)+".txt"
                file_error = open(er_fil_name, "w")
                error_list.append(er_fil_name)
                file_protocol.write("строки с ошибками в файле  ----> " + er_fil_name + '\n')
                file_error.write(str_error[2])
                while True:
                    line = file2.readline()
                    file_error.write(line)
                    if not line:  # конец файла
                        break
                file_error.close()
        finally:
            file1.close()
            fileout.close()
            if not Prom_bool and i > 1:
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), output_files[i-1])
                os.remove(path)         # удаляем временный файл с резултатами одного слияния
            i += 1
    if i_error[1] or i_error[2]:
        if Dec_bool:
            st_p1 = "-d"
        else:
            st_p1 = "-a"
        if Str_bool:
            st_p2 = "-s"
        else:
            st_p2 = "-i"
        file_protocol.write(" исправьте ошибки в файлах error**.txt и запустите программу следующей строкой: " + '\n')
        file_protocol.write("python sort.py " + st_p1 + " " + st_p2 + " n_" + output_files[i-1] + " " + output_files[i-1] + " n_" + ' n_'.join(error_list) + '\n')
        print("***** работа программы sort завершена с ошибками, смотри PROTOCOL.txt *****  результат в файле:  ", output_files[i-1])
    else:
        file_protocol.write("***** работа программы sort завершена без ошибок *****  результат в файле:  " + output_files[i-1])
        print("***** работа программы sort завершена без ошибок *****  результат в файле:  ", output_files[i-1])
    file_protocol.close()
