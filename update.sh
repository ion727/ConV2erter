rm -R Cpkg
mkdir Cpkg
touch Cpkg/__init__.py
cp ConV2erter/Updated_ConV2erter.py Cpkg/ConV2erter.py
cp ConV2erter/Updatr.sh Cpkg.update.sh
chmod +x Cpkg.update.sh
rm -R ConV2erter/
