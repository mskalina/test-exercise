# BIN verifier

## Description

Сервис представляет собой сайт по выдаче информации по карте по bin коду карты. 

При вводе верного bin кода из базы сайта, хранящейся в csv файле, пользователь увидит данные по карте. 

При вводе неверного либо неизвестного bin кода пользователь увидит ошибку.


## Обязательная часть задания

1. Создайте fork от репозитория и дальнейшие действия проводите с ним.
2. В своем новом репозитории создайте новую ветку от main(master) с названием develop. 
3. Запустите сервис с помощью docker, пользуясь готовым dockerfile
4. Создайте файл с UI + Api тест кейсами на функционал сайта. Если текущая документация кажется вам неполной,
самостоятельно определите для себя верное поведение в тех или иных сценариях, и пишите тест кейсы согласно своему видению. Приветствуется написание тест кейсов исходя из анализа кода сервиса.
5. Напишите столько автоматизированных UI/API тестов, сколько посчитаете нужным. Пожелания к стеку: python + pytest + selenium + requests
6. В качестве решения тестового задания пришлите ссылку на свой github репозиторий

## Не обязательная часть задания

Создайте документацию на сервис в отдельном файле исходя из своих тест кейсов и кода сервиса, залейте ее также в ветку develop. 

Любой удобный вам формат документации