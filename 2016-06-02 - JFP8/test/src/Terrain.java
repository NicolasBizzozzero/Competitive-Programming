import java.util.ArrayList;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class Terrain {
    //private boolean[][] grille;
    private ArrayList<Position> allumee;
    public int compteur;

    /*public Terrain(){
        grille = new boolean[Integer.MAX_VALUE-1][Integer.MAX_VALUE];
        compteur = 0;
    }*/

    public Terrain(int largeur, int longueur){
        //grille = new boolean[longueur][largeur];
        allumee = new ArrayList<>();
    }

    /*public boolean[][] getGrille() {
        return grille;
    }*/

    /*public boolean xgetStatus(int x, int y) {
        return grille[y][x];
    }*/

    public boolean getStatus(int x, int y) {
        Position p = new Position(x,y);
        for(Position cherche : allumee) {
            if(cherche.equals(p)) return true;
        }
        return false;
    }

    public int getCompteur() {
        return compteur;
    }

    /*public void xallumer(int x, int y){
        boolean valeur = grille[y][x];

        if (valeur == false){
            grille[y][x] = true;
            compteur++;
        }
    }*/

    public void allumer(int x, int y){
        Position p = new Position(x, y);

        //Vérifier si ça existe déjà
        for(Position cherche : allumee) {
            if(cherche.equals(p)) {
                return;
            }
        }

        allumee.add(p);
        compteur++;
    }

    public void eteindre(int x, int y) {
        Position p = new Position(x,y);
        for(Position cherche : allumee) {
            if(cherche.equals(p)) {
                allumee.remove(cherche);
                compteur--;
                break;
            }
        }
    }

    public void incrementeCompteur() {
        compteur++;
    }

    public void decrementeCompteur() {
        compteur--;
    }
}
