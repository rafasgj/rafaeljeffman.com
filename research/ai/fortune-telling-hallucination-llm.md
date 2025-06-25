---
title: Fortune telling, Hallucination and LLMs
subtitle: Experimenting with LLM models and ways to customize them.
layout: main
section: Artificial Intelligence
sections:
  - Artificial Intelligence
tags:
  - artificial intelligence
  - LLM
  - MCP
  - RAG
  - ramalama
lang: en
copy: 2025
date: 2025-06-25
abstract:
---

One known issue of large language models (LLM) is known as _hallucination_,
when it gives an answer that is wrong. This is caused by a feature of many
machine learning algorithms that it gives an answer based on the training
data, even if the input parameters describe a new pattern, never known by
the model.

The goal of this exeperiment is to evaluate how LLM models respond to queries
it might not have seen during training, and how can the answer be improved
with the use of _retrieval-augmented generation_(RAG) and the model context
protocol (MCP).

The query used for testing is a single question:

> How can I deploy [FreeIPA](https://freeipa.org) using
  [ansible-freeipa](https://github.com/freeipa/ansible-freeipa)?

There will be no further interaction with the prompt.

Since it is not expected that `ansible-freeipa` documentation was used to
train the models, it is expected that the model will give a wrong answer,
that is, it will hallucinate. It is also expected that by providing specific
data on the matter will improve its answer.

## Ramalama

[Ramalama](https://ramalama.ai) simplifies running AI models locally, through
the use of containers. It brings the same language from the container world to
deploying AI models. It also detects hardware capabilities, making it easier
to setup an efficient environment for inference use.

After [installing Ramalama], you run you model in a similar fashion as using
containers:

```nohl
$ ramalama run granite3.3
```

If not avaiable locally, a container image and/or and the model will be pulled
from the repository (like [quay.io](https://quay.io) and [Ollama](https://ollama.com/library)), and a chatbot prompt will be started, so you can query the model.

You can also run the model to be served as a REST API with:

```
$ ramalama server deepseek-r1:7b
```

Use `ramalama list` to see the locally available models.


## Running the raw models

The models used in this experiment are
[DeepSeek R1](https://ollama.com/library/deepseek-r1)
and [Granite 3.3](https://ollama.com/library/granite3.3).

By today's standards, both models are considered "small". Granite, for
example is called a Small Language Model (SLM). The precise definition of
SLM or LLM is not important for this experiment, and the sizes of the models
tested will be similar, and as the idea is to force the model to provide
provide incorrect to partially correct answers and improve it later using
other techniques, using a smaller model was a conscious decision.

### Granite 3.3

The Granite model used has 8 Billion parameters, and its context size is
128K. It took 1:40 minutes to
[give an answer to the query](/files/research/ai/granite-raw.md)). The
answer looks like a step-by-step procedure, which makes sense due to the
nature of the question.

The answer start somewhat well, if small errors, as it try to _guess_ what
it doesn't know by throwing some keywords in the context (like calling
ansible-freeipa a _role_, when it is a collection). But right in the first
example, it contradicts itself, as it says "I assume you have a working
Ansible environment with the required dependencies", but in the first command
it asks to install Ansible: `sudo apt install ansible git`

It goes on with a standard Ansible process that has nothing to do with
ansible-freeipa, and when it should mention it, it invent something that
does not seem to come from ansible-freeipa, but from the FreeIPA documentation.

One nice touch on the given answer is a link to the ansible-freeipa GitHub
repository.

A second run of the same query, in a new environment, with te same model,
gives a completely different answer, including the approach to install
Ansible, and looks like a "fortune teller": it gives a generic answer
on running Ansible playbooks or managing packages and services.

On this run, the definition of FreeIPA s very nice ("an open-source
identity, authentication, and authorization solution"), but it simply invented
a link to the ansible-freeipa documentation that does not exist, while it
listed the correct link to clone the repository (which is the official
URL for the ansible-freeipa documentation).

### DeepSeek R1

The model used for testing DeepSeek R1 was the one with 7 Billion parameters
and context size of 128K tokens. This model has less parameters than the
Granite model due to issue on running the 8 Billion parameters model.

Using the raw DeeSeek R1 model took `2:10` minutes to
[give an answer](/files/research/ai/deepseek-raw.md). As with the Granite
model, it provided a step-by-step procedure, but in this case it was
completelly bogus from the start.

Installation of ansible-freeipa included a command that would never work. It
changed the name of FreeIPA. It "created" an inexistent software `Ansible Broadword`.

If you take a deep breath and read through it uncarefully, you realize that
the text is somewhat well written, but it looks like "fortune telling". It
simply adds some generic output based on managing services and Ansible.

When running the same question against the model, it starts with a similar answer
as on the first round, but soon it changes into creating an invalid Ansible
playbook and non-existing FreeIPA configuration.

> **Note**: A single run was done with the 14 billion parameters model, and,
although Ansible instructions were slightly more precise, the overall result
was not different that the output of the 7 Billion parameters model.

### Evaluation of the raw models

As expected the _hallucination_ effect is present, and very severe. This is
mostly due to the inability of the system, when using the raw models, to say
"I don't know". It is also clear that the generated text tries to pick some
keywords and make a reasonable text around it.

In general, LLMs are pattern matching systems that maps an input to an output,
and there's some randomness in the input. As the machine learning system is
trained to "write text", this is what it does, it writes text, and it does it
well. But it is also a fact that it is writing text about something it doesn't
know, or, at least, doesn't know well.

To improve the answers we could retrain the model with the desired data, but
it is time consuming and costly. The alternative is to use techniques to
provide the wanted knowledge to the system.

## Retrieval-augmented Generation (RAG)

Retrieval-augmented generation (RAG) is a technique that allows new information
to be used by pre-trained language models. It is expected that the model does not
answer a query if it is not part of this new information. The new information
provided to the model is based on a vector database that is
constructed from a set of documents that are organized in a vector database,
and is used along with the user query, augmenting it, so that the generated
output incorporates the given data. It is expected that a model will not respond
to user queries that do not refer to the specified set of documenst.

With Ramalama, you create an OCI image to contain the processed rag data:

```nohl
$ ramalama rag FILES/DIRECTORIES IMAGE_NAME
```

After creating the image you pass the parameter `--rag IMAGE_NAME` to the `run`
command when running the model prompt.

One advantage of using Ramalama for creating the RAG image is that is supports
AsciiDoc and Markdown as document formats, so the data used will be ansible-freeipa's
main README file and the `ipaserver` role README file will be used. Both files with
be stored in a directory `knowledge`.

```nohl
$ ramalama rag ./knowledge ansible_freeipa_rag
```

It took around 5 minutes to create the image with the vector database, what is
not even comparable to retraining the whole model.

As we are creating an OCI image, you can see it with:

```nohl
$ podman image list -f reference=ansible_freeipa_rag
```

With the image created, we can test the models:

```nohl
ramalama run --rag localhost/ansible_freeipa_rag MODEL
```

### Granite with RAG

First test after adding RAG data is to ask somethnig that is not on the
augmented knowledge, like "How to achieve a speed greater than the speed of light?",
to what Ramalama using Granite answered in a very good way. So the expectation
that it would only answer things that is present within the augmented data is not
true.

When we try with something that it should not know ("What is [ipalab-config](https://github.com/rjeffman/ipalab-config)?"), it correctly answers that the term does not appear in the provided docuementation, or in any common context related to IPA or Ansible.

Back to the original query ("How can I deploy FreeIPA using ansible-freeipa?"),
it took 45 seconds to start to provide an answer, but failed to finish the text.

Until if started to write garabage (infitinet punctuation characters) it provided similar responses as without the RAG for installing Ansible (not really correct), but this time, the inventory and playbook files it tried to create were clearly based on the ansible-freeipa documentation.

Hallucination was not better, in any way.

For example:

> **Install ansible-freeipa collection:**
>
>   Install the ansible-freeipa collection using the Ansible Galaxy CLI:
>
>   ```bash
>   ansible-galaxy collection install freeipa.freeipa
>   ```

The collection `freeipa.freeipa` does not exist.

As mentioned before, the example playbook does contain some ansible-freeipa
parameters, but was simply cut before it was ready:

> **Create your playbook:**
>
>    Create an Ansible playbook, e.g., `install_freeipa.yml`, to configure and deploy FreeIPA:
>
>    ```yaml
>    ---
>    - name: FreeIPA deployment
>      hosts: ipaservers
>      become: true
>      vars:
>        ipaserver_realm: EXAMPLE.COM
>        ipaserver_domain: example.com
>        ipaserver_setup_adtrust: yes
>        ipaserver_install_packages: yes
>        ipaserver_setup_dns: yes
>        ipaserver_setup_kra: yes
>        ipaserver_setup_ca: yes
>        ipaserver_dirsrv_config_file: /etc/dirsrv/slapd-EXAMPLE-COM.conf
>        ipaserver_pki_config_override: /etc/pki/ipapki.conf
>        ipaserver_dirsrv_cert_files: /etc/pki/tls/certs/server-cert.pem
>        ipaserver_http_cert_files: /etc/pki/tls/certs/server-cert.pem
>        ipaserver_pkinit_cert_files: /etc/pki/tls/certs/server-cert.pem
>        ipaser_copy_ssh_table
>      ansible
>   ```

This might be due to the context size, even if the ansible-freeipa README data is
not very large.

### DeepSeek R1 with RAG

For the "speed of light" question, DeepSeek R1 gave a similar answer than Granite.
Although, it still tends to be a lot verbose on its answers.

On the "What is ipalab-config?" question, DeepSeek R1 provided an answer that has
nothing to do with the project, or FreeIPA:

```
**ipalab-config** is an Ansible module within the
FreeIPA plugin suite designed to manage the
configuration of a FreeIPA server. It sets up
various parameters essential for user authentication
using One-Time Passwords (OTP).
```

It made a mix of concepts like:

```
5. **DNS Settings**: Configuration of DNS records to
ensure correct DNS lookups and routing of usernames
to service accounts.
```

For the target question on using ansible-freeipa, the model simply throws text
that makes no sense, with invalid YAML files, playboks that look like Python code,
some `openssl` commands that has nothing to do with the task.

It clearly picked up some keywords and try to add text around it, and failed
(more on why it failed in the conclusion).

## Working out the prompt

The query choosen for this experiment was thought on a way that it would
force the models to hallucinate. It was designed without keywords from the
IPA or ansible-freeipa domain, giving the models a harder time to produce
a correct output.

When using words that are from the specific domain, the results are much
better.

In the case of ansible-freeipa, it is usually said that the playbook will
"ensure ipaserver is present" and not to "deploy an IPA server". If the
query is "How to ensure an ipaserver is present?"

The output using Granite 3.3 and RAG becomes:

> To ensure an IPA server is present, you can use the `ipaserver` role with the `state: present` option in your Ansible playbook. Here's an example:
>
> ```yaml
> - name: Playbook to configure IPA servers
>   hosts: ipaserver
>   become: true
>   vars_files:
>   - playbook_sensitive_data.yml
>
>   roles:
>   - role: ipaserver
>     state: present
> ```
>
> Replace `playbook_sensitive_data.yml` with the path to your Ansible Vault file if you are using one for storing sensitive data like passwords.
>
> This playbook will ensure that the `ipaserver` is present on the specified hosts. If the server is not present, it will be installed; if it is present, no action will be taken.
>
> Make sure to include the necessary modules and variables in your role and inventory files to properly configure and manage the IPA servers.

This output clearly comes from the augmented data, and altough it is not complete (it would be nice that an example inventory file was provided), it is correct, but still somewhat generic.

## Conclusions and Future Work

I started working with AI back in the end of the 20th century, and have always
been somewhat annoyed about its black box nature. I wanted to understand what
the models have learned, I wanted to be able to understand its reasoning
and why it answer the way it did.

This experiment is a way a to reconnect to what I did back then, and start
working with natural language models. It is a way to start to find the limits
on the tools, and how to improve the tool or circumvent the issues. And as
can be seen, for generative language models, there are several obstacles to overcome.

It should be clear, for anyone using AI or with a background on it, that
the input data is very important. And here I call it "input data" as all
data consumed by the model is important, the training data, the data used
to customize the model, the data used in the query prompt. All this data
must be representative of the problem to be solved.

Data used to customize the model should be fairly complete, and available in
a way that allow some flexibility on the queries, without loosing track of
the problem domain. Prompt queries must consider the problem domain, but, sometimes,
users are new to the domain, and the answers provided should give guidance.

Another way that the model can be extended is by implementing
[Model Context Protocol](https://modelcontextprotocol.io) servers, enabling other tools to provide data for the
languagem model, for example, by running command against these tools and use
the command output as context for the answer.

When choosing a model to be used, there are two parameters that are very
important, the model size (usually in "billions of parameters", around 8B
for this experiment) and the context window size (128K for this experiemnt).
Both parameters are related to the model "memory". The model parameter size is,
somewhat, related to the long term memory of the model, allowing to recover
data it was trained with. The context window size is the short term memory, and
is related to how much the model "remembers" of the user query and its generated
output. When the context window is too small, it is easier for the model to
hallucinate and diverge from the original query.

A problem on using larger models and larger context windows comes in the
hardware requirements for runing the model, even if it is for inference only.
This experiment was executed on an Intel i7 11-th gen 3GHz CPU, with 32Gb of
memory and with no GPU support for running the model. This does impose severe
limitations on the models that can be used and on the response time.

There are still a lot of open questions, and this should be the first experiment,
on what is expected to be a long series, exploring tools for AI
applications, trying to understand its flaws and limits, so we can design
the tools around these issues and improve user experience.

## References

1. [Ramalama](https://github.com/containers/ramalama)
2. [Ollama Library](https://ollama.com/library)
3. [Simplify AI data integration with RamaLama and RAG](https://developers.redhat.com/articles/2025/04/03/simplify-ai-data-integration-ramalama-and-rag#putting_the_rag_served_model_into_production)
4. [Model Context Protocol](https://modelcontextprotocol.io)
