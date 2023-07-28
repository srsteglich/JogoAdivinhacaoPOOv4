import os
import random
import time

class Joga:
    def __init__(self):
        self.ponto = 0
        self.vezes = 0
        self.infer = 0
        self.super = 0
        self.numCPU =0
        self.pontos = 0        

    def Tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\033[1;30;46m     PROCESSANDO!!!....\033[m1️⃣ ')
        time.sleep(0.8)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('\033[1;30;46m     PROCESSANDO!!!....\033[m2️⃣')
        time.sleep(0.8)
        os.system('cls' if os.name == 'nt' else 'clear') 
        print('\033[1;30;46m     PROCESSANDO!!!....\033[m3️⃣')
        time.sleep(0.8)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\033[1;34m-------------------------------------------------------------------------------")
        print("       Bem-vindo ao jogo de adivinhação de números, com pontuação do jogo!")  
        print("-------------------------------------------------------------------------------\033[m")    

        self.Tentar()
        
    def Tentar(self):
        self.nivel = 0
        while self.nivel != 4:       
            print("  Qual o nível de dificuldade de tentativas? ")
            print("  1 - Fácil (20 Tentativas)")
            print("  2 - Médio (10 Tentativas)")
            print("  3 - Difícil (05 Tentativas)")
            print("  4 - Sair do Jogo")
            self.nivel = input("  Digite um número para nível de dificuldade: ")               
            if self.nivel.isdigit():
                self.nivel = int(self.nivel)        
                if self.nivel == 1:
                    self.ponto = 5
                    self.vezes = 20                                
                    break
                elif self.nivel == 2:
                    self.ponto = 10
                    self.vezes = 10                                              
                    break            
                elif self.nivel == 3:
                    self.ponto = 30            
                    self.vezes = 5                                
                    break
                elif self.nivel == 4:   
                    print("\n\033[0;32m  Saiu...\033[m\n")
                    print("\033[1;36m        Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
                    time.sleep(1.5)
                    os.system('cls' if os.name == 'nt' else 'clear')                         
                    exit()
                else: 
                    print("\n\033[1;31m  Opção inválida.... Escolha os números selecionados! \033[m 👀\n")  
                    time.sleep(1.0)
                    os.system('cls' if os.name == 'nt' else 'clear')                         
                continue
            else:
                print("\n\033[1;31m   Valor informado não é numérico. Favor execute e informe um número selecionado!\033[m 👀")
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')  

        #print(" Metodo Tentar - linha 70 - Ponto", self.ponto, " Vezes",self.vezes)
        self.Limitar()
        
    def Limitar(self):       
        print("\n  Escolha os limites do Jogo de 1 a 100, o ideal é a diferença até 50 números. ")    
        while True:    
            self.infer = int(input("  Digite o limite inferior: "))
            self.super = int(input("  Digite o limite superior: "))                          
            self.quant = (self.super+1) - self.infer   
            # quando maior quantidade do limites é mais dificil    
            if 2 <= self.quant <= 9: 
                self.pontos = self.ponto + 5   
                break            
            elif 10 <= self.quant <= 19:
                self.pontos = self.ponto + 10                    
                break               
            elif 20 <= self.quant <= 29:
                self.pontos = self.ponto + 20
                break               
            elif 30 <= self.quant <= 39:
                self.pontos = self.ponto + 30            
                break              
            elif 40 <= self.quant <= 50:
                self.pontos = self.ponto + 40            
                break   
            elif 51 <= self.quant <=100:             
                self.pontos = self.ponto + 50            
                break   
            else:       
                print("\033[0;31m  Valor invalido.\033[m") 
                print("\033[0;31m  O limite superior não pode ser menor ou igual que limite inferior....\033[m")                           
                continue
                    
        #print(" Metodo Limitar - linha 103 - Pontos +:", self.pontos)
        self.Gerar()
        
    def Gerar(self):
        print("\033[0;32m    O número foi gerado agora precisa adivinhar o número escolhido de",self.infer,"até",self.super,".")
        print("    E tem",self.vezes,"tentativas.\033[m")
        self.numCPU = random.randint(self.infer,self.super)
        for self.vez in range(1, self.vezes + 1):
            print("\033[0;36m   A",self.vez,"tentativa.\033[m")
            self.palpt = int(input("   Digite o seu palpite: "))           
            if self.palpt < self.numCPU:
                print("        Tente um número\033[0;36m MAIOR!\033[m")
                self.pontos = self.pontos - 10
            elif self.palpt > self.numCPU:
                print("        Tente um número\033[0;36m MENOR!\033[m")
                self.pontos = self.pontos - 10
            else:
                break        

        #print(" Metodo Gerar - linha 124 - Ponto -2:", self.pontos, " Numero CPU", self.numCPU)        
        self.Finalizar()       
        
    def Finalizar(self):
        if self.palpt == self.numCPU:
            print("\n\033[0;36m  Uuuuhhhhh.... Você acertou o número ",self.numCPU," e foram ",self.vez,"vezes.")        
            print("  E a tua Pontuação do Jogo foi: ",self.pontos,"pontos.")
            if self.pontos >= 40:
                print("  A tua Pontuação do Jogo foi Muito Excelente!!!!! Parabéns...\033[m\n")
            else:    
                if self.pontos >= 10:
                    print("  A tua Pontuação do Jogo foi Bom!!!!! Parabéns...\033[m\n")      
                else:
                    if self.pontos >= 5:
                        print("  A tua Pontuação do Jogo foi Razoável...\033[m\n")
                    else:    
                        print("  A tua Pontuação do Jogo foi muito Baixo...\033[m\n")                        
        else:
            print("\n  Não foi desta vez.... O Número Secreto era",self.numCPU,".\n")
            print("  E a tua Pontuação do Jogo foi:",self.pontof,"pontos.\033[m\n")

        resp = input("\033[0;33m  Deseja Jogar novamente[S/N]?\033[m]").upper()
        if resp == 'S':               
            self.Tentar() 
        else:    
            print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
            print("\n\033[1;31m   Encerrado, até próxima!!!\033[m\n") 
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')       
            exit()            
        
        #print(" Metodo Finalizar - linha 152- NumCPU ", self.numCPU, " Ponto Final", self.pontof)

jogar = Joga()    
jogar.Tela()