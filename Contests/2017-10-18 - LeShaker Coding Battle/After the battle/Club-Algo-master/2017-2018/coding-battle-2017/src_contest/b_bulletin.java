import java.util.Scanner;

public class b_bulletin {
	
	public static void main(String[] args) {
		try (Scanner in = new Scanner(System.in)) {
			int note = in.nextInt();

			int min = in.nextInt();
			int max = in.nextInt();
			float avg = Float.parseFloat(in.next());
			
			int nbEleve = in.nextInt();
			
			double[] notes = new double[nbEleve + 1];
			notes[nbEleve] = note;
			for (int i = 0; i < nbEleve; i++)
				notes[i] = Integer.parseInt(in.next());
			
			
			double[] maxMinAvgNotes = arrayMaxMinAvg(notes);
			
			
			if (doubleAreEquals(max, maxMinAvgNotes[0])
					&& doubleAreEquals(min, maxMinAvgNotes[1])
					&& doubleAreEquals(avg, maxMinAvgNotes[2])
					&& note >= min && note <= max) {
				System.out.println("RAS");
			}
			else
				System.out.println("Jack ! Viens ici !");
			
			
		}
	}
	
	
	public static boolean doubleAreEquals(double v1, double v2) {
		return Math.abs(v2 - v1) < 0.02;
	}
	
	

	
	public static double[] arrayMaxMinAvg(double[] a) {
		double[] res = new double[3];
		res[0] = a[0];
		res[1] = a[0];
		res[2] = a[0];
		for (int i = 1; i < a.length; i++) {
			res[0] = Math.max(a[i], res[0]);
			res[1] = Math.min(a[i], res[1]);
			res[2] += a[i];
		}
		res[2] /= a.length;
		return res;
	}
	
}
