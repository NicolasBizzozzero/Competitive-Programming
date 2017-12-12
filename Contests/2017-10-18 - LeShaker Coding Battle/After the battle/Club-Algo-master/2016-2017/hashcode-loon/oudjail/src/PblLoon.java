import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PblLoon {


	protected int r; // le nombre de lignes de la grille (
	protected int c; // le nombre de colonnes de la grille
	protected int a; // le nombre d’altitudes différentes de la simulation
	protected int l; // le nombre de cases cibles
	protected int v; // le rayon de la couverture fournie par les ballon
	protected int b; // le nombre de ballons disponibles
	protected int t; // le nombre de tour de la simulation

	protected Vector2I depart; 

	protected List<Vector2I> cibles; // L
	
	protected List<List<List<Vector2I>>> A; 
	

	public PblLoon(Scanner in) {
		this.r = in.nextInt();
		this.c = in.nextInt();
		this.a = in.nextInt();
		this.l = in.nextInt();
		this.v = in.nextInt(); 
		this.b = in.nextInt();
		this.t = in.nextInt();
		
		this.depart = new Vector2I(in.nextInt(), in.nextInt());
		
		this.cibles = new ArrayList<>(l);
		for (int i = 0; i < l; i++) {
			cibles.add(new Vector2I(in.nextInt(), in.nextInt()));
		}
		
		this.A = new ArrayList<>(a);
		for (int i = 0; i < a; i++) {
			A.add(new ArrayList<>(r));
			for (int j = 0; j < r; j++) {
				A.get(i).add(new ArrayList<>(c));
				for (int k = 0; k < c; k++) {
					A.get(i).get(j).add(new Vector2I(in.nextInt(), in.nextInt()));
				}
			}
			
		}
	}

	

}
