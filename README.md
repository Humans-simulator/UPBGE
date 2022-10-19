# Istruzioni per installazione Bridge ROS-Blender
Testato corretto funzionamento con:
- Ubuntu 18.04.6 con ROS Melodic
- Ubuntu 20.04.5 con ROS Noetic

Tutte le vesioni di Blender sono compatibili dalla 3.0.0 in poi, compreso UPBGE 0.30.
***

## Guida step by step 
1. Estrai "UPBGE-0.30-linux-x86_64.tar.xz" nella directory "/home"
2. All'interno della cartella appena estratta apri l'eseguibile "blender" da terminale. (NON aprirlo con il doppio click!)
3. Recati in "Edit - Preferences - Add-on"
4. Clicca "Install..." e seleziona lo zip "Pythonn_Module_Manager_1.0.6.zip"
5. Clicca poi "Install Add-on" e abilita il plugin appena installato
6. Espadilo e nella sezione Preferences seleziona "Ensure PIP", verifica nella console che l'installazione sia andata a buon fine e che la vesione di PIP sia la 21.2.3
7. In "Module name(s):" inserisci "--extra-index-url https://rospypi.github.io/simple rospy-all", clicca poi Install e verifica la corretta installazione
8. In "Module name(s):" inserisci "opencv-python", clicca poi Install e verifica la corretta installazione
9. Installa ora il secondo plugin Blender "ROS_addon.zip"
10. Abilitalo e tornando nella Viewport di Blender premi il tasto "N" e vedrai comparire il menù opzioni di ROS Bridge
