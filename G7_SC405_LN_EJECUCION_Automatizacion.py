import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyboard import press
from selenium.webdriver.support.ui import Select
import time

driver= webdriver.Chrome("/Users/DYL4N16199/Desktop/chromedriver")

def login_exitoso(driver):
    
    username = "admin"
    password = "admin"
    
    

    driver.get("http://localhost:8080/bankoint/administrator/")

    user=driver.find_element ("id","inputEmail")
    user.send_keys(username)
    passw=driver.find_element ("id","inputPassword")
    passw.send_keys(password)
    passw.submit()
    print("logged in succesfully")
    time.sleep (2)
#class="nav-link collapsed" catalogos
#cata= WebDriverWait(driver, 20).until(EC.element_to_be_clickable(driver.find_element ("class","nav-link collapsed")))
#cata.click()
def apartado_Clientes(driver):
    cata=driver.find_element ("link text","CATALOGOS")
    cata.click()
    time.sleep (1)
    clie=driver.find_element ("link text","Clientes")
    clie.click()
    time.sleep(1)








#Nuevo cliente 
def nuevo_cliente(driver):
     
    nuev=driver.find_element ("link text","Nuevo")
    nuev.click()

    #driver.get("http://localhost:8080/bankoint/administrator/index.php?view=persons&opt=new")
    time.sleep(1)
    Nombre=" anonimo"
    Apellido= "apellido"
    Telefono="11111111"
    Direccion= "Casa 9e"
    Email="anonimo@gmail.com"
    Contraseña="1234"
    #Comandos para rellenar datos del cliente # de caso = CU_8
    Nom=driver.find_element ("id", "name")
    Nom.send_keys(Nombre)

    ape=driver.find_element ("id", "lastname")
    ape.send_keys(Apellido)

    tele=driver.find_element ("id", "phone")
    tele.send_keys(Telefono)

    dire=driver.find_element ("id", "address")
    dire.send_keys(Direccion)

    correo=driver.find_element ("id", "email")
    correo.send_keys(Email)

    passcliente=driver.find_element ("id", "inputEmail1")
    passcliente.send_keys(Contraseña)
    time.sleep(5)
    passcliente.submit()
    time.sleep(1)
    
    press("enter")
    print("Cliente agregado exitosamente")
    time.sleep(4)
#editar cliente
def editar_cliente(driver):
    time.sleep(1)
    edit=driver.find_element ("link text","Editar").click()

    EdiNombre= "Cliente1"
    EdiApellido= "cli"
    EdiTelefono="22222222"
    EdiDireccion= "casa 3a"
    EdiEmail= "cliente1@gmail.com"
    EdiContraseña="4321"
    #Comandos para rellenar datos del cliente # de caso = CU_8
    Nom=driver.find_element ("id", "name")
    Nom.clear()
    Nom.send_keys(EdiNombre)

    ape=driver.find_element ("id", "lastname")
    ape.clear()
    ape.send_keys(EdiApellido)

    tele=driver.find_element ("id", "phone")
    tele.clear()
    tele.send_keys(EdiTelefono)

    dire=driver.find_element ("id", "address")
    dire.clear()
    dire.send_keys(EdiDireccion)

    correo=driver.find_element ("id", "email")
    correo.clear()
    correo.send_keys(EdiEmail)

    passcliente=driver.find_element ("id", "inputEmail1")
    passcliente.clear()
    passcliente.send_keys(EdiContraseña)

    passcliente.submit()

    time.sleep(1)

    press("enter")


    print("Cliente modificado exitosamente")

def login_Contraseña_Incorrecta(driver):
    
    username = "admin"
    password = "1234"
    
    

    driver.get("http://localhost:8080/bankoint/administrator/")

    user=driver.find_element ("id","inputEmail")
    user.send_keys(username)
    passw=driver.find_element ("id","inputPassword")
    passw.send_keys(password)
    passw.submit()
    print("logged in succesfully")
    time.sleep (2)



def login_Usuario_No_registrado(driver):
    
    username = "juan"
    password = "1234"
    
    

    driver.get("http://localhost:8080/bankoint/administrator/")

    user=driver.find_element ("id","inputEmail")
    user.send_keys(username)
    passw=driver.find_element ("id","inputPassword")
    passw.send_keys(password)
    passw.submit()
    print("logged in succesfully")
    time.sleep (2)

def prueba_Deposito(driver):
    driver.find_element("link text", "NUEVO DEPOSITO").click()
    descr = "Deposito de prueba 1"
    monto= 1000
    OptionValue= Select(driver.find_element(By.NAME,"person_id"))
    OptionValue.select_by_value("4")
    driver.find_element(By.ID,"description").send_keys(descr)
    driver.find_element(By.ID,"amount").send_keys(monto)
    driver.find_element(By.CSS_SELECTOR,"div button").click()
    time.sleep(2)
    press('enter')

def prueba_Deposito_Negativo(driver):

    driver.find_element("link text", "NUEVO DEPOSITO").click()
    descr = "Deposito negativo"
    monto= -5000
    OptionValue= Select(driver.find_element(By.NAME,"person_id"))
    OptionValue.select_by_value("4")
    driver.find_element(By.ID,"description").send_keys(descr)
    driver.find_element(By.ID,"amount").send_keys(monto)
    driver.find_element(By.CSS_SELECTOR,"div button").click()

def prueba_Log_usuario():
    username = "cliente1@gmail.com"
    password = "1234"

    driver.get("http://localhost/bankoint")
    time.sleep (3)
    driver.find_element("link text", "ACCEDER").click()
    time.sleep (3)
    driver.find_element(By.NAME,"username").send_keys(username)
    time.sleep (3)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep (3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/button").click()
    print("logged in succesfully")
    time.sleep (3)
    driver.find_element(By.LINK_TEXT,"Enviar").click()
    time.sleep (3)

    email ="cliente2@gmail.com"
    driver.find_element(By.NAME,"email").send_keys(email)
    time.sleep (3)

    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/button").click()
    description = "Prestamo"
    time.sleep (3)
    amount = "1000"
    time.sleep (3)
    driver.find_element(By.NAME,"description").send_keys(description)
    time.sleep (3)
    driver.find_element(By.NAME,"amount").send_keys(amount)
    time.sleep (3)  
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/button").click()

def prueba_Log_erroneo(driver):
    username = "cliente5@gmail.com"
    password = "1111"

    driver = webdriver.Edge(executable_path=r"C:\Driver_Crome and Edge\msedgedriver.exe")
    driver.get("http://localhost/bankoint")
    time.sleep (3)
    driver.find_element("link text", "ACCEDER").click()
    time.sleep (3)
    driver.find_element(By.NAME,"username").send_keys(username)
    time.sleep (3)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep (3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/button").click()
    print("logged in succesfully")
    time.sleep (3)
    
def enviar_puntos_sinCompletar(driver):
    username = "cliente1@gmail.com"
    password = "1234"

    driver = webdriver.Edge(executable_path=r"C:\Driver_Crome and Edge\msedgedriver.exe")
    driver.get("http://localhost/bankoint")
    time.sleep (3)
    driver.find_element("link text", "ACCEDER").click()
    time.sleep (3)
    driver.find_element(By.NAME,"username").send_keys(username)
    time.sleep (3)
    driver.find_element(By.NAME,"password").send_keys(password)
    time.sleep (3)
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div[2]/form/button").click()
    print("logged in succesfully")
    time.sleep (3)
    driver.find_element(By.LINK_TEXT,"Enviar").click()

    email ="cliente2@gmail.com"
    time.sleep (3)
    driver.find_element(By.NAME,"email").send_keys(email)
    time.sleep (3)
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/button").click()
    driver.find_element(By.XPATH,"/html/body/div[1]/div/div/form/button").click()

def usuario_administrador(driver):
    Nombre = "Admin2"
    Apellido = "Ape"
    Usuario = "Admin2"
    Email = "admin2@gmail.com"
    Contraseña = "1234"

    driver.find_element("link text", "USUARIOS").click()
    time.sleep (1)
    driver.find_element("link text", "Nuevo").click()

    Nom=driver.find_element("id", "name")
    Nom.send_keys(Nombre)
    time.sleep (1)
    ape=driver.find_element("id", "lastname")
    ape.send_keys(Apellido)
    time.sleep (1)
    user=driver.find_element("id", "username")
    user.send_keys(Usuario)
    time.sleep (1)
    correo=driver.find_element("id", "email")
    correo.send_keys(Email)
    time.sleep (1)
    passAdmin=driver.find_element("id", "inputEmail1")
    passAdmin.send_keys(Contraseña)
    time.sleep (1)
    passAdmin.submit()
    print("Administrador agregado correctamente")
    time.sleep (4)

def eliminar_deposito(driver):
    driver.find_element("link text", "OPERACIONES").click()
    time.sleep (1)
    driver.find_element("link text", "Todas las operaciones").click()
    driver.find_element("link text", "Eliminar").click()
    time.sleep (4)


def eliminar_cliente(driver):
    driver.find_element("link text", "CATALOGOS").click()
    time.sleep (1)
    driver.find_element("link text", "Clientes").click()
    driver.find_element("link text", "Eliminar").click()
    
    
if __name__ == '__main__':
    print("=============================================================")
    print("Pruebas automatizadas del grupo 7")
    print("=============================================================")

    caso1=login_exitoso(driver)

    aparCli= apartado_Clientes(driver)
    
    caso6=nuevo_cliente(driver)
     
    caso7=editar_cliente(driver)

    caso2=login_Contraseña_Incorrecta(driver)

    caso3=login_Usuario_No_registrado(driver)

    caso5=prueba_Deposito(driver)

    caso4=prueba_Deposito_Negativo(driver)

    caso11y13=prueba_Log_usuario(driver)

    caso12=prueba_Log_erroneo(driver)

    caso14=enviar_puntos_sinCompletar(driver)

    caso10= usuario_administrador(driver)

    caso9=eliminar_deposito(driver)

    caso8=eliminar_cliente(driver)


    

    
    


print("Caso de prueba automatizada realizada exitosamente")



