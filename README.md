# Отправка GET и POST запросов на мой микросервис
![Alt Text](gitthings/gf.gif)

# Apache server 
![Alt Text](gitthings/kurtaev_site_apache.jpg)

# HTTPS SSL security
![Alt Text](gitthings/https_ssl_connection.jpg)

## certificate
![Alt Text](gitthings/certificate.jpg)

## Создание микросервиса

### Цель работы

Познакомиться с механизмом работы современных веб-приложений и микросервисной архитектуры в процессе выполнения творческого задания.

### Задания для выполнения

1. На основе предложенного шаблона реализуйте сервис, реализующий регистрацию пользователей. Сервис должен поддерживать REST API и коллекцию /user/, хранящую данные о логинах и паролях пользователей, зарегистрированных в системе. Сервис должен принимать и отдавать информацию в формате JSON. Сервис должен хранить следующую информацию про каждого пользователя: логин, хеш пароля (лучше с солью), дату регистрации.  

1. Настройте веб-сервер по Вашему выбору (Apache2 или nginx) таким образом, чтобы он поддерживал соединение по протоколу HTTPS. Для этого сгенирируйте самоподписанный сертификат SSL. 

1. Модифицируйте код вашего сервиса таким образом, чтобы он поддерживал защищенное соединение.
