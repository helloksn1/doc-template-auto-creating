audodoc文件夹
这个django项目的配置文件集合，是自动创建的.

main文件夹
所有逻辑都现在这里
	migrations文件夹：数据库migration相关的内容自动创建的
	static：js,css等文件集合
	templates：html模板文件夹
	admin.py, apps.py, tests.py 暂时不用管
	urls.py：url对应关系
	views.py：具体逻辑都在这里
	models.py：数据库模型

upload文件夹
上传的图片存储位置

temp：模板docx文件

html中的input可以直接复制文字进去

[1]ListView：展示对象列表[比如，所有用户，所有文章]。
[2]DetailView：展示某个对象的详细信息[比如，用户资料，文章详情]。
[3]CreateView：通过表单创建某个对象[比如，创建用户，新建文章]。
[4]UpdateView：通过表单更新某个对象信息[比如修改密码，修改文字内容]。
[5]FormView：用户填写表单后转到某个完成页面。
[6]DeleteView：删除某个对象。

"r"   以读方式打开，只能读文件 ， 如果文件不存在，会发生异常      

"w" 以写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，先清空，再打开文件   

                                             
"rb"   以二进制读方式打开，只能读文件 ， 如果文件不存在，会发生异常      


"wb" 以二进制写方式打开，只能写文件， 如果文件不存在，创建该文件；如果文件已存在，先清空，再打开文件


