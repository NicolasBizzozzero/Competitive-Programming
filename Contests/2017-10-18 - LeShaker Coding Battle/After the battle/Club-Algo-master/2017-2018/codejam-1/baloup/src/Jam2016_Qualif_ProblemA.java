import java.io.File;
import java.io.PrintStream;
import java.util.Scanner;

public class Jam2016_Qualif_ProblemA {
	
	
	
	public static void main(String[] args) throws Exception {
		
		try (Scanner s = new Scanner(new File("A-large-practice.in"))) {
			try (PrintStream out = new PrintStream("A-large.out")) {
				
				
				int t = s.nextInt();
				
				for (int i = 0; i < t; i++) {
					long n = s.nextLong();
					
					boolean digits[] = new boolean[10];
					
					boolean insomnia = true;
					
					for (int c = 1; c < 1000000; c++) {
						
						long v = n*c;
						
						String vStr = Long.toString(v);
						
						for (char ch: vStr.toCharArray()) {
							int dig = Integer.parseInt(new String(new char[] {ch}));
							
							digits[dig] = true;
						}
						
						
						
						boolean all = true;
						for (boolean b : digits)
							if (!b)
								all = false;
						
						
						if (all) {
							out.println("Case #"+(i+1)+": "+v);
							insomnia = false;
							break;
						}
						
						
					}
					
					if (insomnia)
						out.println("Case #"+(i+1)+": INSOMNIA");
					
					
					
					
				}
				
				
				
				
				
				
			}
			
		}
		
	}
	
	
	
}