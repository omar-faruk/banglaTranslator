echo "[Desktop Entry]
Version=1.0.1
Name=Bangla Translator
Exec="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/Translate.sh
Icon="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"/icon.png
Path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
Terminal=True
Type=Application
Categories=Utility;Application;
Name[en_US]=Bangla Translator" >>Bangla-Translator.desktop

sudo chmod u+x "Bangla-Translator.desktop"
