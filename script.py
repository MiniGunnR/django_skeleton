import os, sys

project_name = sys.argv[1]
app_name = sys.argv[2]
base_dir = os.path.join(os.getcwd(), project_name)

# create project
os.system("django-admin startproject {project_name} --template={base_dir}/../template/project_template".format(project_name=project_name, base_dir=base_dir))
print('Created project named {}...'.format(project_name))

# move inside project directory
os.chdir("{project_name}".format(project_name=project_name))

# create app
os.system("python manage.py startapp {app_name} --template={base_dir}/../template/app_template".format(app_name=app_name, base_dir=base_dir))
print('Created app named {}...'.format(app_name))

# create utils app
os.system("python manage.py startapp utils --template={base_dir}/../template/utils_template".format(base_dir=base_dir))
print('Created utils folder...')

# populate project urls
f = open(os.path.join(base_dir, project_name, 'urls.py'), 'r')
contents = f.readlines()
f.close()

pattern_index = contents.index("urlpatterns = [\n")
value = "    path('', include('{}.urls')),\n".format(app_name)

result = contents[pattern_index]
while result != "]\n":
    pattern_index += 1
    result = contents[pattern_index]

contents.insert(pattern_index, "    \n")
contents.insert(pattern_index + 1, value)

f = open(os.path.join(base_dir, project_name, 'urls.py'), 'w')
f.writelines(contents)
f.close()
print('Added include and app url in project urls...')

# populate installed apps
f = open(os.path.join(base_dir, project_name, 'settings.py'), 'r')
contents = f.readlines()
f.close()

installed_apps_index = contents.index("INSTALLED_APPS = [\n")
value = "    '{}',\n".format(app_name)

result = contents[installed_apps_index]
while result != "]\n":
    installed_apps_index += 1
    result = contents[installed_apps_index]

contents.insert(installed_apps_index, "    \n")
contents.insert(installed_apps_index + 1, value)

f = open(os.path.join(base_dir, project_name, 'settings.py'), 'w')
f.writelines(contents)
f.close()
print('Added {} app in INSTALLED_APPS'.format(app_name))


print('Done!')