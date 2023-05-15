<h1 align="center"> Draw-Project </h1>

<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

<h2> Descrição </h2>

<p>
Site feito para uma empresa de engenharia voltada para instalações elétricas e hidráulicas.
O site foi feito utilizando Python e Django, e tem como objetivo ser um portfólio de projetos e uma página para contato entre clientes e empresa. O adminastrador do site pode publicar/editar/deletar seus projetos que estejam concluidos ou em andamento, receber notificações de novas mensagens de contato e adicionar novos funcionários para administrar o site.
</p>

![jpc home](https://github.com/mga98/jpc-engenharia/assets/95861523/1bc6f31e-050e-4d15-9b14-e62c38f5fb31)

<h2> Features </h2>

<ul>
<li>Exibição de portfólio</li>
<li>Contato direto com a empresa</li>
<li>CRUD de projetos</li>
<li>Notificação de mensagens</li>
<li>Cadastro e autenticação de funcionários</li>
</ul>

<h2> Tecnologias utilizadas </h2>

<ul>
<li>Python</li>
<li>Django</li>
<li>Bootstrap 5</li>
<li>HTML</li>
<li>CSS</li>
<li>Javascript</li>
</ul>

<h2> Rodando o projeto </h2>
<h4> Dependências </h4>
<ul>
<li>Python 3.0 ou +</li>
</ul>
<h4> Clonando o projeto </h4>

```
git clone git@github.com:mga98/jpc-engenharia.git
```

<h4> Configurando o projeto </h4>
<p> Crie um arquivo .env na raiz do projeto com as mesmas constantes indicadas no arquivo
.env-example e crie uma constante DEBUG = 1 dentro dele (como mostrado no arquivo .env-example).</p>
<p> Abra o terminal com o ambiente virtual ativo e execute os seguintes comandos: </p>

```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser # Cria um super usuário
pytest ou python manage.py test # Para executar os testes da aplicação
python manage.py runserver # Inicializa o servidor na porta localhost/8000
No navegador digite localhost:8000 para abrir a página
```
