import os
import time
from FindFiles import FindFiles
from shutil import move
from os import mkdir, chdir


class MakeAll:
    """
    This class create a dir for the files and move it
    """
    classe = FindFiles()
    itens = classe.search()
    imagem, pdf, videos, musica, doc, textos, excel = FindFiles.verify()

    @classmethod
    def imagens(cls):
        # create dir
        if MakeAll.imagem > 0:
            if 'Img' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[0]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Img')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Img')
                time.sleep(1)
                for item in MakeAll.itens[0]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Img')

    @classmethod
    def pdfs(cls):
        if MakeAll.pdf > 0:
            if 'Pdfs' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[2]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Pdfs')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Pdfs')
                time.sleep(1)
                for item in MakeAll.itens[2]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Pdfs')

    @classmethod
    def video(cls):
        if MakeAll.videos > 0:
            if 'Vids' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[1]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Vids')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Vids')
                time.sleep(1)
                for item in MakeAll.itens[1]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Vids')

    @classmethod
    def texto(cls):
        if MakeAll.textos > 0:
            if 'Textos' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[4]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Textos')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Textos')
                time.sleep(1)
                for item in MakeAll.itens[4]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Textos')

    @classmethod
    def musicas(cls):
        if MakeAll.musica > 0:
            if 'Musics' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[6]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Musics')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Musics')
                time.sleep(1)
                for item in MakeAll.itens[6]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Musics')

    @classmethod
    def excels(cls):
        if MakeAll.excel > 0:
            if 'Excels' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[5]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Excels')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Excels')
                time.sleep(1)
                for item in MakeAll.itens[5]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Excels')

    @classmethod
    def docs(cls):
        if MakeAll.doc > 0:
            if 'Docs' in os.listdir(MakeAll.itens[8]):
                for item in MakeAll.itens[3]:
                    chdir(MakeAll.itens[8])
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Docs')
            else:
                chdir(MakeAll.itens[8])
                mkdir(MakeAll.itens[8] + 'Docs')
                time.sleep(1)
                for item in MakeAll.itens[3]:
                    for caminhos in item:
                        move(caminhos, MakeAll.itens[8] + 'Docs')


if __name__ == '__main__':
    MakeAll.imagens()
    MakeAll.pdfs()
    MakeAll.video()
    MakeAll.musicas()
    MakeAll.texto()
    MakeAll.docs()
    MakeAll.excels()
