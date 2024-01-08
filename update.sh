rm -Rf Cpkg
mkdir Cpkg
touch Cpkg/__init__.py Cpkg/ErrorLogs.txt
cp ConV2erter/Updated_ConV2erter.py Cpkg/ConV2erter.py
cp ConV2erter/Cpkg.update.sh Cpkg.update.sh
chmod +x Cpkg.update.sh
rm -Rf ConV2erter/
