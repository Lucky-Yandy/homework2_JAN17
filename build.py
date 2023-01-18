top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()
index = open('./content/index.html').read()
blog=open('./content/blog.html').read()
contact=open('./content/contact.html').read()
project=open('./content/projects.html').read()

home_page = top + index + bottom
my_blog= top + blog + bottom
my_project =top + project + bottom
my_contact = top + contact + bottom

open('docs/index.html','w+').write(home_page)
open('docs/blog.html','a+').write(my_blog)
open('docs/project.html','a+').write(my_project)
open('docs/contact.html','a+').write(my_contact)
