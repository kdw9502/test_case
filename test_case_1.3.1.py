import difflib
import os
import glob
import string

folder_name = input("폴더 이름 입력 : ")

file_directory = folder_name + "/*.py"

file_name_flag = input("파일 이름 변경 필요 여부(1: 필요, 0: 필요 없음): ")

if file_name_flag == '1':
    start = int(input("시작학번 입력: ")) % 1000000
    end = int(input("끝학번 입력: ")) % 1000000    
    
    for s in glob.glob(file_directory):
        if ( s.find('[')!=-1 and (s.find('L')!=-1 or s.find('HW')!=-1 or s.find('hw')!=-1 or s.find('l')!=-1) ):
            s_edited = s.split(']')[1]
            if(s_edited[0]=='s'):
                s_num= s_edited.split('L')[0].split('HW')[0].split('hw')[0].split('s')[1]
                if(s_num[0]!='1' or len(s_num)!=6):
                    print(s,"file name error (in number)")
                    continue
                s_num=int(s_num)
                s_num=s_num%1000000
                if(end>=s_num>=start):
                    make_directory = folder_name + '/' + s_edited
                    os.rename(s, make_directory)
                else:
                    #print("original : " + s+"is deleted")
                    os.remove(s)
            else:
                print(s,"file name error (in snnnnnn form)")
        else:
            print(s,"file name error (in HW or L form)")

input_txt = "test_input.txt"
output_txt = "test_output.txt"

print("케이스는 총 5번 실행됩니다. 중단하려면 '중단'이라고 작성하세요.")
for i in range(0, 5):
    test_case = input("테스트 케이스 입력 : ")

    if test_case == '중단':
        break

    total_result = ''
    
    test_input = open(input_txt, "w")
    test_input.write(test_case + "\n")
    test_input.close()

    test_case_line = "==================================================\n"
    test_case_line += "= test case : " + test_case + "\n"
    test_case_line += "==================================================\n\n"
    total_result += test_case_line
    print(test_case_line)
        
    for s in glob.glob(file_directory):
        if(s.count('s1')>0):            
            test_result = "last executed file :" + s + '\n\n'
            
            os.system("python "+s + " < " + input_txt + " > " + output_txt)
            os.system("")
            
            test_output = open(output_txt, 'r')
            test_result += test_output.read();
            test_result += "\n\n-*-*-*-*-*-*-*-*-*-*-*-*-\n\n"
            
            total_result += test_result
            print(test_result)
            test_output.close()

    result_filename = "result_" + test_case + ".txt"
    result_file = open(result_filename, "w")
    result_file.write(total_result)
    result_file.close()
   

if os.path.exists(input_txt) == True:
    os.remove(input_txt)

if os.path.exists(output_txt) == True:
    os.remove(output_txt)
