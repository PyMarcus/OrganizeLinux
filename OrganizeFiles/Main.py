from MakeD import MakeAll
from colorama import Fore
from threading import Thread


class OrganizeFiles:
    def __init__(self, nomeDir='Downloads'):
        # main class
        self.__nomeDir = nomeDir

    @staticmethod
    def ui():
        print(Fore.LIGHTYELLOW_EX + """     
        
                               TUDO ORGANIZADO  :)                                                                  
                                                                                
                                   #@@%@@@@@#@                                  
         .  .   .                @@ .   .     @@                 . .            
                       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
                      @@                                 @&                     
                      @@                                 @&                     
                      @@                                 @&                     
                      @@                                 @&                     
                      @#                              .  @#                     
                      @%            @@&&&&&@#            ##                     
                      @@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@&                     
                      @@             @@@@@@&             @&                     
                      @@                                 @&                     
                      @@                                 @&                     
                  .   @@                                 @#        .            
            .           @@@@@@@@@@&@@#@@@@@@@@&@@@@@@@@@@                       
                                                                                
                                                                       """.center(20))
        print()

    def run(self, escolha):
        if escolha == '1':
            MakeAll.imagens()
        elif escolha == '2':
            MakeAll.pdfs()
        elif escolha == '3':
            MakeAll.video()
        elif escolha == '4':
            MakeAll.musicas()
        elif escolha == '5':
            MakeAll.texto()
        elif escolha == '6':
            MakeAll.docs()
        elif escolha == '7':
            MakeAll.excels()
        elif escolha == '0':
             threads = [
            Thread(MakeAll.imagens(), args=()),
            Thread(MakeAll.pdfs(), args=()),
            Thread(MakeAll.video(), args=()),
            Thread(MakeAll.musicas(), args=()),
            Thread(MakeAll.texto(), args=()),
            Thread(MakeAll.docs(), args=()),
            Thread(MakeAll.excels(), args=())]

            [t.start() for t in threads]
            [t.join() for t in threads]
        else:
            print(Fore.RED + "Op????o inv??lida")


if __name__ == '__main__':
    objeto = OrganizeFiles()
    ok = True
    while ok:
        try:
            escolha = input(">>> ")
        except ValueError:
            pass
        else:
            OrganizeFiles.ui()
            opcoes = ['0', '1', '2', '3', '4', '5', '6', '7']
            if escolha in opcoes:
                objeto.run(escolha)
                ok = False

