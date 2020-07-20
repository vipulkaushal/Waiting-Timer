from IPython.display import clear_output
import time

j=0

while(j<50):

    print('\ ')
    clear_output(wait=True)
    time.sleep(1)      
    print('|')
    clear_output(wait=True) 
    time.sleep(1)       
    print('/')
    clear_output(wait=True)
    time.sleep(1)       
    print('-')
    clear_output(wait=True)      
    time.sleep(1) 
    print('\ ')
    clear_output(wait=True)
    time.sleep(1)      
    print('|')
    clear_output(wait=True)
    time.sleep(1)       
    print('/')
    clear_output(wait=True)
    time.sleep(1)       
    print('-')  
    clear_output(wait=True)
    time.sleep(1)       
    j=j+1
