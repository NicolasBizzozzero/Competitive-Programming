/**
 * Created by twodn-2 on 02/06/16.
 */
public class Terrain {
    private boolean[][] grille;
    public int compteur;

    /*public Terrain(){
        grille = new boolean[Integer.MAX_VALUE-1][Integer.MAX_VALUE];
        compteur = 0;
    }*/

    public Terrain(int largeur, int longueur){
        grille = new boolean[longueur][largeur];
    }

    public boolean[][] getGrille() {
        return grille;
    }

    public boolean getStatus(int x, int y) {
        return grille[y][x];
    }

    public int getCompteur() {
        return compteur;
    }

    public void allumer(int x, int y){
        boolean valeur = grille[y][x];

        if (valeur == false){
            grille[y][x] = true;
            compteur++;
        }
    }

    public void incrementeCompteur() {
        compteur++;
    }

    public void decrementeCompteur() {
        compteur--;
    }
}
