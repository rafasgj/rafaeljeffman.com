---
title: Procura em _Strings_
section: Complexidade de Algoritmos e Análise de Desempenho
layout: lecture
last_occurrence: 2023-10-16
copy: 2023
institution:
  name: Universidade LaSalle Canoas
  link: /teaching/lasalle/2023/analise-algoritmos
  link: /teaching/lasalle/2023/analise-algoritmos
---

## O problema e as aplicações

* Sejam duas sequências $S$ (_string_ ou _haystack_) e $w$ (_pattern_ ou _needle_), formadas por caracteres do alfabeto $\Sigma$ de tamanho $k = \|\Sigma\|$, com comprimentos $n = \|S\|$ e $m = \|w\|$, respectivamente, tal que $n \le m$, então o conjunto de resposta $R = \{i_0, i_1, \dots, i_k\}$ contém toda posição $i_k$ em $S$ onde é encontrada uma instância de $w$.
* Aplicações
    * Recuperação de documentos
        * Texto
        * Áudio
        * Imagens
    * DNA _matching_

## Busca Ingênua

* Não tem fase de pré-processamento.
* Complexidade de tempo para busca: $\Theta(mn)$
* Complexidade de espaço: $O(1)$
* Algoritmo

        def match(S, w):
            result = []
            for i in 1..len(S):
                for j in 1..len(w):
                    if S[i + j - 1] != w[j]:
                        break
                else:
                    result.append(i)
            return result


## Algoritmo Knuth-Morris-Pratt (KMP)

* Realiza comparações da esquerda para a direita.
* Complexidade de tempo para pré-processamento: $O(m)$
* Complexidade de tempo para busca: $O(n)$
* Complexidade de espaço: $O(m)$
* Algoritmo

        def pre_KMP(w):
            kmp_next = [-1] * len(w)
            i = 0
            j = kmp_next[0]
            while i < len(w):
                while j > -1 and w[i] != w[j]:
                    j = kmp_next[j]
                i += 1
                j += 1
                if w[i] == w[j]:
                    kmp_next[i] = kmp_next[j]
                else:
                    kmp_next[i] = j
            return kmp_next

        def match(S, w):
            result = []
            kmp_next = pre_KMP(w)
            i = j = 0
            while j < len(S):
                while i > -1 and w[i] != S[j]:
                    i = kmp_next[i]
                i += 1
                j += 1
                if i >= len(w):
                    result.append(j - i)
                    i = kmp_next[i]
            return result


## Algoritmo _Two way_

* Requer um alfabeto ordenado._
* Calcula $w_\ell$ e $w_r$ tal que $w = w_{\ell}w_r$
* Compara os caracteres a partir de $x_r$ da esquerda para direita, se coincidire, compara os caracteres até $x_{\ell}$ da direita para a esquerda.
* Complexidade de tempo para pré-processamento: $O(m)$
* Complexidade de tempo para busca: $O(n)$
* Complexidade de espaço (bits): $O(\lceil\log_{\varphi}{m}\rceil) \sim O(1)$
* Originalmente algoritmo _Two Way_ faz, no máximo $2n - m$ comparações de caracteres, no pior caso.
* Uma variante (1996), que armazena $O(\lceil\log_{\varphi}{m}\rceil)$ _offsets_, executa, no máximo $n + \lfloor\(n - m\) / 2\rfloor$ comparações de caracteres.


## Recursos para essa aula

* [Algoritmo KMP](http://www-igm.univ-mlv.fr/~lecroq/string/node8.html#SECTION0080)
* [Algoritmo Two Way](http://www-igm.univ-mlv.fr/~lecroq/string/node26.html#SECTION00260)
* [Exemplo do algoritmo KMP](https://www.cs.utexas.edu/users/moore/best-ideas/string-searching/kpm-example.html)
* [Exemplo do algoritmo Boyer-Moore](https://www.cs.utexas.edu/users/moore/best-ideas/string-searching/fstrpos-example.html)

