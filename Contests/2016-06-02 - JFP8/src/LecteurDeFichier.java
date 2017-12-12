
import java.io.*;
import java.util.ArrayList;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class LecteurDeFichier {
    private Arbre arbre;

    public boolean lireFichier(String nomFichier){
        int compteurLigne = 0;
        String ligne;

        // Lecture du fichier texte
        try {
            // Ouverture du fichier
            InputStream inputStream = new FileInputStream(nomFichier);
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

            // Lecture de la valeur des feuilles
            // Cas ou le fichier est vide
            if ((ligne=bufferedReader.readLine()) == null){
                arbre = new Arbre(false, false, null);
                return true;
            }

            Integer feuille_blanche = Integer.parseInt(ligne);
            compteurLigne++;
            // Cas ou juste la feuille blanche est presente
            if ((ligne=bufferedReader.readLine()) == null){
                arbre = new Arbre(true, false, null);
                return true;
            }
            Integer feuille_noire = Integer.parseInt(ligne);
            compteurLigne++;

            // On lit ensuite tous les autres noeuds
            ArrayList<QuadrupletEntier> listeNoeuds = new ArrayList<>();
            while ((ligne=bufferedReader.readLine()) != null){
                compteurLigne++;

                // On ajoute un noeud dans la liste des noeuds de l'arbre
                String[] noeud = ligne.split(" ");
                QuadrupletEntier quad = new QuadrupletEntier(Integer.parseInt(noeud[0]), Integer.parseInt(noeud[1]), Integer.parseInt(noeud[2]), Integer.parseInt(noeud[3]));
                listeNoeuds.add(quad);
            }

            arbre = new Arbre(false, false, null);

            bufferedReader.close();
        } catch (Exception e){
            System.out.println(e.toString());
        }

        return true;
    }

    public boolean creerEtEcrireFichier(String nomFichier, String valeurAEcrire){
        try {
            // Création et ouverture en écriture du fichier
            FileWriter fileWriter = new FileWriter(nomFichier);
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            PrintWriter fichierSortie = new PrintWriter(bufferedWriter);

            // Ecriture dans le fichier
            fichierSortie.print(valeurAEcrire);

            fichierSortie.close();
        } catch (Exception e){
            System.out.println(e.toString());
        }

        return true;
    }

    public Arbre getArbre() {
        return arbre;
    }
}