/**
 * Created by twodn-2 on 02/06/16.
 */

import java.util.LinkedList;
import java.util.Stack;

public class VM2 {
    private Stack<DirectionPositionEtNumeroInstruction> pile;
    private LinkedList<String> code;
    private int pointeurInstruction;
    private Tortue tortue;

    public VM2(LinkedList<String> code) {
        this.code = code;
        tortue = tortue;
    }

    public void interpreterInstruction() {
        int instruction = this.pointeurInstruction;
        //dépiler
        if(code.get(instruction).equals("ret")) {

        }
    }



    /*public String toString(){
        String s = "";
        boolean[][] grille = tortue.getTerrain().getGrille();

        for (int y=0; y< )

        return s;
    }*/



}
