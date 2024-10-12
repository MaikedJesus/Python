import pyautogui 
#importando a biblioteca que permite monitora o movimento do mouse, do teclado e tbm a digitação;

from time import sleep
#pausa a execução pré definido no logo ao adiante


#pyautogui.click() <-- serve para levar o mouse a clicar na coodenada definida entre parênteses
#pyautogui.write("Mike") <-- como o propria tradução descreve, ele sever pra escrever o texto defido entre("")... 

pyautogui.click(672,385, duration=0.1)
pyautogui.write("Mike")

pyautogui.click(688,409, duration=0.1)
pyautogui.write("1234")

pyautogui.click(597,438, duration=0.1)


with open('produtos.txt','r') as extrair: #laço de repetição, ele vai acessar o arquivo e ler cada linha contido no arquivo;
  
   
  for linha in extrair: 
#split(,) -->splip significa "separar", então ele vai dividir os dados pela ",". nisso agente pode expecificar cada campo que ira ser preenchido, locanlizando pelos indices'[]';  

     produto = linha.split(',')[0]  
     quantidade= linha.split(',')[1]
     preco = linha.split(',')[2]

pyautogui.click(426,366, duration=0.2)
pyautogui.write(produto)

pyautogui.click(394,401, duration=0.2)
pyautogui.write(quantidade)


pyautogui.click(402,421, duration=0.2)
pyautogui.write(preco)


pyautogui.click(323,585, duration=0.2)

sleep(0.1)
