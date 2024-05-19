"""
Folder Oxuma

Bir folder icindeki tum fayllari os kitabxanasi ile oxuya bilerik

import os

tip:
    * folder
    * file
"""

# 1. Yol -> os.listdir()

# import os
# Oxunacaq olan folder
# folder = os.getcwd()
# folder_ici = os.listdir(folder)

# print(folder_ici)

# for ic in folder_ici:
#     print(ic)


# 2. Yol -> os.scandir()

# with os.scandir() as scans:
#     for scan in scans:
#         if scan.is_file():
#             print(scan)

# folder_ici = os.scandir()
# for ic in folder_ici:
#     print(ic)


# 3. Yol -> pathlib.Path.iterdir()
# from pathlib import Path
# folder = Path()
# folder_ic = folder.iterdir()

# for ic in folder_ic:
#     if ic.is_dir():
#         print(ic)


# ===============================================================

"""
Folder yaratma:
1 - os.mkdir()
    * mkdir() - Tek folder yaradir
    * makedirs() - Birden cox folder yaratmaq ucundur
    
2 - path.Path.mkdir() - hem tek hemde ikili folder yaratmaq ucundur
"""

# Tekli folder yaratmaq:
# import os
# from pathlib import Path

# ana_folder_yolu = os.getcwd()

# Numune:
# 1-ci Yol -> os.mkdir()
# os.mkdir("NewFolder2")

# 2-ci Yol -> pathlib.Path.mkdir()
# try:
#     p = Path("Path1")
#     p.mkdir()
# except FileExistsError:
#     print("Bu adda file movcuddur ona gore daha uygun bir adda sizin ucun file yaratdiq")
#     p = Path("Path2")
#     p.mkdir()


# 3. Yol -> Bir nece folder eyni anda yaratmaq os.makedirs()
# os.makedirs("Level1/Level2/Level3", exist_ok=True)


# ===============================================================

"""
Folder axtarma:
    * String Methodlar -> startswith, endswith, find
    * fnmatch 
"""

# import os
# from pathlib import Path
# import fnmatch

# String Methodlar
# string olaraq axtarilir -> r herfi ile baslayirsa

# axtarilan_folder = "C:\Windows"

# for ic in os.listdir(axtarilan_folder):
#     print(ic)


# Indi ise .exe olan fayllari ekrana cixardaq:
# with Path(axtarilan_folder) as folder:
#     for file in folder.iterdir():
#         # tip file-mi? ve sonu .exe-mi?
#         if file.is_file() and file.name.endswith(".exe"):
#             print(file)

# fnmatch ile axtarma:

# axtarilan_hisse = "*.exe"

# with Path(axtarilan_folder) as folder:
#     for file in folder.iterdir():
#         if file.is_file() and fnmatch.fnmatch(file, axtarilan_hisse):
#             print(file)
            
            
# ===============================================================

"""
Folder silme, yeniden adlandirma, kopyalama ve kocurme
"""

# from pathlib import Path
# import shutil
# import os

# Folder filme:
"""
os.rmdir() - Yalniz ici bos olan folderleri silir, doludursa xeta verir
pathlib.Path.rmdir() - Yalniz ici bos olan folderleri silir, doludursa xeta verir
shutil.rmtree() - butun folderi silir (ici dolu olsada)
"""
# os.mkdir("SilinecekFolder")
# os.rmdir("SilinecekFolder")
# Path("SilinecekFolder").rmdir()
# os.remove("SilinecekFolder")

# Ici dolu olan folderi butovlukle silmek isteyirsense:
# shutil.rmtree("SilinecekFolder")


# File kopyalama(kocurme)

# folder1 = "Folder1/"
# folder2 = "Folder2/"

# shutil.copy(folder1, folder2)
# shutil.copytree("Folder3", "Folder4")


# Folder kocurme
# shutil.move("Folder1", "Folder2")

# Folder ad deyisme
# os.rename("Folder2", "NewFolder2")







# .......NEW TASK.......

# Folder taskı

# 1) Ilk olaraq bir "Example" adında bir kateqoriya (directory) yaradırıq.
# 2)Daha sonra isə bu directorynin içərisində bir  "subdirect"  adında alt kateqoriya(subdirectory) yaradırıq.
# 3)Növbəti addımda bu subdirectorynin içərisinə  bir şəkil və bir text faylı əlavə edirik. 
# (şəkli ilk öncə manual olaraq hal hazırda olduğunuz qovluğun içərisinə sürüşdürüb  daha sonra alt kateqoriyaya əlavə edin, path-ini tapmağda çətinlik çəkməmək üçün)
# 4)daha sonra isə subdirectorynin içərisində olub sonu txt ilə bitən faylları subdirectorydən çıxarıb Example directory-sinə göndərirsiniz.



# import os
# import shutil

# os.makedirs('Example', exist_ok=True)

# os.makedirs('Example/subdirect', exist_ok=True)


# shutil.move('m.jpeg', 'Example/subdirect/m.jpeg')
# shutil.move('phyton kodlari.docx', 'Example/subdirect/phyton kodlari.docx')

# for file_name in os.listdir('Example/subdirect'):
#     if file_name.endswith('.txt'):
#         shutil.move(os.path.join('Example/subdirect', file_name), os.path.join('Example', file_name))     #?????????
# 




# Alqoritmik task

# Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. Biz isə onların topladığı xallara görə neçənci yeri tutduğunu print etməliyik. Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
# Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
# Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də o pozulmuş sıraya uyğun sıralanacaq və nəticə  düzgün olmayacaq. (taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
# Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.

def find_ranks(scores):
    sorted_scores = sorted(scores, reverse=True)
    ranks = [sorted_scores.index(score) + 1 for score in scores]
    formatted_ranks = [f"{rank}-ci" for rank in ranks]
    return formatted_ranks


xallar = [10, 32, 49, 21, 12]
yerler = find_ranks(xallar)
print(yerler) 
