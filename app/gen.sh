#!/usr/bin/env bash

echo "Drop Database ctmp"
dropdb ctmp

echo "Drop Database iecms"
dropdb iecms

echo " Dropped Database ctmp"
createdb ctmp

echo " Dropped Database iecms"
createdb iecms

echo "Created Database iecms"
echo "Starting Generating the tables"
# Backup old pony file
cp pomy.py pony-"$(date)".py
# Take the latest pony file and use it
cp `ls pony* | tail -n1` pomy.py
cat p_connect.py >> pomy.py
python pomy.py
echo "Finished Generating the tables"

echo "Generating mod1.py - preliminary data model"
flask-sqlacodegen postgresql://nyimbi:abcd1234@localhost/ctmp --outfile mod1.py --flask --noinflect
echo "Finished generating preliminary data model -- proceding to generate view"

echo "Now starting fixup of the models and generating models.py"
python fixup_models.py mod1.py
echo "Models.py file created"

echo "Creating tables in IECMS "
## We haven't fixed up our views yet, so temp measure
cp views_template.py views.py
cd ..
#fabmanager create-db
echo "GO FIX:   wtf_PageForm, exclude[]"
# Back to where we started from
cd app

# Because we can't use from .mixin import * we need to from mixin import *
echo " Now fixingup the views"
sed s/'from .mixins import'/'from mixins import'/ <models.py >model1.py
python fixup_views.py model1
# Done with this file
rm model1.py


echo " .......... Done fixingup the views"
cat views.py models.py | wc -l
echo "Total lines of code that you did not have to write"

echo " All DONE with generation - now to create the iecms db"

# All done with generation for the time being
# TO DO
cd ..
fabmanager create-db
echo "IECMS DAtabase Created"
echo "Adding features to the database"
pgxn install multicorn
psql -d iecms < db_extensions.sql


#ipython -c "import app"

echo "Now run fabmanager create-db"
