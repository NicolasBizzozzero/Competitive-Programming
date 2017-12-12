import java.util.Locale;
import java.util.Scanner;

public class c_argent_de_poche {
	
	public static void main(String[] args) {
		Locale.setDefault(Locale.US); // important pour lire les valeurs decimales dans le Scanner
		try (Scanner in = new Scanner(System.in)) {
			int n = in.nextInt();
			
			double[] notes = new double[n];
			
			for (int i = 0; i < notes.length; i++) {
				notes[i] = Double.parseDouble(in.next());
			}
			
			double[] maxMinAvg = arrayMaxMinAvg(notes);
			double somme = (20 - (maxMinAvg[0] - maxMinAvg[1])) * maxMinAvg[2] * maxMinAvg[2] * 0.01;
			
			System.out.printf("%.2f\n", somme);
			
			
			
		}
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
	
	public static double arrayMax(double[] a) {
		double max = a[0];
		for (int i = 1; i < a.length; i++) {
			max = Math.max(a[i], max);
		}
		return max;
	}
	
	public static double arrayMin(double[] a) {
		double min = a[0];
		for (int i = 1; i < a.length; i++) {
			min = Math.min(a[i], min);
		}
		return min;
	}
	
	public static double arrayAvg(double[] a) {
		double sum = 0;
		for (int i = 0; i < a.length; i++) {
			sum += a[i];
		}
		return sum / a.length;
	}
}
