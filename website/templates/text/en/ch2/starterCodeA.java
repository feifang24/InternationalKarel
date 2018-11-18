/*
 * File: BeeperPickingKarel.java
 * -----------------------------
 * The BeeperPickingKarel program defines a "run" 
 * method with three commands. These commands cause  
 * Karel to move forward one block, pick up a beeper
 * and then move ahead to the next corner.
 */
import karel.en.*;
public class BeeperPickingKarel extends Karel {
   public void run() {
      move();
      pickBeeper();
      move();
   } 
}