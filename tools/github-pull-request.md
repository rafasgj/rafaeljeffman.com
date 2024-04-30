---
title: Criando um Pull Request no Github
subtitle: Uma introdução ao Git e seu uso em projetos open source.
layout: main
section: Desenvolvimento de Software
sections:
tags:
  - git
  - github
lang: pt
copy: 2024
date: 2024-04-21
extra_styles:
  - lecture
abstract: |
    A colaboração em projetos utilizando [Git](https://git-scm.org) e
    [Github](https://github.com) tem sido cada vez mais comum em empresas de
    tecnologia, uma vez que a depêndencia dos projetos em outros projetos
    _open source_ é cada vez maior. Nesse tutorial são mostrados os passos
    introdutóriou ao uso do Git em conjunto com o Github para auxiliar
    desevolvedores que estão iniciando a carreira a entenderem o processo e
    ter a oportunidade de contribuir e divulgar o seu trabalho. Para realizar
    o tutorial será necessário [criar uma conta no Github](https://github.com/signup).
---

Quando desenvolvemos um projeto de longo prazo, é importante acompanhar o histórico do desenvolvimento e entender porque algumas alterações e decisões foram tomadas ao longo do tempo. Uma forma de obter essas informações é a partir do histórico de modificações do código fonte. Sistemas de controle de versão permitem estudar o histórico de desenvolvimento, _voltar no tempo_ e ver o código como estava em um ponto específico ou criar alterações e provas de conceito que não impactam o fluxo padrão de desenvolvimento do projeto.

O [Git](https://git-scm.org) é um sistema de controle de versão distribuído e é, hoje em dia, um dos mais utilizados no mundo. Diversas empresas utilizam o Git como sistema de controle de versão para seus projetos, e ele é muito utilizado em projetos _open source_, que tem, naturalmente, uma característica de desenvolvimento distribuída.

Este documento apresenta uma introdução ao Git, utilizando uma abordagem prática semelhante ao processo de colaboração em projetos _open source_. Está fora do escopo discutir como participar desse tipo de projeto, no entanto, as ideias e práticas básicas estarão presentes e serão aplicáveis para esses casos. Para realizar o tutorial será necessário [criar uma conta no Github](https://github.com/signup).

## Obtendo uma cópia do projeto

Para experimentar com o uso do Git e Github, utilizaremos um projeto criado para esse propósito. O projeto é o [github-pr-tutorial](https://github.com/exercicios-programacao/github-pr-tutorial). O primeiro passo é criar um _fork_ do projeto.

O _git_ é um sistema de controle de versão distribuído, onde cada participante do projeto possui a sua cópia do repositório contendo "todo" o histórico do projeto (é possível trabalhar apenas com parte do histórico, por exemplo, em projetos grandes e longevos). Por esse motivo é necessário que, ao iniciar o trabalho em um novo projeto, seja necessário obter, para si, uma cópia do projeto original.

Para obter uma cópia do projeto, assumindo que este está hospedado no Github, criamos um _fork_ do projeto para a conta pessoal. Basta clicar no botão ![fork](/images/fork-btn.png){:class="inline"}, que fica na barra de botões existente no projeto:

![fork location](/images/fork-bar.png)

Após clicar no botão aparecerão as informação para criar o _fork_, e, em geral, não é necessário alterar nenhuma informação, mas revise e o usuário para o qual o projeto será copiado é o correto:

![fork data](/images/fork-data.png)

Ao clicar em `Create Fork` o repositório será copiado para o usuário selecionado. Esta operação pode demorar alguns minutos.

Com uma cópia do repositório disponível no seu usuário, que chamaremos `USER` a partir de agora, podemos começar a trabalhar na alteração do projeto. Para isso, será necessário obter uma cópia local do repositório.

O comando `git clone` deve ser utilizado para copiar um repositório remoto para a máquina local. Basta utilizar a URL do repositório, que no caso do github é a mesma URL utilizada no navegador. Em um terminal, digite o comando (não esqueça de substituir `USER` pelo seu usuário do Github):

```
git clone https://github.com/USER/github-pr-tutorial
```

O comando irá criar um diretório `github-pr-tutorial` e copiar os arquivos remotos para dentro desse diretório, mantendo a estrutura original.

Precisamos agora trocar de diretório para o diretório do projeto com o comando `cd github-pr-tutorial`, e, se necessário, configurar o repositório Git com os dados do desenvolvedor. No entanto, é recomendado que a configuração seja global, como no exemplo:

```
git config --global user.name "Nome Completo"
git config --global user.email "username@seu-email.com"
``` 

Com o repositório disponível localmente e devidademente configurado, podemos alterar o projeto, mas, antes, precisamos criar um _branch_ no repositório.


## Realizando alterações no projeto

_Branches_ permitem que novas _features_ ou correções de _bugs_ sejam feitos de forma isolada do desenvolvimento contínuo do projeto. Como o projeto é distribuído e outras pessoas continuam contribuindo alterações, criar um isolamento do estado do projeto para realizar alterações facilita o trabalho.

O comando `git branch` é utilizado para gerenciar _branches_. Para listar todos os branches utilize o comando:

```
git branch --all
```

O _branch_ marcado com `*`(asterisco) é o _branch_ atualmente em uso, alguns _branches_ podem ser remotos, e trabalharemos com eles mais tarde.

Para trocar de _branch_, utilizamos o comando `git switch`, e podemos criar um novo _branch_ utilizando:

```
git switch -c "procura-menor"
```

Após o comando, o _branch_ `procura-menor` será criado e estará ativo. Confirme isso com o comando `git branch` (que mostra apenas os repositórios locais).

Uma vez que o _branch_ de trabalho foi criado, vamos alterar o código para inserir uma nova _feature_ no projeto.

1. Inicialize um ambiente virtual do Pyhon:
    : `python -m venv .venv`
    * No Linux ou macOS, execute o comando (`source`):
        : `. .venv/bin/activate`
    * No Windows, execute:
        : `.venv/bin/activate.bat`
2. Instale a ferramenta `behave`:
    : `pip install behave`
3. Execute o `behave` para garantir que tudo está funcionando:
    : `behave`
4. Altere o arquivo `src/zero.py`, adicionando ao final do arquivo:
    ```python
    def procura_menor(lista):
        """Procura o menor elemento em uma lista."""
        return min(lista)
```
5. Execute o `behave` para testar apenas o teste que foi corrigido:
    : `behave -q -n "Procura o menor elemento em uma lista"`
        ```nohl
        Funcionalidade: Realiza operações sobre listas

        Cenário: Procura o menor elemento em uma lista
            Dada uma lista arbitrária                     # 0.000s
            Quando procuro o menor elemento na lista      # 0.000s
            Então o resultado é o menor elemento da lista # 0.000s

        1 feature passed, 0 failed, 0 skipped
        1 scenario passed, 0 failed, 3 skipped
        3 steps passed, 0 failed, 9 skipped, 0 undefined
        Took 0m0.000s
```

Neste ponto, temos um repositório local, com alterações. Podemos utilizar o comando `git diff` para revisar as alterações:

```
git diff
```

A saída do comando `git diff` mostra os arquivos e linhas que foram alteradas

```diff
diff --git a/src/zero.py b/src/zero.py
index 9bc9d59..55a15e6 100644
--- a/src/zero.py
+++ b/src/zero.py
@@ -14,3 +14,6 @@ def procura_maior(lista):
         if item > maior:
             maior = item
     return maior
+
+def procura_menor(lista):
+    return min(lista)
```

Note que, nesse ponto, as alterações locais ainda não estão gravadas no repositório. Podemos verificar isso com o comando `git status`, cuja saída será semelhante a:

```nohl
On branch procura-menor
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   src/zero.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Note que o `git status` nos mostra o _branch_ que estamos trabalhando e mostra quais os arquivos foram alterados, e nos avisa que essas alterações não estão adicionadas ao repositório.

Para gravar as alterações no repositóiro, precisamos, primeiro, adicionar as alterações realizadas:

```
git add src/zero.py
```

Após a adição, o comando `git status` nos mostra que temos alterações prontas para serem gravadas no repositório:

```nohl
On branch procura-menor
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   src/zero.py
```

Finalmente, vamos gravar as alterações com o comando `git commit`, porém devemos lembrar de adicionar um comentário sobre a alteração realizada, passando uma mensagem para o `commit`:

```
git commit -m "Adicionada função que procura o menor elemento na lista."
```

A mensagem utilizada é importante para estudar o histórico de alterações do projeto, por isso, é importante que ela seja clara e completa. Na maioria dos casos, utilizar apenas uma linha para descrever a alteração realizada não é viável, e utilizamos o comando `git commit` sem a opção `-m`, que adiciona a mensagem, e deixamos que o `git` abra um editor de textos para que possamos editar uma mensagem mais completa.

Para definir o editor de textos que o `git` irá utilizar para editar essa mensagem podemos modificar a sua configuração global com o caminho completo para o executável do editor, como, por exemplo:

```
git config --global core.editor /usr/bin/micro
```

Uma vez que realizamos o `commit` (gravação) das alterações no repositório, o resultado do `git status` nos mostra que não temos nenhuma alteração **local** pendente:

```nohl
On branch procura-menor
nothing to commit, working tree clean
```

Podemos utilizar o comando `git log` para ter uma visão do histórico das alterações do repositório:

```nohl
commit a5969b5f9127c49e8a9581b9bc0dc3bfa5ae6077 (HEAD -> procura-menor)
Author: Rafael Guterres Jeffman <rafasgj@gmail.com>
Date:   Sun Apr 21 11:54:16 2024 -0300

    Adicionada função que procura o menor elemento na lista.

commit 665470276c590ff026db5496650d6c4ce12606d2 (origin/main, origin/HEAD, main)
Author: Rafael Guterres Jeffman <rafasgj@gmail.com>
Date:   Sun Apr 21 09:30:59 2024 -0300

    Configuração do exercício.

commit 2f4ad098c77aeaec0b13d855640f1a0bff8147aa
Author: Rafael Jeffman <rafasgj@gmail.com>
Date:   Sun Apr 21 09:00:11 2024 -0300

    Initial commit
```

Para ver detalhes da nossa última alteração podemos executar o comando `git log -1 -p`:
```
commit a5969b5f9127c49e8a9581b9bc0dc3bfa5ae6077 (HEAD -> procura-menor)
Author: Rafael Guterres Jeffman <rafasgj@gmail.com>
Date:   Sun Apr 21 11:54:16 2024 -0300

    Adicionada função que procura o menor elemento na lista.

diff --git a/src/zero.py b/src/zero.py
index 9bc9d59..55a15e6 100644
--- a/src/zero.py
+++ b/src/zero.py
@@ -14,3 +14,6 @@ def procura_maior(lista):
         if item > maior:
             maior = item
     return maior
+
+def procura_menor(lista):
+    return min(lista)
```

Agora, para que seja finalmente possível criar um _pull request_, precisamos enviar nossas alterações de volta para o Github.

## Atualizando um repositório remoto

Para que as alterações locais sejam gravadas na cópia do repositório no Github é necessário que elas sejam envidas para lá de forma que a mesma contfiguração existente localmente possa ser replicada remotamente.

### Criando uma chave de acesso no Github

Você lembra que todo desenvolvedor do projeto tem uma cópia do repositório? Nesse aspecto, o Github funciona como mais um desenvolvedor do projeto, então é necessário "escrever" no repositório remoto, e como isso traz problemas como segurança dos dados, é necessário que alguns processos para autenticar as alterações sejam realizados.

O Github, já há alguns anos, não aceita o envio de alterações utilizando senhas simples, recorrendo ao uso de _tokens_ para autenticação, portanto, você deverá criar um _token de autenticação_ no site do Github.

Para acessar o formulário de criaçã de _tokens_ de acesso, utilize o item ![Developer Settings](/images/github-developer-settings.png){:class="inline"} na página de `Settings`, acessível pelo menu do perfil do usuário.

Ao acessar o _Developer Settings_, escolha a aba _Tokens (classic)_, e acesse a opção _Generate New Token (classic)_ do menu _Generate New Token_:

![Tokens Classic](/images/github-token-menu.png)

No formulário que é disponibilizado, selecione, pelo menos, a opção `repo` (e todos os itens desta opção), insira uma _nota_ para descrever para qual fim o _token_ será utilizado, e defina o período de validade (embora nunca exprirar seja bastante prático, o uso dessa opção aumenta o risco de comprometimento do _token_):

![Tokens Classic](/images/github-token-minimal-config.png)

Após configurar as opções, clique em _Generate Token_, o token será gerado.

Uma vez gerado o token, ele é exibido uma única vez, e você deve copiá-lo. Caso não o faça, deverá repetir o processo. O _token_ é uma string codificada com um bom número de bits para mantê-la segura, como pode ser visto na imagem abaixo:

![Tokens Classic](/images/github-token-generated.png)

Este token será utilizado para o _login_ com o `git`, para fazer o upload dos dados.

### Gravando os dados no repositório remoto

Agora podemos, finalmente, enviar o código alterado para o github com o comando:

```
git push origin procura-menor
```

Ao invocar o comando, dependendo da configuração do repositório, as credenciais de acesso serão pedidas:

```nohl
username: USERNAME
password: <token de acesso>
```

Dependendo da configuração do repositório, será necessário configurar o _token_ na URL de acesso ao repositório.

### Configurando o repositório para não pedir senha

A necessidade de lembrar um código como o _token_ de accesso é uma grande dificuldade, devido ao tamanho da chave utilizada. Uma alternativa é configurar o repositório local de forma que não seja mais necessário o uso das credenciais para alterar o repositório remoto.

Para isso, precisamos alterar a URL que o Git utiliza para acessar o repositório no Github, e utilizaremos a chave de acesso gerada anteriormente, e definir a configuração do repositório remoto na nossa cópia local com o comando `git remote':

> `git remote set-url origin https://USERNAME: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@github.com/exercicio-programacao/github-pr-tutorial   `

Lembre-se de, no comando anterior, utilizar o seu nome de usuário do Github no lugar de `USERNAME` e o código gerado para a sua _token_ de acesso.

Dessa forma, o Git irá utilizar, sempre, a chave de acesso definida nessa configuração (que será válida enquanto a chave de acesso for válida).

### Fazendo _upload_ dos dados

De posse do _token_ ou com a URL configurada, é finalmente possível enviar os dados para o Github, com o commando `git push origin procura-menor`. O resultado do comando é algo parecido com:

```nohl
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (4/4), 422 bytes | 422.00 KiB/s, done.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'procura-menor' on GitHub by visiting:
remote:      https://github.com/USERNAME/github-pr-tutorial/pull/new/procura-menor
remote: 
To https://github.com/USERNAME/github-pr-tutorial
 * [new branch]      procura-menor -> procura-menor
```

O comando irá fazer _upload_ dos arquivos e criar, no repositório remoto, um _branch_ com o mesmo nome do branch que criamos localmente. Como parte do resultado do comando, o Git nos mostra uma URL que utilizaremos posteriormente para criar o _pull request_.

## Criando o _Pull Request_

Para criar o _pull request_, o ideal é utilizar o _link_ fornecido pelo Github como resultado do `git push`. Esse link irá abrir o formulário para criar o _pull request_.

![Github pull request](/images/github-pull-request.png)

Agora basta preencher as informações relativas a alteração proposta ao projeto e clicar no botão `Create Pull Request`.

## Testes automatizados

Em diversos projetos, ao criar um _pull request_ uma série de testes automatizados será executada, e o resumo pode ser visto na própria página do _pull request_:

![Github Checks](/images/github-checks.png)

Para ver os detalhes de um teste, por exemplo, porque ele falhou, basta clicar no _link Details_, associado ao teste que você deseja ver o resultado, para poder analisar o resultado final.

![Github check details](/images/github-check-details.png)

## Atualizando o repositório local

Para o desenvolvimento de projetos colaborativos, ainda temos mais um comando a ser estudado, pois ele permite que os dados do repositório local sejam atualizados caso o repositório original seja modificado.

Para atualizar o repositório local, o primeiro passo é atualizar o repositório do seu usuário no Github, clicando no botão ![Github Sync Fork](/images/github-sync-fork.png){:class="inline"}

Após atualizar o repositório remoto, basta atualizar o repositório local com o comando:

```
git pull --rebase
```

Para que o comando funcione, você não pode ter operações pendentes (que podem ser salvas com `git stash` e recuperadas depois com `git stash pop`), e não podem haver duas modificações diferentes no mesmo ponto do arquivo.

Quando ocorrerem modificações diferentes no mesmo ponto do arquivo, o Git comunicará a existência de um conflito, e você deve resolver o conflito antes de continuar o processo com o comando `git rebase --continue`. Para cancelar um `git pull --rebase` em andamento, você pode utilizar `git rebase --abort`.

## Onde obter mais informações

Os comandos do Git, me geral, são bem "silenciosos", ou seja, produzem pouca saída. Quando eles produzem alguma saída, o resultado deveria ser analisado com atenção, pois são erros ou avisos importantes.

Cada comando do Git tem uma opção `--help` que mostra uma página de auxílio com todas as opções disponíveis e exemplos, ajudando muito na compreensão do comando.

O livro [Pro Git](https://git-scm.com/book) está disponível gratuitamente para leitura _online_. Caso você prefira, também está disponível [como livro físico](https://www.amazon.com/Pro-Git-Scott-Chacon/dp/1484200772).

A utilização do Git é muito importante no desenvolvimento de projetos de software, atualmente, e muitas outras ferramentas de armazenamento de repositório remotos oferecem características semelhantes ao Github (por exemplo, o [GitLab](https://gitlab.com)).

Conhecer bem as ferramentas de desenvolvimento irá auxiliar nas tarefas do dia-a-dia, reduzindo o tempo gasto com estas ferramentas.

## Referências

* [Pro Git](https://git-scm.com/book)
* [Github CLI Token](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
