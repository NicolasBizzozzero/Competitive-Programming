import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Scanner;

public class d_combinaison {
	
	public static void main(String[] args) {
		Locale.setDefault(Locale.US); // important pour lire les valeurs decimales dans le Scanner
		try (Scanner in = new Scanner(System.in)) {
			long n = in.nextLong();
			int l = in.nextInt();
			
			long minA, maxA2, maxA, minB, max2B, maxB;
			// definir min et max de a et b selon n
			minA = minB = 1;
			maxA2 = n - 2 * minB; // - 2b , bmin = 1
			max2B = n - minA;
			maxB = max2B / 2;
			maxA = (long) Math.sqrt(maxA2);
			
			// a^2 + 2b = n
			// a^2 - n = -2b
			// n - a^2 = 2b
			// (n - a^2)/2 = b
			
			List<String> list = new ArrayList<>();
			
			for (long a = ((n % 2 == 0) == (minA % 2 == 0)) ? minA : (minA + 1); a <= maxA; a += 2) {
				long b = (n - a*a) / 2;
				
				// a croissant donc b decroissant
				if (b > maxB)
					continue;
				if (b < minB)
					break;
				
				String code = a + "" + b;
				
				if (code.length() != l)
					continue;
				
				list.add(code);
			}
			
			if (list.isEmpty()) {
				System.out.println("Zut !");
				return;
			}
			
			list.sort(null);
			
			for (String e : list) {
				System.out.println(e);
			}
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
	
	
	public static BigDecimal sqrt(BigDecimal A, final int SCALE) {
	    BigDecimal x0 = new BigDecimal("0");
	    BigDecimal x1 = new BigDecimal(Math.sqrt(A.doubleValue()));
	    BigDecimal TWO = BigDecimal.valueOf(2);
	    while (!x0.equals(x1)) {
	        x0 = x1;
	        x1 = A.divide(x0, SCALE, BigDecimal.ROUND_HALF_UP);
	        x1 = x1.add(x0);
	        x1 = x1.divide(TWO, SCALE, BigDecimal.ROUND_HALF_UP);

	    }
	    return x1;
	}
}
