# DHT11-INVERNADERO
SITEMA DE MONITOREO DE TEMPERATURA Y HUMEDAD INTEGRADO A IoT
Con la necesidad de poder monitorear parámetros en un invernadero y ser consciente de las condiciones atmosféricas presentes, en este trabajo final se abordará la interacción de sistemas, componentes electrónicos e Internet.
Este proyecto aspira entre sus objetivos principales, obtener mediante gráficos las lecturas de temperatura y humedad mediante el uso de un sensor dht11.
Para llevar a cabo esta idea, se diseñará e implementará una solución que permitirá a los usuarios finales acceder a través de un portal web a la información en tiempo real, mediante la plataforma llamada Thingspeak.

# DIAGRAMA

![diagrama fritzing](https://user-images.githubusercontent.com/79615803/122656838-e3bff200-d123-11eb-8470-486e32a5c3d2.jpg)

# LIBRERIAS
Aunque se ha dicho que el sensor es digital, en realidad esto no es del todo correcto, ya que realmente el sensor es analógico, pero internamente se realiza la conversión a señal digital.
Actualmente existen librerías que recogen y devuelven los valores en decimal. Una de estas librerías es Adafruit. 


![ADAF](https://user-images.githubusercontent.com/79615803/122656883-4adda680-d124-11eb-9fb5-24892f30032e.jpg)
![DGTXXX](https://user-images.githubusercontent.com/79615803/122656884-4dd89700-d124-11eb-8988-9254426bb410.jpg)

