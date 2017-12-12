import java.util.ArrayList;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class Main {
    /*public static void main(String[] args)
    {
        for (int compteurDeFichiers=1; compteurDeFichiers<=15; compteurDeFichiers++) {
            try {
                Arbre arbre;

                // Lire le fichier
                LecteurDeFichier lecteurDeFichier = new LecteurDeFichier();
                lecteurDeFichier.lireFichier(String.format("test_%d.qt", compteurDeFichiers));

                // Initialisation des variables
                arbre = lecteurDeFichier.getArbre();

                // Ecrire un fichier de retour
                lecteurDeFichier.creerEtEcrireFichier(String.format("test_%d.img", compteurDeFichiers), arbre.toString());
            } catch(Exception e){}
        }
    }*/

    public static void main(String[] args) {
        Arbre a = new Arbre(true, false, null);
        System.out.println(a.afficher(4));

        Arbre b = new Arbre(false, true, null);
        System.out.println(b.afficher(8));

        ArrayList<Arbre> enfants = new ArrayList<>();
        enfants.add(a);
        enfants.add(b);
        enfants.add(b);
        enfants.add(a);
        Arbre c = new Arbre(false, false, enfants);
        System.out.println(c.afficher(4));
    }
}
