/*
 * File: MarcadorRecogiendoKarel.java
 * -----------------------------
 * El programa MarcadorRecogiendoKarel define una "ejecución"
 * método con tres comandos. Estos comandos causan
 * Karel para avanzar una cuadra, recoger un beeper,
 * y luego avanzar a la siguiente esquina.
 */
import karel.es.*;
public class MarcadorRecogiendoKarel extends Karel {
   public void run() {
      mueva();
      eligeMarcador();
      mueva();
   } 
}