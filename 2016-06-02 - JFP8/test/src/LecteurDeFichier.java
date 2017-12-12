import javafx.geometry.Pos;

import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class LecteurDeFichier {
    private ArrayList<Position> listePositions;
    private ArrayList<String> listeInstructions;

    private final String SEPARATEUR = "EOI";

    public boolean lireFichier(String nomFichier){
        listePositions = new ArrayList<>();
        listeInstructions = new ArrayList<>();
        String chaine = "";
        int compteurLigne = 0;

        // Lecture du fichier texte
        try {
            // Ouverture du fichier
            InputStream inputStream = new FileInputStream(nomFichier);
            InputStreamReader inputStreamReader = new InputStreamReader(inputStream);
            BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

            // Lecture de la première partie du fichier
            String ligne;
            while ((ligne=bufferedReader.readLine()) != null){
                compteurLigne++;
                if (ligne.equals(SEPARATEUR))
                    break;

                // On ajoute une position dans la liste de points à allumer
                String[] position = ligne.split(" ");
                Position pos = new Position(Integer.parseInt(position[0]), Integer.parseInt(position[1]));
                listePositions.add(pos);
            }

            final int ligneDebutCode = compteurLigne+1;

            // Lecture de la seconde partie du fichier
            while ((ligne=bufferedReader.readLine()) != null){
                compteurLigne++;

                //System.out.println(ligne);

                // On ajoute une instruction dans la liste des instructions
                String instruction = ligne;
                //listeInstructions[compteurLigne-ligneDebutCode] = instruction;
                listeInstructions.add(instruction);
            }

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

    public ArrayList<Position> getListePositions() {
        return listePositions;
    }

    public ArrayList<String> getListeInstructions() {
        return listeInstructions;
    }
}

class Position{
    private int x, y;

    public Position(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public boolean equals(Object p2) {
        Position p = (Position)p2;
        if(p.x == this.x && p.y == this.y) return true;
        return false;
    }
}
