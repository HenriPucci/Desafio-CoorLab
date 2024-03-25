# Resultado - Desáfio CoorLab

* Primeiramente, comecei a montar todo o meu Front com HTML e CSS, utilizando-se do encaixe de componentes na página principal.Dessa forma, separei meu ambiente de Front estático em dois componentes, que seria o menu lateral e a área princiapl da página.

* Após o desenvolvimento do Front que ficaria estático na página, comecei a implementação da lógica do BackEnd, esse sendo feito em Python.

* No desenvolvimento do BackEnd, primeiramente, após criar um servidor na porta 3000, começo carregando os dados do arquivo JSON disponibilizado pelo desafio, possibilitando a extração das cidades dos dados do JSON.

* Após isso, começo o desenvolvimento da classe para o manipulador de requisições http. Primeiro monto o método para poder tratar das requisições Get, envio uma lista de cidades como respsta para a rota destinys,
obtenho o parâmetro destiy da query string, faço o tratamento de erro, faço a filtragem das viagens para o destino especificado, novamente faço um tratamento de erro caso não houver viagens para destino específico, faço a filtragem de viagem mais economica e mais rapida para o destinoe e envio essas viagens.

* Depois do desenvolvimento do Back na pasta app.py, retorno para a pasta com o componente TheMain.vue, para implementar a interação do usuário com a pagina, para isso, começo na parte de Scripts do componente.

* De forma simples, já carrego todos os destinos na hora em que o componente é carregado na página, e após isso, começo a montar os metodos que serão utilizados. o primeiro método seria o de procurar os destinos que estão presentes no servidor, após isso, com a funcionalidade de se buscar por opções de viagens, monto o metodo para buscar viagens que atendem a aquele destino antes escolhido, retornando a viagem mais confortável e a mais economica. Mas antes, preciso garantir que tanto a data quanto o destino foram selecionados pelo usuário, dessa forma, fazendo uma verificação disso.

