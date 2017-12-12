import java.util.ArrayList;

/**
 * Created by twodn-1 on 02/06/16.
 */
public class Main {
    public static void main(String[] args)
    {
        for (int compteurDeFichiers=1; compteurDeFichiers<=40; compteurDeFichiers++) {
            //try {
                ArrayList<Position> listePositions;
                ArrayList<String> listeInstructions;

                // Lire le premier fichier
                LecteurDeFichier lecteurDeFichier = new LecteurDeFichier();
                lecteurDeFichier.lireFichier(String.format("test_%d.vm", compteurDeFichiers));
                listePositions = lecteurDeFichier.getListePositions();
                listeInstructions = lecteurDeFichier.getListeInstructions();

                // Initialisation des variables
                Terrain terrain = new Terrain(1000, 1000);
                for (Position pos : listePositions) {
                    terrain.allumer(pos.getX(), pos.getY());
                }
                VM virtualMachine = new VM(listeInstructions, new Tortue(terrain));

                // Executer les instructions
                String messageAEcrire = virtualMachine.exec();

                // Ecrire un fichier de retour
                lecteurDeFichier.creerEtEcrireFichier(String.format("test_%d.out", compteurDeFichiers), messageAEcrire);
            //} catch(Exception e){}
        }
    }
}
