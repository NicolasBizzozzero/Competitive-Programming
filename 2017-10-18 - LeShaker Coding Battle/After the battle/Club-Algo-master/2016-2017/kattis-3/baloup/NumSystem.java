
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class NumSystem {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		int nbCase = s.nextInt();
		
		for (int cs=0; cs<nbCase; cs++) {
			char[] inputNumber = s.next().toCharArray();
			char[] inputLang = s.next().toCharArray();
			char[] outputLang = s.next().toCharArray();
			
			// convert input to decimal
			
			long decValue = 0;
			int mult = 1;
			for (int i = inputNumber.length - 1; i >= 0; i--) {
				decValue += indexOf(inputLang, inputNumber[i]) * mult;
				mult *= inputLang.length;
			}
			
			// reconvertir en base cible
			long divisé = decValue, diviseur = outputLang.length, quotient, reste;
			List<Character> output = new ArrayList<>();
			do {
				quotient = divisé / diviseur;
				reste = divisé % diviseur;
				output.add(0, outputLang[(int)reste]);
				divisé = quotient;
			} while (quotient != 0);
			
			System.out.print("Case #"+(cs+1)+": ");
			
			for (Character c : output) {
				System.out.print(c);
			}
			System.out.println();
			
		}
		s.close();
	}
	
	
	
	
	public static int indexOf(char[] arr, char search) {
		for (int i=0; i<arr.length; i++) {
			if (arr[i] == search)
				return i;
		}
		return -1;
	}

}
