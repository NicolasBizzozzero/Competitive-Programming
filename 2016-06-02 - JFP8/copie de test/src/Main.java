import java.util.ArrayList;

/**
 * Created by twodn-1 on 02/06/16.
 */
public class Main {
    public static void main(String[] args)
    {
        for (int compteurDeFichiers=1; compteurDeFichiers<=40; compteurDeFichiers++) {
            ArrayList<Position> listePositions;
            String[] listeInstructions;

            // Lire le premier fichier
            LecteurDeFichier lecteurDeFichier = new LecteurDeFichier();
            lecteurDeFichier.lireFichier("test_1.vm");
            listePositions = lecteurDeFichier.getListePositions();
            listeInstructions = lecteurDeFichier.getListeInstructions();

            // Initialisation des variables
            Terrain terrain = new Terrain(100, 100);
            for (Position pos : listePositions) {
                terrain.allumer(pos.getX(), pos.getY());
            }
            VM virtualMachine = new VM(listeInstructions, new Tortue(terrain));

            // Executer les instructions
            String messageAEcrire = virtualMachine.exec();

            // Ecrire un fichier de retour
            lecteurDeFichier.creerEtEcrireFichier("test_1.out", messageAEcrire);
        }
    }
}
