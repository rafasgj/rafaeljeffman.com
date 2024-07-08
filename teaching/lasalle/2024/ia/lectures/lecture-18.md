---
section: Inteligência Artificial
title: Exercícios de Revisão
subtitle:
layout: lecture
last_occurrence: 2024-07-01
copy: 2024
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2024/ia
extra_styles: []
---

## Questão 1

### TEXTO 1

A Inteligência Artificial (IA) generativa é capaz de criar novos dados, únicos, que possibilitam aprender
por conta própria, indo além do que a tecnologia tradicional proporciona, visto que esta precisa de
intervenção humana. Um exemplo da IA generativa é o ChatGPT, que pode gerar imagens, músicas e
textos completamente novos. Entre outras coisas, por meio da IA generativa, é possível elaborar
modelos de previsão de testes clínicos, realizar a identificação de padrões em exames médicos e, ainda,
auxiliar no diagnóstico de doenças.

### TEXTO 2

Acredita-se que a tecnologia de IA generativa será disruptiva e, portanto, capaz de alterar drasticamente
a maneira como o ser humano se relaciona com as máquinas. O uso da IA generativa pode causar
importante revolução no segmento de produção de conteúdo. Muitas dessas consequências poderão
ser maléficas para diversos setores da sociedade. Além do mau uso dessa tecnologia e das questões
éticas, avalia-se que ela pode agravar a desigualdade econômico-social, tanto entre nações quanto
entre indivíduos da mesma nação.

Considerando os textos apresentados, é correto afirmar que a IA generativa:

* proporciona novos recursos de linguagem que geram tecnologias capazes de realizar interações
próprias dos seres humanos.
* restringe o aprendizado ao que é legalmente estabelecido e útil ao ser humano, o que facilita seu
modo de agir no mundo do conhecimento e do trabalho.
* promove a igualdade econômico-social ao substituir o ser humano no exercício de profissões cujas
atividades sejam repetitivas e exijam pouco conhecimento.
* gera pouco impacto socioeconômico em países com elevado desenvolvimento tecnológico, pois,
neles, os processos de criação e inovação já estão bem consolidados.
* estimula o desenvolvimento intelectual dos seres humanos, uma vez que ela assume parte do
conhecimento, resolvendo problemas antes delegados apenas a especialistas.
{:class="lettered"}

<details><summary>Resposta...</summary>
<p>Uma vez que a IA generativa é treinada com um gerador (capaz de gerar exemplos quase reais) e um discriminador (capaz de "entender" os exemplos gerados), é possível criar novas interfaces baseadas numa comunicação mais próxima a linguagem coloquial, fazendo com que a máquina se passe por um humano.</p>
</details>

## Questão 2

O teste de Turing foi projetado para fornecer uma definição operacional satisfatória de inteligência. O computador passará no teste se um interrogador humano, depois de propor algumas perguntas por escrito, não conseguir descobrir se as respostas escritas vêm de uma pessoa ou de um computador. O teste de Turing evitou deliberadamente a interação física direta entre o interrogador e o computador porque a simulação física de uma pessoa é desnecessária para a inteligência. Entretanto, o chamado teste de Turing total inclui um sinal de vídeo, de forma que o interrogador possa testar as habilidades de percepção do indivíduo, além de oferecer ao interrogador a oportunidade de repassar objetos físicos “pela janelinha”. Para ser aprovado no teste de Turing total, o computador precisaria ter seis capacidades.

Sabendo destas informações, numere a coluna da direita (capacidade) de acordo com sua correspondência com a coluna da esquerda (funcionalidade).

| :-- | :-- |
| 1 - Processamento de linguagem natural | ( ) Permite manipular objetos e movimentar-se. |
| 2 - Representação de conhecimento | ( ) Permite adaptar-se a novas circunstâncias, para detectar e extrapolar padrões. |
| 3 - Raciocínio automatizado | ( ) Permite usar as informações armazenadas com a finalidade de responder a perguntas e tirar novas conclusões. |
| 4 - Aprendizado de máquina | ( ) Permite perceber objetos. |
| 5 - Visão computacional | ( ) Permite que o computador se comunique com sucesso em uma linguagem de idioma. |
| 6 - Robótica | ( ) Permite armazenar o que sabe ou ouve. |

<details><summary>Resposta...</summary>
<p>A ordem correta é: $6, 4, 3, 5, 1, 2$</p>
</details>

## Questão 3

Sabendo que o aprendizado por retro-propagação de erro utiliza a derivada da função de ativação para calcular o valor da correção dos pesos, por que a função de ativação ReLU é mais eficiente no aprendizado, em diversas situações, do que a Sigmóide? Quando a ReLU apresenta o mesmo problema da Sigmóide, em relação ao aprendizado?

<details><summary>Resposta...</summary>
<p>Como a taxa de correção de erro de um peso em uma rede neural é, simplificadamente, a multiplicação da derivada da função de ativação pela "responsabilidade" do peso no erro, se a derivada da função de ativação tende a 0, o peso perde a capacidade de se adptar. Isso ocorre na função de ativação da sigmóide quando a soma ponderada tem valores absolutos muito grandes (em geral, maiores que 5). A isso damos o nome de **saturação do aprendizado**. A função ReLU, ao contrário da sigmóide, é uma função linear para valores positivos, logo, ela sempre tem uma derivada diferente de zero, e, para valores positivos, não sofre de saturação. A função _Leaky ReLU_, utiliza uma pequena inclinação linear nos valores negativos, permitindo que a saturação também não ocorra nesses casso (ao contrário da ReLU).</p>
</details>

## Questão 4

Por que é necessário um grande conjunto de dados para o treinamento de redes neurais artificiais?

<details><summary>Resposta...</summary>
<p>É necessário que os dados sejam representativos de todo o úniverso do domínio da aplicação, e para a maioria das aplicações, são necessários grandes volumes de dados para que seja possível cobir com exemplos todo esse universo.</p>
</details>

## Questão 5

Explique a técnica de validação cruzada aplicada ao treinamento de redes neurais artificiais.

<details><summary>Resposta...</summary>
<p>A técnica de validação cruzada consiste em separar um pedaço dos dados de treinamento e utilizá-los como dados de teste para o treinamento da rede. Ao aplicar técnicas relacionadas, como _k-fold_, onde o pedaço do conjunto de dados varia ao longo do treinamento, é possível treinar uma rede neural visando a generalização, mesmo utilizando todos os dados durante o treinamento. Em qualquer um desses casos, o erro da rede deve ser medido a partir do pedaço que serviu de base de teste.<p>
</details>

## Questão 6

Por que é importante utilizar uma base de teste separada da base de treinamento no treinamento de redes neurais artificiais?

<details><summary>Resposta...</summary>
<p>Quanto mais o treinamento progride, mais o erro da rede neural diminui, em relação a base de treinamento, assumindo que a configuração da rede tem capacidade de aprender toda a base de treinamento. O problema é que dado tempo de treinamento suficiente, a rede "decora" as respostas da base de treinamento, causando _overfitting_, e não conseguindo generalizar as respostas para o problema proposto.</p>
<p>O uso de uma base de treinamento, e a medida de erro da rede baseada nessa base de treinamento, permite parar o treinamento quando a capacidade de generalização da rede é maior, evitando o _overfitting_.</p>
</details>

<!--
## Questão 7

Dadas as afirmações abaixo, assinale com $V$ as afirmaçẽs verdadeiras, e com $F$ as afirmações falsas.

```
( ) Em uma rede neural artificial, o valor de entrada de cada neurônio é calculado pelo produto matemático das saídas dos neurônios da camada anterior.
```

Para cada afirmação falsa, escreva a versão corrigida da afirmação.
-->
