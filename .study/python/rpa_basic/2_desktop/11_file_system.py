# img_...png
# kakao_talk_...png
# 202101232343.png

#파일 기본
import os
# print(os.getcwd())        # 현재 작업 공간
# # os.chdir("..")            # 부모폴더
# # print(os.getcwd())
# os.chdir("../..")           # 조부모폴더
# os.chdir(".")                 # 현재 작업공간
# print(os.getcwd())
# os.chdir("rpa_basic")       # rpa_basic으로 공간이동
# print(os.getcwd())
# os.chdir("c:/")             # 주어진 경로로
# print(os.getcwd())
#
# # 다시 원위치 ( /를 쓰려면 "", \를 쓰려면 r"" )
# # os.chdir("C:/Users/J/Desktop/untitled/rpa_basic/2_desktop")
# os.chdir(r"C:\Users\J\Desktop\untitled\rpa_basic\2_desktop")

# 파일 경로 만들기
# print(os.path.join(os.getcwd(), "my_file.txt"))
# file_path = os.path.join(os.getcwd(), "my_file.txt")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"C:\Users\J\Desktop\untitled\rpa_basic\2_desktop\my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime
#
# # 파일 생성 날짜
# file_path = "11_file_system.py"
# ctime = os.path.getctime(file_path)
# print(ctime)                                    # 머선 말이고?
# print(datetime.date.fromtimestamp(ctime))       # 알아듣게 씀
# print("생성날짜:\t\t", datetime.date.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))       # 자세하게
#
# # 파일 수정날짜 확인
# mtime = os.path.getmtime(file_path)
# print("수정날짜:\t\t", datetime.date.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))       # 자세하게
#
# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print("최근 접근날짜:\t", datetime.date.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))       # 자세하게
#
# # 파일 크기
# size = os.path.getsize(file_path)
# print(size)     #bytes


# 파일 목록 가져오기
# print(os.listdir())         # 모든 폴더, 모든 파일 목록 가져옴
# print(os.listdir("../../rpa_basic"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk("../../rpa_basic")         # 주어진 폴더 안 모든 폴더, 파일 목록 가져옴
# print(result)                               # ????? 하단처럼 작성하자.

# for root, dirs, files in result:
#     print(root, dirs, files)

# 폴더 내에서 특정 파일들을 찾으려면??????
# name = "11_file_system.py"
# result = []
# # for root, dirs, files in os.walk("."):            #현재경로에서 출력
# for root, dirs, files in os.walk(os.getcwd()):      #전체경로에서 출력
#     # [a.txt, b.txt, c.txt, ..., 11_file_system.py]
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 폴더 내에서 특정 파일들을 찾으려면??????
# *.xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = "*.py"        # 모든 py파일
# result = []
# for root, dirs, files in os.walk("."):
#     # [a.txt, b.txt, c.txt, ..., 11_file_system.py]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root, name))
# print(result)


# # 주어진 경로가 파일인지 폴더인지 확인하기
# print(os.path.isdir("../../rpa_basic"))     #폴더이면 True
# print(os.path.isfile("../../rpa_basic"))    #파일이면 True
#
# print(os.path.isdir("play.png"))     #폴더이면 True
# print(os.path.isfile("play.png"))    #파일이면 True
#
# # 만약에 지정된 경로에 해당 파일(폴더)가 없다면?
# print(os.path.isfile("./run_btn.png"))      #있으면 True, 없으면 False

# 주어진 경로가 존재하는가?
# if os.path.exists("bug11.png"):
#     print("네, 있네요")
# else:
#     print("없네요...")

# 파일 만들기
# with open("파일명", encoding="utf-8") as f:
#     .... 간단하게 하는걸 알아보자
# open("new_file.txt", "a").close()       #빈 파일 생성

# 파일명 변경하기
# os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 생성
# os.mkdir("new_folder")      # 현재경로에서 폴더생성, 이미 있다면 에러남
# os.makedirs("new_folders/a/b/c")   # 하위 폴더를 가지는 폴더 생성 시도

# 폴더 이름 바꾸기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("new_folder_rename")         # 폴더가 비었을 때만 가능

# import shutil       # shell utillities
# shutil.rmtree("new_folders")            # 있어도 다 날려버림 (주의!)

# 파일 복사하기
import shutil
# shutil.copy("play.png", "test_folder")      # 원본 파일 경로, 대상 폴더 경로
# shutil.copy("play.png", "test_folder/copied_play.png")      # 원본 파일 경로, 대상 경로 (새 파일의 이름)
# shutil.copyfile("play.png", "test_folder/copied_play_2.png")    # 원본 파일 경로, 대상 파일 경로(필수)
# shutil.copy2("play.png", "test_folder/copey2.png")

# copy, copyfile: 메타정보 X -> 복사시점의 메타정보가 대신 들어감
# copy2: 메타정보 복사 O -> 원본의 메타정보가 그대로 들어감 (만든 날짜, 수정 날짜 등)

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")       # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")         # 폴더 통채로 복사

# 폴더 이동
# shutil.move("test_folder", "test_folder3")      #test_folder를 3폴더 밑으로
# shutil.move("test_folder2", "test_folder3")
# shutil.move("test_folder3", "test_folder")      #test_folder가 없으므로 rename한 효과가 남
