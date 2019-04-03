# ZomatoAPI
Para que serve?

Essa Bliblioteca de Python serve para encontrar um restaurante inserindo os parametros latitude e longitude ou então a escolha pelo ip onde trará os restaurantes mais proximos. 

Por que eu usaria tal API?

Para encontrar um restaurante próximo, a API também oferece outros parametros de busca sendo o tipo de cozinha que o restaurante trabalha ou até mesmo o número de estrelas, mas neste exemplo utilizamos a localidade para encontrar todos os restaurantes mais próximos.

Como funciona?

Os parametros para a consulta são latitude e longitude, ou então o IP do dispositivo ao inserir trará os dados do restaurante. 

E se eu quiser apenas testar a API sem ter que criar um novo código?

Basta iniciar o client.py, informar o que é pedido e o link será gerado.

Processo de desenvolvimento:

Consta a documentação em https://developers.zomato.com/api?lang=pt#headline1, basta solicitar uma chave para o uso da API, foi utilizado o Flask para criar uma aplicação web e conforme a documentação foi inserido o header sendo a chave da API que é um dado obrigatório para consulta, e então utilizamos o parametro de consulta Search onde limitamos pela latitude e longitude ou IP do dispositivo, mas existem diversas querys que podem ser feitas.
