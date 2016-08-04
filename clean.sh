echo Cleaning...
touch app/hey.pyc
touch hey.pyc
rm *.pyc
find ./app/ -name *.pyc | xargs rm
find ./ -name __pycache__ | xargs rm -r
echo done!
clear 
