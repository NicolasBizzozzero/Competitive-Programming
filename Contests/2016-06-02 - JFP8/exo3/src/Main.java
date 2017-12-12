import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.PrintWriter;

/**
 * Created by twodn-2 on 02/06/16.
 */
public class Main {
    public static void main(String[] args){
        // Je m'excuse d'avance pour ce code
        try {
            // Création et ouverture en écriture du fichier
            FileWriter fileWriter = new FileWriter("test_8.vm");
            BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);
            PrintWriter fichierSortie = new PrintWriter(bufferedWriter);

            // Ecriture dans le fichier
            // Création du fichier 2
            /*for (int y=0; y<256; y++){
                for (int x=0; x<256; x++){
                    fichierSortie.print("" + x + " " + y + "\n");
                }
            }*/
            /*// Création du fichier 3
            for (int y=0; y<128; y++){
                for (int x=128; x<256; x++){
                    fichierSortie.print("" + x + " " + y + "\n");
                }
            }*/
            /*// Création du fichier 4
            for (int y=0; y<128; y++){
                for (int x=0; x<128; x++){
                    fichierSortie.print("" + x + " " + y + "\n");
                }
            }*/
            /*// Création du fichier 5
            for (int y=128; y<256; y++){
                for (int x=0; x<128; x++){
                    fichierSortie.print("" + x + " " + y + "\n");
                }
            }*/
            /*// Création du fichier 6
            for (int y=128; y<256; y++){
                for (int x=128; x<256; x++){
                    fichierSortie.print("" + x + " " + y + "\n");
                }
            }*/

            fichierSortie.print("EOI\nhalt");

                    fichierSortie.close();
        } catch (Exception e){
            System.out.println(e.toString());
        }
    }
}
