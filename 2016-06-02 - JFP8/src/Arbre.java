import java.util.ArrayList;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class Arbre {
    private boolean FEUILLE_BLANCHE;
    private boolean FEUILLE_NOIRE;
    private ArrayList<Arbre> noeuds;

    public Arbre(boolean feuille_blanche, boolean feuille_noire, ArrayList<Arbre> noeuds){
        this.FEUILLE_BLANCHE = feuille_blanche;
        this.FEUILLE_NOIRE = feuille_noire;
        this.noeuds = noeuds;
    }

    /*public String toString() {
        if(noeuds.size() == 0)
        {
            return
        }
    }*/

    public String afficher(int dimensions) {
        if(FEUILLE_BLANCHE) {
            String str = "";
            str = new String(new char[dimensions]).replace("\0", ".");
            str+="\n";
            str = new String(new char[dimensions]).replace("\0", str);
            return str;
        }
        else if(FEUILLE_NOIRE) {
            String str = "";
            str = new String(new char[dimensions]).replace("\0", "*");
            str+="\n";
            str = new String(new char[dimensions]).replace("\0", str);
            return str;
        }
        else {
            //no: 0
            String no = noeuds.get(0).afficher(dimensions / 2);
            //ne: 1
            String ne = noeuds.get(1).afficher(dimensions / 2);
            //so: 2
            String so = noeuds.get(2).afficher(dimensions / 2);
            //se: 3
            String se = noeuds.get(3).afficher(dimensions / 2);

            int dimsur2 = dimensions/2;

            //Mettre ensemble no et ne
            String N = "";
            for(int ligne = 0; ligne < dimsur2; ligne++) {
                N += no.substring(0,dimsur2);
                no = no.substring(dimsur2+1,no.length());
                N += ne.substring(0,dimsur2);
                ne = ne.substring(dimsur2+1,ne.length());
                N+="\n";
            }

            //Mettre ensemble so et se
            String S = "";
            for(int ligne = 0; ligne < dimsur2; ligne++) {
                S += so.substring(0,dimsur2);
                so = so.substring(dimsur2+1,so.length());
                S += se.substring(0,dimsur2);
                se = se.substring(dimsur2+1,se.length());
                S+="\n";
            }

            return N + S;
        }
    }

    /*public String toString(){
        String s = "";

        // Cas ou le fichier est null
        if (FEUILLE_BLANCHE == null){
            return s;
        }

        // Cas ou l'arbre ne contient qu'une feuille blanche
        if (FEUILLE_NOIRE == null){
            for (int y=0; y<256; y++){
                for (int x=0; x<256; x++){
                    s += ".";
                }

                s += "\n";
            }

            return s;
        }

        int tailleListe = noeuds.size();

        // Cas ou la taille de la liste est de zero
        if (tailleListe == 0){
            for (int y=0; y<256; y++){
                for (int x=0; x<256; x++){
                    s += "*";
                }

                s += "\n";
            }

            return s;
        }

        // Cas ou la taille de la liste est de 1
        if (tailleListe == 1){
            QuadrupletEntier quad = noeuds.get(0);

            // On dessine la moitié haute de l'image
            for (int y=0; y<128; y++){
                for (int x=0; x<128; x++){
                    if (quad.getNord_ouest() == 0)
                        s += ".";
                    else
                        s += "*";
                }

                for (int x=128; x<256; x++){
                    if (quad.getNord_est() == 0)
                        s += ".";
                    else
                        s += "*";
                }

                s += "\n";
            }

            // On dessine la moitié basse de l'image
            for (int y=128; y<256; y++){
                for (int x=0; x<128; x++){
                    if (quad.getSud_ouest() == 0)
                        s += ".";
                    else
                        s += "*";
                }

                for (int x=128; x<256; x++){
                    if (quad.getSud_est() == 0)
                        s += ".";
                    else
                        s += "*";
                }

                s += "\n";
            }

            return s;
        }

        /*for (int i=tailleListe-1; i!=0; i--){
            QuadrupletEntier quad = noeuds.get(i);

        }*/

        //return s;
    //}*/

    public int trouverProfondeur(Arbre a){
        if (a.noeuds.size() == 0){
            return 0;
        }

        int p1 = 1 + trouverProfondeur(a.noeuds.get(0));
        int p2 = 1 + trouverProfondeur(a.noeuds.get(1));
        int p3 = 1 + trouverProfondeur(a.noeuds.get(2));
        int p4 = 1 + trouverProfondeur(a.noeuds.get(3));

        return Math.max(Math.max(p1, p2), Math.max(p3, p4));
    }
}
