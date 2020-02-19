# Game Theory - Teste de Personalidades
> Projeto visa criar um modelo que empiricamente teste modelos de personalidades em jogos simples de tomada de decisão

O projeto possui dois módulos básicos:

    * Players
    * Game

O player é uma classe responsável por categorizar e definir o comportamento de cada jogador dada sua personalidade

O Game é o módulo onde estão definidas as regras e consequência de cada ato para cada um dos players

## Regras

Os tipos de players são:

    * Fool: Sempre aposta
    * Bad: Nunca aposta
    * Raging: Aposta até perder pela primeira vez e nunca mais aposta 
    * Pardoner: Aposta até perder pela primeira vez contudo volta a apostar após uma nova vitória
    * Swindler: Aposta até win streak de 2 do oponente então para de apostar e só retorna após lose streak de 2. 


## Execução

Para execução dos referidos módulos é necessário apenas que o computador possua uma versão de Python3 instalado visto que nenhuma biblioteca externa foi utilizada

## Exemplo de uso

A utilização básica se dá a fins didáticos de reconhecer qual a melhor forma de comportamento dadas as possibilidades de personalidade que virão a ser adotadas 

## Configuração para Desenvolvimento

A fim de executar faz-se necessário apenas execução do comando abaixo estando uma vez dentro da pasta do projeto

```sh
python main.py
```

## Histórico de lançamentos

Ainda em construção

## Meta

Luiz Filipe S Mariz – [@luiz_mustang](https://twitter.com/luiz_mustang) – lfsmariz@gmail.com


[https://github.com/mustang-roy](https://github.com/mustang-roy)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/mustang-roy/test-gametheory>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/fooBar`)
3. Faça o _commit_ (`git commit -am 'Add some fooBar'`)
4. _Push_ (`git push origin feature/fooBar`)
5. Crie um novo _Pull Request_

