/**
 * Created by twodn-1 on 02/06/16.
 */

import java.util.Arrays;
import java.util.EmptyStackException;
import java.util.Stack;
public class VM {
    private Stack<DirectionPositionEtNumeroInstruction> pile;
    private String[] code;
    private int pointeurInstruction;
    private Tortue tortue;

    public VM(String[] code, Tortue tortue) {
        this.code = code;
        this.tortue = tortue;
        this.pointeurInstruction = 0;
        pile = new Stack<>();
    }

    //Retourne true si le programme est arrivé à la fin.
    public boolean interpreterInstruction() {
        String instruction = code[pointeurInstruction];
        //dépiler
        if(instruction == null) {
            throw new WrongInstructionException("null instruction");
        }
        //System.out.println(instruction);
        if(instruction.equals("ret")) {
            DirectionPositionEtNumeroInstruction dpni;
            try {
                dpni = pile.pop();
            }
            catch (EmptyStackException e) {
                throw new WrongInstructionException("ret on empty stack");
            }


            tortue.setPos(dpni.x, dpni.y);
            tortue.setOrientation(dpni.orientation);
            pointeurInstruction=dpni.numeroInstruction;
            return false;
        }
        else if(instruction.equals("halt")) {
            //Arrête le programme.
            //System.out.println(tortue.getTerrain().getCompteur());
            return true;
        }
        else if(instruction.equals("plot")) {
            plot();
            pointeurInstruction++;
            return false;
        }


        //Instructions avec mnemonic de 4 ou 5 caractères.
        else {
            String mnemonic = instruction.substring(0, 5);
            if(mnemonic.equals("call ")) {
                String argumentS = instruction.substring(5,instruction.length());
                int argument = Integer.parseInt(argumentS);

                //Vérifier que l'instruction existe.
                if(argument <0 || argument >=code.length) {
                    throw new WrongInstructionException("call argument is out of bounds.");
                }

                //Empiler la position, orientation, et le pointeur d'instruction+1 actuels.
                DirectionPositionEtNumeroInstruction courant = new DirectionPositionEtNumeroInstruction();
                courant.x = tortue.getX();
                courant.y = tortue.getY();
                courant.orientation = tortue.getOrientation();
                courant.numeroInstruction = pointeurInstruction+1;
                pile.push(courant);

                //Sauter à l'instruction n
                pointeurInstruction=argument;
                return false;
            }
            else if(mnemonic.equals("test ")) {
                String argumentS = instruction.substring(5,instruction.length());
                int argument = Integer.parseInt(argumentS);

                if(tortue.estSurCaseAllumée()) {
                    //Vérifier que l'instruction existe.
                    if(argument <0 || argument >=code.length) {
                        throw new WrongInstructionException("test argument is out of bounds.");
                    }

                    //Sauter à l'instruction n
                    pointeurInstruction=argument;
                }
                else {
                    //Incrémenter le comptueur instruction.
                    pointeurInstruction++;
                }
                return false;
            }
            else if(mnemonic.equals("goto ")) {
                String argumentS = instruction.substring(5,instruction.length());
                int argument = Integer.parseInt(argumentS);

                //Vérifier que l'instruction existe.
                if(argument <0 || argument >=code.length) {
                    throw new WrongInstructionException("goto argument is out of bounds.");
                }

                //Sauter à l'instruction n
                pointeurInstruction=argument;

                return false;

            }
            else if(mnemonic.equals("clear")) {
                clear();
                pointeurInstruction++;
                return false;
            }
            else if(mnemonic.equals("left ")) {
                left();
                pointeurInstruction++;
                return false;
            }
            else if(mnemonic.equals("right")) {
                right();
                pointeurInstruction++;
                return false;
            }
            else if(mnemonic.equals("move ")) {
                move();
                pointeurInstruction++;
                return false;
            }
        }

        throw new WrongInstructionException("Instruction with nonexistent mnemonic.");
    }

    public String exec() {
        try {
            while(true) {
                if(interpreterInstruction()) break;
            }
        }
        catch ( WrongInstructionException w) {
            return "erreur";
        }
        return String.format("%d",tortue.getTerrain().getCompteur());
    }

    public void move(){
        tortue.move();
    }

    public void right(){
        tortue.right();
    }

    public void left(){
        tortue.left();
    }

    public void clear(){
        tortue.clear();
    }

    public void plot(){
        tortue.plot();
    }
}
