import time
from glob import glob
from os import chdir
from getpass import getuser
from colorama import Fore


class FindFiles:
    """
    Find the files in dir and return a list with they
    """
    image = ['.png', '.jpg', '.img', '.jpeg', '.gif']
    pdf = ['.pdf']
    doc = ['.doc', 'docx', '.odt']
    txt = ['.txt']
    #others = ['.ppt', '.deb', '.html', '.docx', '.zip', '.tar', '.log', '.ppt']
    excel = ['.xlx', '.csv', '.xlsx', '.xml']
    music = ['.mp3']
    video = ['.mp4', '.mv', '.mov', '.webm', '.mkv']
    _txt = []
    _images = []
    _doc = []
    _music = []
    _video = []
    _excel = []
    _pdf = []
    _diretorio = ''
    _others = []
    user = getuser()

    def __init__(self, dir_name="Downloads/"):
        """
        prompts for directory name, default = Downloads
        :param dir_name:
        """
        self.__dir_name = f"/home/{FindFiles.user}/{dir_name}"
        _diretorio = self.__dir_name
        self.__images = []
        self.__pdf = []
        self.__video = []
        self.__music = []
        #self.__others = []
        self.__doc = []
        self.__excel = []
        self.__txt = []

    def search(self):
        chdir(self.__dir_name)
        _diretorio = self.__dir_name
        # imagens
        for i in range(len(FindFiles.image)):
            self.__images.append((glob(f"{self.__dir_name}/*{FindFiles.image[i]}")))
        FindFiles._images = [len(x) for x in self.__images]
        # pdf
        for i in range(len(FindFiles.pdf)):
            self.__pdf.append(glob(f"{self.__dir_name}/*{FindFiles.pdf[i]}"))
        FindFiles._pdf = [len(x) for x in self.__pdf]
        # doc
        for i in range(len(FindFiles.doc)):
            self.__doc.append(glob(f"{self.__dir_name}/*{FindFiles.doc[i]}"))
        FindFiles._doc = [len(x) for x in self.__doc]
        # txt
        for i in range(len(FindFiles.txt)):
            self.__txt.append(glob(f"{self.__dir_name}/*{FindFiles.txt[i]}"))
        FindFiles._txt = [len(x) for x in self.__txt]
        # others
        """for i in range(len(FindFiles.others)):
            self.__others.append(f"{self.__dir_name}*{FindFiles.others[i]}")
        FindFiles._others = [len(x) for x in self.__others]"""
        # excel
        for i in range(len(FindFiles.excel)):
            self.__excel.append(glob(f"{self.__dir_name}/*{FindFiles.excel[i]}"))
        FindFiles._excel = [len(x) for x in self.__excel]
        # music
        for i in range(len(FindFiles.music)):
            self.__music.append(glob(f"{self.__dir_name}/*{FindFiles.music[i]}"))
        FindFiles._music = [len(x) for x in self.__music]
        # video
        for i in range(len(FindFiles.video)):
            self.__video.append(glob(f"{self.__dir_name}/*{FindFiles.video[i]}"))
        FindFiles._video = [len(x) for x in self.__video]

        return self.__images, self.__video, self.__pdf, self.__doc, self.__txt, self.__excel, self.__music, self.__video, _diretorio

    @classmethod
    def verify(cls):
        image = sum(list(FindFiles._images))
        pdf = sum(FindFiles._pdf)
        video = sum(FindFiles._video)
        #others = sum(FindFiles._others)
        music = sum(FindFiles._music)
        excel = sum(FindFiles._excel)
        doc = sum(FindFiles._doc)
        txt = sum(FindFiles._txt)
        print(Fore.LIGHTGREEN_EX + "---" * 10)
        time.sleep(2)
        print("Foram encontrados:")
        print(f"{image} imagens\n{pdf} pdfs\n{video} vídeos\n{txt} textos\n{music} música\n{excel} excel e afins\n{doc} doc\n")
        print("---" * 10)
        time.sleep(2)
        print(Fore.CYAN + "Escolha uma das opções:")
        print("0 - todos")
        print("1 - imagens")
        print("2 - pdfs")
        print("3 - vídeos")
        print("4 - músicas")
        print("5 - textos")
        print("6 - docs")
        print("7 - excels")
        total = (image, pdf, video,  music, doc, txt, excel)
        return total


if __name__ == '__main__':
    obje = FindFiles()
    obje.search()
    FindFiles.verify()
