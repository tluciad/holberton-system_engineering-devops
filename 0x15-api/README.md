# 0x15. API

<div class="panel-body">
    <h2>Background Context</h2>

<p><a href="https://youtu.be/-2kyU6-j8ZQ" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220908%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220908T140549Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f80fb8a51aee08fd53e83ebde57c05bca67a1724b398c8dbddd8a70c1e2f5bf5" alt="" loading="lazy" style=""></a></p>

<p>Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.</p>

<p>One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.</p>

<p>This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/I-XLIq5AwH-j29xJtzr6bQ" title="What is an API" target="_blank">What is an API</a> </li>
<li><a href="/rltoken/I1nC8rhySGahG3gXYBfDPA" title="What is an API? In English, please" target="_blank">What is an API? In English, please</a></li>
<li><a href="/rltoken/6_OAlRYOGUuegPfyd4FUVg" title="What is a REST API" target="_blank">What is a REST API</a> </li>
<li><a href="/rltoken/lewYS0z2RuFuiIkIgaCHSA" title="What are microservices" target="_blank">What are microservices</a> </li>
<li><a href="/rltoken/C7zzmgcZJqUC50-pilPPzw" title="PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry" target="_blank">PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/shJvjhQJv488-f7SmzIYPw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is an API</li>
<li>What is a REST API</li>
<li>What are microservices</li>
<li>What is the CSV format</li>
<li>What is the JSON format</li>
<li>Pythonic Package and module name style</li>
<li>Pythonic Class name style</li>
<li>Pythonic Variable name style</li>
<li>Pythonic Function name style</li>
<li>Pythonic Constant name style</li>
<li>Significance of CapWords or CamelCase in Python</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 14.04 LTS using <code>python3</code> (version 3.4.3)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/python3</code></li>
<li><strong>Libraries imported in your Python files must be organized in alphabetical order</strong></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the <code>PEP 8</code> style</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using <code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>You must use <a href="/rltoken/nVy7hbvKVJkhr5LIHIsHSg" title="get" target="_blank">get</a> to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)</li>
<li>Your code should not be executed when imported (by using <code>if __name__ == "__main__":</code>)</li>
</ul>

  </div>